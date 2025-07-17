# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Hostname"]


class Hostname(BaseModel):
    url_hostname: str

    exclude_exact_hostname: Optional[bool] = None
    """Only applies to wildcard hostnames (e.g., \\**.example.com).

    When true (default), only subdomains are blocked. When false, both the root
    domain and subdomains are blocked.
    """
