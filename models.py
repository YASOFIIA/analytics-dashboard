from database import Base
from sqlalchemy import Column, Integer, String, Float

class BarMonthlySales(Base):
    __tablename__ = "bar_monthly_sales"
    id = Column(Integer,  primary_key=True, index=True)
    label = Column(String)
    value = Column(Float)

class BarWeeklyTemperature(Base):
    __tablename__ = "bar_weekly_temperature"
    id = Column(Integer,  primary_key=True, index=True)
    label = Column(String)
    value = Column(Float)

class PieProductStock(Base):
    __tablename__ = "pie_product_stock"
    id = Column(Integer,  primary_key=True, index=True)
    label = Column(String)
    value = Column(Float)

class PieTrafficSources(Base):
    __tablename__ = "pie_traffic_sources"
    id = Column(Integer,  primary_key=True, index=True)
    label = Column(String)
    value = Column(Float)