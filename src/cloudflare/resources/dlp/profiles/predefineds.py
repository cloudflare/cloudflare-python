# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
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
from ....types.dlp.profiles import PredefinedGetResponse, PredefinedUpdateResponse, predefined_update_params

__all__ = ["Predefineds", "AsyncPredefineds"]


class Predefineds(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PredefinedsWithRawResponse:
        return PredefinedsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PredefinedsWithStreamingResponse:
        return PredefinedsWithStreamingResponse(self)

    def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        allowed_match_count: float | NotGiven = NOT_GIVEN,
        entries: Iterable[predefined_update_params.Entry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredefinedUpdateResponse:
        """Updates a DLP predefined profile.

        Only supports enabling/disabling entries.

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.

          entries: The entries for this profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._put(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
            body=maybe_transform(
                {
                    "allowed_match_count": allowed_match_count,
                    "entries": entries,
                },
                predefined_update_params.PredefinedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PredefinedUpdateResponse,
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
    ) -> PredefinedGetResponse:
        """
        Fetches a predefined DLP profile.

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
        return self._get(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PredefinedGetResponse], ResultWrapper[PredefinedGetResponse]),
        )


class AsyncPredefineds(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPredefinedsWithRawResponse:
        return AsyncPredefinedsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPredefinedsWithStreamingResponse:
        return AsyncPredefinedsWithStreamingResponse(self)

    async def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        allowed_match_count: float | NotGiven = NOT_GIVEN,
        entries: Iterable[predefined_update_params.Entry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PredefinedUpdateResponse:
        """Updates a DLP predefined profile.

        Only supports enabling/disabling entries.

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.

          entries: The entries for this profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._put(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
            body=maybe_transform(
                {
                    "allowed_match_count": allowed_match_count,
                    "entries": entries,
                },
                predefined_update_params.PredefinedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PredefinedUpdateResponse,
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
    ) -> PredefinedGetResponse:
        """
        Fetches a predefined DLP profile.

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
        return await self._get(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PredefinedGetResponse], ResultWrapper[PredefinedGetResponse]),
        )


class PredefinedsWithRawResponse:
    def __init__(self, predefineds: Predefineds) -> None:
        self._predefineds = predefineds

        self.update = to_raw_response_wrapper(
            predefineds.update,
        )
        self.get = to_raw_response_wrapper(
            predefineds.get,
        )


class AsyncPredefinedsWithRawResponse:
    def __init__(self, predefineds: AsyncPredefineds) -> None:
        self._predefineds = predefineds

        self.update = async_to_raw_response_wrapper(
            predefineds.update,
        )
        self.get = async_to_raw_response_wrapper(
            predefineds.get,
        )


class PredefinedsWithStreamingResponse:
    def __init__(self, predefineds: Predefineds) -> None:
        self._predefineds = predefineds

        self.update = to_streamed_response_wrapper(
            predefineds.update,
        )
        self.get = to_streamed_response_wrapper(
            predefineds.get,
        )


class AsyncPredefinedsWithStreamingResponse:
    def __init__(self, predefineds: AsyncPredefineds) -> None:
        self._predefineds = predefineds

        self.update = async_to_streamed_response_wrapper(
            predefineds.update,
        )
        self.get = async_to_streamed_response_wrapper(
            predefineds.get,
        )
