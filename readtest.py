import psycopg2
import sys


con = None

try:
    con = psycopg2.connect("host='localhost' dbname='testdb' user='pythonspot' password='Dimas98@srg'")
    cur = con.cursor()
    cur.execute("SELECT * FROM snmptest")


    while True:
        row = cur.fetchone()
        print(row)

        if row == None:
            break

        print("OID: " + row[1] + "\tLocation: " + str(row[2]) + "\tUptime: " + str(row[3]/100/60/60/24) + " days")

except psycopg2.DatabaseError as e:
    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)

finally:
    if con:
        con.close()