# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UsageGetResponse", "UsageGetResponseItem"]


class UsageGetResponseItem(BaseModel):
    """
    A single cost and usage record for a metered product within a specific charge period, aligned with the FinOps FOCUS v1.3 specification.
    """

    billing_account_id: str = FieldInfo(alias="BillingAccountId")
    """Public identifier of the Cloudflare account (account tag)."""

    billing_account_name: str = FieldInfo(alias="BillingAccountName")
    """Display name of the Cloudflare account."""

    charge_category: Literal["Usage"] = FieldInfo(alias="ChargeCategory")
    """
    Highest-level classification of a charge based on the nature of how it gets
    billed. Currently only "Usage" is supported.
    """

    charge_description: str = FieldInfo(alias="ChargeDescription")
    """Self-contained summary of the charge's purpose and price."""

    charge_frequency: Literal["Usage-Based"] = FieldInfo(alias="ChargeFrequency")
    """Indicates how often a charge occurs. Currently only "Usage-Based" is supported."""

    charge_period_end: datetime = FieldInfo(alias="ChargePeriodEnd")
    """Exclusive end of the time interval during which the usage was consumed."""

    charge_period_start: datetime = FieldInfo(alias="ChargePeriodStart")
    """Inclusive start of the time interval during which the usage was consumed."""

    consumed_quantity: float = FieldInfo(alias="ConsumedQuantity")
    """Measured usage amount within the charge period.

    Reflects raw metered consumption before pricing transformations.
    """

    consumed_unit: str = FieldInfo(alias="ConsumedUnit")
    """
    Unit of measure for the consumed quantity (e.g., "GB", "Requests",
    "vCPU-Hours").
    """

    host_provider_name: str = FieldInfo(alias="HostProviderName")
    """Name of the entity providing the underlying infrastructure or platform."""

    invoice_issuer_name: str = FieldInfo(alias="InvoiceIssuerName")
    """Name of the entity responsible for invoicing for the services consumed."""

    service_provider_name: str = FieldInfo(alias="ServiceProviderName")
    """Name of the entity that made the services available for purchase."""

    x_billable_metric_name: str = FieldInfo(alias="x_BillableMetricName")
    """The display name of the billable metric.

    Cloudflare extension; replaces FOCUS SkuMeter.
    """

    billed_cost: Optional[float] = FieldInfo(alias="BilledCost", default=None)
    """
    A charge serving as the basis for invoicing, inclusive of all reduced rates and
    discounts while excluding the amortization of upfront charges (one-time or
    recurring).
    """

    billing_currency: Optional[str] = FieldInfo(alias="BillingCurrency", default=None)
    """Currency that a charge was billed in (ISO 4217)."""

    billing_period_end: Optional[datetime] = FieldInfo(alias="BillingPeriodEnd", default=None)
    """Exclusive end of the billing cycle that contains this usage record."""

    billing_period_start: Optional[datetime] = FieldInfo(alias="BillingPeriodStart", default=None)
    """Inclusive start of the billing cycle that contains this usage record."""

    charge_class: Optional[Literal["Correction"]] = FieldInfo(alias="ChargeClass", default=None)
    """
    Indicates whether the row represents a correction to one or more charges
    invoiced in a previous billing period.
    """

    contracted_cost: Optional[float] = FieldInfo(alias="ContractedCost", default=None)
    """
    Cost calculated by multiplying ContractedUnitPrice and the corresponding
    PricingQuantity.
    """

    contracted_unit_price: Optional[float] = FieldInfo(alias="ContractedUnitPrice", default=None)
    """
    The agreed-upon unit price for a single PricingUnit of the associated billable
    metric, inclusive of negotiated discounts, if present, while excluding any other
    discounts.
    """

    effective_cost: Optional[float] = FieldInfo(alias="EffectiveCost", default=None)
    """
    The amortized cost of the charge after applying all reduced rates, discounts,
    and the applicable portion of relevant, prepaid purchases (one-time or
    recurring) that covered the charge.
    """

    list_cost: Optional[float] = FieldInfo(alias="ListCost", default=None)
    """
    Cost calculated by multiplying ListUnitPrice and the corresponding
    PricingQuantity.
    """

    list_unit_price: Optional[float] = FieldInfo(alias="ListUnitPrice", default=None)
    """
    Suggested provider-published unit price for a single PricingUnit of the
    associated billable metric, exclusive of any discounts.
    """

    pricing_quantity: Optional[float] = FieldInfo(alias="PricingQuantity", default=None)
    """Volume of a given service used or purchased, based on the PricingUnit."""

    pricing_unit: Optional[str] = FieldInfo(alias="PricingUnit", default=None)
    """
    Provider-specified measurement unit for determining unit prices, indicating how
    the provider rates measured usage after applying pricing rules like block
    pricing.
    """

    region_id: Optional[str] = FieldInfo(alias="RegionId", default=None)
    """
    Provider-assigned identifier for an isolated geographic area where a service is
    provided.
    """

    region_name: Optional[str] = FieldInfo(alias="RegionName", default=None)
    """Name of an isolated geographic area where a service is provided."""

    sub_account_id: Optional[str] = FieldInfo(alias="SubAccountId", default=None)
    """Unique identifier assigned to a grouping of services.

    For Cloudflare, this is the subscription or contract ID.
    """

    sub_account_name: Optional[str] = FieldInfo(alias="SubAccountName", default=None)
    """Name assigned to a grouping of services.

    For Cloudflare, this is the subscription or contract display name.
    """

    x_billable_metric_id: Optional[str] = FieldInfo(alias="x_BillableMetricId", default=None)
    """The unique identifier for the billable metric in the Cloudflare catalog.

    Cloudflare extension; replaces FOCUS SkuId.
    """

    x_product_family_name: Optional[str] = FieldInfo(alias="x_ProductFamilyName", default=None)
    """The product family the charge belongs to (e.g., "R2", "Workers").

    Cloudflare extension; replaces FOCUS ServiceName.
    """

    x_zone_id: Optional[str] = FieldInfo(alias="x_ZoneId", default=None)
    """The identifier for the Cloudflare zone (zone tag). Cloudflare extension."""

    x_zone_name: Optional[str] = FieldInfo(alias="x_ZoneName", default=None)
    """The display name of the Cloudflare zone. Cloudflare extension."""


UsageGetResponse: TypeAlias = List[UsageGetResponseItem]
