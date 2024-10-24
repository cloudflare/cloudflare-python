# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NameserverParam"]


class NameserverParam(TypedDict, total=False):
    type: Required[
        Literal["cloudflare.standard", "cloudflare.standard.random", "custom.account", "custom.tenant", "custom.zone"]
    ]
    """Nameserver type"""
