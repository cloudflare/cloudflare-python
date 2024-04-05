# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SamlGroupRuleParam", "Saml"]


class Saml(TypedDict, total=False):
    attribute_name: Required[str]
    """The name of the SAML attribute."""

    attribute_value: Required[str]
    """The SAML attribute value to look for."""


class SamlGroupRuleParam(TypedDict, total=False):
    saml: Required[Saml]
