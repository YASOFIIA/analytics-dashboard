from fastapi import APIRouter, HTTPException
import requests

router = APIRouter(
    prefix="/rates",
    tags=["rates"]
)

def scraping_last_rates(currency: str, n: int):
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/last/{n}/?format=json"
    info = requests.get(url, timeout=10)

    if info.status_code != 200:
        raise HTTPException(status_code=502, detail=f"NBP API error: {info.status_code}")

    data = info.json()
    rates = data.get("rates")
    labels = [item["effectiveDate"] for item in rates]
    values = [item["mid"] for item in rates]

    return{"currency": currency.upper(), "labels": labels, "values": values}

@router.get("/usd")
async def get_usd_rates():
    return scraping_last_rates("usd", 20)

@router.get("/chf")
async def get_chf_rates():
    return scraping_last_rates("chf", 20)
