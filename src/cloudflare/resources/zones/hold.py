# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.zones import HoldEnforceResponse, HoldGetResponse, HoldRemoveResponse

from typing import Type, Optional

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
from ...types.zones import hold_enforce_params
from ...types.zones import hold_remove_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Hold", "AsyncHold"]


class Hold(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HoldWithRawResponse:
        return HoldWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldWithStreamingResponse:
        return HoldWithStreamingResponse(self)

    def enforce(
        self,
        zone_id: str,
        *,
        include_subdomains: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HoldEnforceResponse:
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
                query=maybe_transform(
                    {"include_subdomains": include_subdomains}, hold_enforce_params.HoldEnforceParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HoldEnforceResponse], ResultWrapper[HoldEnforceResponse]),
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

    def remove(
        self,
        zone_id: str,
        *,
        hold_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HoldRemoveResponse]:
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
                query=maybe_transform({"hold_after": hold_after}, hold_remove_params.HoldRemoveParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HoldRemoveResponse]], ResultWrapper[HoldRemoveResponse]),
        )


class AsyncHold(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHoldWithRawResponse:
        return AsyncHoldWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldWithStreamingResponse:
        return AsyncHoldWithStreamingResponse(self)

    async def enforce(
        self,
        zone_id: str,
        *,
        include_subdomains: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HoldEnforceResponse:
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
                query=maybe_transform(
                    {"include_subdomains": include_subdomains}, hold_enforce_params.HoldEnforceParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[HoldEnforceResponse], ResultWrapper[HoldEnforceResponse]),
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

    async def remove(
        self,
        zone_id: str,
        *,
        hold_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HoldRemoveResponse]:
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
                query=maybe_transform({"hold_after": hold_after}, hold_remove_params.HoldRemoveParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HoldRemoveResponse]], ResultWrapper[HoldRemoveResponse]),
        )


class HoldWithRawResponse:
    def __init__(self, hold: Hold) -> None:
        self._hold = hold

        self.enforce = to_raw_response_wrapper(
            hold.enforce,
        )
        self.get = to_raw_response_wrapper(
            hold.get,
        )
        self.remove = to_raw_response_wrapper(
            hold.remove,
        )


class AsyncHoldWithRawResponse:
    def __init__(self, hold: AsyncHold) -> None:
        self._hold = hold

        self.enforce = async_to_raw_response_wrapper(
            hold.enforce,
        )
        self.get = async_to_raw_response_wrapper(
            hold.get,
        )
        self.remove = async_to_raw_response_wrapper(
            hold.remove,
        )


class HoldWithStreamingResponse:
    def __init__(self, hold: Hold) -> None:
        self._hold = hold

        self.enforce = to_streamed_response_wrapper(
            hold.enforce,
        )
        self.get = to_streamed_response_wrapper(
            hold.get,
        )
        self.remove = to_streamed_response_wrapper(
            hold.remove,
        )


class AsyncHoldWithStreamingResponse:
    def __init__(self, hold: AsyncHold) -> None:
        self._hold = hold

        self.enforce = async_to_streamed_response_wrapper(
            hold.enforce,
        )
        self.get = async_to_streamed_response_wrapper(
            hold.get,
        )
        self.remove = async_to_streamed_response_wrapper(
            hold.remove,
        )
