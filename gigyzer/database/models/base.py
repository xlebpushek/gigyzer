from sqlalchemy.orm import Mapped, as_declarative, mapped_column


@as_declarative()
class BaseModel:
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, index=True)


__all__ = ['BaseModel']
