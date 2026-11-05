# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = [
    "NameserverSetGetResponse",
    "DNSSettingsNameserverSetStandardResponse",
    "DNSSettingsNameserverSetStandardResponseNameserver",
    "DNSSettingsNameserverSetAdvancedResponse",
    "DNSSettingsNameserverSetAdvancedResponseNameserver",
]


class DNSSettingsNameserverSetStandardResponseNameserver(BaseModel):
    ipv4: List[str]
    """IPv4 addresses assigned to the nameserver."""

    ipv6: List[str]
    """IPv6 addresses assigned to the nameserver."""

    name: str
    """A unique lowercase Punycode nameserver name within the set."""


class DNSSettingsNameserverSetStandardResponse(BaseModel):
    id: str
    """Identifier for a nameserver set."""

    advanced: Literal[False]
    """Whether the nameserver set uses Advanced anycast groups."""

    created_on: datetime
    """When the nameserver set was created."""

    ip_set: int
    """Selects the account-specific IP set that supplies the nameserver addresses.

    Nameserver sets with the same `ip_set` and `advanced` value may reuse addresses;
    otherwise, they use disjoint address groups.
    """

    name: str
    """
    Customer-defined name, unique within the account by exact string equality
    (case-sensitive, with no Unicode normalization). Must be valid UTF-8 and at most
    255 UTF-8 bytes, not 255 characters. Only graphical Unicode characters are
    allowed; leading or trailing whitespace is rejected. The name can be changed
    without changing the set's nameservers or addresses.
    """

    nameservers: List[DNSSettingsNameserverSetStandardResponseNameserver]


class DNSSettingsNameserverSetAdvancedResponseNameserver(BaseModel):
    ipv4: List[str]
    """IPv4 addresses assigned to the nameserver."""

    ipv4_groups: List[Literal["a", "b", "c"]]
    """Advanced anycast group for each address in the corresponding address array.

    Entries have the same order as, and correspond one-to-one with, the addresses.
    """

    ipv6: List[str]
    """IPv6 addresses assigned to the nameserver."""

    ipv6_groups: List[Literal["a", "b", "c"]]
    """Advanced anycast group for each address in the corresponding address array.

    Entries have the same order as, and correspond one-to-one with, the addresses.
    """

    name: str
    """A unique lowercase Punycode nameserver name within the set."""


class DNSSettingsNameserverSetAdvancedResponse(BaseModel):
    id: str
    """Identifier for a nameserver set."""

    advanced: Literal[True]
    """Whether the nameserver set uses Advanced anycast groups."""

    created_on: datetime
    """When the nameserver set was created."""

    ip_set: int
    """Selects the account-specific IP set that supplies the nameserver addresses.

    Nameserver sets with the same `ip_set` and `advanced` value may reuse addresses;
    otherwise, they use disjoint address groups.
    """

    name: str
    """
    Customer-defined name, unique within the account by exact string equality
    (case-sensitive, with no Unicode normalization). Must be valid UTF-8 and at most
    255 UTF-8 bytes, not 255 characters. Only graphical Unicode characters are
    allowed; leading or trailing whitespace is rejected. The name can be changed
    without changing the set's nameservers or addresses.
    """

    nameservers: List[DNSSettingsNameserverSetAdvancedResponseNameserver]


NameserverSetGetResponse: TypeAlias = Union[
    DNSSettingsNameserverSetStandardResponse, DNSSettingsNameserverSetAdvancedResponse
]
