# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .nameserver_param import NameserverParam

__all__ = ["DNSSettingEditParams"]


class DNSSettingEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    nameservers: NameserverParam
    """
    Settings determining the nameservers through which the zone should be available.
    """
