from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from .base import Base


class Form(Base):
    
    __tablename__ = "forms"

    salary: Mapped[int] = mapped_column(nullable=False)
    expenses: Mapped[int] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    goal: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    

