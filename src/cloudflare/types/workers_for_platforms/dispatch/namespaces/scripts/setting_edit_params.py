# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ......types import shared_params

__all__ = ["SettingEditParams", "Result", "ResultTailConsumer"]


class SettingEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    errors: Required[Iterable[shared_params.UnnamedSchemaRef172]]

    messages: Required[Iterable[shared_params.UnnamedSchemaRef172]]

    result: Required[Result]

    success: Required[Literal[True]]
    """Whether the API call was successful"""


class ResultTailConsumer(TypedDict, total=False):
    service: Required[str]
    """Name of Worker that is to be the consumer."""

    environment: str
    """Optional environment if the Worker utilizes one."""

    namespace: str
    """Optional dispatch namespace the script belongs to."""


class Result(TypedDict, total=False):
    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    tail_consumers: Iterable[ResultTailConsumer]
    """List of Workers that will consume logs from the attached Worker."""
