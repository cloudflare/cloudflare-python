# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["LiveInputStreamLiveInputsListLiveInputsParams"]


class LiveInputStreamLiveInputsListLiveInputsParams(TypedDict, total=False):
    include_counts: bool
    """
    Includes the total number of videos associated with the submitted query
    parameters.
    """
