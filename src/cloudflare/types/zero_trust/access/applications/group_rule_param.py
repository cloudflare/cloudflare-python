# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GroupRuleParam", "Group"]


class Group(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created Access group."""


class GroupRuleParam(TypedDict, total=False):
    group: Required[Group]
