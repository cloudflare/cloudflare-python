# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GSuiteGroupRuleParam", "GSuite"]


class GSuite(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Google Workspace identity provider."""

    email: Required[str]
    """The email of the Google Workspace group."""


class GSuiteGroupRuleParam(TypedDict, total=False):
    gsuite: Required[GSuite]
