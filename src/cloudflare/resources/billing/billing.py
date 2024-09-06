# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .profiles import ProfilesResource, AsyncProfilesResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .profiles import (
    ProfilesResource,
    AsyncProfilesResource,
    ProfilesResourceWithRawResponse,
    AsyncProfilesResourceWithRawResponse,
    ProfilesResourceWithStreamingResponse,
    AsyncProfilesResourceWithStreamingResponse,
)

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def profiles(self) -> ProfilesResource:
        return ProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self)


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        return AsyncProfilesResource(self._client)

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
    def profiles(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self._billing.profiles)


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self._billing.profiles)


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self._billing.profiles)


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self._billing.profiles)
