# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PolicyTestGetResponse"]


class PolicyTestGetResponse(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy test."""

    pages_processed: Optional[int] = None
    """The number of pages of (processed) users."""

    percent_approved: Optional[int] = None
    """
    The percentage of (processed) users approved based on policy evaluation results.
    """

    percent_blocked: Optional[int] = None
    """The percentage of (processed) users blocked based on policy evaluation results."""

    percent_users_processed: Optional[int] = None
    """The percentage of users processed so far (of the entire user base)."""

    status: Optional[Literal["blocked", "processing", "complete"]] = None
    """The status of the policy test."""

    total_users: Optional[int] = None
    """The total number of users in the user base."""

    users_approved: Optional[int] = None
    """The number of (processed) users approved based on policy evaluation results."""

    users_blocked: Optional[int] = None
    """The number of (processed) users blocked based on policy evaluation results."""
