# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BillingCreditBalanceResponse", "PaymentMethod", "TopupConfig"]


class PaymentMethod(BaseModel):
    brand: Optional[str] = None

    last4: Optional[str] = None


class TopupConfig(BaseModel):
    amount: Optional[float] = None

    disabled_reason: Optional[str] = FieldInfo(alias="disabledReason", default=None)

    error: Optional[str] = None

    last_failed_at: Optional[float] = FieldInfo(alias="lastFailedAt", default=None)

    threshold: Optional[float] = None


class BillingCreditBalanceResponse(BaseModel):
    balance: float

    has_default_payment_method: bool

    payment_method: Optional[PaymentMethod] = None

    topup_config: TopupConfig

    first_topup_success: Optional[bool] = None
