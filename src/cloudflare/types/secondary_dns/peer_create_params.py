# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PeerCreateParams"]


class PeerCreateParams(TypedDict, total=False):
    account_id: Required[object]

    body: Required[object]
