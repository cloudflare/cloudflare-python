# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ServiceCreateParams", "Host"]


class ServiceCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier"""

    host: Required[Host]

    name: Required[str]

    type: Required[Literal["http"]]

    http_port: Optional[int]

    https_port: Optional[int]


class Host(TypedDict, total=False):
    hostname: Optional[str]

    ipv4: str

    ipv6: str

    network: object

    resolver_network: object
