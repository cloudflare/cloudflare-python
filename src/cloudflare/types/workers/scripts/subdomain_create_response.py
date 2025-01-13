# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SubdomainCreateResponse"]


class SubdomainCreateResponse(BaseModel):
    enabled: Optional[bool] = None
    """Whether the Worker is available on the workers.dev subdomain."""

    previews_enabled: Optional[bool] = None
    """
    Whether the Worker's Preview URLs should be available on the workers.dev
    subdomain.
    """
