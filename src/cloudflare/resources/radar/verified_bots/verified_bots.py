# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .top import TopResource, AsyncTopResource

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .top import TopResource, AsyncTopResource, TopResourceWithRawResponse, AsyncTopResourceWithRawResponse, TopResourceWithStreamingResponse, AsyncTopResourceWithStreamingResponse

__all__ = ["VerifiedBotsResource", "AsyncVerifiedBotsResource"]

class VerifiedBotsResource(SyncAPIResource):
    @cached_property
    def top(self) -> TopResource:
        return TopResource(self._client)

    @cached_property
    def with_raw_response(self) -> VerifiedBotsResourceWithRawResponse:
        return VerifiedBotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifiedBotsResourceWithStreamingResponse:
        return VerifiedBotsResourceWithStreamingResponse(self)

class AsyncVerifiedBotsResource(AsyncAPIResource):
    @cached_property
    def top(self) -> AsyncTopResource:
        return AsyncTopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVerifiedBotsResourceWithRawResponse:
        return AsyncVerifiedBotsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifiedBotsResourceWithStreamingResponse:
        return AsyncVerifiedBotsResourceWithStreamingResponse(self)

class VerifiedBotsResourceWithRawResponse:
    def __init__(self, verified_bots: VerifiedBotsResource) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def top(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self._verified_bots.top)

class AsyncVerifiedBotsResourceWithRawResponse:
    def __init__(self, verified_bots: AsyncVerifiedBotsResource) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def top(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self._verified_bots.top)

class VerifiedBotsResourceWithStreamingResponse:
    def __init__(self, verified_bots: VerifiedBotsResource) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def top(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self._verified_bots.top)

class AsyncVerifiedBotsResourceWithStreamingResponse:
    def __init__(self, verified_bots: AsyncVerifiedBotsResource) -> None:
        self._verified_bots = verified_bots

    @cached_property
    def top(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self._verified_bots.top)