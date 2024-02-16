# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.addressing.prefixes import (
    BGPPrefixUpdateResponse,
    BGPPrefixListResponse,
    BGPPrefixGetResponse,
    bgp_prefix_update_params,
)

from typing import Type, Optional

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.addressing.prefixes import bgp_prefix_update_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

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
        bgp_prefix_id: str,
        *,
        account_id: str,
        prefix_id: str,
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
          account_id: Identifier

          prefix_id: Identifier

          bgp_prefix_id: Identifier

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
        prefix_id: str,
        *,
        account_id: str,
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
          account_id: Identifier

          prefix_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes",
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
    ) -> BGPPrefixGetResponse:
        """
        Retrieve a single BGP Prefix according to its identifier

        Args:
          account_id: Identifier

          prefix_id: Identifier

          bgp_prefix_id: Identifier

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
        bgp_prefix_id: str,
        *,
        account_id: str,
        prefix_id: str,
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
          account_id: Identifier

          prefix_id: Identifier

          bgp_prefix_id: Identifier

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
        prefix_id: str,
        *,
        account_id: str,
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
          account_id: Identifier

          prefix_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not prefix_id:
            raise ValueError(f"Expected a non-empty value for `prefix_id` but received {prefix_id!r}")
        return await self._get(
            f"/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes",
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
    ) -> BGPPrefixGetResponse:
        """
        Retrieve a single BGP Prefix according to its identifier

        Args:
          account_id: Identifier

          prefix_id: Identifier

          bgp_prefix_id: Identifier

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
