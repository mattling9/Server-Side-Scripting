import sys, sqlite3

def createTable(db_name,table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        cursor.execute("drop table if exists {0}".format(table_name))
        cursor.execute(sql)
        db.commit()

def createItemTable():
    sql = """create table Item
              (ItemID integer,
              ItemName string,
              ItemPrice string,
              TypeName string,
              Primary Key(ItemID),
              foreign key(TypeName) references ItemType(TypeName))"""
    createTable("ScriptingDatabase.db", "Item", sql)

def createTypeTable():
    sql = """create table ItemType
              (TypeID integer,
              TypeName string,
              Primary Key(TypeID))"""
    createTable("ScriptingDatabase.db", "Item", sql)

def createDatabase():
    DbName = "ScriptingDatabase.db"
    createTypeTable()
    createItemTable()
createDatabase()
