# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["PolicySetCreateParams", "Policy"]


class PolicySetCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    name: Required[str]
    """Name of the policy set"""

    policies: Required[Optional[Iterable[Policy]]]
    """Policies to include with per-membership enforcement mode"""

    description: str
    """Optional free-form description."""

    exclude_workload_ids: Optional[SequenceNotStr[str]]
    """Workload IDs that exclude matching requests. Exclusions take precedence."""

    include_workload_ids: Optional[SequenceNotStr[str]]
    """Workload IDs that include matching requests.

    Empty or omitted includes all requests before exclusions.
    """

    tags: Dict[str, str]
    """Tags to attach.

    Keys are limited to 256 UTF-8 bytes and values to 1024 UTF-8 bytes.
    """


class Policy(TypedDict, total=False):
    policy_id: Required[str]
    """ID of the member policy"""

    enforce: bool
    """Whether this policy should enforce when it matches.

    Defaults to true; false keeps the policy attached for non-enforcing evaluation.
    """
