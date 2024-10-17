# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["PageShieldUpdateResponse"]


class PageShieldUpdateResponse(BaseModel):
    enabled: bool
    """When true, indicates that Page Shield is enabled."""

    updated_at: str
    """The timestamp of when Page Shield was last updated."""

    use_cloudflare_reporting_endpoint: bool
    """
    When true, CSP reports will be sent to
    https://csp-reporting.cloudflare.com/cdn-cgi/script_monitor/report
    """

    use_connection_url_path: bool
    """When true, the paths associated with connections URLs will also be analyzed."""
