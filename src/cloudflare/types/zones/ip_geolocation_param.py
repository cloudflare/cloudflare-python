# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["IPGeolocationParam"]


class IPGeolocationParam(TypedDict, total=False):
    id: Literal["ip_geolocation"]
    """
    Cloudflare adds a CF-IPCountry HTTP header containing the country code that
    corresponds to the visitor.
    """

    value: Literal["on", "off"]
    """The status of adding the IP Geolocation Header."""
