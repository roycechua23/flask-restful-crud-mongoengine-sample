from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine

# Create an instance of the Flask app
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'myDatabase',
    'host': 'localhost',
    'port': 27017
}

# Create an instance of the mongo engine
db = MongoEngine()
db.init_app(app)

# Initialize the rest api instance
api = Api(app)

# Use the mongo engine to create a model of a mongodb collection
class User(db.Document):
    id = db.IntField()
    name = db.StringField(required=True, unique=True)
    age = db.IntField()

# Add the parser to be able to accept body{} content
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('age')

# Add or retrieve users to the mongodb collection
class UsersList(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

    def post(self):
        args = parser.parse_args()
        print(args)
        user = User(name=args["name"],
                    age=args["age"]).save()
        id = user.id
        return {"id": str(id), "message": "Record Added"}, 200

# Edit or delete the users 
class Users(Resource):
    def put(self, name):
        args = parser.parse_args()
        user = User.objects(name=name)
        user.update(age=args["age"])
        return {"message": "Record Updated"}, 200            

    def delete(self, name):
        args = parser.parse_args()
        user = User.objects(name=name).delete()
        return {"message": "Record Deleted"}, 200    
    
# Add the resources (API endpoints)    
api.add_resource(UsersList, '/userslist')
api.add_resource(Users, '/users/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)