from sqlalchemy import BIGINT, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from jobbing import db

class User(db.Model):
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False) 
    email: Mapped[str] = mapped_column(String(255))
    