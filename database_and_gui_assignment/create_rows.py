def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(id, major, begin_date, end_date)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid # returns the row id of the cursor object, the student id

