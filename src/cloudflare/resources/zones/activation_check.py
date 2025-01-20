# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._base_client import make_request_options
from ...types.zones.activation_check_trigger_response import ActivationCheckTriggerResponse

__all__ = ["ActivationCheckResource", "AsyncActivationCheckResource"]


class ActivationCheckResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivationCheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ActivationCheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivationCheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ActivationCheckResourceWithStreamingResponse(self)

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
    ) -> Optional[ActivationCheckTriggerResponse]:
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
                post_parser=ResultWrapper[Optional[ActivationCheckTriggerResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ActivationCheckTriggerResponse]], ResultWrapper[ActivationCheckTriggerResponse]),
        )


class AsyncActivationCheckResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivationCheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActivationCheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivationCheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncActivationCheckResourceWithStreamingResponse(self)

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
    ) -> Optional[ActivationCheckTriggerResponse]:
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
                post_parser=ResultWrapper[Optional[ActivationCheckTriggerResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ActivationCheckTriggerResponse]], ResultWrapper[ActivationCheckTriggerResponse]),
        )


class ActivationCheckResourceWithRawResponse:
    def __init__(self, activation_check: ActivationCheckResource) -> None:
        self._activation_check = activation_check

        self.trigger = to_raw_response_wrapper(
            activation_check.trigger,
        )


class AsyncActivationCheckResourceWithRawResponse:
    def __init__(self, activation_check: AsyncActivationCheckResource) -> None:
        self._activation_check = activation_check

        self.trigger = async_to_raw_response_wrapper(
            activation_check.trigger,
        )


class ActivationCheckResourceWithStreamingResponse:
    def __init__(self, activation_check: ActivationCheckResource) -> None:
        self._activation_check = activation_check

        self.trigger = to_streamed_response_wrapper(
            activation_check.trigger,
        )


class AsyncActivationCheckResourceWithStreamingResponse:
    def __init__(self, activation_check: AsyncActivationCheckResource) -> None:
        self._activation_check = activation_check

        self.trigger = async_to_streamed_response_wrapper(
            activation_check.trigger,
        )
