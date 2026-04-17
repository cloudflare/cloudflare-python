# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DestinationCreateParams", "Configuration"]


class DestinationCreateParams(TypedDict, total=False):
    account_id: str

    configuration: Required[Configuration]

    enabled: Required[bool]

    name: Required[str]

    skip_preflight_check: Annotated[bool, PropertyInfo(alias="skipPreflightCheck")]


class Configuration(TypedDict, total=False):
    headers: Required[Dict[str, str]]

    logpush_dataset: Required[
        Annotated[Literal["opentelemetry-traces", "opentelemetry-logs"], PropertyInfo(alias="logpushDataset")]
    ]

    type: Required[Literal["logpush"]]

    url: Required[str]
