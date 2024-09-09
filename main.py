from flask import Flask
from getUsers import app1
from Companies import app2

app = Flask(__name__)

app.register_blueprint(app1)
app.register_blueprint(app2)

if __name__ == '__main__' : 
    app.run(debug=True)



    