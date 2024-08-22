# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CookieAttributesParam"]


class CookieAttributesParam(TypedDict, total=False):
    samesite: Literal["auto", "lax", "none", "strict"]
    """Configures the SameSite attribute on the waiting room cookie.

    Value `auto` will be translated to `lax` or `none` depending if **Always Use
    HTTPS** is enabled. Note that when using value `none`, the secure attribute
    cannot be set to `never`.
    """

    secure: Literal["auto", "always", "never"]
    """Configures the Secure attribute on the waiting room cookie.

    Value `always` indicates that the Secure attribute will be set in the Set-Cookie
    header, `never` indicates that the Secure attribute will not be set, and `auto`
    will set the Secure attribute depending if **Always Use HTTPS** is enabled.
    """
