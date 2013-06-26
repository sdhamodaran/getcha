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
    try:
        cursor.execute("Select id from Images")
        ids = cursor.fetchall
        properlyFormedIds = [x[0] for x in ids]
        return len(properlyFormedIds), properlyFormedIds
    except:
        return "Cursor error"

def fetchURL(randomNumber):
    cursor = connect()
    try:
        cursor.execute("Select name from Images where id= ")
        name = cursor.fetchone()
        return name
    except:
        return None
        
