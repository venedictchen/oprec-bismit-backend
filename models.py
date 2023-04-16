from database import Base
from sqlalchemy import String,Integer,Column,Text


class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=False)
    description=Column(Text)
    deadline=Column(Text)

    def __repr__(self):
        return f"<Item name={self.name} description={self.description} deadline={self.deadline}>"