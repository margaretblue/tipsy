"""
model.py
"""
import sqlite3

def connect_db():
    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):          
    c = db.cursor()                                     
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""                                                           
    result=c.execute(query, (email, password, name))
    db.commit()
    return result.lastrowid

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))

    return None

def get_user(db, user_id):
    """Gets a user dictionary out of the database given an id"""
    c = db.cursor()
    query = """SELECT * FROM Users WHERE user_id=?"""
    c.execute(query, (user_id))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "username"]
        return dict(zip(fields, result))

    return None

def new_task(db, title, user_id):

    """Given a title and a user_id, create a new task belonging to that user. Return the id of the created task"""
    c= db.cursor()
    query="""INSERT INTO Tasks VALUES (NULL, ?, datetime('now'), NULL, ?)"""
    result=c.execute(query,(title,user_id))
    db.commit()
    return result.lastrowid

def complete_task(db, task_id):
    """Mark the task with the given task_id as being complete."""
    c = db.cursor()
    query="""UPDATE Tasks SET completed_at = datetime('now') WHERE task_id=?"""
    result = c.execute(query,(task_id))
    db.commit()
    return None

def get_tasks(db, user_id=None):
    """Get all the tasks matching the user_id, getting all the tasks in the system if the user_id is not provided. Returns the results as a list of dictionaries."""
    c=db.cursor()
    query="""SELECT * FROM Tasks WHERE user_id=?"""
    c.execute(query,(user_id))
    result = c.fetchone()
    if result:
        fields=["task_id", "title","created_at", "completed_at", "user_id"]
        return dict(zip(fields,result))
    return None

def get_task(db, task_id):
    """Gets a single task, given its id. Returns a dictionary of the task data."""
    c=db.cursor()
    query = """SELECT title FROM Tasks WHERE task_id=?"""
    c.execute(query,(task_id))
    result = c.fetchone()
    if result:
        fields=["title"]
        return dict(zip(fields, result))
    return None