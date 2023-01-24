from flask import get_flashed_messages, render_template, request, redirect, url_for, session, flash
from werkzeug import exceptions
from auth_page import bp
from database import Database, QueryContainer, User 
from auth_page.email_conf import genCode, sendCode
from flask_login import login_required, login_user, logout_user, current_user
from dataLoader import check_first_login, fetch_user_info, update_user_info, fetch_acc_info, fetch_order_hist

qC = QueryContainer()

@bp.route('/account/login', defaults={'setting': 'login'}, methods=['GET', 'POST'])
@bp.route('/account/<setting>', methods=['GET', 'POST'])
def acc(setting='login'):
    
    if setting == 'login':
        temp = 'account.html'
    elif setting == 'signup':
        temp = 'account_signup.html'
    
    if request.method == 'GET':
        return render_template(temp, valid_login=True, valid_signup=True, pastInput='')
    
    elif request.method == 'POST':

        try:
            inpName = request.form['email']
            inpPwd = request.form['pswd']
            
            db = Database('test1')
            connection = db.connection
            cur = connection.cursor()
            
            cur.execute(f'''SELECT passWords FROM ACCOUNTS WHERE accID = \'{inpName}\' OR email = \'{inpName}\'''')
            userPW = cur.fetchall()
            
            if len(userPW) > 0:
                if inpPwd == userPW[0][0]:
                    #SIGN IN SUCCESSFUL
                    db.close()
                    user = User.create_user(inpName)
                    login_user(user)

                    isFirstLogin = check_first_login(Database('test1'), current_user.get_id())
                    if isFirstLogin:
                        return redirect(url_for('auth.config', userID=current_user.get_id()))
                    
                    return redirect(url_for('home.index'))           
            db.close()
            return render_template(temp, valid_login=False, valid_signup=True, pastInput=inpName)
           
           
            
        except exceptions.BadRequestKeyError:
            # If the form submitted is the Sign up form (the code above will throw an error because of the absence of input)
            inpName = request.form['usernameSU']
            inpEmail = request.form['emailSU']
            phone = request.form['phone']
            inpPwd = request.form['pswdSU']
            
            try:
                phone = int(phone)
            except:
                return render_template('account_signup.html', valid_login=True, valid_signup=False, pastSUname=inpName, pastSUemail=inpEmail)

                
            db = Database('test1')
            connection = db.connection
            cur = connection.cursor()
            
            cur.execute(f'''SELECT accID, email FROM ACCOUNTS WHERE accID = \'{inpName}\' OR email = \'{inpEmail}\'''')
            userInfo = cur.fetchall()
            
            db.close()
            
            if len(userInfo) == 0:
                #proceed to email confirmation              
                
                query = f"INSERT INTO ACCOUNTS VALUES ('{inpName}', '{inpEmail}', '{inpPwd}', {phone})"
                
                qC.registerQuery(query)             
                
                
                return redirect(url_for('auth.emailconf', email=inpEmail))
            
            else:
                
                #check which input is already used and return signup page
                if userInfo[0][0] == inpName and userInfo[0][1] == inpEmail:
                    #both username and email are already used
                    print('Email address already exists')
                    return redirect(url_for('auth.acc'))
                elif userInfo[0][0] == inpName:
                    # the userName is used
                    print('UserName Already Taken')
                    return render_template('account_signup.html', valid_login=True, valid_signup=False, pastSUname=inpName, pastSUemail=inpEmail)
                elif userInfo[0][1] == inpEmail:
                    # email already used
                    print('Email address already exists')
                    return redirect(url_for('auth.acc'))
                
                return render_template('account_signup.html', valid_login=True, valid_signup=False, pastSUname=inpName, pastSUemail=inpEmail)





@bp.route('/confirm/<email>', methods=['GET', 'POST'])
def emailconf(email):
         
    if request.method == 'GET': # When you enter the Page
        
        return render_template('email_confirm.html', inpEmail = email)
    
    elif request.method == 'POST': # When you perform some POST request
        
        
        if request.form.__contains__('sendcode'):
            # If Send Code is Pressed
            
            session['OTP'] = genCode()
            sendCode(email)
            return render_template('email_confirm.html', inpEmail = email)
            
        elif request.form.__contains__('confCode'):
            # If Confirm is pressed
            
            confCode = request.form['confCode']
            
            try:
                if int(confCode) == int(session['OTP']):
                    #Allow Signup
                    qC.executeInsertQuery()
                    session.pop("OTP")
                    return redirect(url_for('auth.acc', pI=email))
                else:
                    
                    session.pop("OTP")
                    return "Wrong Code"
            except TypeError:
                return "<h1>Your Code Has Expired</h1>"
            except Exception as e:
                print(e)
                session.pop("OTP")
                return "Wrong Code"
    
        else:
            # If none Are Pressed And Something unexpected Happens
            session.pop("OTP")
            return "Can't Signup"


@bp.route('/config', methods=["GET", "POST"])
@login_required
def config():
    if request.method == "GET":
        return render_template('config.html', userID = current_user.get_id())
    elif request.method == "POST":
        
        fName = request.form['fName']
        lName = request.form['lName']
        city = request.form['city']
        strt = request.form['strt']
        reg = request.form['reg']
        bld = request.form['bld']
        flr = request.form['flr']
        notes = request.form['notes']
        
        db = Database('test1')
        con = db.connection
        cur = con.cursor()
        
        cur.execute(f''' INSERT INTO CUSTOMER
                    VALUES ("{current_user.get_id()}", "{fName}", "{lName}", "{city}", "{strt}", "{reg}", "{bld}", "{flr}", "{notes}"); ''')
        con.commit()
        
        db.close()
        
        return redirect(url_for('main.rest'))
    


@bp.route('/account_information', methods=['GET', 'POST'])
@login_required
def acc_info():
    if request.method == 'GET':
        user_id = current_user.get_id()
        
        acc_info = fetch_acc_info(Database(), user_id)
        user_info = fetch_user_info(Database(), user_id)
        order_hist = fetch_order_hist(Database(), user_id)
        
        return render_template('account_info.html', user_info=user_info, 
                               acc_info=acc_info, order_hist=order_hist)
    
    elif request.method == 'POST':
        if request.json['req'] == 'acc_edit': 
            try:
                db = Database()
                con = db.connection
                cur = con.cursor()
                
                cur.execute(f'''   UPDATE ACCOUNTS
                            SET phoneNumber = {int(request.json['info'][0])}
                            WHERE accID="{current_user.get_id()}"; ''')
                con.commit()
                db.close()
            except:
                pass
            
            return redirect(url_for('.acc_info'))
        
        elif request.json['req'] == 'user_edit':
            user_id = current_user.get_id()
            update_user_info(Database(), user_id, request.json['info'])
            
            return redirect(url_for('.acc_info')) 



@bp.route('/redirect')
def signup():
    return redirect(url_for('auth.acc', setting='signup'))

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))
    
    

    
    

