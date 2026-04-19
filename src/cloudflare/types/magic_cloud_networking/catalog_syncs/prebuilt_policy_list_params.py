# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PrebuiltPolicyListParams"]


class PrebuiltPolicyListParams(TypedDict, total=False):
    account_id: str

    destination_type: Literal["NONE", "ZERO_TRUST_LIST"]
    """Specify type of destination, omit to return all."""
