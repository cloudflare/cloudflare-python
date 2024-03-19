# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.zones import ActivationCheckTriggerResponse
from ..._base_client import (
    make_request_options,
)

__all__ = ["ActivationCheck", "AsyncActivationCheck"]


class ActivationCheck(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivationCheckWithRawResponse:
        return ActivationCheckWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivationCheckWithStreamingResponse:
        return ActivationCheckWithStreamingResponse(self)

    def trigger(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationCheckTriggerResponse:
        """Triggeres a new activation check for a PENDING Zone.

        This can be triggered every
        5 min for paygo/ent customers, every hour for FREE Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/activation_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ActivationCheckTriggerResponse], ResultWrapper[ActivationCheckTriggerResponse]),
        )


class AsyncActivationCheck(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivationCheckWithRawResponse:
        return AsyncActivationCheckWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivationCheckWithStreamingResponse:
        return AsyncActivationCheckWithStreamingResponse(self)

    async def trigger(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationCheckTriggerResponse:
        """Triggeres a new activation check for a PENDING Zone.

        This can be triggered every
        5 min for paygo/ent customers, every hour for FREE Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/activation_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ActivationCheckTriggerResponse], ResultWrapper[ActivationCheckTriggerResponse]),
        )


class ActivationCheckWithRawResponse:
    def __init__(self, activation_check: ActivationCheck) -> None:
        self._activation_check = activation_check

        self.trigger = to_raw_response_wrapper(
            activation_check.trigger,
        )


class AsyncActivationCheckWithRawResponse:
    def __init__(self, activation_check: AsyncActivationCheck) -> None:
        self._activation_check = activation_check

        self.trigger = async_to_raw_response_wrapper(
            activation_check.trigger,
        )


class ActivationCheckWithStreamingResponse:
    def __init__(self, activation_check: ActivationCheck) -> None:
        self._activation_check = activation_check

        self.trigger = to_streamed_response_wrapper(
            activation_check.trigger,
        )


class AsyncActivationCheckWithStreamingResponse:
    def __init__(self, activation_check: AsyncActivationCheck) -> None:
        self._activation_check = activation_check

        self.trigger = async_to_streamed_response_wrapper(
            activation_check.trigger,
        )
