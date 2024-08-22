# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["WhoisGetResponse"]


class WhoisGetResponse(BaseModel):
    domain: str

    extension: str

    found: bool

    nameservers: List[str]

    punycode: str

    registrant: str

    registrar: str

    id: Optional[str] = None

    administrative_city: Optional[str] = None

    administrative_country: Optional[str] = None

    administrative_email: Optional[str] = None

    administrative_fax: Optional[str] = None

    administrative_fax_ext: Optional[str] = None

    administrative_id: Optional[str] = None

    administrative_name: Optional[str] = None

    administrative_org: Optional[str] = None

    administrative_phone: Optional[str] = None

    administrative_phone_ext: Optional[str] = None

    administrative_postal_code: Optional[str] = None

    administrative_province: Optional[str] = None

    administrative_referral_url: Optional[str] = None

    administrative_street: Optional[str] = None

    billing_city: Optional[str] = None

    billing_country: Optional[str] = None

    billing_email: Optional[str] = None

    billing_fax: Optional[str] = None

    billing_fax_ext: Optional[str] = None

    billing_id: Optional[str] = None

    billing_name: Optional[str] = None

    billing_org: Optional[str] = None

    billing_phone: Optional[str] = None

    billing_phone_ext: Optional[str] = None

    billing_postal_code: Optional[str] = None

    billing_province: Optional[str] = None

    billing_referral_url: Optional[str] = None

    billing_street: Optional[str] = None

    created_date: Optional[datetime] = None

    created_date_raw: Optional[str] = None

    dnssec: Optional[bool] = None

    expiration_date: Optional[datetime] = None

    expiration_date_raw: Optional[str] = None

    registrant_city: Optional[str] = None

    registrant_country: Optional[str] = None

    registrant_email: Optional[str] = None

    registrant_fax: Optional[str] = None

    registrant_fax_ext: Optional[str] = None

    registrant_id: Optional[str] = None

    registrant_name: Optional[str] = None

    registrant_org: Optional[str] = None

    registrant_phone: Optional[str] = None

    registrant_phone_ext: Optional[str] = None

    registrant_postal_code: Optional[str] = None

    registrant_province: Optional[str] = None

    registrant_referral_url: Optional[str] = None

    registrant_street: Optional[str] = None

    registrar_city: Optional[str] = None

    registrar_country: Optional[str] = None

    registrar_email: Optional[str] = None

    registrar_fax: Optional[str] = None

    registrar_fax_ext: Optional[str] = None

    registrar_id: Optional[str] = None

    registrar_name: Optional[str] = None

    registrar_org: Optional[str] = None

    registrar_phone: Optional[str] = None

    registrar_phone_ext: Optional[str] = None

    registrar_postal_code: Optional[str] = None

    registrar_province: Optional[str] = None

    registrar_referral_url: Optional[str] = None

    registrar_street: Optional[str] = None

    status: Optional[List[str]] = None

    technical_city: Optional[str] = None

    technical_country: Optional[str] = None

    technical_email: Optional[str] = None

    technical_fax: Optional[str] = None

    technical_fax_ext: Optional[str] = None

    technical_id: Optional[str] = None

    technical_name: Optional[str] = None

    technical_org: Optional[str] = None

    technical_phone: Optional[str] = None

    technical_phone_ext: Optional[str] = None

    technical_postal_code: Optional[str] = None

    technical_province: Optional[str] = None

    technical_referral_url: Optional[str] = None

    technical_street: Optional[str] = None

    updated_date: Optional[datetime] = None

    updated_date_raw: Optional[str] = None

    whois_server: Optional[str] = None
