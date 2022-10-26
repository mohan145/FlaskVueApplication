from sqlalchemy import Integer, Boolean, Column, DateTime, ForeignKey, Identity, String, text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Order(Base):
    __tablename__ = 'Orders'
    __table_args__ = {'schema': 'dbo'}

    Id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    CustomerId = Column(Integer)
    CreationDateTimeUTC = Column(DateTime, server_default=text("(now() AT TIME ZONE 'utc'::text)"))