from datetime import datetime

from sqlalchemy import BigInteger, Column
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=True, index=True)
    user_id: Mapped[int] = Column(BigInteger, unique=True, nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)


__all__ = ["UserModel"]
