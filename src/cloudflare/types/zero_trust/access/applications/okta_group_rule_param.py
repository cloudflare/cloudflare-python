# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OktaGroupRuleParam", "Okta"]


class Okta(TypedDict, total=False):
    identity_provider_id: Required[str]
    """The ID of your Okta identity provider."""

    name: Required[str]
    """The name of the Okta group."""


class OktaGroupRuleParam(TypedDict, total=False):
    okta: Required[Okta]
