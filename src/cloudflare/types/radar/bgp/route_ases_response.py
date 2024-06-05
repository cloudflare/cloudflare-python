# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RouteAsesResponse", "ASN", "Meta"]


class ASN(BaseModel):
    asn: int

    cone_size: int = FieldInfo(alias="coneSize")
    """AS's customer cone size"""

    country: str
    """2-letter country code for the AS's registration country"""

    ipv4_count: int = FieldInfo(alias="ipv4Count")
    """number of IPv4 addresses originated by the AS"""

    ipv6_count: str = FieldInfo(alias="ipv6Count")
    """number of IPv6 addresses originated by the AS"""

    name: str
    """name of the AS"""

    pfxs_count: int = FieldInfo(alias="pfxsCount")
    """number of total IP prefixes originated by the AS"""

    rpki_invalid: int = FieldInfo(alias="rpkiInvalid")
    """number of RPKI invalid prefixes originated by the AS"""

    rpki_unknown: int = FieldInfo(alias="rpkiUnknown")
    """number of RPKI unknown prefixes originated by the AS"""

    rpki_valid: int = FieldInfo(alias="rpkiValid")
    """number of RPKI valid prefixes originated by the AS"""


class Meta(BaseModel):
    data_time: str = FieldInfo(alias="dataTime")
    """the timestamp of when the data is generated"""

    query_time: str = FieldInfo(alias="queryTime")
    """the timestamp of the query"""

    total_peers: int = FieldInfo(alias="totalPeers")
    """total number of route collector peers used to generate this data"""


class RouteAsesResponse(BaseModel):
    asns: List[ASN]

    meta: Meta
