# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "TenantEntitlements",
    "AllowAddSubdomain",
    "AllowAutoAcceptInvites",
    "CNAMESetupAllowed",
    "CustomEntitlement",
    "CustomEntitlementAllocation",
    "CustomEntitlementAllocationOrganizationsAPIMaxCountAllocation",
    "CustomEntitlementAllocationOrganizationsAPIBoolAllocation",
    "CustomEntitlementAllocationOrganizationsAPINullAllocation",
    "CustomEntitlementFeature",
    "MhsCertificateCount",
    "PartialSetupAllowed",
]


class AllowAddSubdomain(BaseModel):
    type: Literal["bool"]

    value: bool


class AllowAutoAcceptInvites(BaseModel):
    type: Literal["bool"]

    value: bool


class CNAMESetupAllowed(BaseModel):
    type: Literal["bool"]

    value: bool


class CustomEntitlementAllocationOrganizationsAPIMaxCountAllocation(BaseModel):
    type: Literal["max_count"]

    value: int


class CustomEntitlementAllocationOrganizationsAPIBoolAllocation(BaseModel):
    type: Literal["bool"]

    value: bool


class CustomEntitlementAllocationOrganizationsAPINullAllocation(BaseModel):
    type: Literal[""]

    value: Optional[object] = None


CustomEntitlementAllocation: TypeAlias = Union[
    CustomEntitlementAllocationOrganizationsAPIMaxCountAllocation,
    CustomEntitlementAllocationOrganizationsAPIBoolAllocation,
    CustomEntitlementAllocationOrganizationsAPINullAllocation,
]


class CustomEntitlementFeature(BaseModel):
    key: str


class CustomEntitlement(BaseModel):
    allocation: CustomEntitlementAllocation

    feature: CustomEntitlementFeature


class MhsCertificateCount(BaseModel):
    type: Literal["max_count"]

    value: int


class PartialSetupAllowed(BaseModel):
    type: Literal["bool"]

    value: bool


class TenantEntitlements(BaseModel):
    allow_add_subdomain: AllowAddSubdomain

    allow_auto_accept_invites: AllowAutoAcceptInvites

    cname_setup_allowed: CNAMESetupAllowed

    custom_entitlements: Optional[List[CustomEntitlement]] = None

    mhs_certificate_count: MhsCertificateCount

    partial_setup_allowed: PartialSetupAllowed
