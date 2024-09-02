# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["InviteEditParams"]


class InviteEditParams(TypedDict, total=False):
    status: Required[Literal["accepted", "rejected"]]
    """Status of your response to the invitation (rejected or accepted)."""
