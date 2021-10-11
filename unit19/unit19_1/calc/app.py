# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_op():
    '''Add the given numbers'''
    a = request.args['a']
    b = request.args['b']
    result = f'''
        <html>
        <body>
            <h1>Add</h1>
            <p>{a} + {b} = {add(int(a),int(b))}</p>
        </body>
    </html>
    '''
    return result

@app.route('/sub')
def sub_op():
    '''Subtract b from a'''
    a = request.args['a']
    b = request.args['b']
    result = f'''
        <html>
        <body>
            <h1>Subtract</h1>
            <p>{a} - {b} = {sub(int(a),int(b))}</p>
        </body>
    </html>
    '''
    return result

@app.route('/mult')
def mult_op():
    '''Multiply a and b'''
    a = request.args['a']
    b = request.args['b']
    result = f'''
        <html>
        <body>
            <h1>Multiply</h1>
            <p>{a} x {b} = {mult(int(a),int(b))}</p>
        </body>
    </html>
    '''
    return result

@app.route('/div')
def div_op():
    '''divide a by b'''
    a = request.args['a']
    b = request.args['b']
    result = f'''
        <html>
        <body>
            <h1>Divide</h1>
            <p>{a} / {b} = {div(int(a),int(b))}</p>
        </body>
    </html>
    '''
    return result

@app.route('/math/<operator>')
def math_operation(operator):
    a = int(request.args['a'])
    b = int(request.args['b'])
    operators = {
        'add': add(a,b),
        'sub': sub(a,b),
        'mult': mult(a,b),
        'div': div(a,b)
    }
    op = operators.get(operator, 'Operator Not Found')
    result = f'''
    <p>The operator is: {operator}</p> 
    <p>a = {a}</p> 
    <p> b = {b}</p>
    <p> The result is {op}</p>
    '''
    return result