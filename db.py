
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def save_session(conn, session):
    """
    Create a new sesson
    :param conn:
    :param session:
    :return:
    """

    sql = ''' INSERT INTO sessions(task,date,time)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (session.task,session.date,session.time))
    conn.commit()
    conn.close()
    return cur.lastrowid


def select_all_sessions(conn):
    """
    Query all rows in the sessions table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM sessions")

    rows = cur.fetchall()
    conn.close()
    for row in rows:
        print(row)


def init_db():
    conn = create_connection("db.sqlite3")
    sql_create_sessions_table = """CREATE TABLE IF NOT EXISTS sessions (
                                    id integer PRIMARY KEY,
                                    task text NOT NULL,
                                    date text NOT NULL,
                                    time integer NOT NULL
                                );"""
    create_table(conn, sql_create_sessions_table)
    return conn
