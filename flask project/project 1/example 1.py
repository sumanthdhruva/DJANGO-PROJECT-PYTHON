from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/a')
def hello1():
    return 'welcome to PFSD'
@app.route('/emp/<int:emp1>')
def show_emp(emp1):
    return 'Emp id number %d' %emp1
@app.route('/empl/<float:emp2>')
def show_empl(emp2):
    return 'Emp id number in float %f' %emp2
@app.route('/ex1')
def index():
    return render_template('hello.html')

if __name__=="__main__":
    app.run(debug=True)