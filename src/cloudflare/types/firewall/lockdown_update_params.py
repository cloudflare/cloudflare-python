# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LockdownUpdateParams"]


class LockdownUpdateParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    body: Required[object]
