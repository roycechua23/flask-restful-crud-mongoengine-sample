# flask-restful-crud-mongoengine-sample
A sample CRUD rest api with Flask-RESTful and Flask-MongoEngine. 

# Requirements
You will need to have a machine with **Python 3** installed. The dependencies can be installed using the terminal with the command
``` python
pip install -r requirements.txt
```

You'll also need to install **postman** ([https://www.postman.com/downloads/](https://www.postman.com/downloads/)) to test out the API endpoints (GET, POST, PUT, DELETE).

Lastly, you'll need to install **MongoDB** for the backend NoSQL Database ([https://docs.mongodb.com/manual/administration/install-community/](https://docs.mongodb.com/manual/administration/install-community/))

# Run the app
To run the app, open your terminal or commandline and run
```
python app.py
```

By default you can access it using **localhost:5000**

The two endpoints are 
- **/userslist** (for GET and POST)
- **/users/<<string:name>>** (for PUT and DELETE)

**Example:** http://localhost:5000/userslist will return all the records