# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["AppSpectrumApplicationsListSpectrumApplicationsParams"]


class AppSpectrumApplicationsListSpectrumApplicationsParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """Sets the direction by which results are ordered."""

    order: Literal["protocol", "app_id", "created_on", "modified_on", "dns"]
    """Application field by which results are ordered."""

    page: float
    """Page number of paginated results.

    This parameter is required in order to use other pagination parameters. If
    included in the query, `result_info` will be present in the response.
    """

    per_page: float
    """Sets the maximum number of results per page."""
