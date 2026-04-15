# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ZoneTagUpdateParams",
    "ResourceTaggingSetTagsRequestZoneLevelBase",
    "ResourceTaggingSetTagsRequestZoneLevelAccessApplicationPolicy",
]


class ResourceTaggingSetTagsRequestZoneLevelBase(TypedDict, total=False):
    zone_id: str
    """Zone ID is required only for zone-level resources"""

    resource_id: Required[str]
    """Identifies the unique resource."""

    resource_type: Required[
        Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
        ]
    ]
    """Enum for base zone-level resource types (those with no extra required fields)."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags."""

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]


class ResourceTaggingSetTagsRequestZoneLevelAccessApplicationPolicy(TypedDict, total=False):
    zone_id: str
    """Zone ID is required only for zone-level resources"""

    access_application_id: Required[str]
    """Access application ID is required only for access_application_policy resources"""

    resource_id: Required[str]
    """Identifies the unique resource."""

    resource_type: Required[
        Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
            "access_application_policy",
        ]
    ]
    """Enum for base zone-level resource types (those with no extra required fields)."""

    tags: Dict[str, str]
    """Contains key-value pairs of tags."""

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]


ZoneTagUpdateParams: TypeAlias = Union[
    ResourceTaggingSetTagsRequestZoneLevelBase, ResourceTaggingSetTagsRequestZoneLevelAccessApplicationPolicy
]
