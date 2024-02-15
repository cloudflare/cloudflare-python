# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OriginTLSClientAuthCreateParams"]


class OriginTLSClientAuthCreateParams(TypedDict, total=False):
    certificate: Required[str]
    """The zone's leaf certificate."""

    private_key: Required[str]
    """The zone's private key."""
