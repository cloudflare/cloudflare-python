# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from ....._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo
from .....types import shared_params

__all__ = ["CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsParams"]


class CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsParams(TypedDict, total=False):
    app_id_param: str
    """Comma-delimited list of Spectrum Application Id(s).

    If provided, the response will be limited to Spectrum Application Id(s) that
    match.
    """

    app_id: Annotated[str, PropertyInfo(alias="appID")]
    """Comma-delimited list of Spectrum Application Id(s).

    If provided, the response will be limited to Spectrum Application Id(s) that
    match.
    """

    colo_name: str
    """Co-location identifier."""
