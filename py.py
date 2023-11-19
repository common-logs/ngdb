from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
 
app = Flask(__name__)

db_client = MongoClient('localhost', 27017)
db = db_client['tree_database']
tree = db['tree']

db_login = db_client['tree_login']
login_user = db_login['login']

user = "admin@gmail.com"
password = ""

@app.route('/index/<name>', methods = ['POST', 'GET'])
def index(name):
		name = name.split('@')
		return render_template("index.html", name = name[0])

@app.route('/add', methods = ['POST', 'GET'])
def add():
		global tree
		global user

		val = list(tree.find())
		print(val)

		if request.method == 'GET':
				val = list(tree.find())
				print(val)

				loca = request.args.get('loca')
				area = request.args.get('area')
				tree_name = request.args.get('tree')
				count = int(request.args.get('count'))

				tree_info = {}

				val = list(tree.find({"location" : loca}))
				print(val)

				if not val:
					tree_info['location'] = loca
					tree_info['area'] = area
					tree_info['tree'] = [{"name": tree_name, "count": count}]
					tree.insert_one(tree_info)
				else:
					val = list(tree.find({"$and": [{"location": loca}, {"tree": {"$elemMatch": {"name": tree_name}}}]}))

					if not val:
						tree.update_one({"location": loca}, {"$push": {"tree": {"name": tree_name, "count": count}}})
					else:
						for i in val[0]['tree']:
							print(i)
							if i['name'] == tree_name:
								count = i['count'] + count
								tree.update_one({"location": loca}, {"$pull": {"tree": {"name": tree_name}}})
								tree.update_one({"location": loca}, {"$push": {"tree": {"name": tree_name, "count": count}}})

				print(list(tree.find()))

		return redirect(url_for('index', name = str(user)))

@app.route('/view', methods = ['POST', 'GET'])
def view():
		global tree

		data = list(tree.find())

		return render_template("view.html", data = data);

@app.route('/login', methods = ['POST', 'GET'])
def login():
		global user
		global password
		global login_user

		if request.method == 'POST':
				user = request.form['user']
				password = request.form['password']

				val = list(login_user.find({"users": {"$elemMatch": {"user": "admin"}}}))
				print("val = {} password = {}".format(val, password))

				if val[0]["users"][0]["password"] != password:
					print("password = {} password = {}".format(val[0]["users"][0]["password"], password))
					return render_template("login.html")

				return redirect(url_for('index', name = str(user)))

@app.route('/', methods = ['POST', 'GET'])
def login_view():
		return render_template("login.html");
 
if __name__ == '__main__':
    app.run(debug = True)
