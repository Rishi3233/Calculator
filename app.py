from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# start
@app.route('/',methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/math_raj', methods = ['POST'])
def math_operation():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = "the sum of     " + str(num1) + " and   " + str(num2) + " is  " + str(r)
       

        if(ops == 'subtract'):
            r = num1 - num2
            result = "the subtract of     " + str(num1) + " and   " + str(num2) + " is  " + str(r)
       

        if(ops == 'multiply'):
            r = num1 * num2
            result = "the multiply of     " + str(num1) + " and   " + str(num2) + " is  " + str(r)
        

        if(ops == 'divide'):
            r = num1 / num2
            result = "the divide of     " + str(num1) + " and   " + str(num2) + " is  " + str(r)


        return render_template('results.html', result = result)






# Do by using postman

@app.route('/post_man', methods = ['POST'])
def math_operation_1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = "the sum of     " + str(num1) + " and   " + str(num2) + " is  " + str(r)
       

        if(ops == 'subtract'):
            r = num1 - num2
            result = "the subtract of     " + str(num1) + " and   " + str(num2) + " is  " + str(r)
       

        if(ops == 'multiply'):
            r = num1 * num2
            result = "the multiply of     " + str(num1) + " and   " + str(num2) + " is  " + str(r)
        

        if(ops == 'divide'):
            r = num1 / num2
            result = "the divide of     " + str(num1) + " and   " + str(num2) + " is  " + str(r)


        return jsonify(result)

# end
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")
