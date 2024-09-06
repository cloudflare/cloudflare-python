# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.addressing.prefixes.bgp.bgp_prefix import BGPPrefix

from .....pagination import SyncSinglePage, AsyncSinglePage

from ....._base_client import make_request_options, AsyncPaginator

from ....._wrappers import ResultWrapper

from ....._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from .....types.addressing.prefixes.bgp import prefix_edit_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.addressing.prefixes.bgp import prefix_edit_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["PrefixesResource", "AsyncPrefixesResource"]


class PrefixesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrefixesResourceWithRawResponse:
        return PrefixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrefixesResourceWithStreamingResponse:
        return PrefixesResourceWithStreamingResponse(self)

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
        on_demand: prefix_edit_params.OnDemand | NotGiven = NOT_GIVEN,
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
            body=maybe_transform({"on_demand": on_demand}, prefix_edit_params.PrefixEditParams),
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
                post_parser=ResultWrapper[Optional[BGPPrefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefix]], ResultWrapper[BGPPrefix]),
        )


class AsyncPrefixesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrefixesResourceWithRawResponse:
        return AsyncPrefixesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrefixesResourceWithStreamingResponse:
        return AsyncPrefixesResourceWithStreamingResponse(self)

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
        on_demand: prefix_edit_params.OnDemand | NotGiven = NOT_GIVEN,
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
            body=await async_maybe_transform({"on_demand": on_demand}, prefix_edit_params.PrefixEditParams),
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
                post_parser=ResultWrapper[Optional[BGPPrefix]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BGPPrefix]], ResultWrapper[BGPPrefix]),
        )


class PrefixesResourceWithRawResponse:
    def __init__(self, prefixes: PrefixesResource) -> None:
        self._prefixes = prefixes

        self.list = to_raw_response_wrapper(
            prefixes.list,
        )
        self.edit = to_raw_response_wrapper(
            prefixes.edit,
        )
        self.get = to_raw_response_wrapper(
            prefixes.get,
        )


class AsyncPrefixesResourceWithRawResponse:
    def __init__(self, prefixes: AsyncPrefixesResource) -> None:
        self._prefixes = prefixes

        self.list = async_to_raw_response_wrapper(
            prefixes.list,
        )
        self.edit = async_to_raw_response_wrapper(
            prefixes.edit,
        )
        self.get = async_to_raw_response_wrapper(
            prefixes.get,
        )


class PrefixesResourceWithStreamingResponse:
    def __init__(self, prefixes: PrefixesResource) -> None:
        self._prefixes = prefixes

        self.list = to_streamed_response_wrapper(
            prefixes.list,
        )
        self.edit = to_streamed_response_wrapper(
            prefixes.edit,
        )
        self.get = to_streamed_response_wrapper(
            prefixes.get,
        )


class AsyncPrefixesResourceWithStreamingResponse:
    def __init__(self, prefixes: AsyncPrefixesResource) -> None:
        self._prefixes = prefixes

        self.list = async_to_streamed_response_wrapper(
            prefixes.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            prefixes.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            prefixes.get,
        )
