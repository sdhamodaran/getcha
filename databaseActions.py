#!/usr/bin/python
import psycopg2
def connect():
    try:
        conn = psycopg2.connect(database='camuto_dev',user='dhamodaran')
        cur = conn.cursor()
        return cur
    except:
        return None

def imageCount():
    cursor = connect()
    if cursor is not None:
        try:
            cursor.execute("SELECT id FROM Images;")
            ids = cursor.fetchall()
            properlyFormedIds = [x[0] for x in ids]

            return properlyFormedIds
        except:
            return None
    else:
        print "connection not established"


def fetchURL(randomNumber):
    cursor = connect()
    if cursor is not None:
        try:
            cursor.execute("Select filename from Images where id="+str(randomNumber)+";")
            name = cursor.fetchone()
            return name
        except:
            return None
    else:
        print "Connection issue"        
