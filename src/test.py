import mysql.connector
from util import *
import flask

def get_results(time):
    try:
        mydb = connect_to_db()
    except mysql.connector.Error as error:
        print("failed to connect", error)
        return error
    res = get_html_results(time)

    if res:
        for x in res:
            print(x[0],x[1])

    return str(res)


# print(get_results('16'))