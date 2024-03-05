# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

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
from .....types.zero_trust.devices.policies import (
    IncludeGetResponse,
    IncludeListResponse,
    IncludeUpdateResponse,
    TeamsDevicesSplitTunnelIncludeParam,
    include_update_params,
)

__all__ = ["Includes", "AsyncIncludes"]


class Includes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IncludesWithRawResponse:
        return IncludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IncludesWithStreamingResponse:
        return IncludesWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: object,
        body: Iterable[TeamsDevicesSplitTunnelIncludeParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeUpdateResponse]:
        """
        Sets the list of routes included in the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/devices/policy/include",
            body=maybe_transform(body, include_update_params.IncludeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncludeUpdateResponse]], ResultWrapper[IncludeUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeListResponse]:
        """
        Fetches the list of routes included in the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/devices/policy/include",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncludeListResponse]], ResultWrapper[IncludeListResponse]),
        )

    def get(
        self,
        policy_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeGetResponse]:
        """
        Fetches the list of routes included in the WARP client's tunnel for a specific
        device settings profile.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/policy/{policy_id}/include",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncludeGetResponse]], ResultWrapper[IncludeGetResponse]),
        )


class AsyncIncludes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIncludesWithRawResponse:
        return AsyncIncludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIncludesWithStreamingResponse:
        return AsyncIncludesWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: object,
        body: Iterable[TeamsDevicesSplitTunnelIncludeParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeUpdateResponse]:
        """
        Sets the list of routes included in the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/devices/policy/include",
            body=await async_maybe_transform(body, include_update_params.IncludeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncludeUpdateResponse]], ResultWrapper[IncludeUpdateResponse]),
        )

    async def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeListResponse]:
        """
        Fetches the list of routes included in the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/devices/policy/include",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncludeListResponse]], ResultWrapper[IncludeListResponse]),
        )

    async def get(
        self,
        policy_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IncludeGetResponse]:
        """
        Fetches the list of routes included in the WARP client's tunnel for a specific
        device settings profile.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/policy/{policy_id}/include",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IncludeGetResponse]], ResultWrapper[IncludeGetResponse]),
        )


class IncludesWithRawResponse:
    def __init__(self, includes: Includes) -> None:
        self._includes = includes

        self.update = to_raw_response_wrapper(
            includes.update,
        )
        self.list = to_raw_response_wrapper(
            includes.list,
        )
        self.get = to_raw_response_wrapper(
            includes.get,
        )


class AsyncIncludesWithRawResponse:
    def __init__(self, includes: AsyncIncludes) -> None:
        self._includes = includes

        self.update = async_to_raw_response_wrapper(
            includes.update,
        )
        self.list = async_to_raw_response_wrapper(
            includes.list,
        )
        self.get = async_to_raw_response_wrapper(
            includes.get,
        )


class IncludesWithStreamingResponse:
    def __init__(self, includes: Includes) -> None:
        self._includes = includes

        self.update = to_streamed_response_wrapper(
            includes.update,
        )
        self.list = to_streamed_response_wrapper(
            includes.list,
        )
        self.get = to_streamed_response_wrapper(
            includes.get,
        )


class AsyncIncludesWithStreamingResponse:
    def __init__(self, includes: AsyncIncludes) -> None:
        self._includes = includes

        self.update = async_to_streamed_response_wrapper(
            includes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            includes.list,
        )
        self.get = async_to_streamed_response_wrapper(
            includes.get,
        )
