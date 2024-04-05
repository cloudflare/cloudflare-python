# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GsuiteGroupRuleParam", "Gsuite"]


class Gsuite(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Google Workspace identity provider."""

    email: Required[str]
    """The email of the Google Workspace group."""


class GsuiteGroupRuleParam(TypedDict, total=False):
    gsuite: Required[Gsuite]
