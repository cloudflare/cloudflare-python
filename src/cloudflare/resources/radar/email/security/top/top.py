# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tlds.tlds import TldsResource, AsyncTldsResource

from ......_compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......types import shared_params
from .tlds import TldsResource, AsyncTldsResource, TldsResourceWithRawResponse, AsyncTldsResourceWithRawResponse, TldsResourceWithStreamingResponse, AsyncTldsResourceWithStreamingResponse

__all__ = ["TopResource", "AsyncTopResource"]

class TopResource(SyncAPIResource):
    @cached_property
    def tlds(self) -> TldsResource:
        return TldsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self)

class AsyncTopResource(AsyncAPIResource):
    @cached_property
    def tlds(self) -> AsyncTldsResource:
        return AsyncTldsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self)

class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> TldsResourceWithRawResponse:
        return TldsResourceWithRawResponse(self._top.tlds)

class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> AsyncTldsResourceWithRawResponse:
        return AsyncTldsResourceWithRawResponse(self._top.tlds)

class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> TldsResourceWithStreamingResponse:
        return TldsResourceWithStreamingResponse(self._top.tlds)

class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> AsyncTldsResourceWithStreamingResponse:
        return AsyncTldsResourceWithStreamingResponse(self._top.tlds)