# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["AddressEmailRoutingDestinationAddressesListDestinationAddressesParams"]


class AddressEmailRoutingDestinationAddressesListDestinationAddressesParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """Sorts results in an ascending or descending order."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""

    verified: Literal[True, False]
    """Filter by verified destination addresses."""
