# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .history import HistoryResource, AsyncHistoryResource

from ...._compat import cached_property

from .profile import ProfileResource, AsyncProfileResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .history import HistoryResource, AsyncHistoryResource, HistoryResourceWithRawResponse, AsyncHistoryResourceWithRawResponse, HistoryResourceWithStreamingResponse, AsyncHistoryResourceWithStreamingResponse
from .profile import ProfileResource, AsyncProfileResource, ProfileResourceWithRawResponse, AsyncProfileResourceWithRawResponse, ProfileResourceWithStreamingResponse, AsyncProfileResourceWithStreamingResponse

__all__ = ["BillingResource", "AsyncBillingResource"]

class BillingResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def profile(self) -> ProfileResource:
        return ProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self)

class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        return AsyncProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self)

class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._billing.history)

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self._billing.profile)

class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._billing.history)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self._billing.profile)

class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._billing.history)

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self._billing.profile)

class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._billing.history)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self._billing.profile)