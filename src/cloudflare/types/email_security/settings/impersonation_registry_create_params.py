# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ImpersonationRegistryCreateParams"]


class ImpersonationRegistryCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    email: Required[str]

    is_email_regex: Required[bool]

    name: Required[str]
