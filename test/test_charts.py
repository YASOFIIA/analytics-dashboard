import pytest
from main import app
from test.utils import override_get_db, test_db
from routers.charts import get_db
from fastapi.testclient import TestClient
from models import BarMonthlySales, BarWeeklyTemperature, PieProductStock, PieTrafficSources

app.dependency_overrides[get_db]= override_get_db

client = TestClient(app)

def test_get_bar_monthly_sales(test_db):
    test_db.add_all([
        BarMonthlySales(id=1, label="Jan", value=100.0),
        BarMonthlySales(id=2, label="Feb", value=200.0),
    ])
    test_db.commit()

    response = client.get("/charts/bar-monthly-sales")
    assert response.status_code == 200

    data = response.json()
    assert "labels" in data
    assert "values" in data
    assert data["labels"] == ["Jan", "Feb"]
    assert data["values"] == [100.0, 200.0]

def test_get_bar_weekly_temperature(test_db):
    test_db.add_all([
        BarWeeklyTemperature(id=1, label="Mon", value=100.0),
        BarWeeklyTemperature(id=2, label="Tue", value=200.0),
    ])
    test_db.commit()

    response = client.get("/charts/bar-weekly-temperature")
    assert response.status_code == 200

    data = response.json()
    assert "labels" in data
    assert "values" in data
    assert data["labels"] == ["Mon", "Tue"]
    assert data["values"] == [100.0, 200.0]

def test_get_pie_product_stock(test_db):
    test_db.add_all([
        PieProductStock(id=1, label="Laptop", value=100.0),
        PieProductStock(id=2, label="Phone", value=200.0)
    ])
    test_db.commit()

    response = client.get("/charts/pie-product-stock")
    assert response.status_code == 200

    data = response.json()
    assert "labels" in data
    assert "values" in data
    assert data["labels"] == ["Laptop", "Phone"]
    assert data["values"] == [100.0, 200.0]

def test_get_pie_traffic_sources(test_db):
    test_db.add_all([
        PieTrafficSources(id=1, label="Google", value=100.0),
        PieTrafficSources(id=2, label="Tiktok", value=200.0),
    ])
    test_db.commit()

    response = client.get("/charts/pie-traffic-sources")
    assert response.status_code == 200

    data = response.json()
    assert "labels" in data
    assert "values" in data
    assert data["labels"] == ["Google", "Tiktok"]
    assert data["values"] == [100.0, 200.0]