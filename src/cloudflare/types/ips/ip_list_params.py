# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["IPListParams"]

class IPListParams(TypedDict, total=False):
    networks: str
    """Specified as `jdcloud` to list IPs used by JD Cloud data centers."""