from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Receipt(SQLModel, table=True):
    receipt_id: Optional[int] = Field(defualt=None, primary_key=True)
    taxpayer_number: str = Field(None, max_length=15)
    taxpayer_name: str = Field(None, max_length=100)
    taxpayer_address: str = Field(None, max_length=100)
    taxpayer_city: str = Field(None, max_length=30)
    taxpayer_state: str = Field(None, max_length=2)
    taxpayer_zip: str = Field(None, max_length=5)
    taxpayer_county: str = Field(None, max_length=3)
    location_number: str = Field(None, max_length=15)
    location_name: str = Field(None, max_length=100)
    location_address: str = Field(None, max_length=100)
    location_city: str = Field(None, max_length=30)
    location_state: str = Field(None, max_length=2)
    location_zip: str = Field(None, max_length=5)
    location_county: str = Field(None, max_length=3)
    inside_city_limits: bool = Field(None, alias="inside_outside_city_limits_code_y_n")
    tabc_permit_number: str = Field(None, max_length=10)
    responsibility_begin: datetime = Field(
        None, alias="responsibility_begin_date_yyyymmdd"
    )
    responsibility_end: datetime = Field(None, alias="responsibility_end_date_yyyymmdd")
    obligation_end: datetime = Field(None, alias="obligation_end_date_yyyymmdd")
    liquor_receipts: int = Field(None, ge=0)
    wine_receipts: int = Field(None, ge=0)
    beer_receipts: int = Field(None, ge=0)
    cover_charge_receipts: int = Field(None, ge=0)
    total_receipts: int = Field(None, ge=0)

    class Config:
        schema_extra = {"db_table_name": "bev_receipts"}
