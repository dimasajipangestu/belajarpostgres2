#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
    con = psycopg2.connect("host='localhost' dbname='testdb' user='pythonspot' password='Dimas98@srg'")
    cur = con.cursor()
    cur.execute("UPDATE Dimas SET Name = 'Hai' WHERE Id = 2")
    #cur.execute("CREATE TABLE Dimas(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    #cur.execute("INSERT INTO Dimas VALUES(1,'Dimas',2)")
    #cur.execute("INSERT INTO Dimas VALUES(2,'Aji',2)")
    #cur.execute("INSERT INTO Dimas VALUES(3,'Pangestu',2)")
    #cur.execute("INSERT INTO Dimas VALUES(4,'Bread',5)")
    #cur.execute("INSERT INTO Dimas VALUES(5,'Oranges',3)")
    con.commit()
except psycopg2.DatabaseError as e:
    if con:
        con.rollback()

    print('Error %s') % e
    sys.exit(1)

finally:
    if con:
        con.close()
