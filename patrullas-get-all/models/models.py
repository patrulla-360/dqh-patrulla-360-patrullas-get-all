from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MaePatrulla(Base):
    __tablename__ = "mae_patrulla"
    __table_args__ = {"schema": "usr_p360"}  

    patrulla_id = Column(Integer, primary_key=True, index=True)
    d_vehiculo_id = Column(Integer, nullable=True)
    d_cuadricula_id = Column(Integer, nullable=True)
    d_dispositivo_id = Column(Integer, nullable=True)
    d_tipo_patrulla_id = Column(Integer, nullable=True)

__all__ = ["MaePatrulla"]
