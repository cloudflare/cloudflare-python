# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from .acl_configuration import ACLConfiguration

from .allowed_protocol import AllowedProtocol

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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