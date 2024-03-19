# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import ZonesOpportunisticOnion, opportunistic_onion_edit_params

__all__ = ["OpportunisticOnion", "AsyncOpportunisticOnion"]


class OpportunisticOnion(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpportunisticOnionWithRawResponse:
        return OpportunisticOnionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpportunisticOnionWithStreamingResponse:
        return OpportunisticOnionWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesOpportunisticOnion]:
        """
        Add an Alt-Svc header to all legitimate requests from Tor, allowing the
        connection to use our onion services instead of exit nodes.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/opportunistic_onion",
            body=maybe_transform({"value": value}, opportunistic_onion_edit_params.OpportunisticOnionEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOpportunisticOnion]], ResultWrapper[ZonesOpportunisticOnion]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesOpportunisticOnion]:
        """
        Add an Alt-Svc header to all legitimate requests from Tor, allowing the
        connection to use our onion services instead of exit nodes.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/opportunistic_onion",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOpportunisticOnion]], ResultWrapper[ZonesOpportunisticOnion]),
        )


class AsyncOpportunisticOnion(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpportunisticOnionWithRawResponse:
        return AsyncOpportunisticOnionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpportunisticOnionWithStreamingResponse:
        return AsyncOpportunisticOnionWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesOpportunisticOnion]:
        """
        Add an Alt-Svc header to all legitimate requests from Tor, allowing the
        connection to use our onion services instead of exit nodes.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/opportunistic_onion",
            body=await async_maybe_transform(
                {"value": value}, opportunistic_onion_edit_params.OpportunisticOnionEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOpportunisticOnion]], ResultWrapper[ZonesOpportunisticOnion]),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesOpportunisticOnion]:
        """
        Add an Alt-Svc header to all legitimate requests from Tor, allowing the
        connection to use our onion services instead of exit nodes.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/opportunistic_onion",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOpportunisticOnion]], ResultWrapper[ZonesOpportunisticOnion]),
        )


class OpportunisticOnionWithRawResponse:
    def __init__(self, opportunistic_onion: OpportunisticOnion) -> None:
        self._opportunistic_onion = opportunistic_onion

        self.edit = to_raw_response_wrapper(
            opportunistic_onion.edit,
        )
        self.get = to_raw_response_wrapper(
            opportunistic_onion.get,
        )


class AsyncOpportunisticOnionWithRawResponse:
    def __init__(self, opportunistic_onion: AsyncOpportunisticOnion) -> None:
        self._opportunistic_onion = opportunistic_onion

        self.edit = async_to_raw_response_wrapper(
            opportunistic_onion.edit,
        )
        self.get = async_to_raw_response_wrapper(
            opportunistic_onion.get,
        )


class OpportunisticOnionWithStreamingResponse:
    def __init__(self, opportunistic_onion: OpportunisticOnion) -> None:
        self._opportunistic_onion = opportunistic_onion

        self.edit = to_streamed_response_wrapper(
            opportunistic_onion.edit,
        )
        self.get = to_streamed_response_wrapper(
            opportunistic_onion.get,
        )


class AsyncOpportunisticOnionWithStreamingResponse:
    def __init__(self, opportunistic_onion: AsyncOpportunisticOnion) -> None:
        self._opportunistic_onion = opportunistic_onion

        self.edit = async_to_streamed_response_wrapper(
            opportunistic_onion.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            opportunistic_onion.get,
        )
