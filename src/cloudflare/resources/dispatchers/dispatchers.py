# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .scripts import Scripts, AsyncScripts

from ..._compat import cached_property

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
from .scripts import (
    Scripts,
    AsyncScripts,
    ScriptsWithRawResponse,
    AsyncScriptsWithRawResponse,
    ScriptsWithStreamingResponse,
    AsyncScriptsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Dispatchers", "AsyncDispatchers"]


class Dispatchers(SyncAPIResource):
    @cached_property
    def scripts(self) -> Scripts:
        return Scripts(self._client)

    @cached_property
    def with_raw_response(self) -> DispatchersWithRawResponse:
        return DispatchersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DispatchersWithStreamingResponse:
        return DispatchersWithStreamingResponse(self)


class AsyncDispatchers(AsyncAPIResource):
    @cached_property
    def scripts(self) -> AsyncScripts:
        return AsyncScripts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDispatchersWithRawResponse:
        return AsyncDispatchersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDispatchersWithStreamingResponse:
        return AsyncDispatchersWithStreamingResponse(self)


class DispatchersWithRawResponse:
    def __init__(self, dispatchers: Dispatchers) -> None:
        self._dispatchers = dispatchers

    @cached_property
    def scripts(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self._dispatchers.scripts)


class AsyncDispatchersWithRawResponse:
    def __init__(self, dispatchers: AsyncDispatchers) -> None:
        self._dispatchers = dispatchers

    @cached_property
    def scripts(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self._dispatchers.scripts)


class DispatchersWithStreamingResponse:
    def __init__(self, dispatchers: Dispatchers) -> None:
        self._dispatchers = dispatchers

    @cached_property
    def scripts(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self._dispatchers.scripts)


class AsyncDispatchersWithStreamingResponse:
    def __init__(self, dispatchers: AsyncDispatchers) -> None:
        self._dispatchers = dispatchers

    @cached_property
    def scripts(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self._dispatchers.scripts)
