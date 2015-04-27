#!C:\Python34\python.exe

import cgi, sqlite3

def htmlTop(html):
    print("""<!DOCTYPE html>
            <html>
            <head>
            </head>
            <body>

            <table style="width:100%"; border="1"; padding="3px" >
              <tr>
                <th>Name</th>
                <th>Price</th>		
                <th>Type</th>
              </tr> {0}""".format(html))


def htmlTail():
    print("""</table>
            </body>
             </html>""")

def getData():
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

def saveToDatabase(info):
    data = ( info[0], info[1], str(info[2]),)
    with sqlite3.connect("ScriptingDatabase.db") as db:
        cursor = db.cursor()
        sql = "insert into Item (ItemName, ItemPrice, TypeName) values (?,?,?)"
        cursor.execute(sql, data)

def getProductHtml():
    with sqlite3.connect("ScriptingDatabase.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * from Item")
        productList = cursor.fetchall()

        html = ""
        for item in productList:
            name = item[1]
            price = str(item[2])
            drinkType = str(item[3])
            html += ("""<tr>
                            <td>"""+ name +"""</td>
                            <td>"""+ price +"""</td>		
                            <td>"""+ drinkType +"""</td>
                        </tr>
                    """)
    return html
    
def main():
    try:
        dataList = getData()
        saveToDatabase(dataList)
        html = getProductHtml()
        htmlTop(html)
        htmlTail()
    
    except:
        cgi.print_exception()

if __name__ == '__main__':
    main()
