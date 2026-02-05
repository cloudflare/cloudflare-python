# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HostnameParam"]


class HostnameParam(TypedDict, total=False):
    """
    Valid characters for hostnames are ASCII(7) letters from a to z, the digits from 0 to 9, wildcards (*), and the hyphen (-).
    """

    url_hostname: Required[str]

    exclude_exact_hostname: bool
    """Only applies to wildcard hostnames (e.g., \\**.example.com).

    When true (default), only subdomains are blocked. When false, both the root
    domain and subdomains are blocked.
    """
