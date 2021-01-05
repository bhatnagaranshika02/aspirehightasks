from flask import Flask,request 
app = Flask('__main__')

@app.route('/CreateDish',methods=['POST'])
def CreateDish():
	username = request.form["username"]
	password = request.form["password"]
	dishName = request.form["dishName"]
	dishCost = request.form["dishCost"]
@app.route('/UpdateDish',methods=['GET','POST'])
def UpdateDish():
	username = request.form["username"]
	password = request.form["password"]
	image = request.form["image"]
	dishName = request.form["dishName"]
	dishCost = request.form["dishCost"]
	return "Dish Updated"
	

@app.route('/ExistingDish',methods=["GET"])
def ExistingDish():
	username = request.form["username"]
	password = request.form["password"]

@app.route('/DishInfo',methods=['GET'])
def DishInfo():
	username = request.form["username"]
	password = request.form["password"]

@app.route('/DeleteDish',methods=['DELETE'])
def DeleteDish():
	username = request.form["username"]
	password = request.form["password"]
	

app.run()
