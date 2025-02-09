from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class MaePatrulla(Base):
    __tablename__ = "mae_patrulla"
    __table_args__ = {"schema": "usr_p360"}  

    patrulla_id = Column(Integer, primary_key=True, index=True)
    d_vehiculo_id = Column(Integer, nullable=True)
    d_cuadricula_id = Column(Integer, nullable=True)
    d_dispositivo_id = Column(Integer, nullable=True)
    d_tipo_patrulla_id = Column(Integer, nullable=True)

    # Relación con RelPatrullaEstado
    estados = relationship("RelPatrullaEstado", back_populates="patrulla")

class RelPatrullaEstado(Base):
    __tablename__ = "rel_patrulla_estado"
    __table_args__ = {"schema": "usr_p360"}  

    d_estado_id = Column(Integer, ForeignKey("usr_p360.d_estado.d_estado_id"), primary_key=True)
    patrulla_id = Column(Integer, ForeignKey("usr_p360.mae_patrulla.patrulla_id"), primary_key=True)
    fecha_inicio = Column(DateTime, nullable=True)
    fecha_fin = Column(DateTime, nullable=True)

    # Relación con MaePatrulla
    patrulla = relationship("MaePatrulla", back_populates="estados")

    # Relación con DEstado
    estado = relationship("DEstado", back_populates="patrullas")

class DEstado(Base):
    __tablename__ = "d_estado"
    __table_args__ = {"schema": "usr_p360"}  

    d_estado_id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)

    # Relación con RelPatrullaEstado
    patrullas = relationship("RelPatrullaEstado", back_populates="estado")

__all__ = ["MaePatrulla", "RelPatrullaEstado", "DEstado"]
