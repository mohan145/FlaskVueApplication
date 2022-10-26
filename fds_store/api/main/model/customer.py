from sqlalchemy import Integer, Boolean, Column, DateTime, ForeignKey, Identity, String, text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'Customers'
    __table_args__ = {'schema': 'dbo'}

    Id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    FirstName = Column(String(250), nullable=False)
    LastName = Column(String(250), nullable=False)
    MiddleName = Column(String(250))
    IsDeleted = Column(Boolean)
    CreationDateTimeUTC = Column(DateTime, server_default=text("(now() AT TIME ZONE 'utc'::text)"))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}