from flask import Flask, request, render_template,jsonify
from db.create import createTables, createUser
from db.GetUsers import getAllusers, getSpecificUsers
from db.UserOperation import updateUserAccess

app = Flask(__name__)

@app.route('/createUser', methods = ['POST'])
def create_user():
    
    name = request.form['name']
    password = request.form['password']
    address = request.form['address']
    email = request.form['email']
    phone = request.form['phone']
    pincode = request.form['pincode']

    dbRes = createUser(name= name, password= password, Email= email, Address= address, Phone= phone, PinCode= pincode)
    if dbRes==True:
        return jsonify({'success':200,"message":"Seccessfully created"})
    else:
        return jsonify({'Error':404,"message":"Unable to create User"})


@app.route('/getAllusers', methods = ['GET'])
def getAllUser():
    return getAllusers()

@app.route('/getSpecificUser', methods = ['GET'])
def getSpecificUser():
    userID = request.form['userID']
    return getSpecificUsers(userId=str(userID))

@app.route('/updateUserAccess', methods = ['PATCH '])
def updateUser_Access():
    userId = request.form['userID']
    approved = request.form['approved']
    blocked = request.form['blocked']
    updateUserAccess(id=userId, approved=approved, blocked=blocked)
    return "access updated successfully"

@app.route('/', methods = ['GET'])
def hello():
    return "Hello"

if __name__ == "__main__":
    # createTables()
    app.run()