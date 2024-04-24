# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ....types.addressing.address_maps import zone_update_params
from ....types.addressing.address_maps.zone_delete_response import ZoneDeleteResponse
from ....types.addressing.address_maps.zone_update_response import ZoneUpdateResponse

__all__ = ["ZonesResource", "AsyncZonesResource"]


class ZonesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZonesResourceWithRawResponse:
        return ZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZonesResourceWithStreamingResponse:
        return ZonesResourceWithStreamingResponse(self)

    def update(
        self,
        address_map_id: str,
        *,
        zone_id: str,
        account_id: str,
        body: object,
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
        return self._put(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}",
            body=maybe_transform(body, zone_update_params.ZoneUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneUpdateResponse]], ResultWrapper[ZoneUpdateResponse]),
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
        return self._delete(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneDeleteResponse]], ResultWrapper[ZoneDeleteResponse]),
        )


class AsyncZonesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZonesResourceWithRawResponse:
        return AsyncZonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZonesResourceWithStreamingResponse:
        return AsyncZonesResourceWithStreamingResponse(self)

    async def update(
        self,
        address_map_id: str,
        *,
        zone_id: str,
        account_id: str,
        body: object,
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
        return await self._put(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}",
            body=await async_maybe_transform(body, zone_update_params.ZoneUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneUpdateResponse]], ResultWrapper[ZoneUpdateResponse]),
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
        return await self._delete(
            f"/accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneDeleteResponse]], ResultWrapper[ZoneDeleteResponse]),
        )


class ZonesResourceWithRawResponse:
    def __init__(self, zones: ZonesResource) -> None:
        self._zones = zones

        self.update = to_raw_response_wrapper(
            zones.update,
        )
        self.delete = to_raw_response_wrapper(
            zones.delete,
        )


class AsyncZonesResourceWithRawResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
        self._zones = zones

        self.update = async_to_raw_response_wrapper(
            zones.update,
        )
        self.delete = async_to_raw_response_wrapper(
            zones.delete,
        )


class ZonesResourceWithStreamingResponse:
    def __init__(self, zones: ZonesResource) -> None:
        self._zones = zones

        self.update = to_streamed_response_wrapper(
            zones.update,
        )
        self.delete = to_streamed_response_wrapper(
            zones.delete,
        )


class AsyncZonesResourceWithStreamingResponse:
    def __init__(self, zones: AsyncZonesResource) -> None:
        self._zones = zones

        self.update = async_to_streamed_response_wrapper(
            zones.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            zones.delete,
        )
