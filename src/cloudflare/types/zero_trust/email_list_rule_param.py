# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailListRuleParam", "EmailList"]


class EmailList(TypedDict, total=False):
    id: Required[str]
    """The ID of a previously created email list."""


class EmailListRuleParam(TypedDict, total=False):
    email_list: Required[EmailList]
