# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .dns_record import DNSRecord

__all__ = ["DNSGetResponse"]

DNSGetResponse: TypeAlias = List[DNSRecord]
