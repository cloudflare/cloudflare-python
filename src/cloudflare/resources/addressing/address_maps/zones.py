# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.addressing.address_maps import ZoneDeleteResponse, ZoneUpdateResponse

__all__ = ["Zones", "AsyncZones"]


class Zones(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZonesWithRawResponse:
        return ZonesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZonesWithStreamingResponse:
        return ZonesWithStreamingResponse(self)

    def update(
        self,
        address_map_id: str,
        *,
        zone_id: str,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneUpdateResponse]:
        """
        Add a zone as a member of a particular address map.

        Args:
          zone_id: Identifier

          account_id: Identifier

          address_map_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[ZoneUpdateResponse],
            self._put(
                f"/accounts/{account_or_zone}/addressing/address_maps/{address_map_id}/zones/{account_or_zone_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ZoneUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        address_map_id: str,
        *,
        zone_id: str,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneDeleteResponse]:
        """
        Remove a zone as a member of a particular address map.

        Args:
          zone_id: Identifier

          account_id: Identifier

          address_map_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[ZoneDeleteResponse],
            self._delete(
                f"/accounts/{account_or_zone}/addressing/address_maps/{address_map_id}/zones/{account_or_zone_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ZoneDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncZones(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZonesWithRawResponse:
        return AsyncZonesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZonesWithStreamingResponse:
        return AsyncZonesWithStreamingResponse(self)

    async def update(
        self,
        address_map_id: str,
        *,
        zone_id: str,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneUpdateResponse]:
        """
        Add a zone as a member of a particular address map.

        Args:
          zone_id: Identifier

          account_id: Identifier

          address_map_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[ZoneUpdateResponse],
            await self._put(
                f"/accounts/{account_or_zone}/addressing/address_maps/{address_map_id}/zones/{account_or_zone_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ZoneUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        address_map_id: str,
        *,
        zone_id: str,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneDeleteResponse]:
        """
        Remove a zone as a member of a particular address map.

        Args:
          zone_id: Identifier

          account_id: Identifier

          address_map_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not address_map_id:
            raise ValueError(f"Expected a non-empty value for `address_map_id` but received {address_map_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            Optional[ZoneDeleteResponse],
            await self._delete(
                f"/accounts/{account_or_zone}/addressing/address_maps/{address_map_id}/zones/{account_or_zone_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ZoneDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ZonesWithRawResponse:
    def __init__(self, zones: Zones) -> None:
        self._zones = zones

        self.update = to_raw_response_wrapper(
            zones.update,
        )
        self.delete = to_raw_response_wrapper(
            zones.delete,
        )


class AsyncZonesWithRawResponse:
    def __init__(self, zones: AsyncZones) -> None:
        self._zones = zones

        self.update = async_to_raw_response_wrapper(
            zones.update,
        )
        self.delete = async_to_raw_response_wrapper(
            zones.delete,
        )


class ZonesWithStreamingResponse:
    def __init__(self, zones: Zones) -> None:
        self._zones = zones

        self.update = to_streamed_response_wrapper(
            zones.update,
        )
        self.delete = to_streamed_response_wrapper(
            zones.delete,
        )


class AsyncZonesWithStreamingResponse:
    def __init__(self, zones: AsyncZones) -> None:
        self._zones = zones

        self.update = async_to_streamed_response_wrapper(
            zones.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            zones.delete,
        )
