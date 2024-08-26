# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .namespaces.namespaces import NamespacesResource, AsyncNamespacesResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .namespaces import NamespacesResource, AsyncNamespacesResource, NamespacesResourceWithRawResponse, AsyncNamespacesResourceWithRawResponse, NamespacesResourceWithStreamingResponse, AsyncNamespacesResourceWithStreamingResponse

__all__ = ["DurableObjectsResource", "AsyncDurableObjectsResource"]

class DurableObjectsResource(SyncAPIResource):
    @cached_property
    def namespaces(self) -> NamespacesResource:
        return NamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DurableObjectsResourceWithRawResponse:
        return DurableObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DurableObjectsResourceWithStreamingResponse:
        return DurableObjectsResourceWithStreamingResponse(self)

class AsyncDurableObjectsResource(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespacesResource:
        return AsyncNamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDurableObjectsResourceWithRawResponse:
        return AsyncDurableObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDurableObjectsResourceWithStreamingResponse:
        return AsyncDurableObjectsResourceWithStreamingResponse(self)

class DurableObjectsResourceWithRawResponse:
    def __init__(self, durable_objects: DurableObjectsResource) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> NamespacesResourceWithRawResponse:
        return NamespacesResourceWithRawResponse(self._durable_objects.namespaces)

class AsyncDurableObjectsResourceWithRawResponse:
    def __init__(self, durable_objects: AsyncDurableObjectsResource) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithRawResponse:
        return AsyncNamespacesResourceWithRawResponse(self._durable_objects.namespaces)

class DurableObjectsResourceWithStreamingResponse:
    def __init__(self, durable_objects: DurableObjectsResource) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> NamespacesResourceWithStreamingResponse:
        return NamespacesResourceWithStreamingResponse(self._durable_objects.namespaces)

class AsyncDurableObjectsResourceWithStreamingResponse:
    def __init__(self, durable_objects: AsyncDurableObjectsResource) -> None:
        self._durable_objects = durable_objects

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithStreamingResponse:
        return AsyncNamespacesResourceWithStreamingResponse(self._durable_objects.namespaces)