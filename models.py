from sqlalchemy import Column, DateTime, Integer, String, Date, DECIMAL
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base


# Definir la base para los modelos
Base = declarative_base()

# Modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False)

# Modelo Camiseta
class Camiseta(Base):
    __tablename__ = 'camisetas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(100), nullable=False)
    talla = Column(String(50), nullable=False)
    material = Column(String(100), nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)

# Modelo de Estampa
class Estampa(Base):
    __tablename__ = 'estampas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    artista = Column(String(100), nullable=False)
    precio = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)

#Modelo de Pedido
class Pedido(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, nullable=False)
    fecha_pedido = Column(DateTime, default=func.now(), nullable=False)  
    total = Column(DECIMAL(10, 2), nullable=False)
    estado = Column(String(50), nullable=False)