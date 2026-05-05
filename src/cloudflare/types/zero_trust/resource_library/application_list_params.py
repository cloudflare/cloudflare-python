# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    account_id: Required[str]

    filter: str
    """Filter applications using key:value format. Supported filter keys:

    - name: Filter by application name (e.g., name:HR)
    - id: Filter by application ID (e.g., id:0b63249c-95bf-4cc0-a7cc-d7faaaf1dac0)
    - human_id: Filter by human-readable ID (e.g., human_id:HR)
    - hostname: Filter by hostname or support domain (e.g.,
      hostname:portal.example.com)
    - source: Filter by application source name (e.g., source:cloudflare)
    - ip_subnet: Filter by IP subnet using CIDR containment — returns applications
      where any stored subnet contains the search value (e.g., ip_subnet:10.0.1.5/32
      matches apps with 10.0.0.0/16)
    - intel_id: Filter by Intel API ID (e.g., intel_id:498). .
    """

    limit: int
    """Limit of number of results to return (max 250)."""

    offset: int
    """Offset of results to return."""

    order_by: str
    """Order by result by field name and order (e.g., name:asc)."""
