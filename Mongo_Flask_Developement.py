__author__ = 'Umesh'



import flask

from flask import Flask,render_template, request, jsonify

## Deging the API POint
app = flask.Flask(__name__)
app.config["DEBUG"] = True


employee = [
    {
        "id":101,
        "dept":"Marketing",
        "email":"hariumesh3@gmail.com"
    },

    {
        "id":102,
        "dept":"Marketing",
        "email":"umesh@gmail.com"
    },
{
        "id":103,
        "dept":"Sales",
        "email":"umesh3@gmail.com"
    },
]



## Creating the API point with the decorator
@app.route('/', methods=['GET'])
def get_page():
    return '''<h1>Distant Reading Archive</h1>
    <p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/dept', methods=['GET'])
def get_employee_details():
    #result= request.params.require('dept').permit('dept')
    return jsonify(employee)

@app.route('/calc')
def calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(sum(a,b))

def sum(a,b):
    return a+b



app.run()



