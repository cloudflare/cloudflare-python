# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from datetime import date

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Whois"]

class Whois(BaseModel):
    created_date: Optional[date] = None

    domain: Optional[str] = None

    nameservers: Optional[List[str]] = None

    registrant: Optional[str] = None

    registrant_country: Optional[str] = None

    registrant_email: Optional[str] = None

    registrant_org: Optional[str] = None

    registrar: Optional[str] = None

    updated_date: Optional[date] = None