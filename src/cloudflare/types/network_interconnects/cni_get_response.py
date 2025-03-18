# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CNIGetResponse", "Magic", "BGP"]


class Magic(BaseModel):
    conduit_name: str

    description: str

    mtu: int


class BGP(BaseModel):
    customer_asn: int
    """ASN used on the customer end of the BGP session"""

    extra_prefixes: List[str]
    """Extra set of static prefixes to advertise to the customer's end of the session"""

    md5_key: Optional[str] = None
    """MD5 key to use for session authentication.

    Note that _this is not a security measure_. MD5 is not a valid security
    mechanism, and the key is not treated as a secret value. This is _only_
    supported for preventing misconfiguration, not for defending against malicious
    attacks.

    The MD5 key, if set, must be of non-zero length and consist only of the
    following types of character:

    - ASCII alphanumerics: `[a-zA-Z0-9]`
    - Special characters in the set `'!@#$%^&*()+[]{}<>/.,;:_-~`= \\||`

    In other words, MD5 keys may contain any printable ASCII character aside from
    newline (0x0A), quotation mark (`"`), vertical tab (0x0B), carriage return
    (0x0D), tab (0x09), form feed (0x0C), and the question mark (`?`). Requests
    specifying an MD5 key with one or more of these disallowed characters will be
    rejected.
    """


class CNIGetResponse(BaseModel):
    id: str

    account: str
    """Customer account tag"""

    cust_ip: str
    """Customer end of the point-to-point link

    This should always be inside the same prefix as `p2p_ip`.
    """

    interconnect: str
    """Interconnect identifier hosting this CNI"""

    magic: Magic

    p2p_ip: str
    """Cloudflare end of the point-to-point link"""

    bgp: Optional[BGP] = None
