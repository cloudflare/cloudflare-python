# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TagCreateParams"]


class TagCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: Required[str]
    """The name of the tag"""

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
