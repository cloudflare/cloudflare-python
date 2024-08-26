# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.user.billing.profile_get_response import ProfileGetResponse

__all__ = ["ProfileResource", "AsyncProfileResource"]


class ProfileResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileGetResponse:
        """Accesses your billing profile object."""
        return self._get(
            "/user/billing/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ProfileGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ProfileGetResponse], ResultWrapper[ProfileGetResponse]),
        )


class AsyncProfileResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileGetResponse:
        """Accesses your billing profile object."""
        return await self._get(
            "/user/billing/profile",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ProfileGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ProfileGetResponse], ResultWrapper[ProfileGetResponse]),
        )


class ProfileResourceWithRawResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.get = to_raw_response_wrapper(
            profile.get,
        )


class AsyncProfileResourceWithRawResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.get = async_to_raw_response_wrapper(
            profile.get,
        )


class ProfileResourceWithStreamingResponse:
    def __init__(self, profile: ProfileResource) -> None:
        self._profile = profile

        self.get = to_streamed_response_wrapper(
            profile.get,
        )


class AsyncProfileResourceWithStreamingResponse:
    def __init__(self, profile: AsyncProfileResource) -> None:
        self._profile = profile

        self.get = async_to_streamed_response_wrapper(
            profile.get,
        )
