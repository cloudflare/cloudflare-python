# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ImpersonationRegistryEditParams"]


class ImpersonationRegistryEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    email: Optional[str]

    is_email_regex: Optional[bool]

    name: Optional[str]
