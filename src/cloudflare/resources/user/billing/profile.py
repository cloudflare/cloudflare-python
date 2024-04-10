# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

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
from ...._base_client import (
    make_request_options,
)
from ....types.user.billing import ProfileGetResponse

__all__ = ["Profile", "AsyncProfile"]


class Profile(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfileWithRawResponse:
        return ProfileWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileWithStreamingResponse:
        return ProfileWithStreamingResponse(self)

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
        return cast(
            ProfileGetResponse,
            self._get(
                "/user/billing/profile",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ProfileGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncProfile(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfileWithRawResponse:
        return AsyncProfileWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileWithStreamingResponse:
        return AsyncProfileWithStreamingResponse(self)

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
        return cast(
            ProfileGetResponse,
            await self._get(
                "/user/billing/profile",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ProfileGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ProfileWithRawResponse:
    def __init__(self, profile: Profile) -> None:
        self._profile = profile

        self.get = to_raw_response_wrapper(
            profile.get,
        )


class AsyncProfileWithRawResponse:
    def __init__(self, profile: AsyncProfile) -> None:
        self._profile = profile

        self.get = async_to_raw_response_wrapper(
            profile.get,
        )


class ProfileWithStreamingResponse:
    def __init__(self, profile: Profile) -> None:
        self._profile = profile

        self.get = to_streamed_response_wrapper(
            profile.get,
        )


class AsyncProfileWithStreamingResponse:
    def __init__(self, profile: AsyncProfile) -> None:
        self._profile = profile

        self.get = async_to_streamed_response_wrapper(
            profile.get,
        )
