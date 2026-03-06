# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UsagePaygoResponse", "UsagePaygoResponseItem"]


class UsagePaygoResponseItem(BaseModel):
    """Represents a single billable usage record."""

    billing_currency: str = FieldInfo(alias="BillingCurrency")
    """Specifies the billing currency code (ISO 4217)."""

    billing_period_start: datetime = FieldInfo(alias="BillingPeriodStart")
    """Indicates the start of the billing period."""

    charge_period_end: datetime = FieldInfo(alias="ChargePeriodEnd")
    """Indicates the end of the charge period."""

    charge_period_start: datetime = FieldInfo(alias="ChargePeriodStart")
    """Indicates the start of the charge period."""

    consumed_quantity: float = FieldInfo(alias="ConsumedQuantity")
    """Specifies the quantity consumed during this charge period."""

    consumed_unit: str = FieldInfo(alias="ConsumedUnit")
    """Specifies the unit of measurement for consumed quantity."""

    contracted_cost: float = FieldInfo(alias="ContractedCost")
    """Specifies the cost for this charge period in the billing currency."""

    cumulated_contracted_cost: float = FieldInfo(alias="CumulatedContractedCost")
    """Specifies the cumulated cost for the billing period in the billing currency."""

    cumulated_pricing_quantity: int = FieldInfo(alias="CumulatedPricingQuantity")
    """Specifies the cumulated pricing quantity for the billing period."""

    pricing_quantity: int = FieldInfo(alias="PricingQuantity")
    """Specifies the pricing quantity for this charge period."""

    service_name: str = FieldInfo(alias="ServiceName")
    """Identifies the Cloudflare service."""


UsagePaygoResponse: TypeAlias = List[UsagePaygoResponseItem]
