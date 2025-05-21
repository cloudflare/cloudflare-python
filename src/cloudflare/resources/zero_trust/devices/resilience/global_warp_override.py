# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
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
from .....types.zero_trust.devices.resilience import global_warp_override_create_params
from .....types.zero_trust.devices.resilience.global_warp_override_get_response import GlobalWARPOverrideGetResponse
from .....types.zero_trust.devices.resilience.global_warp_override_create_response import (
    GlobalWARPOverrideCreateResponse,
)

__all__ = ["GlobalWARPOverrideResource", "AsyncGlobalWARPOverrideResource"]


class GlobalWARPOverrideResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalWARPOverrideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return GlobalWARPOverrideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalWARPOverrideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return GlobalWARPOverrideResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        disconnect: bool,
        justification: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GlobalWARPOverrideCreateResponse]:
        """
        Sets the Global WARP override state.

        Args:
          disconnect: Disconnects all devices on the account using Global WARP override.

          justification: Reasoning for setting the Global WARP override state. This will be surfaced in
              the audit log.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/resilience/disconnect",
            body=maybe_transform(
                {
                    "disconnect": disconnect,
                    "justification": justification,
                },
                global_warp_override_create_params.GlobalWARPOverrideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GlobalWARPOverrideCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[GlobalWARPOverrideCreateResponse]], ResultWrapper[GlobalWARPOverrideCreateResponse]
            ),
        )

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
    ) -> Optional[GlobalWARPOverrideGetResponse]:
        """
        Fetch the Global WARP override state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/resilience/disconnect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GlobalWARPOverrideGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GlobalWARPOverrideGetResponse]], ResultWrapper[GlobalWARPOverrideGetResponse]),
        )


class AsyncGlobalWARPOverrideResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalWARPOverrideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalWARPOverrideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalWARPOverrideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncGlobalWARPOverrideResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        disconnect: bool,
        justification: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GlobalWARPOverrideCreateResponse]:
        """
        Sets the Global WARP override state.

        Args:
          disconnect: Disconnects all devices on the account using Global WARP override.

          justification: Reasoning for setting the Global WARP override state. This will be surfaced in
              the audit log.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/resilience/disconnect",
            body=await async_maybe_transform(
                {
                    "disconnect": disconnect,
                    "justification": justification,
                },
                global_warp_override_create_params.GlobalWARPOverrideCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GlobalWARPOverrideCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[GlobalWARPOverrideCreateResponse]], ResultWrapper[GlobalWARPOverrideCreateResponse]
            ),
        )

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
    ) -> Optional[GlobalWARPOverrideGetResponse]:
        """
        Fetch the Global WARP override state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/resilience/disconnect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GlobalWARPOverrideGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GlobalWARPOverrideGetResponse]], ResultWrapper[GlobalWARPOverrideGetResponse]),
        )


class GlobalWARPOverrideResourceWithRawResponse:
    def __init__(self, global_warp_override: GlobalWARPOverrideResource) -> None:
        self._global_warp_override = global_warp_override

        self.create = to_raw_response_wrapper(
            global_warp_override.create,
        )
        self.get = to_raw_response_wrapper(
            global_warp_override.get,
        )


class AsyncGlobalWARPOverrideResourceWithRawResponse:
    def __init__(self, global_warp_override: AsyncGlobalWARPOverrideResource) -> None:
        self._global_warp_override = global_warp_override

        self.create = async_to_raw_response_wrapper(
            global_warp_override.create,
        )
        self.get = async_to_raw_response_wrapper(
            global_warp_override.get,
        )


class GlobalWARPOverrideResourceWithStreamingResponse:
    def __init__(self, global_warp_override: GlobalWARPOverrideResource) -> None:
        self._global_warp_override = global_warp_override

        self.create = to_streamed_response_wrapper(
            global_warp_override.create,
        )
        self.get = to_streamed_response_wrapper(
            global_warp_override.get,
        )


class AsyncGlobalWARPOverrideResourceWithStreamingResponse:
    def __init__(self, global_warp_override: AsyncGlobalWARPOverrideResource) -> None:
        self._global_warp_override = global_warp_override

        self.create = async_to_streamed_response_wrapper(
            global_warp_override.create,
        )
        self.get = async_to_streamed_response_wrapper(
            global_warp_override.get,
        )
