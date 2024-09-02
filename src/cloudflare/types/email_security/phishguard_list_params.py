# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Union

from datetime import date

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["PhishguardListParams"]


class PhishguardListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account Identifier"""

    from_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    to_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
