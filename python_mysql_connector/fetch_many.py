from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def iter_row(cursor, size=10):
    """ a generator for chunk data
    :param cursor: database cursor
    :param size: size of chunks
    :yield: a row of result(s)
    """
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def query_with_fetchmany():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users")
        
        for row in iter_row(cursor, 10):
            print(row)
            
    except Error as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()
