# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "TenantListResponse",
    "TenantContacts",
    "TenantMetadata",
    "TenantMetadataDNS",
    "TenantMetadataDNSNSPool",
    "TenantMetadataInnateAccountEntitlement",
    "TenantMetadataInnateAccountEntitlementAllocation",
    "TenantMetadataInnateAccountEntitlementFeature",
    "TenantMetadataTenantEntitlement",
    "TenantMetadataTenantEntitlementAllocation",
    "TenantMetadataTenantEntitlementFeature",
    "TenantNetwork",
    "TenantUnit",
    "TenantUnitUnitMembership",
    "UIFlags",
]


class TenantContacts(BaseModel):
    email: Optional[str] = None

    website: Optional[str] = None


class TenantMetadataDNSNSPool(BaseModel):
    primary: Optional[str] = None

    secondary: Optional[str] = None


class TenantMetadataDNS(BaseModel):
    ns_pool: TenantMetadataDNSNSPool


class TenantMetadataInnateAccountEntitlementAllocation(BaseModel):
    type: str

    value: Union[bool, float, str, Optional[Dict[str, object]], List[object]]


class TenantMetadataInnateAccountEntitlementFeature(BaseModel):
    key: str


class TenantMetadataInnateAccountEntitlement(BaseModel):
    allocation: TenantMetadataInnateAccountEntitlementAllocation

    feature: TenantMetadataInnateAccountEntitlementFeature


class TenantMetadataTenantEntitlementAllocation(BaseModel):
    type: str

    value: Union[bool, float, str, Optional[Dict[str, object]], List[object]]


class TenantMetadataTenantEntitlementFeature(BaseModel):
    key: str


class TenantMetadataTenantEntitlement(BaseModel):
    allocation: TenantMetadataTenantEntitlementAllocation

    feature: TenantMetadataTenantEntitlementFeature


class TenantMetadata(BaseModel):
    billing_account_type: Optional[str] = None

    configuration_account: Optional[str] = None

    created_by: Optional[str] = None

    dns: Optional[TenantMetadataDNS] = None

    flags: Optional[Dict[str, str]] = None

    innate_account_entitlements: Optional[List[TenantMetadataInnateAccountEntitlement]] = None

    tenant_entitlements: Optional[List[TenantMetadataTenantEntitlement]] = None


class TenantNetwork(BaseModel):
    choices: Optional[Dict[str, object]] = None


class TenantUnitUnitMembership(BaseModel):
    member_metadata: object

    member_status: str

    member_tag: str


class TenantUnit(BaseModel):
    unit_memberships: Optional[List[TenantUnitUnitMembership]] = None

    unit_metadata: object

    unit_name: str

    unit_status: str

    unit_tag: str


class UIFlags(BaseModel):
    """
    Which top-level dashboard experiences to render for this tenant; both may be true.
    """

    show_orgs_ui: bool
    """Render the Organizations experience for this tenant."""

    show_tenants_ui: bool
    """Render the legacy Tenants experience for this tenant."""


class TenantListResponse(BaseModel):
    cdate: datetime

    customer_id: Optional[str] = None

    edate: datetime

    tenant_contacts: TenantContacts

    tenant_labels: Optional[List[str]] = None

    tenant_metadata: TenantMetadata

    tenant_name: str

    tenant_network: TenantNetwork

    tenant_status: str

    tenant_tag: str

    tenant_type: str

    tenant_units: Optional[List[TenantUnit]] = None

    ui_flags: UIFlags
    """
    Which top-level dashboard experiences to render for this tenant; both may be
    true.
    """
