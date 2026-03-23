# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SubdomainCreateResponse"]


class SubdomainCreateResponse(BaseModel):
    email_sending_enabled: bool
    """Whether Email Sending is enabled on this subdomain."""

    name: str
    """The subdomain domain name."""

    tag: str
    """Sending subdomain identifier."""

    created: Optional[datetime] = None
    """The date and time the destination address has been created."""

    email_sending_dkim_selector: Optional[str] = None
    """The DKIM selector used for email signing."""

    email_sending_return_path_domain: Optional[str] = None
    """The return-path domain used for bounce handling."""

    enabled: Optional[bool] = None
    """Whether Email Routing (receiving) is enabled on this subdomain.

    Read-only; included for informational purposes since both services share the
    subdomain row.
    """

    modified: Optional[datetime] = None
    """The date and time the destination address was last modified."""
