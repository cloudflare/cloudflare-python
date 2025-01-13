# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TrueClientIPHeaderParam"]


class TrueClientIPHeaderParam(TypedDict, total=False):
    id: Literal["true_client_ip_header"]
    """Turn on or off the True-Client-IP Header feature of the Cloudflare Network app."""

    value: Literal["on", "off"]
    """The status of True Client IP Header."""
