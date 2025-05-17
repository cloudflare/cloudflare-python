# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RouteAsesResponse", "ASN", "Meta"]


class ASN(BaseModel):
    asn: int

    cone_size: int = FieldInfo(alias="coneSize")
    """AS's customer cone size."""

    country: str
    """Alpha-2 code for the AS's registration country."""

    ipv4_count: int = FieldInfo(alias="ipv4Count")
    """Number of IPv4 addresses originated by the AS."""

    ipv6_count: str = FieldInfo(alias="ipv6Count")
    """Number of IPv6 addresses originated by the AS."""

    name: str
    """Name of the AS."""

    pfxs_count: int = FieldInfo(alias="pfxsCount")
    """Number of total IP prefixes originated by the AS."""

    rpki_invalid: int = FieldInfo(alias="rpkiInvalid")
    """Number of RPKI invalid prefixes originated by the AS."""

    rpki_unknown: int = FieldInfo(alias="rpkiUnknown")
    """Number of RPKI unknown prefixes originated by the AS."""

    rpki_valid: int = FieldInfo(alias="rpkiValid")
    """Number of RPKI valid prefixes originated by the AS."""


class Meta(BaseModel):
    data_time: str = FieldInfo(alias="dataTime")
    """The timestamp of when the data is generated."""

    query_time: str = FieldInfo(alias="queryTime")
    """The timestamp of the query."""

    total_peers: int = FieldInfo(alias="totalPeers")
    """Total number of route collector peers used to generate this data."""


class RouteAsesResponse(BaseModel):
    asns: List[ASN]

    meta: Meta
