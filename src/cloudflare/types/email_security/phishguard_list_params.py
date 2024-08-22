# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PhishguardListParams"]


class PhishguardListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    from_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    to_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
