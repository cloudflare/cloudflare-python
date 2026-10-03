# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KeyListParams"]


class KeyListParams(TypedDict, total=False):
    account_id: Required[str]
    """ID of the Cloudflare account that owns the Workers KV namespaces."""

    cursor: str
    """Opaque pagination token from `result_info.cursor` in the previous response.

    Pass it unchanged to request the next page of keys.
    """

    limit: float
    """Maximum number of keys to return in one response.

    Pass `result_info.cursor` from the response as `cursor` to request the next
    page.
    """

    prefix: str
    """Filters returned keys by a name prefix.

    Exact matches and any key names that begin with the prefix will be returned.
    """
