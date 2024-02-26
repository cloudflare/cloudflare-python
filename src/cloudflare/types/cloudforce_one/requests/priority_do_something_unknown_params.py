# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PriorityDoSomethingUnknownParams"]


class PriorityDoSomethingUnknownParams(TypedDict, total=False):
    page: Required[int]
    """Page number of results"""

    per_page: Required[int]
    """Number of results per page"""
