# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.zones import (
    HoldGetResponse,
    HoldCreateResponse,
    HoldDeleteResponse,
    hold_create_params,
    hold_delete_params,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Holds", "AsyncHolds"]


class Holds(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HoldsWithRawResponse:
        return HoldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldsWithStreamingResponse:
        return HoldsWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        include_subdomains: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HoldCreateResponse:
        """
        Enforce a zone hold on the zone, blocking the creation and activation of zones
        with this zone's hostname.

        Args:
          zone_id: Identifier

          include_subdomains: If provided, the zone hold will extend to block any subdomain of the given zone,
              as well as SSL4SaaS Custom Hostnames. For example, a zone hold on a zone with
              the hostname 'example.com' and include_subdomains=true will block 'example.com',
              'staging.example.com', 'api.staging.example.com', etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_subdomains": include_subdomains}, hold_create_params.HoldCreateParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HoldCreateResponse], ResultWrapper[HoldCreateResponse]),
        )

    def delete(
        self,
        *,
        zone_id: str,
        hold_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HoldDeleteResponse]:
        """
        Stop enforcement of a zone hold on the zone, permanently or temporarily,
        allowing the creation and activation of zones with this zone's hostname.

        Args:
          zone_id: Identifier

          hold_after: If `hold_after` is provided, the hold will be temporarily disabled, then
              automatically re-enabled by the system at the time specified in this
              RFC3339-formatted timestamp. Otherwise, the hold will be disabled indefinitely.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            f"/zones/{zone_id}/hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"hold_after": hold_after}, hold_delete_params.HoldDeleteParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HoldDeleteResponse]], ResultWrapper[HoldDeleteResponse]),
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
    ) -> HoldGetResponse:
        """
        Retrieve whether the zone is subject to a zone hold, and metadata about the
        hold.

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
            f"/zones/{zone_id}/hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HoldGetResponse], ResultWrapper[HoldGetResponse]),
        )


class AsyncHolds(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHoldsWithRawResponse:
        return AsyncHoldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldsWithStreamingResponse:
        return AsyncHoldsWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        include_subdomains: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HoldCreateResponse:
        """
        Enforce a zone hold on the zone, blocking the creation and activation of zones
        with this zone's hostname.

        Args:
          zone_id: Identifier

          include_subdomains: If provided, the zone hold will extend to block any subdomain of the given zone,
              as well as SSL4SaaS Custom Hostnames. For example, a zone hold on a zone with
              the hostname 'example.com' and include_subdomains=true will block 'example.com',
              'staging.example.com', 'api.staging.example.com', etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_subdomains": include_subdomains}, hold_create_params.HoldCreateParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HoldCreateResponse], ResultWrapper[HoldCreateResponse]),
        )

    async def delete(
        self,
        *,
        zone_id: str,
        hold_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HoldDeleteResponse]:
        """
        Stop enforcement of a zone hold on the zone, permanently or temporarily,
        allowing the creation and activation of zones with this zone's hostname.

        Args:
          zone_id: Identifier

          hold_after: If `hold_after` is provided, the hold will be temporarily disabled, then
              automatically re-enabled by the system at the time specified in this
              RFC3339-formatted timestamp. Otherwise, the hold will be disabled indefinitely.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"hold_after": hold_after}, hold_delete_params.HoldDeleteParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HoldDeleteResponse]], ResultWrapper[HoldDeleteResponse]),
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
    ) -> HoldGetResponse:
        """
        Retrieve whether the zone is subject to a zone hold, and metadata about the
        hold.

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
            f"/zones/{zone_id}/hold",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HoldGetResponse], ResultWrapper[HoldGetResponse]),
        )


class HoldsWithRawResponse:
    def __init__(self, holds: Holds) -> None:
        self._holds = holds

        self.create = to_raw_response_wrapper(
            holds.create,
        )
        self.delete = to_raw_response_wrapper(
            holds.delete,
        )
        self.get = to_raw_response_wrapper(
            holds.get,
        )


class AsyncHoldsWithRawResponse:
    def __init__(self, holds: AsyncHolds) -> None:
        self._holds = holds

        self.create = async_to_raw_response_wrapper(
            holds.create,
        )
        self.delete = async_to_raw_response_wrapper(
            holds.delete,
        )
        self.get = async_to_raw_response_wrapper(
            holds.get,
        )


class HoldsWithStreamingResponse:
    def __init__(self, holds: Holds) -> None:
        self._holds = holds

        self.create = to_streamed_response_wrapper(
            holds.create,
        )
        self.delete = to_streamed_response_wrapper(
            holds.delete,
        )
        self.get = to_streamed_response_wrapper(
            holds.get,
        )


class AsyncHoldsWithStreamingResponse:
    def __init__(self, holds: AsyncHolds) -> None:
        self._holds = holds

        self.create = async_to_streamed_response_wrapper(
            holds.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            holds.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            holds.get,
        )
