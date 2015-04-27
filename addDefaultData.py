import sqlite3

def addingDefaultTypes():
    defaultTypes = ["Coffee", "Tea", "Hot Chocolate"]
    with sqlite3.connect("ScriptingDatabase.db") as db:
        cursor = db.cursor()
        for item in defaultTypes:
            itemTuple = (item,)
            sql = "insert into ItemType (TypeName) values(?)"
            cursor.execute(sql, itemTuple)
        db.commit()

def addingDefaultDrinks():
    defaultDrink = ("Espresso", "6.99", "Coffee")
    with sqlite3.connect("ScriptingDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Item (ItemName, ItemPrice, TypeName) values(?,?,?)"
        cursor.execute(sql, defaultDrink)
        db.commit()

addingDefaultDrinks()
addingDefaultTypes()
