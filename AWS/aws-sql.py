import pymysql 
db = pymysql.connect(host="ola201-vishtej-auroradb-01.cluster-caddif7rrut7.ap-south-1.rds.amazonaws.com",
                     user = "admin",
                     password="password1!")
cursor = db.cursor()
sql1 = '''use maindb'''
cursor.execute(sql1)
cursor.connection.commit()
sql2 = '''create table if not exists ravirajperson ( id int not null auto_increment,fname text, lname text, primary key (id))'''
cursor.execute(sql2)
print("table is created")
print("enter firstname and lastname")
fn = input("enter the firstname")
ln = input("enter lastname")
sql3 = ''' insert into ravirajperson(fname, lname) values('%s', '%s')''' % (fn,ln)
cursor.execute(sql3)
db.commit()
#Lets select the data from above added table

sql4 = '''select * from ravirajperson'''
cursor.execute(sql4)
#cursor.fetchall()  
query_results = cursor.fetchall()
print(query_results)