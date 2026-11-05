# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    account_id: Required[str]

    cursor: str
    """Opaque value from `result_info.cursor` of the previous response.

    Returns the results that follow it. Send the same `filter`, `search`, `lookup`,
    and `order_by` values as the request that returned it; `limit` and `fields` may
    change. An empty value is the same as no cursor. A modified cursor, or one used
    with different values, returns `400`.
    """

    fields: str
    """
    Return only the listed properties on each application, as a comma-separated
    list. Use this to keep responses small when you only need part of each
    application, for example populating a picker with `fields=id,name` instead of
    downloading every hostname and IP subnet.

    Omit this parameter to receive the full application object, including when
    lookup is used.

    `id` is always returned.

    Selectable properties: `id`, `name`, `human_id`, `version`, `hostnames`,
    `support_domains`, `ip_subnets`, `port_protocols`, `supported`, `gen_ai_score`,
    `application_confidence_score`, `created_at`, `updated_at`, `review_status`.

    Unknown or empty property names return `400`.
    """

    filter: str
    """Filter applications using `key:value` format. Supported filter keys:

    - `name`: application name (for example, `name:HR`).
    - `id`: application ID (for example, `id:498`).
    - `human_id`: human-readable ID (for example, `human_id:HR`).
    - `hostname`: hostname or support domain (for example,
      `hostname:portal.example.com`).
    - `source`: application source name (for example, `source:cloudflare`).
    - `ip_subnet`: CIDR containment; returns applications where a stored subnet
      contains the search value (for example, `ip_subnet:10.0.1.5/32` matches
      `10.0.0.0/16`).
    - `category_id`: category ID (for example, `category_id:12`).
    - `category_name`: category name (for example, `category_name:HR`).
    - `supported`: supported Cloudflare product. Values: `GATEWAY`, `ACCESS`,
      `CASB`.
    - `review_status`: account-specific Gateway review status. Values: `approved`,
      `unapproved`, `in_review`, `unreviewed`.
    """

    limit: int
    """Number of results to return. Defaults to 25; values are clamped to 1–250."""

    lookup: str
    """
    Find complete, case-insensitive application name mentions in a phrase or rule
    sentence. Misspelled names do not match. Returns matching applications ranked by
    relevance. Must be between 2 and 1000 characters, with no control characters
    other than tab and line breaks. Uses the same filters, fields, and pagination as
    listing. `search` cannot be combined with lookup. Results are ranked by
    relevance, so `order_by` is ignored. To keep the text out of URLs, send it to
    `POST .../applications/lookup` instead.
    """

    offset: int
    """Number of results to skip.

    Defaults to 0; negative values are clamped to 0. Ignored when `cursor` is
    provided.
    """

    order_by: str
    """Order results using field:direction format.

    Supported fields are name, id, human_id, category_id, application_type,
    application_confidence_score, and gen_ai_score. Supported directions are asc and
    desc. Ignored when search is provided; results are ranked by relevance instead.
    Also ignored when lookup is provided.
    """

    search: str
    """Fuzzy search across application name and hostnames.

    Results are ranked by relevance. Must be between 2 and 200 characters. Can be
    combined with filter parameters.
    """
