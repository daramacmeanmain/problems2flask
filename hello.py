from flask import Flask
app = Flask(__name__)

@app.route('/name/<name>') 
def fname(name): 
	return 'Your name is ' + name
	
@app.route("/")
def hello():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()