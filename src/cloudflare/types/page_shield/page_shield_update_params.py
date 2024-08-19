# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PageShieldUpdateParams"]


class PageShieldUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    enabled: bool
    """When true, indicates that Page Shield is enabled."""

    use_cloudflare_reporting_endpoint: bool
    """
    When true, CSP reports will be sent to
    https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report
    """

    use_connection_url_path: bool
    """When true, the paths associated with connections URLs will also be analyzed."""
