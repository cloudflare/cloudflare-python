# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TokenUpdateParams"]


class TokenUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    cf_api_id: Required[str]

    cf_api_key: Required[str]

    name: Required[str]
