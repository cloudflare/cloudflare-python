# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    password: Required[str]
    """Password stored only as a one-way hash and never returned.

    Maximum 72 UTF-8 bytes.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Optional deactivation deadline (RFC 3339). Omit or null for no expiry."""
