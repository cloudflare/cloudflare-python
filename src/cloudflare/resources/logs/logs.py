# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .controls.controls import Controls, AsyncControls

from ..._compat import cached_property

from .rayids import Rayids, AsyncRayids

from .receiveds.receiveds import Receiveds, AsyncReceiveds

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .controls import (
    Controls,
    AsyncControls,
    ControlsWithRawResponse,
    AsyncControlsWithRawResponse,
    ControlsWithStreamingResponse,
    AsyncControlsWithStreamingResponse,
)
from .rayids import (
    Rayids,
    AsyncRayids,
    RayidsWithRawResponse,
    AsyncRayidsWithRawResponse,
    RayidsWithStreamingResponse,
    AsyncRayidsWithStreamingResponse,
)
from .receiveds import (
    Receiveds,
    AsyncReceiveds,
    ReceivedsWithRawResponse,
    AsyncReceivedsWithRawResponse,
    ReceivedsWithStreamingResponse,
    AsyncReceivedsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Logs", "AsyncLogs"]


class Logs(SyncAPIResource):
    @cached_property
    def controls(self) -> Controls:
        return Controls(self._client)

    @cached_property
    def rayids(self) -> Rayids:
        return Rayids(self._client)

    @cached_property
    def receiveds(self) -> Receiveds:
        return Receiveds(self._client)

    @cached_property
    def with_raw_response(self) -> LogsWithRawResponse:
        return LogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsWithStreamingResponse:
        return LogsWithStreamingResponse(self)


class AsyncLogs(AsyncAPIResource):
    @cached_property
    def controls(self) -> AsyncControls:
        return AsyncControls(self._client)

    @cached_property
    def rayids(self) -> AsyncRayids:
        return AsyncRayids(self._client)

    @cached_property
    def receiveds(self) -> AsyncReceiveds:
        return AsyncReceiveds(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLogsWithRawResponse:
        return AsyncLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsWithStreamingResponse:
        return AsyncLogsWithStreamingResponse(self)


class LogsWithRawResponse:
    def __init__(self, logs: Logs) -> None:
        self._logs = logs

    @cached_property
    def controls(self) -> ControlsWithRawResponse:
        return ControlsWithRawResponse(self._logs.controls)

    @cached_property
    def rayids(self) -> RayidsWithRawResponse:
        return RayidsWithRawResponse(self._logs.rayids)

    @cached_property
    def receiveds(self) -> ReceivedsWithRawResponse:
        return ReceivedsWithRawResponse(self._logs.receiveds)


class AsyncLogsWithRawResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

    @cached_property
    def controls(self) -> AsyncControlsWithRawResponse:
        return AsyncControlsWithRawResponse(self._logs.controls)

    @cached_property
    def rayids(self) -> AsyncRayidsWithRawResponse:
        return AsyncRayidsWithRawResponse(self._logs.rayids)

    @cached_property
    def receiveds(self) -> AsyncReceivedsWithRawResponse:
        return AsyncReceivedsWithRawResponse(self._logs.receiveds)


class LogsWithStreamingResponse:
    def __init__(self, logs: Logs) -> None:
        self._logs = logs

    @cached_property
    def controls(self) -> ControlsWithStreamingResponse:
        return ControlsWithStreamingResponse(self._logs.controls)

    @cached_property
    def rayids(self) -> RayidsWithStreamingResponse:
        return RayidsWithStreamingResponse(self._logs.rayids)

    @cached_property
    def receiveds(self) -> ReceivedsWithStreamingResponse:
        return ReceivedsWithStreamingResponse(self._logs.receiveds)


class AsyncLogsWithStreamingResponse:
    def __init__(self, logs: AsyncLogs) -> None:
        self._logs = logs

    @cached_property
    def controls(self) -> AsyncControlsWithStreamingResponse:
        return AsyncControlsWithStreamingResponse(self._logs.controls)

    @cached_property
    def rayids(self) -> AsyncRayidsWithStreamingResponse:
        return AsyncRayidsWithStreamingResponse(self._logs.rayids)

    @cached_property
    def receiveds(self) -> AsyncReceivedsWithStreamingResponse:
        return AsyncReceivedsWithStreamingResponse(self._logs.receiveds)
