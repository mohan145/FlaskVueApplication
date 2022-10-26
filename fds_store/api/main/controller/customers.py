

from flask import Blurprint,jsonify,request, make_response

from api.main.service.customers import Customer


blueprint_customer =


@blueprint_customer.route("/api/v1/customers/",methods = ["POST"])

def post():
    """ ..."""
    try:
        data = Customer.insert_customer(request.json)

        return make_response({"Status": 201, "StatusDescription": "Resource created Successfully"})

    except Exception  as ex:
        return  make_response({"Status":500,"StatusDescription": "Internal Server error"})





@blueprint_customer.route("/api/v1/customers/<int:cid>",methods = ["POST"])
def delete(cid):


