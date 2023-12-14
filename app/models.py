from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(10), nullable=False, unique=True)
    email = Column(String(20), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    is_staff = Column(Boolean, server_default='FALSE', nullable=False)
    is_active = Column(Boolean, server_default='FALSE', nullable=False)
    order = relationship('Order', back_populates='users')

    def __repr__(self):
        return f"<User {self.username}>"


class Order(Base):

    ORDER_STATUSES = (
        ('PENDING', 'pending'),
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered')
    )

    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large')
    )

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), server_default="PENDING", nullable=False)
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), server_default="SMALL", nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return f"<Order {self.id}>"
    