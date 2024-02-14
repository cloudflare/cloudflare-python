# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import IPV6UpdateResponse, IPV6GetResponse

from typing import Type, Optional

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.settings import ipv6_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["IPV6", "AsyncIPV6"]


class IPV6(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPV6WithRawResponse:
        return IPV6WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPV6WithStreamingResponse:
        return IPV6WithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPV6UpdateResponse]:
        """
        Enable IPv6 on all subdomains that are Cloudflare enabled.
        (https://support.cloudflare.com/hc/en-us/articles/200168586).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/ipv6",
            body=maybe_transform({"value": value}, ipv6_update_params.IPV6UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPV6UpdateResponse]], ResultWrapper[IPV6UpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPV6GetResponse]:
        """
        Enable IPv6 on all subdomains that are Cloudflare enabled.
        (https://support.cloudflare.com/hc/en-us/articles/200168586).

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
            f"/zones/{zone_id}/settings/ipv6",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPV6GetResponse]], ResultWrapper[IPV6GetResponse]),
        )


class AsyncIPV6(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPV6WithRawResponse:
        return AsyncIPV6WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPV6WithStreamingResponse:
        return AsyncIPV6WithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPV6UpdateResponse]:
        """
        Enable IPv6 on all subdomains that are Cloudflare enabled.
        (https://support.cloudflare.com/hc/en-us/articles/200168586).

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/ipv6",
            body=maybe_transform({"value": value}, ipv6_update_params.IPV6UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPV6UpdateResponse]], ResultWrapper[IPV6UpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPV6GetResponse]:
        """
        Enable IPv6 on all subdomains that are Cloudflare enabled.
        (https://support.cloudflare.com/hc/en-us/articles/200168586).

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
            f"/zones/{zone_id}/settings/ipv6",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IPV6GetResponse]], ResultWrapper[IPV6GetResponse]),
        )


class IPV6WithRawResponse:
    def __init__(self, ipv6: IPV6) -> None:
        self._ipv6 = ipv6

        self.update = to_raw_response_wrapper(
            ipv6.update,
        )
        self.get = to_raw_response_wrapper(
            ipv6.get,
        )


class AsyncIPV6WithRawResponse:
    def __init__(self, ipv6: AsyncIPV6) -> None:
        self._ipv6 = ipv6

        self.update = async_to_raw_response_wrapper(
            ipv6.update,
        )
        self.get = async_to_raw_response_wrapper(
            ipv6.get,
        )


class IPV6WithStreamingResponse:
    def __init__(self, ipv6: IPV6) -> None:
        self._ipv6 = ipv6

        self.update = to_streamed_response_wrapper(
            ipv6.update,
        )
        self.get = to_streamed_response_wrapper(
            ipv6.get,
        )


class AsyncIPV6WithStreamingResponse:
    def __init__(self, ipv6: AsyncIPV6) -> None:
        self._ipv6 = ipv6

        self.update = async_to_streamed_response_wrapper(
            ipv6.update,
        )
        self.get = async_to_streamed_response_wrapper(
            ipv6.get,
        )
