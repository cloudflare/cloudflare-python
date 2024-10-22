# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

from .a_record_param import ARecordParam
from .ds_record_param import DSRecordParam
from .mx_record_param import MXRecordParam
from .ns_record_param import NSRecordParam
from .caa_record_param import CAARecordParam
from .loc_record_param import LOCRecordParam
from .ptr_record_param import PTRRecordParam
from .srv_record_param import SRVRecordParam
from .txt_record_param import TXTRecordParam
from .uri_record_param import URIRecordParam
from .aaaa_record_param import AAAARecordParam
from .cert_record_param import CERTRecordParam
from .svcb_record_param import SVCBRecordParam
from .tlsa_record_param import TLSARecordParam
from .cname_record_param import CNAMERecordParam
from .https_record_param import HTTPSRecordParam
from .naptr_record_param import NAPTRRecordParam
from .sshfp_record_param import SSHFPRecordParam
from .dnskey_record_param import DNSKEYRecordParam
from .smimea_record_param import SMIMEARecordParam

__all__ = ["RecordParam", "Openpgpkey"]


class Openpgpkey(TypedDict, total=False):
    content: str
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    type: Literal["OPENPGPKEY"]
    """Record type."""


RecordParam: TypeAlias = Union[
    ARecordParam,
    AAAARecordParam,
    CAARecordParam,
    CERTRecordParam,
    CNAMERecordParam,
    DNSKEYRecordParam,
    DSRecordParam,
    HTTPSRecordParam,
    LOCRecordParam,
    MXRecordParam,
    NAPTRRecordParam,
    NSRecordParam,
    Openpgpkey,
    PTRRecordParam,
    SMIMEARecordParam,
    SRVRecordParam,
    SSHFPRecordParam,
    SVCBRecordParam,
    TLSARecordParam,
    TXTRecordParam,
    URIRecordParam,
]
