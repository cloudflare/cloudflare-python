# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["DeploymentUpdateParams"]


class DeploymentUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    basic_auth_credential_ids: Required[Optional[SequenceNotStr[str]]]
    """Replacement set of basic-auth credential IDs"""

    default_mode: Required[Literal["ALLOW", "BLOCK"]]
    """Default traffic mode: ALLOW or BLOCK"""

    name: Required[str]
    """Name of the deployment"""

    policy_set_ids: Required[Optional[SequenceNotStr[str]]]
    """Replacement set of policy set IDs"""

    description: str
    """Optional free-form description."""

    domain_acl_id: Optional[str]
    """ID of the domain ACL to attach (omit or null to clear)"""

    on_error_action: Literal["BLOCK", "SKIP"]
    """Action for runtime Rego errors. Omit to reset to BLOCK."""

    rego_raise_error: bool
    """Whether OPA builtin failures are raised as runtime evaluation errors.

    Omit to reset to true.
    """

    tags: Dict[str, str]
    """Replacement tag set.

    Omit or use {} to clear. Keys are limited to 256 UTF-8 bytes and values to 1024
    UTF-8 bytes.
    """
