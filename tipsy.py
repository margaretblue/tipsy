"""
tipsy.py -- A flask-based todo list
"""
from flask import Flask, render_template, redirect, request, session, g
import model



app = Flask(__name__)

#configuration
app.secret_key = 'admin'

@app.before_request
def set_up_db():
	g.db = model.connect_db()

@app.route("/")
def index():
    return render_template("index.html", user_name="chriszf")

@app.route("/login")
def login():
	error="no error"
	return render_template("login.html" , error=error)

@app.route("/logout")
def logout():
	session.pop('user_id', None)
	print session
	return redirect("/")

@app.route("/authenticate", methods=["POST"])
def authenticate():
	email=request.form['email']
	password=request.form['password']
	user_id=model.authenticate(g.db, email, password)
	if user_id == None:
		error="no user with that combination"
		return render_template("/login.html", error=error)
	session['user_id']=user_id
	return redirect("/tasks")

@app.route("/new_user")
def new_user():
 	return render_template("new_user.html")


@app.route("/save_user", methods=["POST"])
def save_user():
	email = request.form['email']
	password = request.form['password']
	name = request.form['name']
	user_id=model.new_user(g.db, email, password, name)
	session['user_id']=user_id
	return redirect("/tasks")

@app.route("/save_task", methods=["POST"])
def save_task():
    title = request.form['title']
    user_id=session['user_id']
    model.new_task(g.db, title,user_id)
    return redirect("/tasks")

@app.route("/tasks")
def list_tasks():
	print session
	user_id = session.get('user_id', None)
	tasks_from_db = model.get_tasks(g.db, user_id)
	return render_template("list_tasks.html", tasks=tasks_from_db)

@app.route("/completed_task/<int:task_id>", methods=["POST"])
def completed_task(task_id):
	model.complete_task(g.db, task_id)
	return redirect("/tasks")


@app.route("/task/<int:id>", methods=["GET"])
def view_task(id):
    task_from_db = model.get_task(g.db, id)
    return render_template("view_task.html", task=task_from_db)

@app.route("/task/<int:id>", methods=["POST"])
def complete_task(id):
    model.complete_task(g.db, id)
    return redirect("/tasks")

@app.route("/set_date")
def set_date():
	session['date'] = datetime.datetime.now()
	return "Date set"

@app.route("/get_date")
def get_date():
	return str(session['date'])

@app.teardown_request
def disconnect_db(exception):
	g.db.close()

if __name__ == "__main__":
    app.run(debug=True)