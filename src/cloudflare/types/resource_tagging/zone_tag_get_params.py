# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZoneTagGetParams"]


class ZoneTagGetParams(TypedDict, total=False):
    zone_id: str
    """Zone ID is required only for zone-level resources"""

    resource_id: Required[str]
    """The ID of the resource to retrieve tags for."""

    resource_type: Required[
        Literal[
            "access_application_policy",
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
        ]
    ]
    """The type of the resource."""

    access_application_id: str
    """Access application ID identifier.

    Required for access_application_policy resources.
    """
