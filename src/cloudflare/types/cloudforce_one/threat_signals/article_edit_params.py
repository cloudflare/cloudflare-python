# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ArticleEditParams"]


class ArticleEditParams(TypedDict, total=False):
    account_id: Required[str]

    read: Required[bool]
