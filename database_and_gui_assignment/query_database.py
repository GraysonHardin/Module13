def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows  # return the rows


def select_all_students(conn):
    """Query all rows of student table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    return rows  # return the rows


