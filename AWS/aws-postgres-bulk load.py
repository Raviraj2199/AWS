import psycopg2


connection = psycopg2.connect(
    host = "ola201-ravirajpostgre01.cluster-caddif7rrut7.ap-south-1.rds.amazonaws.com",
    port = 5432,
    user = 'postgsuperuser',
    password = 'password1!',
    database='postgmaindb'
    )
cursor=connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tripinfo(
id SERIAL PRIMARY KEY,
pclass integer,
ticket text,
fare float,
cabin text,
embarked text)""")

connection.commit()

with open('trip_info.csv', 'r') as row:
    next(row)
    cursor.copy_from(row, 'tripinfo', sep=',')

connection.commit()
