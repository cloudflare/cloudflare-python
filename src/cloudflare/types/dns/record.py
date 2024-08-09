# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .a_record import ARecord
from .ds_record import DSRecord
from .mx_record import MXRecord
from .ns_record import NSRecord
from .caa_record import CAARecord
from .loc_record import LOCRecord
from .ptr_record import PTRRecord
from .srv_record import SRVRecord
from .txt_record import TXTRecord
from .uri_record import URIRecord
from .aaaa_record import AAAARecord
from .cert_record import CERTRecord
from .svcb_record import SVCBRecord
from .tlsa_record import TLSARecord
from .cname_record import CNAMERecord
from .https_record import HTTPSRecord
from .naptr_record import NAPTRRecord
from .sshfp_record import SSHFPRecord
from .dnskey_record import DNSKEYRecord
from .smimea_record import SMIMEARecord

__all__ = ["Record"]

Record: TypeAlias = Annotated[
    Union[
        ARecord,
        AAAARecord,
        CAARecord,
        CERTRecord,
        CNAMERecord,
        DNSKEYRecord,
        DSRecord,
        HTTPSRecord,
        LOCRecord,
        MXRecord,
        NAPTRRecord,
        NSRecord,
        PTRRecord,
        SMIMEARecord,
        SRVRecord,
        SSHFPRecord,
        SVCBRecord,
        TLSARecord,
        TXTRecord,
        URIRecord,
    ],
    PropertyInfo(discriminator="type"),
]
