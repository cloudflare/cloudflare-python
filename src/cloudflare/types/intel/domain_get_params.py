# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DomainGetParams"]


class DomainGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    domain: str

    skip_dns: bool
    """Skip DNS resolution lookups for faster response."""

    skip_ranking: bool
    """Skip the domain ranking lookup for faster responses.

    Defaults to `false` (ranking is included). Set to `true` to opt out — primarily
    used by callers like Cloudflare Radar that need to avoid a circular dependency
    when building the domain details page. Note: the bulk endpoint
    (`/intel/domain/bulk`) uses opposite defaults — see `include_ranking` there.
    """
