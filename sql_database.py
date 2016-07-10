""" module for creating and operating the database """

import sqlite3

conn = sqlite3.connect("names1.db")
c = conn.cursor()

def table(table_name, name, age, Id):
    """ creates the tables for different users """

    try:
        c.execute("CREATE TABLE IF NOT EXISTS table_"+ table_name +"(ID INT, NAME TEXT, AGE REAL)")
    except sqlite3.OperationalError:
        return "Table creation Failed"
    
    c.execute("INSERT INTO table_" + table_name + "(ID, NAME, AGE) VALUES (?, ?, ?)", (Id, name, age))
    
    #commit will save the operation performed on the table
    conn.commit()
    
def read_db(table_name):
    """ prints the database """

    try:
        c.execute("SELECT * FROM table_"+table_name)
        db = c.fetchall()
        for row in db:
            print("name {} age {} ".format(row[1] ,row[2]))
    except sqlite3.OperationalError:
        return "Data Fetching failed"

def update(table_name, age, Id):
    """ updates the table """

    c.execute("UPDATE table_"+table_name+" SET AGE=? WHERE ID=?",(age, Id))
    conn.commit()

def delete(table_name):
    c.execute("DELETE FROM table_"+table_name+" WHERE ID=3")
    conn.commit()
    
table("self", "NAME1", 21, 1)
table("self", "NAME2", 22, 2)              
table("self", "NAME3", 23, 3)              

print(" Database ")
db = read_db("self")

update("self", 25, 2)
print(" Database after Update")
db = read_db("self")

delete("self")
print(" Database after Deletion")
db = read_db("self")

conn.close()
