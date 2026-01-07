from fastapi import APIRouter, Depends
from typing import Annotated
from database import SessionLocal
from models import BarMonthlySales, BarWeeklyTemperature, PieProductStock, PieTrafficSources
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/charts",
    tags=["charts"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/bar-monthly-sales")
async def get_bar_monthly_sales(db: db_dependency):
    rows= db.query(BarMonthlySales).all()
    return {
        "labels": [row.label for row in rows],
        "values": [row.value for row in rows]
    }

@router.get('/bar-weekly-temperature')
async def get_bar_weekly_temperature(db: db_dependency):
    rows = db.query(BarWeeklyTemperature).all()
    return{
        "labels": [row.label for row in rows],
        "values": [row.value for row in rows]
    }

@router.get('/pie-product-stock')
async def get_pie_product_stock(db: db_dependency):
    rows = db.query(PieProductStock).all()
    return {
        "labels": [row.label for row in rows],
        "values": [row.value for row in rows]
    }
@router.get('/pie-traffic-sources')
async def get_pie_traffic_sources(db: db_dependency):
    rows = db.query(PieTrafficSources).all()
    return{
        "labels": [row.label for row in rows],
        "values": [row.value for row in rows]
    }