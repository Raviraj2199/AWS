with phone numbver int 

import psycopg2


connection = psycopg2.connect(
    host = "ola201-vishtejpostgre01.cluster-caddif7rrut7.ap-south-1.rds.amazonaws.com",
    port = 5432,
    user = 'postgsuperuser',
    password = 'password1!',
    database='postgmaindb'
    )
cursor=connection.cursor()



cursor.execute("""CREATE TABLE IF NOT EXISTS phonebookint(phone INT, firstname VARCHAR(32), lastname VARCHAR(32), address VARCHAR(64))""")

print("table has been created ")

print("please enter the details")

fn=input("please enter your first name ---->")
ln=input("please enter your last name ---->")
phn=int(input("please enter your phone no ---->"))
addr=input("please enter your address ---->")


sql1 = """INSERT INTO phonebookint(phone, firstname, lastname, address) VALUES('%d','%s','%s','%s')""" %(phn,fn,ln,addr)
cursor.execute(sql1)



connection.commit()

postgreSQL_select_Query = "SELECT * FROM phonebookint ORDER BY firstname"

cursor.execute(postgreSQL_select_Query)
print("Selecting rows from mobile table using cursor.fetchall")
records = cursor.fetchall() 

print(records)
cursor.close()
connection.close()
