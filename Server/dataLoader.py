from database import Database

def check_first_login(db, userID):
    con = db.connection
    cur = con.cursor()
    
    cur.execute(f'''   SELECT * FROM CUSTOMER
                   WHERE userName="{userID}" ''')
    
    if len(cur.fetchall()) < 1:
        db.close()
        return True
    db.close()
    return False


def fetch_user_info(db, user_id):
    con = db.connection
    cur = con.cursor()
    
    cur.execute(f'''   SELECT * FROM CUSTOMER
                   WHERE userName="{user_id}" ''')
    
    fetched = cur.fetchall()[0]
    user_info = []
    
    for item in fetched:
        user_info.append(item)

    db.close()
    return user_info



def load_rest(db):
    connection = db.connection
    cursor = connection.cursor()

    rest_dict = {}
    cursor.execute('''SELECT R.restName, AVG(V.rating) FROM RESTAURANT R LEFT JOIN REVIEWS V
                   ON R.restName = V.restName
                   GROUP BY restName;''')

    for name, avgRating in cursor.fetchall():
        try:
            rest_dict[name] = float(avgRating)
        except:
            rest_dict[name] = 0
            
    db.close()
    return rest_dict


def load_items(db, rest_name):
    connection = db.connection
    cursor = connection.cursor()

    item_dict = {}
    cursor.execute(f'''SELECT itemID, itemName, itemDesc, subCategory, price FROM ITEM
                   WHERE restName = "{rest_name}";
                   ''')
    
    for id, name, desc, subC, price in cursor.fetchall():
        item_dict[id] = [name, desc, subC, int(price), rest_name]
    
    subC_list = []
    
    for key in item_dict.keys():
        subC = item_dict[key][2]
        subC_list.append(subC)
    
    subC_list = set(subC_list)
    
    item_dict['subC_list'] = subC_list
    
    db.close()
    
    return item_dict


def check_if_reviewed(db, restName, userName):
    
    from datetime import date
    con = db.connection
    cur = con.cursor()
    
    cur.execute(f'''SELECT DAY(postDate), MONTH(postDate), YEAR(postDate) FROM REVIEWS 
                WHERE userName = "{userName}" AND restName = "{restName}"; ''')

    today = date.today()
    for d, m, y in cur.fetchall():
        if d == today.day and m == today.month and y == today.year:
            db.close()
            return True
    db.close()
    return False

def insert_review(db, restName, userName, rating, comment):
    con = db.connection
    cur = con.cursor()
    from datetime import date
    t = date.today()
    cur.execute(f'''INSERT INTO REVIEWS
                VALUES ("{userName}", "{restName}", "{t.year}-{t.month}-{t.day}", {rating}, "{comment}")''')
    
    con.commit()
    
    
    db.close()
    return

def load_item_data(db , itemID):
    con = db.connection
    cur = con.cursor()
    
    itemID = int(itemID)
    ## Getting Item Information
    cur.execute(f''' SELECT DISTINCT I.itemID, I.restName, I.itemName, I.itemDesc, I.subCategory, I.price
                FROM ITEM I WHERE I.itemID = {itemID}''')
    
    items = []
    
    res = cur.fetchall()

    cur.reset()

    for content in res[0]:
        items.append(content)
        
    ## Getting Options
    cur.execute(f''' SELECT DISTINCT O.optionID, O.optionName
                FROM ITEM I, test1.OPTION O, HASOPTION HO WHERE I.itemID = HO.itemID AND O.optionID = HO.optionID AND I.itemID = {itemID}''')
    
    options = {}
    
    res = cur.fetchall()

    cur.reset()

    for id, name in res:
        options[id] = name

    ## Getting Combos
    cur.execute(f''' SELECT DISTINCT C.comboID, C.subCategory
                FROM ITEM I, HASCOMBO HC, COMBO C WHERE I.itemID = HC.itemID AND HC.comboID = C.comboID AND I.itemID = {itemID}''')
    
    combos = {}
    
    res = cur.fetchall()

    cur.reset()

    for id, subC in res:
        if combos.get(id, None) is None:
            combos[id] = set()
            
        combos[id].add(subC)
    
    for id in combos:
        comb_str = "" 
        for item in combos[id]:
            comb_str = comb_str + "" + item + " "
        comb_str = comb_str[0:-1]
        combos[id] = comb_str
        
    
    return items, options, combos

def fetch_unfinished_order(db, userID):
    con = db.connection
    cur = con.cursor()
    
    cur.execute(f'''SELECT orderID FROM test1.ORDER WHERE userName = '{userID}' AND orderTime IS NULL;''')
    res = cur.fetchall()
    if len(res) < 1:
        return 
    else:

        return res[0][0]

def create_order(db, userID):
    con = db.connection
    cur = con.cursor()
    
    cur.execute(''' SELECT MAX(orderID) FROM test1.ORDER; ''')
    
    X = int(cur.fetchall()[0][0])
    
    cur.reset()
    cur.execute(f'''INSERT INTO test1.ORDER VALUES ( {X+1} , '{userID}', NULL, NULL, 30000, NULL, NULL )''')
    con.commit()
    db.close()
    return X+1

def create_inst(db, comb, specI):
    con = db.connection
    cur = con.cursor()
    
    cur.execute(''' SELECT MAX(instID) FROM INSTRUCTIONS; ''')
    
    X = int(cur.fetchall()[0][0])
    
    cur.reset()
    
    cur.execute(f'''INSERT INTO INSTRUCTIONS 
                VALUES ( {X+1}, {comb}, "{specI}"  );''')
    
    con.commit()
    
    db.close()
    
    return X+1
    
