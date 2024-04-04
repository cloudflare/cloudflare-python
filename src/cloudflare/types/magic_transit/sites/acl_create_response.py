# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ...._models import BaseModel
from .unnamed_schema_ref_87fa9e5fe9f6b8d607be1df57340d916 import UnnamedSchemaRef87fa9e5fe9f6b8d607be1df57340d916

__all__ = ["ACLCreateResponse", "ACL", "ACLLAN1", "ACLLAN2"]


class ACLLAN1(BaseModel):
    lan_id: str
    """The identifier for the LAN you want to create an ACL policy with."""

    lan_name: Optional[str] = None
    """The name of the LAN based on the provided lan_id."""

    ports: Optional[List[int]] = None
    """Array of ports on the provided LAN that will be included in the ACL.

    If no ports are provided, communication on any port on this LAN is allowed.
    """

    subnets: Optional[List[Union[str, str]]] = None
    """Array of subnet IPs within the LAN that will be included in the ACL.

    If no subnets are provided, communication on any subnets on this LAN are
    allowed.
    """


class ACLLAN2(BaseModel):
    lan_id: str
    """The identifier for the LAN you want to create an ACL policy with."""

    lan_name: Optional[str] = None
    """The name of the LAN based on the provided lan_id."""

    ports: Optional[List[int]] = None
    """Array of ports on the provided LAN that will be included in the ACL.

    If no ports are provided, communication on any port on this LAN is allowed.
    """

    subnets: Optional[List[Union[str, str]]] = None
    """Array of subnet IPs within the LAN that will be included in the ACL.

    If no subnets are provided, communication on any subnets on this LAN are
    allowed.
    """


class ACL(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    description: Optional[str] = None
    """Description for the ACL."""

    forward_locally: Optional[bool] = None
    """The desired forwarding action for this ACL policy.

    If set to "false", the policy will forward traffic to Cloudflare. If set to
    "true", the policy will forward traffic locally on the Magic WAN Connector. If
    not included in request, will default to false.
    """

    lan_1: Optional[ACLLAN1] = None

    lan_2: Optional[ACLLAN2] = None

    name: Optional[str] = None
    """The name of the ACL."""

    protocols: Optional[List[UnnamedSchemaRef87fa9e5fe9f6b8d607be1df57340d916]] = None


class ACLCreateResponse(BaseModel):
    acls: Optional[List[ACL]] = None
