from main_page import bp
from flask_login import login_required, current_user
from flask import abort, flash, render_template, url_for, redirect, request, session
from dataLoader import load_rest, load_items, check_if_reviewed, insert_review, load_item_data, fetch_unfinished_order, create_order
from dataLoader import create_inst, create_excludes, create_cont, get_order_info, get_filled_info, modify_inst, modify_excludes, delete_record
from dataLoader import close_order
from database import Database

@bp.route('/restaurants')
def rest():

    rest_dict = load_rest(Database('test1'))
    return render_template("restaurants.html", rest_dict=rest_dict)


@bp.route('menu/<name>')
def menu(name):
    item_dict = load_items(Database('test1'), name)
    subC_list = item_dict.pop('subC_list')
    list_size = len(subC_list)
    return render_template("menu.html", name=name, item_dict=item_dict, subC_list=subC_list, list_size=list_size)

@bp.route('check_review/<name>')
@login_required
def check_review(name):

    has_reviewed = check_if_reviewed(Database('test1'), 
                                     name, 
                                     current_user.get_id())
    
    if has_reviewed:
        return f"<h2>You have already reviewed {name} today! (You can review a restaurant only Once A Day)</h2>"
    session['checkedRev'] = True
    return redirect(url_for('main.review', name=name))


@bp.route('review/<name>', methods=['GET', 'POST'])
@login_required
def review(name):
    if request.method == "GET":
        try:
            if not session['checkedRev']:
                return redirect(url_for('main.rest'))
        except :
            return redirect(url_for('main.rest'))
    
        session.pop('checkedRev')
        return render_template("review.html", name=name)
    elif request.method == "POST":
        try:
            rating = float(request.form['rating'])
        except ValueError:
            flash('Invalid Rating, please try again')
            return render_template("review.html", name=name)
        
        com = request.form['comment']
        
        if rating not in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]:
            # rating invalid
            flash('Invalid Rating, please try again')
            return render_template("review.html", name=name)
        
        else:
            #rating valid, proceed to registering to DB
            
            insert_review(Database('test1'), 
                          name, 
                          current_user.get_id(), 
                          rating, com)
            
        
        return redirect(url_for('main.rest'))


@bp.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    
    id = current_user.get_id()
    
    order_id = fetch_unfinished_order(Database(), id)
    
    if order_id == None:
        order_id = create_order(Database(), current_user.get_id())
    

    
    order_info = get_order_info(Database(), order_id)
    
    if order_info == None:
        return render_template('cart.html', isEmpty=True, fee=0, TP=0)
    
    
    fee = order_info.pop('fee')
    keys = list(order_info.keys())
    list.sort(keys)
    
    TP = 0
    
    for key in keys:
        total_item_price = 0
        item_price = int(order_info[key][0][2])
        combo_price = 0
        for subC, cPrice in order_info[key][1]:
            combo_price = combo_price + cPrice
        
        total_item_price = total_item_price + item_price + combo_price
        order_info[key].append(total_item_price)
        TP = TP + total_item_price
    
    TPs = "{:,}".format(TP + fee) + ' LBP'    
        
    if request.method == "GET":     
        return render_template('cart.html', isEmpty=False, order_info=order_info, fee=fee, keys=keys, TP=TPs)
    
    elif request.method == "POST":
        if request.json['req'] == 'remove':
            delete_record(Database(), request.json['instID'])
            return redirect(url_for('cart.html'))

        elif request.json['req'] == 'edit':         
            return redirect(url_for('main.custom', itemID=request.json['itemID']))
        
        elif request.json['req'] == 'confirm':
            close_order(Database(), order_id, TP+fee)
            return redirect(url_for('home.index'))
        
       
@bp.route('/order/<order_id>') 
def past_order(order_id):
    order_info = get_order_info(Database(), order_id)
    fee = order_info.pop('fee')
    keys = list(order_info.keys())
    list.sort(keys)
    
    TP = 0
    
    for key in keys:
        total_item_price = 0
        item_price = int(order_info[key][0][2])
        combo_price = 0
        for subC, cPrice in order_info[key][1]:
            combo_price = combo_price + cPrice
        
        total_item_price = total_item_price + item_price + combo_price
        order_info[key].append(total_item_price)
        TP = TP + total_item_price
    
    TPs = "{:,}".format(TP + fee) + ' LBP' 
    
    return render_template('past_order.html', order_info = order_info, keys=keys, fee=fee, TP = TPs)



@bp.route('/add to order/<itemID>/<instID>', methods=["POST"])
@bp.route('/add to order/<itemID>', methods=["POST"], defaults={'instID': None})
@login_required
def createOrder(itemID, instID=None) :
    
    order_id = fetch_unfinished_order(Database(), current_user.get_id())
    
    if order_id is None:
        order_id = create_order(Database(), current_user.get_id())

    options = {}
    
    C = -1
    for key in request.form.keys():
        if key[0] == 'O':
            options[key] = request.form[key]
        elif key[0] == 'C':
            C = request.form[key]
        else:
            specialInst = request.form[key]

    
    if len(options) == 0:
        options['dummy'] = -1
    
    if instID is None:
        instID = create_inst(Database(), C, specialInst)
        create_excludes(Database(), instID, options)
        create_cont(Database(), order_id, itemID, instID)
        
    else:
        modify_inst(Database(), instID, C, specialInst)
        modify_excludes(Database(), instID, options)
    
    return redirect(url_for('main.cart'))

@bp.route('/custom/<itemID>', defaults={'instID': None}, methods=['GET', 'POST'])
@bp.route('/custom/<itemID>/<instID>', methods=['GET', 'POST'])
@login_required
def custom(itemID, instID=None):
    items, options, combos = load_item_data(Database('test1'), itemID)
    
    if instID is None:
        return render_template('custom.html', item_data=items, options=options, combos=combos, 
                               cLen = len(combos), oLen = len(options), isDirect=True)
    
    else:
        id = current_user.get_id()
    
        order_id = fetch_unfinished_order(Database(), id)
        
        if order_id == None:
            order_id = create_order(Database(), current_user.get_id())
        
        
        filled_customization = get_filled_info(Database(), itemID ,order_id, instID)
        
        if filled_customization is None:
            return redirect(url_for('main.custom', itemID = itemID))
        
        filled_inst = filled_customization[0]
        
        filled_comb = filled_customization[1]
        
        filled_op_list = filled_customization[2]
        
        return render_template('custom.html', item_data=items, options=options, combos=combos, 
                               cLen = len(combos), FI=filled_inst, FC=filled_comb,
                               FO=filled_op_list, instID=instID, isDirect=False)
    
    



  

@bp.route('/redirect/custom/<itemID>/<instID>')
@login_required
def red_custom(itemID, instID):

    return redirect(url_for('main.custom', itemID=itemID, instID=instID))


    
@bp.route('/redirect/<n>')
def red(n):
    return redirect(url_for('main.menu', name=n))


@bp.route('/test')
def test():
    return render_template('test.html')


