# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectionListParams"]


class ConnectionListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """The direction used to sort returned connections."""

    exclude_cdn_cgi: bool
    """
    When true, excludes connections seen in a `/cdn-cgi` path from the returned
    connections. The default value is true.
    """

    exclude_urls: str
    """
    Excludes connections whose URL contains one of the URL-encoded URLs separated by
    commas.
    """

    export: Literal["csv"]
    """Export the list of connections as a file."""

    hosts: str
    """
    Includes connections that match one or more URL-encoded hostnames separated by
    commas.

    Wildcards are supported at the start and end of each hostname to support starts
    with, ends with and contains. If no wildcards are used, results will be filtered
    by exact match
    """

    order_by: Literal["first_seen_at", "last_seen_at"]
    """The field used to sort returned connections."""

    page: str
    """The current page number of the paginated results.

    We additionally support a special value "all". When "all" is used, the API will
    return all the connections with the applied filters in a single page. This
    feature is best-effort and it may only work for zones with a low number of
    connections
    """

    page_url: str
    """
    Includes connections that match one or more page URLs (separated by commas)
    where they were last seen

    Wildcards are supported at the start and end of each page URL to support starts
    with, ends with and contains. If no wildcards are used, results will be filtered
    by exact match
    """

    per_page: float
    """The number of results per page."""

    prioritize_malicious: bool
    """When true, malicious connections appear first in the returned connections."""

    status: str
    """
    Filters the returned connections using a comma-separated list of connection
    statuses. Accepted values: `active`, `infrequent`, and `inactive`. The default
    value is `active`.
    """

    urls: str
    """
    Includes connections whose URL contain one or more URL-encoded URLs separated by
    commas.
    """
