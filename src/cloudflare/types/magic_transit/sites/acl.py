# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .acl_configuration import ACLConfiguration
from .unnamed_schema_ref_87fa9e5fe9f6b8d607be1df57340d916 import UnnamedSchemaRef87fa9e5fe9f6b8d607be1df57340d916

__all__ = ["ACL"]


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

    lan_1: Optional[ACLConfiguration] = None

    lan_2: Optional[ACLConfiguration] = None

    name: Optional[str] = None
    """The name of the ACL."""

    protocols: Optional[List[UnnamedSchemaRef87fa9e5fe9f6b8d607be1df57340d916]] = None
