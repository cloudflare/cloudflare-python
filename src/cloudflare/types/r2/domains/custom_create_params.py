# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["CustomCreateParams"]


class CustomCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    domain: Required[str]
    """Name of the custom domain to be added"""

    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]
    """Zone ID of the custom domain"""

    enabled: bool
    """Whether to enable public bucket access at the custom domain.

    If undefined, the domain will be enabled.
    """
