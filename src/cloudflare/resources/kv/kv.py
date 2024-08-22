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

__all__ = ["KVResource", "AsyncKVResource"]

class KVResource(SyncAPIResource):
    @cached_property
    def namespaces(self) -> NamespacesResource:
        return NamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> KVResourceWithRawResponse:
        return KVResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KVResourceWithStreamingResponse:
        return KVResourceWithStreamingResponse(self)

class AsyncKVResource(AsyncAPIResource):
    @cached_property
    def namespaces(self) -> AsyncNamespacesResource:
        return AsyncNamespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKVResourceWithRawResponse:
        return AsyncKVResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKVResourceWithStreamingResponse:
        return AsyncKVResourceWithStreamingResponse(self)

class KVResourceWithRawResponse:
    def __init__(self, kv: KVResource) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> NamespacesResourceWithRawResponse:
        return NamespacesResourceWithRawResponse(self._kv.namespaces)

class AsyncKVResourceWithRawResponse:
    def __init__(self, kv: AsyncKVResource) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithRawResponse:
        return AsyncNamespacesResourceWithRawResponse(self._kv.namespaces)

class KVResourceWithStreamingResponse:
    def __init__(self, kv: KVResource) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> NamespacesResourceWithStreamingResponse:
        return NamespacesResourceWithStreamingResponse(self._kv.namespaces)

class AsyncKVResourceWithStreamingResponse:
    def __init__(self, kv: AsyncKVResource) -> None:
        self._kv = kv

    @cached_property
    def namespaces(self) -> AsyncNamespacesResourceWithStreamingResponse:
        return AsyncNamespacesResourceWithStreamingResponse(self._kv.namespaces)