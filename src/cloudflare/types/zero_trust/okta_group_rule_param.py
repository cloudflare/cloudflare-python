# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["OktaGroupRuleParam", "Okta"]


class Okta(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of your Okta identity provider."""

    email: Required[str]
    """The email of the Okta group."""


class OktaGroupRuleParam(TypedDict, total=False):
    okta: Required[Okta]
