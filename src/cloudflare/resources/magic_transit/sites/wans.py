# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.magic_transit.sites import (
    WAN,
    WANCreateResponse,
    WANStaticAddressingParam,
    wan_create_params,
    wan_delete_params,
    wan_update_params,
)

__all__ = ["WANs", "AsyncWANs"]


class WANs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WANsWithRawResponse:
        return WANsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WANsWithStreamingResponse:
        return WANsWithStreamingResponse(self)

    def create(
        self,
        site_id: str,
        *,
        account_id: str,
        physport: int,
        vlan_tag: int,
        name: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        static_addressing: WANStaticAddressingParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WANCreateResponse:
        """
        Creates a new WAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          vlan_tag: VLAN port number.

          static_addressing: (optional) if omitted, use DHCP. Submit secondary_address when site is in high
              availability mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans",
            body=maybe_transform(
                {
                    "physport": physport,
                    "vlan_tag": vlan_tag,
                    "name": name,
                    "priority": priority,
                    "static_addressing": static_addressing,
                },
                wan_create_params.WANCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WANCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[WANCreateResponse], ResultWrapper[WANCreateResponse]),
        )

    def update(
        self,
        wan_id: str,
        *,
        account_id: str,
        site_id: str,
        name: str | NotGiven = NOT_GIVEN,
        physport: int | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        static_addressing: WANStaticAddressingParam | NotGiven = NOT_GIVEN,
        vlan_tag: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WAN:
        """
        Update a specific WAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          wan_id: Identifier

          static_addressing: (optional) if omitted, use DHCP. Submit secondary_address when site is in high
              availability mode.

          vlan_tag: VLAN port number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not wan_id:
            raise ValueError(f"Expected a non-empty value for `wan_id` but received {wan_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "physport": physport,
                    "priority": priority,
                    "static_addressing": static_addressing,
                    "vlan_tag": vlan_tag,
                },
                wan_update_params.WANUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WAN]._unwrapper,
            ),
            cast_to=cast(Type[WAN], ResultWrapper[WAN]),
        )

    def list(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[WAN]:
        """
        Lists WANs associated with an account and site.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans",
            page=SyncSinglePage[WAN],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WAN,
        )

    def delete(
        self,
        wan_id: str,
        *,
        account_id: str,
        site_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WAN:
        """
        Remove a specific WAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          wan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not wan_id:
            raise ValueError(f"Expected a non-empty value for `wan_id` but received {wan_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}",
            body=maybe_transform(body, wan_delete_params.WANDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WAN]._unwrapper,
            ),
            cast_to=cast(Type[WAN], ResultWrapper[WAN]),
        )

    def get(
        self,
        wan_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WAN:
        """
        Get a specific WAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          wan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not wan_id:
            raise ValueError(f"Expected a non-empty value for `wan_id` but received {wan_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WAN]._unwrapper,
            ),
            cast_to=cast(Type[WAN], ResultWrapper[WAN]),
        )


class AsyncWANs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWANsWithRawResponse:
        return AsyncWANsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWANsWithStreamingResponse:
        return AsyncWANsWithStreamingResponse(self)

    async def create(
        self,
        site_id: str,
        *,
        account_id: str,
        physport: int,
        vlan_tag: int,
        name: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        static_addressing: WANStaticAddressingParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WANCreateResponse:
        """
        Creates a new WAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          vlan_tag: VLAN port number.

          static_addressing: (optional) if omitted, use DHCP. Submit secondary_address when site is in high
              availability mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans",
            body=await async_maybe_transform(
                {
                    "physport": physport,
                    "vlan_tag": vlan_tag,
                    "name": name,
                    "priority": priority,
                    "static_addressing": static_addressing,
                },
                wan_create_params.WANCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WANCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[WANCreateResponse], ResultWrapper[WANCreateResponse]),
        )

    async def update(
        self,
        wan_id: str,
        *,
        account_id: str,
        site_id: str,
        name: str | NotGiven = NOT_GIVEN,
        physport: int | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        static_addressing: WANStaticAddressingParam | NotGiven = NOT_GIVEN,
        vlan_tag: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WAN:
        """
        Update a specific WAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          wan_id: Identifier

          static_addressing: (optional) if omitted, use DHCP. Submit secondary_address when site is in high
              availability mode.

          vlan_tag: VLAN port number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not wan_id:
            raise ValueError(f"Expected a non-empty value for `wan_id` but received {wan_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "physport": physport,
                    "priority": priority,
                    "static_addressing": static_addressing,
                    "vlan_tag": vlan_tag,
                },
                wan_update_params.WANUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WAN]._unwrapper,
            ),
            cast_to=cast(Type[WAN], ResultWrapper[WAN]),
        )

    def list(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WAN, AsyncSinglePage[WAN]]:
        """
        Lists WANs associated with an account and site.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans",
            page=AsyncSinglePage[WAN],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WAN,
        )

    async def delete(
        self,
        wan_id: str,
        *,
        account_id: str,
        site_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WAN:
        """
        Remove a specific WAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          wan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not wan_id:
            raise ValueError(f"Expected a non-empty value for `wan_id` but received {wan_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}",
            body=await async_maybe_transform(body, wan_delete_params.WANDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WAN]._unwrapper,
            ),
            cast_to=cast(Type[WAN], ResultWrapper[WAN]),
        )

    async def get(
        self,
        wan_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WAN:
        """
        Get a specific WAN.

        Args:
          account_id: Identifier

          site_id: Identifier

          wan_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not wan_id:
            raise ValueError(f"Expected a non-empty value for `wan_id` but received {wan_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WAN]._unwrapper,
            ),
            cast_to=cast(Type[WAN], ResultWrapper[WAN]),
        )


class WANsWithRawResponse:
    def __init__(self, wans: WANs) -> None:
        self._wans = wans

        self.create = to_raw_response_wrapper(
            wans.create,
        )
        self.update = to_raw_response_wrapper(
            wans.update,
        )
        self.list = to_raw_response_wrapper(
            wans.list,
        )
        self.delete = to_raw_response_wrapper(
            wans.delete,
        )
        self.get = to_raw_response_wrapper(
            wans.get,
        )


class AsyncWANsWithRawResponse:
    def __init__(self, wans: AsyncWANs) -> None:
        self._wans = wans

        self.create = async_to_raw_response_wrapper(
            wans.create,
        )
        self.update = async_to_raw_response_wrapper(
            wans.update,
        )
        self.list = async_to_raw_response_wrapper(
            wans.list,
        )
        self.delete = async_to_raw_response_wrapper(
            wans.delete,
        )
        self.get = async_to_raw_response_wrapper(
            wans.get,
        )


class WANsWithStreamingResponse:
    def __init__(self, wans: WANs) -> None:
        self._wans = wans

        self.create = to_streamed_response_wrapper(
            wans.create,
        )
        self.update = to_streamed_response_wrapper(
            wans.update,
        )
        self.list = to_streamed_response_wrapper(
            wans.list,
        )
        self.delete = to_streamed_response_wrapper(
            wans.delete,
        )
        self.get = to_streamed_response_wrapper(
            wans.get,
        )


class AsyncWANsWithStreamingResponse:
    def __init__(self, wans: AsyncWANs) -> None:
        self._wans = wans

        self.create = async_to_streamed_response_wrapper(
            wans.create,
        )
        self.update = async_to_streamed_response_wrapper(
            wans.update,
        )
        self.list = async_to_streamed_response_wrapper(
            wans.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            wans.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            wans.get,
        )
