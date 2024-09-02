# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["SAMLGroupRuleParam", "SAML"]


class SAML(TypedDict, total=False):
    attribute_name: Required[str]
    """The name of the SAML attribute."""

    attribute_value: Required[str]
    """The SAML attribute value to look for."""


class SAMLGroupRuleParam(TypedDict, total=False):
    saml: Required[SAML]
