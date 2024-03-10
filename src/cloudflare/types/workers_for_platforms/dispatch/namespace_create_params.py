# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NamespaceCreateParams"]


class NamespaceCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: str
    """The name of the dispatch namespace"""
