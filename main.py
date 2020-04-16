from belajarpostgres3 import get
import psycopg2

import schedule
import time

getdata = get()

def get_hostip():
    con = psycopg2.connect("host='localhost' dbname='testdb' user='pythonspot' password='Dimas98@srg'")
    cur = con.cursor()
    cur.execute("SELECT ip FROM hosttable")
    hostip = []

    while True:
        row = cur.fetchone()


        if row == None:
            return hostip
            break
        else:
            hostip.append(''.join(row))

def runget():
    ips = get_hostip()
    print(ips)
    for ip in ips:
        get().getdata(ip, 161)
        print("done")
        print("")
        print("")


schedule.every(1).minutes.do(runget)

while True:

    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)