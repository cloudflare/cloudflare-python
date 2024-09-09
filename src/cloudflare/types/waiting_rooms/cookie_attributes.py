# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CookieAttributes"]


class CookieAttributes(BaseModel):
    samesite: Optional[Literal["auto", "lax", "none", "strict"]] = None
    """Configures the SameSite attribute on the waiting room cookie.

    Value `auto` will be translated to `lax` or `none` depending if **Always Use
    HTTPS** is enabled. Note that when using value `none`, the secure attribute
    cannot be set to `never`.
    """

    secure: Optional[Literal["auto", "always", "never"]] = None
    """Configures the Secure attribute on the waiting room cookie.

    Value `always` indicates that the Secure attribute will be set in the Set-Cookie
    header, `never` indicates that the Secure attribute will not be set, and `auto`
    will set the Secure attribute depending if **Always Use HTTPS** is enabled.
    """
