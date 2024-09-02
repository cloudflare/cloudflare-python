# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .namespaces.namespaces import NamespacesResource, AsyncNamespacesResource

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .namespaces import (
    NamespacesResource,
    AsyncNamespacesResource,
    NamespacesResourceWithRawResponse,
    AsyncNamespacesResourceWithRawResponse,
    NamespacesResourceWithStreamingResponse,
    AsyncNamespacesResourceWithStreamingResponse,
)

__all__ = ["DispatchResource", "AsyncDispatchResource"]


class DispatchResource(SyncAPIResource):
    @cached_property
    def namespaces(self) -> NamespacesResource:
        return NamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DispatchResourceWithRawResponse:
        return DispatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DispatchResourceWithStreamingResponse:
        return DispatchResourceWithStreamingResponse(self)


class AsyncDispatchResource(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespacesResource:
        return AsyncNamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDispatchResourceWithRawResponse:
        return AsyncDispatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDispatchResourceWithStreamingResponse:
        return AsyncDispatchResourceWithStreamingResponse(self)


class DispatchResourceWithRawResponse:
    def __init__(self, dispatch: DispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> NamespacesResourceWithRawResponse:
        return NamespacesResourceWithRawResponse(self._dispatch.namespaces)


class AsyncDispatchResourceWithRawResponse:
    def __init__(self, dispatch: AsyncDispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithRawResponse:
        return AsyncNamespacesResourceWithRawResponse(self._dispatch.namespaces)


class DispatchResourceWithStreamingResponse:
    def __init__(self, dispatch: DispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> NamespacesResourceWithStreamingResponse:
        return NamespacesResourceWithStreamingResponse(self._dispatch.namespaces)


class AsyncDispatchResourceWithStreamingResponse:
    def __init__(self, dispatch: AsyncDispatchResource) -> None:
        self._dispatch = dispatch

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithStreamingResponse:
        return AsyncNamespacesResourceWithStreamingResponse(self._dispatch.namespaces)
