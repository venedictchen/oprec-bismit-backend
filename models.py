from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text


class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)
    spend=Column(Integer,nullable=False)
    income=Column(Integer,nullable=False)
    plan=Column(Boolean,default=False)

    def __repr__(self):
        return f"<Item name={self.name} spend={self.spend} income={self.income}>"