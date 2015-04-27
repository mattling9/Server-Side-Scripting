#!C:\Python34\python.exe

import sqlite3, cgi


def htmlTop(html):
    print("""Content-type:text\html\n\n
    <!DOCTYPE html>
    <html lang ='en'>
    <head>
    <title> My First Script </title>
    <meta charset='utf-8'/>
    </head>
    <body>
    <form method="post" action="/cgi-bin/list.py">
    <strong>Name: </strong> <input type="text" name="nameInput" placeholder="eg Latte..." autofocus required><br><br>
    <strong>Price: </strong> <input type="number" name="priceInput" placeholder="00.00" step="0.01" required><br><br>
    <strong>Type: </strong> <select name="typeInput"> <br><br> {0}""".format(html))
    

def addItems(itemList):
    html = ""
    for item in itemList:
        html += ("<option>"+ str(item[0]) +"</option>")
    html += ("</select>")
    return html

def htmlTail():
    print("""
    <input type="submit" value="Submit">
    </form>
    </body>
    </html>""")

def getTypes():
    with sqlite3.connect("ScriptingDatabase.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT TypeName From ItemType")
        itemTypes = cursor.fetchall()
    return itemTypes

def main():
    try:
        itemList = getTypes()
        html = addItems(itemList)
        htmlTop(html)
        htmlTail()
        
    except:
        cgi.print_exception()
        
if __name__ == '__main__':
    main()
