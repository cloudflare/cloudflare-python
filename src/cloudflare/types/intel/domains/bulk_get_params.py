# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["BulkGetParams"]


class BulkGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    domain: SequenceNotStr[str]
    """Accepts multiple values like `?domain=cloudflare.com&domain=example.com`."""

    include_ranking: bool
    """Whether to include domain ranking data in the response.

    Defaults to `false` — ranking lookups are expensive at bulk scale and most
    callers do not need them. Set to `true` to opt in. This parameter replaces the
    deprecated `skip_ranking` (see below).
    """

    skip_ranking: bool
    """
    **Deprecated.** Previously controlled whether the ranking lookup was skipped
    (defaulted to `false`, meaning ranking ran). The endpoint's default behavior is
    being flipped — ranking is now opt-in via `include_ranking=true` — and this
    parameter will be silently ignored. Remove it from your callers and use
    `include_ranking` instead.
    """
