# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Tenant", "TenantContacts", "TenantMetadata", "TenantMetadataDNS", "TenantMetadataDNSNSPool", "TenantUnit"]


class TenantContacts(BaseModel):
    email: Optional[str] = None

    website: Optional[str] = None


class TenantMetadataDNSNSPool(BaseModel):
    primary: Optional[str] = None

    secondary: Optional[str] = None


class TenantMetadataDNS(BaseModel):
    ns_pool: TenantMetadataDNSNSPool


class TenantMetadata(BaseModel):
    dns: Optional[TenantMetadataDNS] = None


class TenantUnit(BaseModel):
    unit_memberships: List[object]

    unit_metadata: object

    unit_name: str

    unit_status: str

    unit_tag: str


class Tenant(BaseModel):
    cdate: datetime

    edate: datetime

    tenant_contacts: TenantContacts

    tenant_labels: List[str]

    tenant_metadata: TenantMetadata

    tenant_name: str

    tenant_network: object

    tenant_status: str

    tenant_tag: str

    tenant_type: str

    tenant_units: List[TenantUnit]

    customer_id: Optional[str] = None
