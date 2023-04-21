from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

# # creating a Flask app
# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# # on the terminal type: curl http://127.0.0.1:5000/
# # returns hello world when we use GET.
# # returns the data that we send when we use POST.

# @cross_origin()
# @app.route('/', methods = ['GET'])
# def home():
#     if(request.method == 'GET'):
#         data = "hello world"
#         return jsonify({'data': data})

# # A simple function to calculate the square of a number
# # the number to be squared is sent in the URL when we use GET
# # on the terminal type: curl http://127.0.0.1:5000 / home / 10
# # this returns 100 (square of 10)

# @cross_origin()
# @app.route('/home/<int:num>', methods = ['GET'])
# def disp(num):
#     return jsonify({'data': num**2})

# # driver function
# if __name__ == '__main__':
#     app.run(debug = True)
  
app =   Flask(__name__)

cors = CORS(app)

@cross_origin()
@app.route('/', methods = ['GET'])
def ReturnJSON():
    _data = {
            "stud1" : { "Modules" : 15,
                        "Subject" : "Data Structures and Algorithms",
            },
        }

    if(request.method == 'GET'):
        data = _data
        return jsonify(data)
  
if __name__=='__main__':
    app.run(debug=True)