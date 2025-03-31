# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .allowed_protocol import AllowedProtocol
from .acl_configuration import ACLConfiguration

__all__ = ["ACL"]


class ACL(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    description: Optional[str] = None
    """Description for the ACL."""

    forward_locally: Optional[bool] = None
    """The desired forwarding action for this ACL policy.

    If set to "false", the policy will forward traffic to Cloudflare. If set to
    "true", the policy will forward traffic locally on the Magic Connector. If not
    included in request, will default to false.
    """

    lan_1: Optional[ACLConfiguration] = None

    lan_2: Optional[ACLConfiguration] = None

    name: Optional[str] = None
    """The name of the ACL."""

    protocols: Optional[List[AllowedProtocol]] = None

    unidirectional: Optional[bool] = None
    """The desired traffic direction for this ACL policy.

    If set to "false", the policy will allow bidirectional traffic. If set to
    "true", the policy will only allow traffic in one direction. If not included in
    request, will default to false.
    """
