from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.db import get_db
from models.models import MaePatrulla, RelPatrullaEstado, DEstado

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


@router.get("/patrullas/activas")
async def get_active_patrullas(db: AsyncSession = Depends(get_db)):
    """
    Obtiene las patrullas activas cuyo estado es 'Disponible'.
    """
    try:
        stmt = (
            select(MaePatrulla.patrulla_id, DEstado.titulo)
            .join(RelPatrullaEstado, RelPatrullaEstado.patrulla_id == MaePatrulla.patrulla_id)
            .join(DEstado, DEstado.d_estado_id == RelPatrullaEstado.d_estado_id)
            .where(DEstado.titulo == 'Disponible')
        )

        result = await db.execute(stmt)
        patrullas_activas = result.all()
        
        return [{"patrulla_id": p.patrulla_id, "titulo": p.titulo} for p in patrullas_activas]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
