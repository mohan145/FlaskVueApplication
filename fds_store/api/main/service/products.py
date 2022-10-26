
from ..model.product import  Product
from ..util.db_engine import  session


class Products:

    @staticmethod
    def get_all_products():

        products = session.query(Product).with_entities(Product.Name,Product.Description).all()
        if products is not None and len(products) > 0 :
            items = []
            for item in products:
                items.append(dict(item))
            return items
        return {}

    








