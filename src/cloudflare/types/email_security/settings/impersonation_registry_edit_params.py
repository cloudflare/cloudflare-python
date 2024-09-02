# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ImpersonationRegistryEditParams"]


class ImpersonationRegistryEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    email: Optional[str]

    is_email_regex: Optional[bool]

    name: Optional[str]
