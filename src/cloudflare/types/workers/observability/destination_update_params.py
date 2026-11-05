# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DestinationUpdateParams", "Configuration"]


class DestinationUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    enabled: Required[bool]

    configuration: Configuration


class Configuration(TypedDict, total=False):
    headers: Required[Dict[str, Optional[str]]]

    type: Required[Literal["logpush"]]

    url: Required[str]

    replace_headers: Annotated[bool, PropertyInfo(alias="replaceHeaders")]
