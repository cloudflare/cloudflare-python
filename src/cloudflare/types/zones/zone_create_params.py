# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .type import Type

__all__ = ["ZoneCreateParams", "Account"]


class ZoneCreateParams(TypedDict, total=False):
    account: Required[Account]

    name: Required[str]
    """The domain name.

    Per [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035#section-2.3.4) the
    overall zone name can be up to 253 characters, with each segment ("label") not
    exceeding 63 characters.
    """

    type: Type
    """A full zone implies that DNS is hosted with Cloudflare.

    A partial zone is typically a partner-hosted zone or a CNAME setup.
    """


class Account(TypedDict, total=False):
    id: str
    """Identifier"""
