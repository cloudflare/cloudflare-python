# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AIRunParams"]


class AIRunParams(TypedDict, total=False):
    account_id: Required[str]

    body: Required[object]
