#!C:\Python34\python.exe

import cgi, sqlite3

def htmlTop():
    print("""Content-type:text\html\n\n
             <!DOCTYPE html>
             <html lang ='en'>
             <head>
             <title> My First Script </title>
             <meta charset='utf-8'/>
             </head>
             <body>""")

def htmlTail():
    print("""</body>
             </html>""")

def get_data():
    values = cgi.FieldStorage()
    name = values.getvalue("nameInput")
    price = values.getvalue("priceInput")
    itemType = values.getvalue("typeInput")
    dataList = [name, price, itemType]
    return dataList

def create_table(db_name,table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        cursor.execute("drop table if exists {0}".format(table_name))
        cursor.execute(sql)
        db.commit()

        
def main():
    try:
        htmlTop()
        dataList = get_data()
        print("<h1> Hello {0} </h1>".format(firstName.capitalize()))
        htmlTail()
    
    except:
        cgi.print_exception()

if __name__ == '__main__':
    main()
