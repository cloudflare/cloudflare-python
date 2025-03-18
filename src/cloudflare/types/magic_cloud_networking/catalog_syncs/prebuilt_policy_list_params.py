# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PrebuiltPolicyListParams"]


class PrebuiltPolicyListParams(TypedDict, total=False):
    account_id: Required[str]

    destination_type: Literal["NONE", "ZERO_TRUST_LIST"]
    """specify type of destination, omit to return all"""
