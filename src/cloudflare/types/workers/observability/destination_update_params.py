# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DestinationUpdateParams", "Configuration"]


class DestinationUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    configuration: Required[Configuration]

    enabled: Required[bool]


class Configuration(TypedDict, total=False):
    headers: Required[Dict[str, str]]

    type: Required[Literal["logpush"]]

    url: Required[str]
