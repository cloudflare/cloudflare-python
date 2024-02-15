# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["ConfigGetParams"]


class ConfigGetParams(TypedDict, total=False):
    ids: Required[Iterable[int]]
    """Comma separated list of Zaraz configuration IDs"""
