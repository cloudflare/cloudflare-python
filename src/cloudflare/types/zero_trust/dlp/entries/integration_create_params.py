# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["IntegrationCreateParams"]


class IntegrationCreateParams(TypedDict, total=False):
    account_id: Required[str]

    enabled: Required[bool]

    entry_id: Required[str]

    profile_id: Optional[str]
    """
    This field is not used as the owning profile. For predefined entries it is
    already set to a predefined profile.
    """
