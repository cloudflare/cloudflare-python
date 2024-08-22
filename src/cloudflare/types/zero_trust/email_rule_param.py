# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailRuleParam", "Email"]


class Email(TypedDict, total=False):
    email: Required[str]
    """The email of the user."""


class EmailRuleParam(TypedDict, total=False):
    email: Required[Email]
