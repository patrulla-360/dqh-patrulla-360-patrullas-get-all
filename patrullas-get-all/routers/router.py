from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.db import get_db
from models.models import MaePatrulla

router = APIRouter()

@router.get("/patrullas")
async def get_all_patrullas(db: AsyncSession = Depends(get_db)):
    """
    Obtiene todas las patrullas de la tabla `usr_p360.mae_patrulla`.
    """
    try:
        result = await db.execute(select(MaePatrulla).limit(1000))
        patrullas = result.scalars().all()
        
        return [{"patrulla_id": p.patrulla_id, 
                 "d_vehiculo_id": p.d_vehiculo_id, 
                 "d_cuadricula_id": p.d_cuadricula_id,
                 "d_dispositivo_id": p.d_dispositivo_id,
                 "d_tipo_patrulla_id": p.d_tipo_patrulla_id} for p in patrullas]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
