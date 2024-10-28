from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)
ma = Marshmallow(app)

class CustomerSchema(ma.Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ("name", "email", "phone")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

@app.route('/')
def home():
    return "Welcome to Flask Music Festival!"

if __name__ == "__name__":
    app.run(debug=True)