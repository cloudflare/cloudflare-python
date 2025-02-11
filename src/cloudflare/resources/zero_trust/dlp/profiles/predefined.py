# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, Optional, cast

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
from ....._base_client import make_request_options
from .....types.zero_trust.dlp.profile import Profile
from .....types.zero_trust.dlp.profiles import predefined_update_params
from .....types.zero_trust.dlp.context_awareness_param import ContextAwarenessParam

__all__ = ["PredefinedResource", "AsyncPredefinedResource"]


class PredefinedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PredefinedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PredefinedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PredefinedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PredefinedResourceWithStreamingResponse(self)

    def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        entries: Iterable[predefined_update_params.Entry],
        ai_context_enabled: bool | NotGiven = NOT_GIVEN,
        allowed_match_count: Optional[int] | NotGiven = NOT_GIVEN,
        confidence_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        context_awareness: ContextAwarenessParam | NotGiven = NOT_GIVEN,
        ocr_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Profile]:
        """Updates a DLP predefined profile.

        Only supports enabling/disabling entries.

        Args:
          context_awareness: Scan the context of predefined entries to only return matches surrounded by
              keywords.

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
            Optional[Profile],
            self._put(
                f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
                body=maybe_transform(
                    {
                        "entries": entries,
                        "ai_context_enabled": ai_context_enabled,
                        "allowed_match_count": allowed_match_count,
                        "confidence_threshold": confidence_threshold,
                        "context_awareness": context_awareness,
                        "ocr_enabled": ocr_enabled,
                    },
                    predefined_update_params.PredefinedUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Profile]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Profile]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> Optional[Profile]:
        """
        Fetches a predefined DLP profile by id.

        Args:
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
            Optional[Profile],
            self._get(
                f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Profile]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Profile]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncPredefinedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPredefinedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPredefinedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPredefinedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPredefinedResourceWithStreamingResponse(self)

    async def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        entries: Iterable[predefined_update_params.Entry],
        ai_context_enabled: bool | NotGiven = NOT_GIVEN,
        allowed_match_count: Optional[int] | NotGiven = NOT_GIVEN,
        confidence_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        context_awareness: ContextAwarenessParam | NotGiven = NOT_GIVEN,
        ocr_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Profile]:
        """Updates a DLP predefined profile.

        Only supports enabling/disabling entries.

        Args:
          context_awareness: Scan the context of predefined entries to only return matches surrounded by
              keywords.

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
            Optional[Profile],
            await self._put(
                f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
                body=await async_maybe_transform(
                    {
                        "entries": entries,
                        "ai_context_enabled": ai_context_enabled,
                        "allowed_match_count": allowed_match_count,
                        "confidence_threshold": confidence_threshold,
                        "context_awareness": context_awareness,
                        "ocr_enabled": ocr_enabled,
                    },
                    predefined_update_params.PredefinedUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Profile]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Profile]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> Optional[Profile]:
        """
        Fetches a predefined DLP profile by id.

        Args:
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
            Optional[Profile],
            await self._get(
                f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Profile]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Profile]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class PredefinedResourceWithRawResponse:
    def __init__(self, predefined: PredefinedResource) -> None:
        self._predefined = predefined

        self.update = to_raw_response_wrapper(
            predefined.update,
        )
        self.get = to_raw_response_wrapper(
            predefined.get,
        )


class AsyncPredefinedResourceWithRawResponse:
    def __init__(self, predefined: AsyncPredefinedResource) -> None:
        self._predefined = predefined

        self.update = async_to_raw_response_wrapper(
            predefined.update,
        )
        self.get = async_to_raw_response_wrapper(
            predefined.get,
        )


class PredefinedResourceWithStreamingResponse:
    def __init__(self, predefined: PredefinedResource) -> None:
        self._predefined = predefined

        self.update = to_streamed_response_wrapper(
            predefined.update,
        )
        self.get = to_streamed_response_wrapper(
            predefined.get,
        )


class AsyncPredefinedResourceWithStreamingResponse:
    def __init__(self, predefined: AsyncPredefinedResource) -> None:
        self._predefined = predefined

        self.update = async_to_streamed_response_wrapper(
            predefined.update,
        )
        self.get = async_to_streamed_response_wrapper(
            predefined.get,
        )
