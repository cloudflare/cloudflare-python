# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
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
from ....types.addressing.prefixes import (
    BGPPrefixGetResponse,
    BGPPrefixListResponse,
    BGPPrefixUpdateResponse,
    bgp_prefix_update_params,
)

__all__ = ["BGPPrefixes", "AsyncBGPPrefixes"]


class BGPPrefixes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BGPPrefixesWithRawResponse:
        return BGPPrefixesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BGPPrefixesWithStreamingResponse:
        return BGPPrefixesWithStreamingResponse(self)

    def update(
        self,
        bgp_prefix_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        on_demand: bgp_prefix_update_params.OnDemand | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BGPPrefixUpdateResponse:
        """
        Update the properties of a BGP Prefix, such as the on demand advertisement
        status (advertised or withdrawn).

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          bgp_prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not bgp_prefix_identifier:
            raise ValueError(
                f"Expected a non-empty value for `bgp_prefix_identifier` but received {bgp_prefix_identifier!r}"
            )
        return self._patch(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/prefixes/{bgp_prefix_identifier}",
            body=maybe_transform({"on_demand": on_demand}, bgp_prefix_update_params.BGPPrefixUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BGPPrefixUpdateResponse], ResultWrapper[BGPPrefixUpdateResponse]),
        )

    def list(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BGPPrefixListResponse]:
        """List all BGP Prefixes within the specified IP Prefix.

        BGP Prefixes are used to
        control which specific subnets are advertised to the Internet. It is possible to
        advertise subnets more specific than an IP Prefix by creating more specific BGP
        Prefixes.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/prefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefixListResponse]], ResultWrapper[BGPPrefixListResponse]),
        )

    def get(
        self,
        bgp_prefix_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BGPPrefixGetResponse:
        """
        Retrieve a single BGP Prefix according to its identifier

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          bgp_prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not bgp_prefix_identifier:
            raise ValueError(
                f"Expected a non-empty value for `bgp_prefix_identifier` but received {bgp_prefix_identifier!r}"
            )
        return self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/prefixes/{bgp_prefix_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BGPPrefixGetResponse], ResultWrapper[BGPPrefixGetResponse]),
        )


class AsyncBGPPrefixes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBGPPrefixesWithRawResponse:
        return AsyncBGPPrefixesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBGPPrefixesWithStreamingResponse:
        return AsyncBGPPrefixesWithStreamingResponse(self)

    async def update(
        self,
        bgp_prefix_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        on_demand: bgp_prefix_update_params.OnDemand | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BGPPrefixUpdateResponse:
        """
        Update the properties of a BGP Prefix, such as the on demand advertisement
        status (advertised or withdrawn).

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          bgp_prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not bgp_prefix_identifier:
            raise ValueError(
                f"Expected a non-empty value for `bgp_prefix_identifier` but received {bgp_prefix_identifier!r}"
            )
        return await self._patch(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/prefixes/{bgp_prefix_identifier}",
            body=maybe_transform({"on_demand": on_demand}, bgp_prefix_update_params.BGPPrefixUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BGPPrefixUpdateResponse], ResultWrapper[BGPPrefixUpdateResponse]),
        )

    async def list(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BGPPrefixListResponse]:
        """List all BGP Prefixes within the specified IP Prefix.

        BGP Prefixes are used to
        control which specific subnets are advertised to the Internet. It is possible to
        advertise subnets more specific than an IP Prefix by creating more specific BGP
        Prefixes.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/prefixes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefixListResponse]], ResultWrapper[BGPPrefixListResponse]),
        )

    async def get(
        self,
        bgp_prefix_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BGPPrefixGetResponse:
        """
        Retrieve a single BGP Prefix according to its identifier

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          bgp_prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not bgp_prefix_identifier:
            raise ValueError(
                f"Expected a non-empty value for `bgp_prefix_identifier` but received {bgp_prefix_identifier!r}"
            )
        return await self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bgp/prefixes/{bgp_prefix_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BGPPrefixGetResponse], ResultWrapper[BGPPrefixGetResponse]),
        )


class BGPPrefixesWithRawResponse:
    def __init__(self, bgp_prefixes: BGPPrefixes) -> None:
        self._bgp_prefixes = bgp_prefixes

        self.update = to_raw_response_wrapper(
            bgp_prefixes.update,
        )
        self.list = to_raw_response_wrapper(
            bgp_prefixes.list,
        )
        self.get = to_raw_response_wrapper(
            bgp_prefixes.get,
        )


class AsyncBGPPrefixesWithRawResponse:
    def __init__(self, bgp_prefixes: AsyncBGPPrefixes) -> None:
        self._bgp_prefixes = bgp_prefixes

        self.update = async_to_raw_response_wrapper(
            bgp_prefixes.update,
        )
        self.list = async_to_raw_response_wrapper(
            bgp_prefixes.list,
        )
        self.get = async_to_raw_response_wrapper(
            bgp_prefixes.get,
        )


class BGPPrefixesWithStreamingResponse:
    def __init__(self, bgp_prefixes: BGPPrefixes) -> None:
        self._bgp_prefixes = bgp_prefixes

        self.update = to_streamed_response_wrapper(
            bgp_prefixes.update,
        )
        self.list = to_streamed_response_wrapper(
            bgp_prefixes.list,
        )
        self.get = to_streamed_response_wrapper(
            bgp_prefixes.get,
        )


class AsyncBGPPrefixesWithStreamingResponse:
    def __init__(self, bgp_prefixes: AsyncBGPPrefixes) -> None:
        self._bgp_prefixes = bgp_prefixes

        self.update = async_to_streamed_response_wrapper(
            bgp_prefixes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            bgp_prefixes.list,
        )
        self.get = async_to_streamed_response_wrapper(
            bgp_prefixes.get,
        )
