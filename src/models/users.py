from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from .base import Base


class User(Base):
    
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    form_id: Mapped[int] = mapped_column(nullable=True)
    

