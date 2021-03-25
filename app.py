from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/",methods = ['POST', 'GET'])
def home():
    return render_template("index.html")

@app.route("/<query>")
def result(query):
    return render_template("index.html")

@app.route('/search',methods = ['POST', 'GET'])
def search():
	if request.method == 'POST':
		string = request.form['srch']
		return redirect(url_for('result',query = string))
	else:
		string = request.args.get('srch')
		return redirect(url_for('result',query = string))

if __name__ == "__main__":
	app.run(host="localhost", port=8000, debug=True)