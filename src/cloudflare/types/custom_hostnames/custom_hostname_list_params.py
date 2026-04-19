# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CustomHostnameListParams", "Hostname"]


class CustomHostnameListParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    id: str
    """Hostname ID to match against.

    This ID was generated and returned during the initial custom_hostname creation.
    This parameter cannot be used with the 'hostname' parameter.
    """

    certificate_authority: Literal["google", "lets_encrypt", "ssl_com"]
    """Filter by the certificate authority that issued the SSL certificate."""

    custom_origin_server: str
    """Filter by custom origin server name."""

    direction: Literal["asc", "desc"]
    """Direction to order hostnames."""

    hostname: Hostname

    hostname_status: Literal[
        "active",
        "pending",
        "active_redeploying",
        "moved",
        "pending_deletion",
        "deleted",
        "pending_blocked",
        "pending_migration",
        "pending_provisioned",
        "test_pending",
        "test_active",
        "test_active_apex",
        "test_blocked",
        "test_failed",
        "provisioned",
        "blocked",
    ]
    """Filter by the hostname's activation status."""

    order: Literal["ssl", "ssl_status"]
    """Field to order hostnames by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of hostnames per page."""

    ssl: Literal[0, 1]
    """Whether to filter hostnames based on if they have SSL enabled."""

    ssl_status: Literal[
        "initializing",
        "pending_validation",
        "deleted",
        "pending_issuance",
        "pending_deployment",
        "pending_deletion",
        "pending_expiration",
        "expired",
        "active",
        "initializing_timed_out",
        "validation_timed_out",
        "issuance_timed_out",
        "deployment_timed_out",
        "deletion_timed_out",
        "pending_cleanup",
        "staging_deployment",
        "staging_active",
        "deactivating",
        "inactive",
        "backup_issued",
        "holding_deployment",
    ]
    """Filter by SSL certificate status."""

    wildcard: bool
    """Filter by whether the custom hostname is a wildcard hostname."""


class Hostname(TypedDict, total=False):
    contain: str
    """Filters hostnames by a substring match on the hostname value.

    This parameter cannot be used with the 'id' parameter.
    """
