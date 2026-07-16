# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ......_types import SequenceNotStr

__all__ = ["JobCreateParams"]


class JobCreateParams(TypedDict, total=False):
    account_id: Required[str]

    finding_instance_ids: Required[SequenceNotStr[str]]
    """UUIDs identifying Finding Instances."""

    remediation_type_id: Required[str]
    """A UUID identifying this Remediation Type."""
