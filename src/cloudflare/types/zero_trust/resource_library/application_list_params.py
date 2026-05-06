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
    - intel_id: Filter by Intel API ID (e.g., intel_id:498). also supports multiple
      values (e.g., intel_id:498,1001)
    - category_id: Filter by category ID (e.g.,
      category_id:37f8ec03-8766-49d4-9a15-369b044c842c).
    - category_name: Filter by category name (e.g., category_name:HR).
    - supported: Filter by supported Cloudflare product (e.g., supported:ACCESS).
      Values: GATEWAY, ACCESS, CASB. .
    """

    limit: int
    """Limit of number of results to return (max 250)."""

    offset: int
    """Offset of results to return."""

    order_by: str
    """Order results by field name and direction (e.g., name:asc).

    Ignored when search is provided; results are ranked by relevance instead.
    """

    search: str
    """Fuzzy search across application name and hostnames.

    Results are ranked by relevance. Must be between 2 and 200 characters. Can be
    combined with filter parameters.
    """
