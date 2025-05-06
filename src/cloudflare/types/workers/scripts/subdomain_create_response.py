# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["SubdomainCreateResponse"]


class SubdomainCreateResponse(BaseModel):
    enabled: bool
    """Whether the Worker is available on the workers.dev subdomain."""

    previews_enabled: bool
    """Whether the Worker's Preview URLs are available on the workers.dev subdomain."""
