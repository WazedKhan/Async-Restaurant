from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from ...database import Base


class FoodItem(Base):
    __tablename__ = "food_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True, nullable=False)
    preparation_time = Column(Integer, default=1)
