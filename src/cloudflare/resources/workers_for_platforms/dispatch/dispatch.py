# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .namespaces.namespaces import Namespaces, AsyncNamespaces

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from .namespaces import (
    Namespaces,
    AsyncNamespaces,
    NamespacesWithRawResponse,
    AsyncNamespacesWithRawResponse,
    NamespacesWithStreamingResponse,
    AsyncNamespacesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Dispatch", "AsyncDispatch"]


class Dispatch(SyncAPIResource):
    @cached_property
    def namespaces(self) -> Namespaces:
        return Namespaces(self._client)

    @cached_property
    def with_raw_response(self) -> DispatchWithRawResponse:
        return DispatchWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DispatchWithStreamingResponse:
        return DispatchWithStreamingResponse(self)


class AsyncDispatch(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespaces:
        return AsyncNamespaces(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDispatchWithRawResponse:
        return AsyncDispatchWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDispatchWithStreamingResponse:
        return AsyncDispatchWithStreamingResponse(self)


class DispatchWithRawResponse:
    def __init__(self, dispatch: Dispatch) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self._dispatch.namespaces)


class AsyncDispatchWithRawResponse:
    def __init__(self, dispatch: AsyncDispatch) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self._dispatch.namespaces)


class DispatchWithStreamingResponse:
    def __init__(self, dispatch: Dispatch) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self._dispatch.namespaces)


class AsyncDispatchWithStreamingResponse:
    def __init__(self, dispatch: AsyncDispatch) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self._dispatch.namespaces)
