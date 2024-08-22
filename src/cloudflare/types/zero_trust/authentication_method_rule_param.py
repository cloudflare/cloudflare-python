# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["AuthenticationMethodRuleParam", "AuthMethod"]

class AuthMethod(TypedDict, total=False):
    auth_method: Required[str]
    """
    The type of authentication method https://datatracker.ietf.org/doc/html/rfc8176.
    """

class AuthenticationMethodRuleParam(TypedDict, total=False):
    auth_method: Required[AuthMethod]