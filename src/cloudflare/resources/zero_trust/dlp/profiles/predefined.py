# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
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
from .....types.zero_trust.dlp.profiles import DLPPredefinedProfile, predefined_update_params

__all__ = ["Predefined", "AsyncPredefined"]


class Predefined(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PredefinedWithRawResponse:
        return PredefinedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PredefinedWithStreamingResponse:
        return PredefinedWithStreamingResponse(self)

    def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        allowed_match_count: float | NotGiven = NOT_GIVEN,
        context_awareness: predefined_update_params.ContextAwareness | NotGiven = NOT_GIVEN,
        entries: Iterable[predefined_update_params.Entry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DLPPredefinedProfile:
        """Updates a DLP predefined profile.

        Only supports enabling/disabling entries.

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.

          context_awareness: Scan the context of predefined entries to only return matches surrounded by
              keywords.

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
                    "context_awareness": context_awareness,
                    "entries": entries,
                },
                predefined_update_params.PredefinedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DLPPredefinedProfile,
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
    ) -> DLPPredefinedProfile:
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
            cast_to=cast(Type[DLPPredefinedProfile], ResultWrapper[DLPPredefinedProfile]),
        )


class AsyncPredefined(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPredefinedWithRawResponse:
        return AsyncPredefinedWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPredefinedWithStreamingResponse:
        return AsyncPredefinedWithStreamingResponse(self)

    async def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        allowed_match_count: float | NotGiven = NOT_GIVEN,
        context_awareness: predefined_update_params.ContextAwareness | NotGiven = NOT_GIVEN,
        entries: Iterable[predefined_update_params.Entry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DLPPredefinedProfile:
        """Updates a DLP predefined profile.

        Only supports enabling/disabling entries.

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.

          context_awareness: Scan the context of predefined entries to only return matches surrounded by
              keywords.

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
            body=await async_maybe_transform(
                {
                    "allowed_match_count": allowed_match_count,
                    "context_awareness": context_awareness,
                    "entries": entries,
                },
                predefined_update_params.PredefinedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DLPPredefinedProfile,
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
    ) -> DLPPredefinedProfile:
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
            cast_to=cast(Type[DLPPredefinedProfile], ResultWrapper[DLPPredefinedProfile]),
        )


class PredefinedWithRawResponse:
    def __init__(self, predefined: Predefined) -> None:
        self._predefined = predefined

        self.update = to_raw_response_wrapper(
            predefined.update,
        )
        self.get = to_raw_response_wrapper(
            predefined.get,
        )


class AsyncPredefinedWithRawResponse:
    def __init__(self, predefined: AsyncPredefined) -> None:
        self._predefined = predefined

        self.update = async_to_raw_response_wrapper(
            predefined.update,
        )
        self.get = async_to_raw_response_wrapper(
            predefined.get,
        )


class PredefinedWithStreamingResponse:
    def __init__(self, predefined: Predefined) -> None:
        self._predefined = predefined

        self.update = to_streamed_response_wrapper(
            predefined.update,
        )
        self.get = to_streamed_response_wrapper(
            predefined.get,
        )


class AsyncPredefinedWithStreamingResponse:
    def __init__(self, predefined: AsyncPredefined) -> None:
        self._predefined = predefined

        self.update = async_to_streamed_response_wrapper(
            predefined.update,
        )
        self.get = async_to_streamed_response_wrapper(
            predefined.get,
        )
