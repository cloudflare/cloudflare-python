# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .....types.zero_trust.devices.policies.default_policy_get_response import DefaultPolicyGetResponse

__all__ = ["DefaultPolicyResource", "AsyncDefaultPolicyResource"]


class DefaultPolicyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefaultPolicyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DefaultPolicyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultPolicyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DefaultPolicyResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DefaultPolicyGetResponse]:
        """
        Fetches the default device settings profile for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/policy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DefaultPolicyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DefaultPolicyGetResponse]], ResultWrapper[DefaultPolicyGetResponse]),
        )


class AsyncDefaultPolicyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefaultPolicyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefaultPolicyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultPolicyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDefaultPolicyResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DefaultPolicyGetResponse]:
        """
        Fetches the default device settings profile for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/policy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DefaultPolicyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DefaultPolicyGetResponse]], ResultWrapper[DefaultPolicyGetResponse]),
        )


class DefaultPolicyResourceWithRawResponse:
    def __init__(self, default_policy: DefaultPolicyResource) -> None:
        self._default_policy = default_policy

        self.get = to_raw_response_wrapper(
            default_policy.get,
        )


class AsyncDefaultPolicyResourceWithRawResponse:
    def __init__(self, default_policy: AsyncDefaultPolicyResource) -> None:
        self._default_policy = default_policy

        self.get = async_to_raw_response_wrapper(
            default_policy.get,
        )


class DefaultPolicyResourceWithStreamingResponse:
    def __init__(self, default_policy: DefaultPolicyResource) -> None:
        self._default_policy = default_policy

        self.get = to_streamed_response_wrapper(
            default_policy.get,
        )


class AsyncDefaultPolicyResourceWithStreamingResponse:
    def __init__(self, default_policy: AsyncDefaultPolicyResource) -> None:
        self._default_policy = default_policy

        self.get = async_to_streamed_response_wrapper(
            default_policy.get,
        )
