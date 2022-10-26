
from ..model.order import  Order
from ..util.db_engine import  session

def insert_order(customer_id, product_list):
    order_object  = Order()
    order_object.CustomerId = customer_id
    session.add(order_object)

    # commits changes to db
    # session.commit()


    # After session Flush we'll be getting Order id

    session.flush()
    order_id = order_object.Id

    return  order_id

