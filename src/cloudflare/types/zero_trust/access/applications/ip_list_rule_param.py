# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPListRuleParam", "IPList"]


class IPList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created IP list."""


class IPListRuleParam(TypedDict, total=False):
    ip_list: Required[IPList]
