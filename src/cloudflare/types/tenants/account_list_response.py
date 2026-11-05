# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountListResponse", "Settings"]


class Settings(BaseModel):
    access_approval_expiry: Optional[datetime] = None

    api_access_enabled: bool

    enforce_two_factor: bool

    use_account_custom_ns_by_default: bool


class AccountListResponse(BaseModel):
    account_pubname: Optional[str] = None

    account_tag: str

    account_type: Literal["standard", "enterprise"]

    created_on: datetime

    settings: Settings
