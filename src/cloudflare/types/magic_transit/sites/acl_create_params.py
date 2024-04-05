# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .acl_configuration_param import ACLConfigurationParam
from .unnamed_schema_ref_87fa9e5fe9f6b8d607be1df57340d916 import UnnamedSchemaRef87fa9e5fe9f6b8d607be1df57340d916

__all__ = ["ACLCreateParams", "ACL"]


class ACLCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    acl: ACL


class ACL(TypedDict, total=False):
    lan_1: Required[ACLConfigurationParam]

    lan_2: Required[ACLConfigurationParam]

    name: Required[str]
    """The name of the ACL."""

    description: str
    """Description for the ACL."""

    forward_locally: bool
    """The desired forwarding action for this ACL policy.

    If set to "false", the policy will forward traffic to Cloudflare. If set to
    "true", the policy will forward traffic locally on the Magic WAN Connector. If
    not included in request, will default to false.
    """

    protocols: List[UnnamedSchemaRef87fa9e5fe9f6b8d607be1df57340d916]
