# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from .request_model_param import RequestModelParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["ManagedHeaderEditParams"]


class ManagedHeaderEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    managed_request_headers: Required[Iterable[RequestModelParam]]

    managed_response_headers: Required[Iterable[RequestModelParam]]
