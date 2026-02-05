# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Hostname"]


class Hostname(BaseModel):
    """
    Valid characters for hostnames are ASCII(7) letters from a to z, the digits from 0 to 9, wildcards (*), and the hyphen (-).
    """

    url_hostname: str

    exclude_exact_hostname: Optional[bool] = None
    """Only applies to wildcard hostnames (e.g., \\**.example.com).

    When true (default), only subdomains are blocked. When false, both the root
    domain and subdomains are blocked.
    """
