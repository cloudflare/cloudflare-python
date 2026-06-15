# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomProviderCreateParams"]


class CustomProviderCreateParams(TypedDict, total=False):
    account_id: Required[str]

    base_url: Required[str]

    name: Required[str]

    slug: Required[str]

    beta: bool

    curl_example: str

    description: str

    enable: bool

    headers: str

    js_example: str

    link: str

    position: int
