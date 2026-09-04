# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UsageGetAccountUsageV1Response", "UsageGetAccountUsageV1ResponseItem"]


class UsageGetAccountUsageV1ResponseItem(BaseModel):
    """Represents a single billable usage record.

    This schema carries 19 of the 21 columns FOCUS 1.3 marks as mandatory. Mandatory columns are always present, using an explicit null when the value is unknown, so consumers can distinguish "unknown" from "not provided".

    Known gap 1: `ServiceCategory` (FOCUS 1.3 section 3.1.55) is not yet implemented and does not appear in this schema. Cloudflare's product catalog does not yet have a stakeholder-approved mapping from product family to a FOCUS ServiceCategory value, so the column is omitted entirely rather than shipping unapproved values. It will be added once that mapping exists.

    Known gap 2: `BillingPeriodEnd` (FOCUS 1.3 section 3.1.4) is not yet implemented and does not appear in this schema, because no authoritative source for it exists today. Deriving it by calendar arithmetic drifts for billing cycle anchors on day 29-31, and the billing provider's current period end describes only the current period, so it is wrong for backdated records. `BillingPeriodStart` is correctly sourced and is still reported, so records carry a billing period start with no corresponding end until an authoritative end date is available.

    Per FOCUS 1.3 section 4.1.4.1, the columns that are not part of FOCUS (`ServiceFamilyName`, `CumulatedPricingQuantity`, `CumulatedContractedCost`, `ZoneId`, `ZoneName` and `SubscriptionId`) would normally carry an `x_` prefix. They are kept unprefixed here to avoid a breaking change for existing consumers.
    """

    billed_cost: float = FieldInfo(alias="BilledCost")
    """The amount invoiced for this charge.

    PayGo is billed directly by Cloudflare, so this equals ContractedCost.
    """

    billing_account_id: str = FieldInfo(alias="BillingAccountId")
    """The identifier of the account the charge is billed to (account tag)."""

    billing_account_name: Optional[str] = FieldInfo(alias="BillingAccountName", default=None)
    """The display name of the billing account.

    Null when the name could not be resolved.
    """

    billing_currency: str = FieldInfo(alias="BillingCurrency")
    """Specifies the billing currency code (ISO 4217)."""

    billing_period_start: datetime = FieldInfo(alias="BillingPeriodStart")
    """Indicates the start of the billing period.

    There is no `BillingPeriodEnd` counterpart; see the known gaps described on this
    schema.
    """

    charge_category: Literal["Usage"] = FieldInfo(alias="ChargeCategory")
    """Describes the nature of the charge.

    Always "Usage" for this endpoint, which only returns metered usage.
    """

    charge_class: Optional[str] = FieldInfo(alias="ChargeClass", default=None)
    """Indicates whether the row corrects a previously invoiced billing period.

    Always null for this endpoint, which does not return corrections.
    """

    charge_description: Optional[str] = FieldInfo(alias="ChargeDescription", default=None)
    """A human-readable summary of the charge."""

    charge_period_end: datetime = FieldInfo(alias="ChargePeriodEnd")
    """Indicates the end of the charge period."""

    charge_period_start: datetime = FieldInfo(alias="ChargePeriodStart")
    """Indicates the start of the charge period."""

    consumed_quantity: float = FieldInfo(alias="ConsumedQuantity")
    """Specifies the quantity consumed during this charge period."""

    consumed_unit: str = FieldInfo(alias="ConsumedUnit")
    """
    A display name for the unit of measurement used for the product (for example,
    "GB-months", "GB-seconds"). May be empty when the unit is implicit in the
    service name.
    """

    contracted_cost: float = FieldInfo(alias="ContractedCost")
    """Specifies the cost for this charge period in the billing currency."""

    cumulated_contracted_cost: float = FieldInfo(alias="CumulatedContractedCost")
    """Specifies the cumulated cost for the billing period in the billing currency."""

    cumulated_pricing_quantity: int = FieldInfo(alias="CumulatedPricingQuantity")
    """Specifies the portion of usage that is actually subject to a unit price."""

    effective_cost: float = FieldInfo(alias="EffectiveCost")
    """The amortized cost of the charge.

    PayGo has no upfront commitments, so this equals ContractedCost.
    """

    host_provider_name: str = FieldInfo(alias="HostProviderName")
    """The provider that hosts the infrastructure or platform the service runs on."""

    invoice_issuer_name: str = FieldInfo(alias="InvoiceIssuerName")
    """The entity that issues the invoice for this charge."""

    list_cost: float = FieldInfo(alias="ListCost")
    """The cost at published list prices, before any discount.

    PayGo has no commitment discounts, so this equals ContractedCost.
    """

    pricing_quantity: int = FieldInfo(alias="PricingQuantity")
    """Specifies the pricing quantity for this charge period."""

    pricing_unit: str = FieldInfo(alias="PricingUnit")
    """The unit that PricingQuantity is expressed in.

    Unlike ConsumedUnit this is never empty; it falls back to "Count" when the
    service has no explicit unit.
    """

    service_name: str = FieldInfo(alias="ServiceName")
    """Identifies the Cloudflare service."""

    service_provider_name: str = FieldInfo(alias="ServiceProviderName")
    """The provider of the purchased service."""

    service_family_name: Optional[str] = FieldInfo(alias="ServiceFamilyName", default=None)
    """Identifies the product family for the Cloudflare service."""

    subscription_id: Optional[str] = FieldInfo(alias="SubscriptionId", default=None)
    """The identifier for the Cloudflare subscription."""

    zone_id: Optional[str] = FieldInfo(alias="ZoneId", default=None)
    """The identifier for the Cloudflare zone (zone tag)."""

    zone_name: Optional[str] = FieldInfo(alias="ZoneName", default=None)
    """The display name of the Cloudflare zone."""


UsageGetAccountUsageV1Response: TypeAlias = List[UsageGetAccountUsageV1ResponseItem]
