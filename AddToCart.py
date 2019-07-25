import pymysql


def addToCart(order_id, item_id, quantity):
    if checkQuantity(item_id, quantity):
        connection = pymysql.connect(host="localhost",
                                     user="root",
                                     password=None,
                                     db="grocerytech",
                                     charset="utf8mb4")

        cursor = connection.cursor()
        update = ('INSERT INTO SELECTITEM VALUES ({}, {}, {});'.format(item_id, quantity, order_id))
        cursor.execute(update)
        connection.commit()

        new_quantity = newQuantity(item_id, quantity)
        quant = ('UPDATE ITEM WHERE item_id={} SET quantity={};'.format(item_id, new_quantity))
        cursor.execute(quant)

        connection.commit()

        connection.close()

    else:
        return



def checkQuantity(item_id, quantity):
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 password=None,
                                 db="grocerytech",
                                 charset="utf8mb4")

    print("connection is ok")

    cursor = connection.cursor()

    select = ('SELECT quantity FROM ITEM WHERE item_id={};'.format(item_id))
    cursor.execute(select)
    found = int(cursor.fetchone()[0])

    connection.close()

    if quantity > found:
        return False

    return True

def newQuantity(item_id, quantity):
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 password=None,
                                 db="grocerytech",
                                 charset="utf8mb4")

    cursor = connection.cursor()

    select = ('SELECT quantity FROM ITEM WHERE item_id={};'.format(item_id))
    cursor.execute(select)
    old = cursor.fetchone()[0]

    return old - quantity