def modify_inst(db, inst_id, comb, specI):
    con = db.connection
    cur = con.cursor()
    
    cur.execute(f'''UPDATE INSTRUCTIONS 
                SET comboID={comb}, specInstructions="{specI}"
                WHERE instID = {inst_id};''')
    
    con.commit()
    
    db.close()
    
    return
    
    
def create_excludes(db, instID, options):
    con = db.connection
    cur = con.cursor()
    for key in options.keys():
        cur.execute(f''' INSERT INTO EXCLUDES
                    VALUES ( {instID}, {options[key]} )''')
        con.commit()
    
    db.close()
    return

def modify_excludes(db, instID, options):
    con = db.connection
    cur = con.cursor()
    
    cur.execute(f''' DELETE FROM EXCLUDES
                WHERE instID = {instID};''')
    con.commit()

    for key in options.keys():
        cur.execute(f''' INSERT INTO EXCLUDES
                    VALUES ( {instID}, {options[key]} )''')
        con.commit()
    
    db.close()
    return

def create_cont(db, order_id, itemID, instID):
    con = db.connection
    cur = con.cursor()
    cur.execute(f''' INSERT INTO test1.CONTAINS
                VALUES ( {order_id}, {itemID}, {instID} ) ''')
    con.commit()
    db.close()
    return

def get_order_info(db, order_id):
    con = db.connection
    cur = con.cursor()
    

    cur.execute(f'''SELECT I.itemID, INS.instID, I.itemName, I.restName, I.price, INS.specInstructions, CM.subCategory, 
                CM.price, OP.optionName, O.delivFee FROM test1.ORDER O NATURAL JOIN test1.CONTAINS C NATURAL JOIN INSTRUCTIONS INS
                NATURAL JOIN COMBO CM NATURAL JOIN EXCLUDES E NATURAL JOIN test1.OPTION OP, ITEM I
                    WHERE I.itemID = C.itemID AND orderID = {order_id};''')
    
    dicts = cur.fetchall()
    
    if len(dicts) == 0:
        return None

    order_info = {}
    for itID, ins, item, rest, price, specI, subC, cPrice, oName, fee in dicts:
        order_info[ins] = [[item, rest, price, specI, itID], [], []]

    order_info['fee'] = int(dicts[0][9])
    
    for itID, ins, item, rest, price, specI, subC, cPrice, oName, fee in dicts:    
        order_info[ins][1].append((subC, cPrice))
        order_info[ins][1] = list(set(order_info[ins][1]))
    
    for itID, ins, item, rest, price, specI, subC, cPrice, oName, fee in dicts:
        if oName not in order_info[ins][2]:    
            order_info[ins][2].append(oName)
    
    db.close()
    return order_info


def get_filled_info(db, item_id, order_id, inst_id):
    con = db.connection
    cur = con.cursor()
    
    cur.execute(f'''SELECT INS.specInstructions, CM.comboID,
            OP.optionID FROM test1.ORDER O NATURAL JOIN test1.CONTAINS C NATURAL JOIN INSTRUCTIONS INS
            NATURAL JOIN COMBO CM NATURAL JOIN EXCLUDES E NATURAL JOIN test1.OPTION OP, ITEM I
                WHERE I.itemID = C.itemID AND orderID = {order_id} AND INS.instID = {inst_id} AND I.itemID = {item_id};''')

    dicts = cur.fetchall()
    
    if len(dicts) == 0:
        return None

    cust_info = []
    for specI, combID, oID in dicts:
        cust_info = [specI, combID, []]
    
    for specI, combID, oID in dicts:
        if oID not in cust_info[2]:    
            cust_info[2].append(oID)
    
    db.close()
    return cust_info


def close_order(db, order_id):
    con = db.connection
    cur = con.cursor()

    cur.execute(f''' SELECT D.driverID FROM DRIVER D, test1.ORDER O
                WHERE D.driverID = O.driverID AND arrivalTime IS NOT NULL;''')

    available_drivers = cur.fetchall()
    drivers = []
    for driver in available_drivers[0]:
        drivers.append(driver)

    from random import randint
    
    rand_index = randint(0, len(drivers) - 1)
    
    driver_id = drivers[rand_index]

    cur.reset()

    cur.execute(f''' UPDATE test1.ORDER 
                SET orderTime = CURRENT_TIME(), driverID = {driver_id}, orderDate = CURRENT_DATE()
                WHERE orderID = {order_id}''')
    con.commit()
    
    db.close()
    return


def delete_record(db, inst_id):
    con = db.connection
    cur = con.cursor()
    
    cur.execute(f''' DELETE FROM EXCLUDES
                WHERE instID = {inst_id};''')
    con.commit()

    cur.execute(f''' DELETE FROM CONTAINS
                WHERE instID = {inst_id};''')
    con.commit()
    
    cur.execute(f''' DELETE FROM INSTRUCTIONS   
                WHERE instID = {inst_id};''')
    con.commit()
    
    db.close()
    return


def initiate_db(file_list):
    db = Database('test1') 
    for file in file_list:
        with open(f'Server/DBs/{file}', 'r') as f:
            
            db.connection.reconnect()
            
            cursor = db.connection.cursor()
            query = f.read()
            res = cursor.execute(query)
            

    db.close()

if __name__ == '__main__':
    # initiate_db([
    #     'test1_accounts.sql',
    #     'test1_restaurant.sql',
    #     'test1_customer.sql',
    #     'test1_reviews.sql',
    #     'test1_item.sql',
    #     'test1_hasoption.sql',
    #     'test1_option.sql',
    #     'test1_hascombo.sql',
    #     'test1_combo.sql',
    #     'test1_order.sql',
    #     'test1_instructions.sql',
    #     'test1_contains.sql',
    #     'test1_excludes.sql',        
    #     'test1_driver.sql'   
    # ])
    pass