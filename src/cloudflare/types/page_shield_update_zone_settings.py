# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PageShieldUpdateZoneSettings"]


class PageShieldUpdateZoneSettings(BaseModel):
    enabled: Optional[bool] = None
    """When true, indicates that Page Shield is enabled."""

    updated_at: Optional[str] = None
    """The timestamp of when Page Shield was last updated."""

    use_cloudflare_reporting_endpoint: Optional[bool] = None
    """
    When true, CSP reports will be sent to
    https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report
    """

    use_connection_url_path: Optional[bool] = None
    """When true, the paths associated with connections URLs will also be analyzed."""
