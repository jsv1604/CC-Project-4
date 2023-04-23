from flask import Flask,request
from flask_restful import Resource,Api
import math


app = Flask(__name__)
api = Api(app)


class Gcd(Resource):
    def get(self,x,y):
        x = int(float(x))
        y = int(float(y))
        return math.gcd(x,y)

api.add_resource(Gcd,'/gcd/<x>/<y>')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5005)

