# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ContentPolicyCreateParams"]


class ContentPolicyCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    enabled: Required[bool]
    """Whether the policy is active."""

    name: Required[str]
    """Human-readable name of the policy."""

    pattern: Required[str]
    """Regular expression the policy matches against."""

    targets: Required[List[Literal["SUBJECT", "BODY"]]]
    """Parts of the email the pattern is matched against."""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Timestamp at which the policy expires.

    After this time, Email Security ignores the policy. The value must lie in the
    future. Send `null` to clear the expiration.
    """

    notes: Optional[str]
    """Optional note describing the purpose of the policy."""
