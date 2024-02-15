# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.devices import UnrevokeDevicesUnrevokeDevicesResponse, unrevoke_devices_unrevoke_devices_params

__all__ = ["Unrevokes", "AsyncUnrevokes"]


class Unrevokes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnrevokesWithRawResponse:
        return UnrevokesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnrevokesWithStreamingResponse:
        return UnrevokesWithStreamingResponse(self)

    def devices_unrevoke_devices(
        self,
        identifier: object,
        *,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnrevokeDevicesUnrevokeDevicesResponse]:
        """
        Unrevokes a list of devices.

        Args:
          body: A list of device ids to unrevoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[UnrevokeDevicesUnrevokeDevicesResponse],
            self._post(
                f"/accounts/{identifier}/devices/unrevoke",
                body=maybe_transform(
                    body, unrevoke_devices_unrevoke_devices_params.UnrevokeDevicesUnrevokeDevicesParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnrevokeDevicesUnrevokeDevicesResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUnrevokes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnrevokesWithRawResponse:
        return AsyncUnrevokesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnrevokesWithStreamingResponse:
        return AsyncUnrevokesWithStreamingResponse(self)

    async def devices_unrevoke_devices(
        self,
        identifier: object,
        *,
        body: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnrevokeDevicesUnrevokeDevicesResponse]:
        """
        Unrevokes a list of devices.

        Args:
          body: A list of device ids to unrevoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Optional[UnrevokeDevicesUnrevokeDevicesResponse],
            await self._post(
                f"/accounts/{identifier}/devices/unrevoke",
                body=maybe_transform(
                    body, unrevoke_devices_unrevoke_devices_params.UnrevokeDevicesUnrevokeDevicesParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UnrevokeDevicesUnrevokeDevicesResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class UnrevokesWithRawResponse:
    def __init__(self, unrevokes: Unrevokes) -> None:
        self._unrevokes = unrevokes

        self.devices_unrevoke_devices = to_raw_response_wrapper(
            unrevokes.devices_unrevoke_devices,
        )


class AsyncUnrevokesWithRawResponse:
    def __init__(self, unrevokes: AsyncUnrevokes) -> None:
        self._unrevokes = unrevokes

        self.devices_unrevoke_devices = async_to_raw_response_wrapper(
            unrevokes.devices_unrevoke_devices,
        )


class UnrevokesWithStreamingResponse:
    def __init__(self, unrevokes: Unrevokes) -> None:
        self._unrevokes = unrevokes

        self.devices_unrevoke_devices = to_streamed_response_wrapper(
            unrevokes.devices_unrevoke_devices,
        )


class AsyncUnrevokesWithStreamingResponse:
    def __init__(self, unrevokes: AsyncUnrevokes) -> None:
        self._unrevokes = unrevokes

        self.devices_unrevoke_devices = async_to_streamed_response_wrapper(
            unrevokes.devices_unrevoke_devices,
        )
