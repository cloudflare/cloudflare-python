# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ProfileGetResponse"]


class ProfileGetResponse(BaseModel):
    id: Optional[str] = None
    """Billing item identifier tag."""

    account_type: Optional[str] = None

    address: Optional[str] = None

    address2: Optional[str] = None

    balance: Optional[str] = None

    card_expiry_month: Optional[int] = None

    card_expiry_year: Optional[int] = None

    card_number: Optional[str] = None

    city: Optional[str] = None

    company: Optional[str] = None

    country: Optional[str] = None

    created_on: Optional[datetime] = None

    device_data: Optional[str] = None

    edited_on: Optional[datetime] = None

    enterprise_billing_email: Optional[str] = None

    enterprise_primary_email: Optional[str] = None

    first_name: Optional[str] = None

    is_partner: Optional[bool] = None

    last_name: Optional[str] = None

    next_bill_date: Optional[datetime] = None

    payment_address: Optional[str] = None

    payment_address2: Optional[str] = None

    payment_city: Optional[str] = None

    payment_country: Optional[str] = None

    payment_email: Optional[str] = None

    payment_first_name: Optional[str] = None

    payment_gateway: Optional[str] = None

    payment_last_name: Optional[str] = None

    payment_nonce: Optional[str] = None

    payment_state: Optional[str] = None

    payment_zipcode: Optional[str] = None

    primary_email: Optional[str] = None

    state: Optional[str] = None

    tax_id_type: Optional[str] = None

    telephone: Optional[str] = None

    use_legacy: Optional[bool] = None

    validation_code: Optional[str] = None

    vat: Optional[str] = None

    zipcode: Optional[str] = None
