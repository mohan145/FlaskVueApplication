
from ..model.order import  Order
from ..util.db_engine import  session

def insert_order(customer_id, product_list):
    order_object  = Order()
    order_object.CustomerId = customer_id
    session.add(order_object)
    session.commit()


    
