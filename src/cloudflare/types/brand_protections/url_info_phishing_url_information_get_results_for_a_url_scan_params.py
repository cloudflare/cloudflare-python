# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["URLInfoPhishingURLInformationGetResultsForAURLScanParams", "URLIDParam"]


class URLInfoPhishingURLInformationGetResultsForAURLScanParams(TypedDict, total=False):
    url: str

    url_id_param: URLIDParam


class URLIDParam(TypedDict, total=False):
    url_id: int
    """Submission ID(s) to filter submission results by."""
