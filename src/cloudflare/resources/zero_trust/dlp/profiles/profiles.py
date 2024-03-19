# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from .custom import (
    Custom,
    AsyncCustom,
    CustomWithRawResponse,
    AsyncCustomWithRawResponse,
    CustomWithStreamingResponse,
    AsyncCustomWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .predefined import (
    Predefined,
    AsyncPredefined,
    PredefinedWithRawResponse,
    AsyncPredefinedWithRawResponse,
    PredefinedWithStreamingResponse,
    AsyncPredefinedWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.dlp import ProfileGetResponse, ProfileListResponse

__all__ = ["Profiles", "AsyncProfiles"]


class Profiles(SyncAPIResource):
    @cached_property
    def custom(self) -> Custom:
        return Custom(self._client)

    @cached_property
    def predefined(self) -> Predefined:
        return Predefined(self._client)

    @cached_property
    def with_raw_response(self) -> ProfilesWithRawResponse:
        return ProfilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesWithStreamingResponse:
        return ProfilesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProfileListResponse]:
        """
        Lists all DLP profiles in an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/dlp/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProfileListResponse]], ResultWrapper[ProfileListResponse]),
        )

    def get(
        self,
        profile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileGetResponse:
        """Fetches a DLP profile by ID.

        Supports both predefined and custom profiles

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return cast(
            ProfileGetResponse,
            self._get(
                f"/accounts/{account_id}/dlp/profiles/{profile_id}",
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


class AsyncProfiles(AsyncAPIResource):
    @cached_property
    def custom(self) -> AsyncCustom:
        return AsyncCustom(self._client)

    @cached_property
    def predefined(self) -> AsyncPredefined:
        return AsyncPredefined(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfilesWithRawResponse:
        return AsyncProfilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesWithStreamingResponse:
        return AsyncProfilesWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProfileListResponse]:
        """
        Lists all DLP profiles in an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dlp/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ProfileListResponse]], ResultWrapper[ProfileListResponse]),
        )

    async def get(
        self,
        profile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileGetResponse:
        """Fetches a DLP profile by ID.

        Supports both predefined and custom profiles

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return cast(
            ProfileGetResponse,
            await self._get(
                f"/accounts/{account_id}/dlp/profiles/{profile_id}",
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


class ProfilesWithRawResponse:
    def __init__(self, profiles: Profiles) -> None:
        self._profiles = profiles

        self.list = to_raw_response_wrapper(
            profiles.list,
        )
        self.get = to_raw_response_wrapper(
            profiles.get,
        )

    @cached_property
    def custom(self) -> CustomWithRawResponse:
        return CustomWithRawResponse(self._profiles.custom)

    @cached_property
    def predefined(self) -> PredefinedWithRawResponse:
        return PredefinedWithRawResponse(self._profiles.predefined)


class AsyncProfilesWithRawResponse:
    def __init__(self, profiles: AsyncProfiles) -> None:
        self._profiles = profiles

        self.list = async_to_raw_response_wrapper(
            profiles.list,
        )
        self.get = async_to_raw_response_wrapper(
            profiles.get,
        )

    @cached_property
    def custom(self) -> AsyncCustomWithRawResponse:
        return AsyncCustomWithRawResponse(self._profiles.custom)

    @cached_property
    def predefined(self) -> AsyncPredefinedWithRawResponse:
        return AsyncPredefinedWithRawResponse(self._profiles.predefined)


class ProfilesWithStreamingResponse:
    def __init__(self, profiles: Profiles) -> None:
        self._profiles = profiles

        self.list = to_streamed_response_wrapper(
            profiles.list,
        )
        self.get = to_streamed_response_wrapper(
            profiles.get,
        )

    @cached_property
    def custom(self) -> CustomWithStreamingResponse:
        return CustomWithStreamingResponse(self._profiles.custom)

    @cached_property
    def predefined(self) -> PredefinedWithStreamingResponse:
        return PredefinedWithStreamingResponse(self._profiles.predefined)


class AsyncProfilesWithStreamingResponse:
    def __init__(self, profiles: AsyncProfiles) -> None:
        self._profiles = profiles

        self.list = async_to_streamed_response_wrapper(
            profiles.list,
        )
        self.get = async_to_streamed_response_wrapper(
            profiles.get,
        )

    @cached_property
    def custom(self) -> AsyncCustomWithStreamingResponse:
        return AsyncCustomWithStreamingResponse(self._profiles.custom)

    @cached_property
    def predefined(self) -> AsyncPredefinedWithStreamingResponse:
        return AsyncPredefinedWithStreamingResponse(self._profiles.predefined)
