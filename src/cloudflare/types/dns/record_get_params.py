# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RecordGetParams"]


class RecordGetParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    include_shadow_metadata: bool
    """
    Whether to include shadow metadata in the `meta` field of each record in the
    response. See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """
