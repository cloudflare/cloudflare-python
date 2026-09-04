# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    account_id: Required[str]

    fields: str
    """
    Return only the listed properties on each application, as a comma-separated
    list. Use this to keep responses small when you only need part of each
    application — for example populating a picker with `fields=id,name` instead of
    downloading every hostname and IP subnet.

    Omit this parameter to receive the full application object.

    `id` is always returned.

    Selectable properties: `id`, `name`, `human_id`, `version`, `hostnames`,
    `support_domains`, `ip_subnets`, `port_protocols`, `supported`, `gen_ai_score`,
    `application_confidence_score`, `created_at`, `updated_at`, `review_status`.

    Unknown or empty property names return `400`.
    """

    filter: str
    """Filter applications using key:value format. Supported filter keys:

    - name: Filter by application name (e.g., name:HR)
    - id: Filter by application ID (e.g., id:498)
    - human_id: Filter by human-readable ID (e.g., human_id:HR)
    - hostname: Filter by hostname or support domain (e.g.,
      hostname:portal.example.com)
    - source: Filter by application source name (e.g., source:cloudflare)
    - ip_subnet: Filter by IP subnet using CIDR containment — returns applications
      where any stored subnet contains the search value (e.g., ip_subnet:10.0.1.5/32
      matches apps with 10.0.0.0/16)
    - category_id: Filter by category ID (e.g., category_id:12).
    - category_name: Filter by category name (e.g., category_name:HR).
    - supported: Filter by supported Cloudflare product (e.g., supported:ACCESS).
      Values: GATEWAY, ACCESS, CASB.
    - review_status: Filter by the account's Gateway review status. Values:
      approved, unapproved, in_review, unreviewed. .
    """

    limit: int
    """Limit of number of results to return (max 250)."""

    offset: int
    """Offset of results to return."""

    order_by: str
    """Order results using field:direction format.

    Supported fields are name, id, human_id, category_id, application_type,
    application_confidence_score, and gen_ai_score. Supported directions are asc and
    desc. Ignored when search is provided; results are ranked by relevance instead.
    """

    search: str
    """Fuzzy search across application name and hostnames.

    Results are ranked by relevance. Must be between 2 and 200 characters. Can be
    combined with filter parameters.
    """
