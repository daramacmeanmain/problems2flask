from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/name', methods=['GET']) 
def fname(): 
	return 'Your name is ' +  request.values["name"]
	
@app.route("/")
def hello():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()