from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Identity, Integer, String, text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'Customers'
    __table_args__ = {'schema': 'dbo'}

    Id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    FirstName = Column(String(250), nullable=False)
    LastName = Column(String(250), nullable=False)
    MiddleName = Column(String(250))
    IsDeleted = Column(Boolean)
    CreationDateTimeUTC = Column(DateTime, server_default=text("(now() AT TIME ZONE 'utc'::text)"))

    Orders = relationship('Orders', back_populates='Customers')


class Products(Base):
    __tablename__ = 'Products'
    __table_args__ = {'schema': 'dbo'}

    Id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    Name = Column(String(500), nullable=False)
    Description = Column(String(250))
    IsDeleted = Column(Boolean)
    CreationDateTimeUTC = Column(DateTime, server_default=text("(now() AT TIME ZONE 'utc'::text)"))

    OrderItem = relationship('OrderItem', back_populates='Products')


class Orders(Base):
    __tablename__ = 'Orders'
    __table_args__ = {'schema': 'dbo'}

    Id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    CustomerId = Column(ForeignKey('dbo.Customers.Id'))
    CreationDateTimeUTC = Column(DateTime, server_default=text("(now() AT TIME ZONE 'utc'::text)"))

    Customers = relationship('Customers', back_populates='Orders')
    OrderItem = relationship('OrderItem', back_populates='Orders')


class OrderItem(Base):
    __tablename__ = 'OrderItem'
    __table_args__ = {'schema': 'dbo'}

    Id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    OrderId = Column(ForeignKey('dbo.Orders.Id'))
    ProductId = Column(ForeignKey('dbo.Products.Id'))
    Quantity = Column(Integer)

    Orders = relationship('Orders', back_populates='OrderItem')
    Products = relationship('Products', back_populates='OrderItem')