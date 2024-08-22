# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .a_record import ARecord

from .aaaa_record import AAAARecord

from .caa_record import CAARecord

from .cert_record import CERTRecord

from .cname_record import CNAMERecord

from .dnskey_record import DNSKEYRecord

from .ds_record import DSRecord

from .https_record import HTTPSRecord

from .loc_record import LOCRecord

from .mx_record import MXRecord

from .naptr_record import NAPTRRecord

from .ns_record import NSRecord

from .ptr_record import PTRRecord

from .smimea_record import SMIMEARecord

from .srv_record import SRVRecord

from .sshfp_record import SSHFPRecord

from .svcb_record import SVCBRecord

from .tlsa_record import TLSARecord

from .txt_record import TXTRecord

from .uri_record import URIRecord

from ..._utils import PropertyInfo

from typing_extensions import TypeAlias, Annotated

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Record"]

Record: TypeAlias = Annotated[Union[ARecord, AAAARecord, CAARecord, CERTRecord, CNAMERecord, DNSKEYRecord, DSRecord, HTTPSRecord, LOCRecord, MXRecord, NAPTRRecord, NSRecord, PTRRecord, SMIMEARecord, SRVRecord, SSHFPRecord, SVCBRecord, TLSARecord, TXTRecord, URIRecord], PropertyInfo(discriminator="type")]