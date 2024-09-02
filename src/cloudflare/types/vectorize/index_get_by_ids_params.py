# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["IndexGetByIDsParams"]


class IndexGetByIDsParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    ids: List[str]
    """A list of vector identifiers to retrieve from the index indicated by the path."""
