# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..types.fraud import fraud_update_params
from .._base_client import make_request_options
from ..types.fraud.fraud_settings import FraudSettings

__all__ = ["FraudResource", "AsyncFraudResource"]


class FraudResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FraudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FraudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FraudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FraudResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        user_profiles: Literal["enabled", "disabled"] | Omit = omit,
        username_expressions: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FraudSettings]:
        """
        Update Fraud Detection settings for a zone.

        Notes on `username_expressions` behavior:

        - If omitted or set to null, expressions are not modified.
        - If provided as an empty array `[]`, all expressions will be cleared.

        Args:
          zone_id: Identifier.

          user_profiles: Whether Fraud User Profiles is enabled for the zone.

          username_expressions: List of expressions to detect usernames in write HTTP requests.

              - Maximum of 10 expressions.
              - Omit or set to null to leave unchanged on update.
              - Provide an empty array `[]` to clear all expressions on update.
              - Invalid expressions will result in a 10400 Bad Request with details in the
                `messages` array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/fraud_detection/settings",
            body=maybe_transform(
                {
                    "user_profiles": user_profiles,
                    "username_expressions": username_expressions,
                },
                fraud_update_params.FraudUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FraudSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FraudSettings]], ResultWrapper[FraudSettings]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FraudSettings]:
        """
        Retrieve Fraud Detection settings for a zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/fraud_detection/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FraudSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FraudSettings]], ResultWrapper[FraudSettings]),
        )


class AsyncFraudResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFraudResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFraudResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFraudResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFraudResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        user_profiles: Literal["enabled", "disabled"] | Omit = omit,
        username_expressions: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FraudSettings]:
        """
        Update Fraud Detection settings for a zone.

        Notes on `username_expressions` behavior:

        - If omitted or set to null, expressions are not modified.
        - If provided as an empty array `[]`, all expressions will be cleared.

        Args:
          zone_id: Identifier.

          user_profiles: Whether Fraud User Profiles is enabled for the zone.

          username_expressions: List of expressions to detect usernames in write HTTP requests.

              - Maximum of 10 expressions.
              - Omit or set to null to leave unchanged on update.
              - Provide an empty array `[]` to clear all expressions on update.
              - Invalid expressions will result in a 10400 Bad Request with details in the
                `messages` array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/fraud_detection/settings",
            body=await async_maybe_transform(
                {
                    "user_profiles": user_profiles,
                    "username_expressions": username_expressions,
                },
                fraud_update_params.FraudUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FraudSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FraudSettings]], ResultWrapper[FraudSettings]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[FraudSettings]:
        """
        Retrieve Fraud Detection settings for a zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/fraud_detection/settings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FraudSettings]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FraudSettings]], ResultWrapper[FraudSettings]),
        )


class FraudResourceWithRawResponse:
    def __init__(self, fraud: FraudResource) -> None:
        self._fraud = fraud

        self.update = to_raw_response_wrapper(
            fraud.update,
        )
        self.get = to_raw_response_wrapper(
            fraud.get,
        )


class AsyncFraudResourceWithRawResponse:
    def __init__(self, fraud: AsyncFraudResource) -> None:
        self._fraud = fraud

        self.update = async_to_raw_response_wrapper(
            fraud.update,
        )
        self.get = async_to_raw_response_wrapper(
            fraud.get,
        )


class FraudResourceWithStreamingResponse:
    def __init__(self, fraud: FraudResource) -> None:
        self._fraud = fraud

        self.update = to_streamed_response_wrapper(
            fraud.update,
        )
        self.get = to_streamed_response_wrapper(
            fraud.get,
        )


class AsyncFraudResourceWithStreamingResponse:
    def __init__(self, fraud: AsyncFraudResource) -> None:
        self._fraud = fraud

        self.update = async_to_streamed_response_wrapper(
            fraud.update,
        )
        self.get = async_to_streamed_response_wrapper(
            fraud.get,
        )
