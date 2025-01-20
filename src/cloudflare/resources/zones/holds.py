# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

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
from ...types.zones import hold_edit_params, hold_create_params, hold_delete_params
from ..._base_client import make_request_options
from ...types.zones.zone_hold import ZoneHold

__all__ = ["HoldsResource", "AsyncHoldsResource"]


class HoldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HoldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HoldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HoldsResourceWithStreamingResponse(self)

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
    ) -> ZoneHold:
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
                post_parser=ResultWrapper[ZoneHold]._unwrapper,
            ),
            cast_to=cast(Type[ZoneHold], ResultWrapper[ZoneHold]),
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
    ) -> ZoneHold:
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
                post_parser=ResultWrapper[ZoneHold]._unwrapper,
            ),
            cast_to=cast(Type[ZoneHold], ResultWrapper[ZoneHold]),
        )

    def edit(
        self,
        *,
        zone_id: str,
        hold_after: str | NotGiven = NOT_GIVEN,
        include_subdomains: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZoneHold:
        """
        Update the `hold_after` and/or `include_subdomains` values on an existing zone
        hold. The hold is enabled if the `hold_after` date-time value is in the past.

        Args:
          zone_id: Identifier

          hold_after: If `hold_after` is provided and future-dated, the hold will be temporarily
              disabled, then automatically re-enabled by the system at the time specified in
              this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
              effect on an existing, enabled hold. Providing an empty string will set its
              value to the current time.

          include_subdomains: If `true`, the zone hold will extend to block any subdomain of the given zone,
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
        return self._patch(
            f"/zones/{zone_id}/hold",
            body=maybe_transform(
                {
                    "hold_after": hold_after,
                    "include_subdomains": include_subdomains,
                },
                hold_edit_params.HoldEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ZoneHold]._unwrapper,
            ),
            cast_to=cast(Type[ZoneHold], ResultWrapper[ZoneHold]),
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
    ) -> ZoneHold:
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
                post_parser=ResultWrapper[ZoneHold]._unwrapper,
            ),
            cast_to=cast(Type[ZoneHold], ResultWrapper[ZoneHold]),
        )


class AsyncHoldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHoldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHoldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHoldsResourceWithStreamingResponse(self)

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
    ) -> ZoneHold:
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
                post_parser=ResultWrapper[ZoneHold]._unwrapper,
            ),
            cast_to=cast(Type[ZoneHold], ResultWrapper[ZoneHold]),
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
    ) -> ZoneHold:
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
                post_parser=ResultWrapper[ZoneHold]._unwrapper,
            ),
            cast_to=cast(Type[ZoneHold], ResultWrapper[ZoneHold]),
        )

    async def edit(
        self,
        *,
        zone_id: str,
        hold_after: str | NotGiven = NOT_GIVEN,
        include_subdomains: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZoneHold:
        """
        Update the `hold_after` and/or `include_subdomains` values on an existing zone
        hold. The hold is enabled if the `hold_after` date-time value is in the past.

        Args:
          zone_id: Identifier

          hold_after: If `hold_after` is provided and future-dated, the hold will be temporarily
              disabled, then automatically re-enabled by the system at the time specified in
              this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
              effect on an existing, enabled hold. Providing an empty string will set its
              value to the current time.

          include_subdomains: If `true`, the zone hold will extend to block any subdomain of the given zone,
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
        return await self._patch(
            f"/zones/{zone_id}/hold",
            body=await async_maybe_transform(
                {
                    "hold_after": hold_after,
                    "include_subdomains": include_subdomains,
                },
                hold_edit_params.HoldEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ZoneHold]._unwrapper,
            ),
            cast_to=cast(Type[ZoneHold], ResultWrapper[ZoneHold]),
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
    ) -> ZoneHold:
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
                post_parser=ResultWrapper[ZoneHold]._unwrapper,
            ),
            cast_to=cast(Type[ZoneHold], ResultWrapper[ZoneHold]),
        )


class HoldsResourceWithRawResponse:
    def __init__(self, holds: HoldsResource) -> None:
        self._holds = holds

        self.create = to_raw_response_wrapper(
            holds.create,
        )
        self.delete = to_raw_response_wrapper(
            holds.delete,
        )
        self.edit = to_raw_response_wrapper(
            holds.edit,
        )
        self.get = to_raw_response_wrapper(
            holds.get,
        )


class AsyncHoldsResourceWithRawResponse:
    def __init__(self, holds: AsyncHoldsResource) -> None:
        self._holds = holds

        self.create = async_to_raw_response_wrapper(
            holds.create,
        )
        self.delete = async_to_raw_response_wrapper(
            holds.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            holds.edit,
        )
        self.get = async_to_raw_response_wrapper(
            holds.get,
        )


class HoldsResourceWithStreamingResponse:
    def __init__(self, holds: HoldsResource) -> None:
        self._holds = holds

        self.create = to_streamed_response_wrapper(
            holds.create,
        )
        self.delete = to_streamed_response_wrapper(
            holds.delete,
        )
        self.edit = to_streamed_response_wrapper(
            holds.edit,
        )
        self.get = to_streamed_response_wrapper(
            holds.get,
        )


class AsyncHoldsResourceWithStreamingResponse:
    def __init__(self, holds: AsyncHoldsResource) -> None:
        self._holds = holds

        self.create = async_to_streamed_response_wrapper(
            holds.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            holds.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            holds.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            holds.get,
        )
