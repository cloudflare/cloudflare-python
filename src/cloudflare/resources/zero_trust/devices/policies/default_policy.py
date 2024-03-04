# File generated from our OpenAPI spec by Stainless.

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
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.devices.policies import DefaultPolicyGetResponse

__all__ = ["DefaultPolicy", "AsyncDefaultPolicy"]


class DefaultPolicy(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefaultPolicyWithRawResponse:
        return DefaultPolicyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultPolicyWithStreamingResponse:
        return DefaultPolicyWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: object,
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
        return self._get(
            f"/accounts/{account_id}/devices/policy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DefaultPolicyGetResponse]], ResultWrapper[DefaultPolicyGetResponse]),
        )


class AsyncDefaultPolicy(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefaultPolicyWithRawResponse:
        return AsyncDefaultPolicyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultPolicyWithStreamingResponse:
        return AsyncDefaultPolicyWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: object,
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
        return await self._get(
            f"/accounts/{account_id}/devices/policy",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DefaultPolicyGetResponse]], ResultWrapper[DefaultPolicyGetResponse]),
        )


class DefaultPolicyWithRawResponse:
    def __init__(self, default_policy: DefaultPolicy) -> None:
        self._default_policy = default_policy

        self.get = to_raw_response_wrapper(
            default_policy.get,
        )


class AsyncDefaultPolicyWithRawResponse:
    def __init__(self, default_policy: AsyncDefaultPolicy) -> None:
        self._default_policy = default_policy

        self.get = async_to_raw_response_wrapper(
            default_policy.get,
        )


class DefaultPolicyWithStreamingResponse:
    def __init__(self, default_policy: DefaultPolicy) -> None:
        self._default_policy = default_policy

        self.get = to_streamed_response_wrapper(
            default_policy.get,
        )


class AsyncDefaultPolicyWithStreamingResponse:
    def __init__(self, default_policy: AsyncDefaultPolicy) -> None:
        self._default_policy = default_policy

        self.get = async_to_streamed_response_wrapper(
            default_policy.get,
        )
