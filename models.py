from sqlalchemy import Column, Integer, String, Text
from database import Base

class Ad(Base):
    __tablename__ = "ads"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Especificar longitud máxima
    href = Column(String(255), unique=True, index=True)  # Especificar longitud máxima
    price = Column(String(50))  # Especificar longitud máxima
    img_url = Column(String(255))  # Especificar longitud máxima
    features = Column(Text)
    location = Column(Text)