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
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.addressing.prefixes import bgp_prefix_edit_params, bgp_prefix_create_params
from ....types.addressing.prefixes.bgp_prefix import BGPPrefix

__all__ = ["BGPPrefixesResource", "AsyncBGPPrefixesResource"]


class BGPPrefixesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BGPPrefixesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BGPPrefixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BGPPrefixesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BGPPrefixesResourceWithStreamingResponse(self)

    def create(
        self,
        prefix_id: str,
        *,
        account_id: str,
        cidr: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BGPPrefix]:
        """
        Create a BGP prefix, controlling the BGP advertisement status of a specific
        subnet. When created, BGP prefixes are initially withdrawn, and can be
        advertised with the Update BGP Prefix API.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._post(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes",
            body=maybe_transform({"cidr": cidr}, bgp_prefix_create_params.BGPPrefixCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BGPPrefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefix]], ResultWrapper[BGPPrefix]),
        )

    def list(
        self,
        prefix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[BGPPrefix]:
        """List all BGP Prefixes within the specified IP Prefix.

        BGP Prefixes are used to
        control which specific subnets are advertised to the Internet. It is possible to
        advertise subnets more specific than an IP Prefix by creating more specific BGP
        Prefixes.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes",
            page=SyncSinglePage[BGPPrefix],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=BGPPrefix,
        )

    def edit(
        self,
        bgp_prefix_id: str,
        *,
        account_id: str,
        prefix_id: str,
        on_demand: bgp_prefix_edit_params.OnDemand | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BGPPrefix]:
        """
        Update the properties of a BGP Prefix, such as the on demand advertisement
        status (advertised or withdrawn).

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          bgp_prefix_id: Identifier of BGP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not bgp_prefix_id:
            raise ValueError(f"Expected a non-empty value for `bgp_prefix_id` but received {bgp_prefix_id!r}")
        return self._patch(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}",
            body=maybe_transform({"on_demand": on_demand}, bgp_prefix_edit_params.BGPPrefixEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BGPPrefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefix]], ResultWrapper[BGPPrefix]),
        )

    def get(
        self,
        bgp_prefix_id: str,
        *,
        account_id: str,
        prefix_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BGPPrefix]:
        """
        Retrieve a single BGP Prefix according to its identifier

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          bgp_prefix_id: Identifier of BGP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not bgp_prefix_id:
            raise ValueError(f"Expected a non-empty value for `bgp_prefix_id` but received {bgp_prefix_id!r}")
        return self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BGPPrefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefix]], ResultWrapper[BGPPrefix]),
        )


class AsyncBGPPrefixesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBGPPrefixesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBGPPrefixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBGPPrefixesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBGPPrefixesResourceWithStreamingResponse(self)

    async def create(
        self,
        prefix_id: str,
        *,
        account_id: str,
        cidr: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BGPPrefix]:
        """
        Create a BGP prefix, controlling the BGP advertisement status of a specific
        subnet. When created, BGP prefixes are initially withdrawn, and can be
        advertised with the Update BGP Prefix API.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return await self._post(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes",
            body=await async_maybe_transform({"cidr": cidr}, bgp_prefix_create_params.BGPPrefixCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BGPPrefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefix]], ResultWrapper[BGPPrefix]),
        )

    def list(
        self,
        prefix_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BGPPrefix, AsyncSinglePage[BGPPrefix]]:
        """List all BGP Prefixes within the specified IP Prefix.

        BGP Prefixes are used to
        control which specific subnets are advertised to the Internet. It is possible to
        advertise subnets more specific than an IP Prefix by creating more specific BGP
        Prefixes.

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes",
            page=AsyncSinglePage[BGPPrefix],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=BGPPrefix,
        )

    async def edit(
        self,
        bgp_prefix_id: str,
        *,
        account_id: str,
        prefix_id: str,
        on_demand: bgp_prefix_edit_params.OnDemand | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BGPPrefix]:
        """
        Update the properties of a BGP Prefix, such as the on demand advertisement
        status (advertised or withdrawn).

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          bgp_prefix_id: Identifier of BGP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not bgp_prefix_id:
            raise ValueError(f"Expected a non-empty value for `bgp_prefix_id` but received {bgp_prefix_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}",
            body=await async_maybe_transform({"on_demand": on_demand}, bgp_prefix_edit_params.BGPPrefixEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BGPPrefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefix]], ResultWrapper[BGPPrefix]),
        )

    async def get(
        self,
        bgp_prefix_id: str,
        *,
        account_id: str,
        prefix_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BGPPrefix]:
        """
        Retrieve a single BGP Prefix according to its identifier

        Args:
          account_id: Identifier of a Cloudflare account.

          prefix_id: Identifier of an IP Prefix.

          bgp_prefix_id: Identifier of BGP Prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        if not bgp_prefix_id:
            raise ValueError(f"Expected a non-empty value for `bgp_prefix_id` but received {bgp_prefix_id!r}")
        return await self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[BGPPrefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefix]], ResultWrapper[BGPPrefix]),
        )


class BGPPrefixesResourceWithRawResponse:
    def __init__(self, bgp_prefixes: BGPPrefixesResource) -> None:
        self._bgp_prefixes = bgp_prefixes

        self.create = to_raw_response_wrapper(
            bgp_prefixes.create,
        )
        self.list = to_raw_response_wrapper(
            bgp_prefixes.list,
        )
        self.edit = to_raw_response_wrapper(
            bgp_prefixes.edit,
        )
        self.get = to_raw_response_wrapper(
            bgp_prefixes.get,
        )


class AsyncBGPPrefixesResourceWithRawResponse:
    def __init__(self, bgp_prefixes: AsyncBGPPrefixesResource) -> None:
        self._bgp_prefixes = bgp_prefixes

        self.create = async_to_raw_response_wrapper(
            bgp_prefixes.create,
        )
        self.list = async_to_raw_response_wrapper(
            bgp_prefixes.list,
        )
        self.edit = async_to_raw_response_wrapper(
            bgp_prefixes.edit,
        )
        self.get = async_to_raw_response_wrapper(
            bgp_prefixes.get,
        )


class BGPPrefixesResourceWithStreamingResponse:
    def __init__(self, bgp_prefixes: BGPPrefixesResource) -> None:
        self._bgp_prefixes = bgp_prefixes

        self.create = to_streamed_response_wrapper(
            bgp_prefixes.create,
        )
        self.list = to_streamed_response_wrapper(
            bgp_prefixes.list,
        )
        self.edit = to_streamed_response_wrapper(
            bgp_prefixes.edit,
        )
        self.get = to_streamed_response_wrapper(
            bgp_prefixes.get,
        )


class AsyncBGPPrefixesResourceWithStreamingResponse:
    def __init__(self, bgp_prefixes: AsyncBGPPrefixesResource) -> None:
        self._bgp_prefixes = bgp_prefixes

        self.create = async_to_streamed_response_wrapper(
            bgp_prefixes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            bgp_prefixes.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            bgp_prefixes.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            bgp_prefixes.get,
        )
