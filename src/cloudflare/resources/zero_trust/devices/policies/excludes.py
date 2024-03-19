# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
    ExcludeGetResponse,
    ExcludeListResponse,
    ExcludeUpdateResponse,
    TeamsDevicesSplitTunnelParam,
    exclude_update_params,
)

__all__ = ["Excludes", "AsyncExcludes"]


class Excludes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExcludesWithRawResponse:
        return ExcludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExcludesWithStreamingResponse:
        return ExcludesWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: object,
        body: Iterable[TeamsDevicesSplitTunnelParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeUpdateResponse]:
        """
        Sets the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/devices/policy/exclude",
            body=maybe_transform(body, exclude_update_params.ExcludeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeUpdateResponse]], ResultWrapper[ExcludeUpdateResponse]),
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
    ) -> Optional[ExcludeListResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/devices/policy/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeListResponse]], ResultWrapper[ExcludeListResponse]),
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
    ) -> Optional[ExcludeGetResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel for a specific
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
            f"/accounts/{account_id}/devices/policy/{policy_id}/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeGetResponse]], ResultWrapper[ExcludeGetResponse]),
        )


class AsyncExcludes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExcludesWithRawResponse:
        return AsyncExcludesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExcludesWithStreamingResponse:
        return AsyncExcludesWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: object,
        body: Iterable[TeamsDevicesSplitTunnelParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ExcludeUpdateResponse]:
        """
        Sets the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/devices/policy/exclude",
            body=await async_maybe_transform(body, exclude_update_params.ExcludeUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeUpdateResponse]], ResultWrapper[ExcludeUpdateResponse]),
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
    ) -> Optional[ExcludeListResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/devices/policy/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeListResponse]], ResultWrapper[ExcludeListResponse]),
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
    ) -> Optional[ExcludeGetResponse]:
        """
        Fetches the list of routes excluded from the WARP client's tunnel for a specific
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
            f"/accounts/{account_id}/devices/policy/{policy_id}/exclude",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ExcludeGetResponse]], ResultWrapper[ExcludeGetResponse]),
        )


class ExcludesWithRawResponse:
    def __init__(self, excludes: Excludes) -> None:
        self._excludes = excludes

        self.update = to_raw_response_wrapper(
            excludes.update,
        )
        self.list = to_raw_response_wrapper(
            excludes.list,
        )
        self.get = to_raw_response_wrapper(
            excludes.get,
        )


class AsyncExcludesWithRawResponse:
    def __init__(self, excludes: AsyncExcludes) -> None:
        self._excludes = excludes

        self.update = async_to_raw_response_wrapper(
            excludes.update,
        )
        self.list = async_to_raw_response_wrapper(
            excludes.list,
        )
        self.get = async_to_raw_response_wrapper(
            excludes.get,
        )


class ExcludesWithStreamingResponse:
    def __init__(self, excludes: Excludes) -> None:
        self._excludes = excludes

        self.update = to_streamed_response_wrapper(
            excludes.update,
        )
        self.list = to_streamed_response_wrapper(
            excludes.list,
        )
        self.get = to_streamed_response_wrapper(
            excludes.get,
        )


class AsyncExcludesWithStreamingResponse:
    def __init__(self, excludes: AsyncExcludes) -> None:
        self._excludes = excludes

        self.update = async_to_streamed_response_wrapper(
            excludes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            excludes.list,
        )
        self.get = async_to_streamed_response_wrapper(
            excludes.get,
        )
