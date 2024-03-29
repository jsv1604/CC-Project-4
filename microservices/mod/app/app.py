from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class Mod(Resource):
    def get(self, x, y):
        x = float(x)
        y = float(y)
        if y == 0:
            return "Error: division by zero"
        return x % y

api.add_resource(Mod,'/mod/<x>/<y>')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5006)

