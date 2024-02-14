# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["AccountMemberCreateParams"]


class AccountMemberCreateParams(TypedDict, total=False):
    email: Required[str]
    """The contact email address of the user."""

    roles: Required[List[str]]
    """Array of roles associated with this member."""

    status: Literal["accepted", "pending"]
