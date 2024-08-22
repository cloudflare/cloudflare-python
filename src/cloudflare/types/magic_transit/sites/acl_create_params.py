# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from .acl_configuration_param import ACLConfigurationParam

from typing import List

from .allowed_protocol import AllowedProtocol

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ACLCreateParams"]

class ACLCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    lan_1: Required[ACLConfigurationParam]

    lan_2: Required[ACLConfigurationParam]

    name: Required[str]
    """The name of the ACL."""

    description: str
    """Description for the ACL."""

    forward_locally: bool
    """The desired forwarding action for this ACL policy.

    If set to "false", the policy will forward traffic to Cloudflare. If set to
    "true", the policy will forward traffic locally on the Magic Connector. If not
    included in request, will default to false.
    """

    protocols: List[AllowedProtocol]