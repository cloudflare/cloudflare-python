# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Union

from datetime import date

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["DNSPassiveDNSByIPGetPassiveDNSByIPParams", "StartEndParams"]


class DNSPassiveDNSByIPGetPassiveDNSByIPParams(TypedDict, total=False):
    ipv4: str

    page: float
    """Requested page within paginated list of results."""

    per_page: float
    """Maximum number of results requested."""

    start_end_params: StartEndParams


class StartEndParams(TypedDict, total=False):
    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Defaults to the current date."""

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Defaults to 30 days before the end parameter value."""
