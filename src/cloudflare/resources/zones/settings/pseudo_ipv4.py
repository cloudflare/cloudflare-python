# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ....types.zones.settings import PseudoIPV4, pseudo_ipv4_edit_params

__all__ = ["PseudoIPV4Resource", "AsyncPseudoIPV4Resource"]


class PseudoIPV4Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PseudoIPV4ResourceWithRawResponse:
        return PseudoIPV4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PseudoIPV4ResourceWithStreamingResponse:
        return PseudoIPV4ResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "add_header", "overwrite_header"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PseudoIPV4]:
        """
        Value of the Pseudo IPv4 setting.

        Args:
          zone_id: Identifier

          value: Value of the Pseudo IPv4 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/pseudo_ipv4",
            body=maybe_transform({"value": value}, pseudo_ipv4_edit_params.PseudoIPV4EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PseudoIPV4]], ResultWrapper[PseudoIPV4]),
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
    ) -> Optional[PseudoIPV4]:
        """
        Value of the Pseudo IPv4 setting.

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
            f"/zones/{zone_id}/settings/pseudo_ipv4",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PseudoIPV4]], ResultWrapper[PseudoIPV4]),
        )


class AsyncPseudoIPV4Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPseudoIPV4ResourceWithRawResponse:
        return AsyncPseudoIPV4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPseudoIPV4ResourceWithStreamingResponse:
        return AsyncPseudoIPV4ResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "add_header", "overwrite_header"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PseudoIPV4]:
        """
        Value of the Pseudo IPv4 setting.

        Args:
          zone_id: Identifier

          value: Value of the Pseudo IPv4 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/pseudo_ipv4",
            body=await async_maybe_transform({"value": value}, pseudo_ipv4_edit_params.PseudoIPV4EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PseudoIPV4]], ResultWrapper[PseudoIPV4]),
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
    ) -> Optional[PseudoIPV4]:
        """
        Value of the Pseudo IPv4 setting.

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
            f"/zones/{zone_id}/settings/pseudo_ipv4",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PseudoIPV4]], ResultWrapper[PseudoIPV4]),
        )


class PseudoIPV4ResourceWithRawResponse:
    def __init__(self, pseudo_ipv4: PseudoIPV4Resource) -> None:
        self._pseudo_ipv4 = pseudo_ipv4

        self.edit = to_raw_response_wrapper(
            pseudo_ipv4.edit,
        )
        self.get = to_raw_response_wrapper(
            pseudo_ipv4.get,
        )


class AsyncPseudoIPV4ResourceWithRawResponse:
    def __init__(self, pseudo_ipv4: AsyncPseudoIPV4Resource) -> None:
        self._pseudo_ipv4 = pseudo_ipv4

        self.edit = async_to_raw_response_wrapper(
            pseudo_ipv4.edit,
        )
        self.get = async_to_raw_response_wrapper(
            pseudo_ipv4.get,
        )


class PseudoIPV4ResourceWithStreamingResponse:
    def __init__(self, pseudo_ipv4: PseudoIPV4Resource) -> None:
        self._pseudo_ipv4 = pseudo_ipv4

        self.edit = to_streamed_response_wrapper(
            pseudo_ipv4.edit,
        )
        self.get = to_streamed_response_wrapper(
            pseudo_ipv4.get,
        )


class AsyncPseudoIPV4ResourceWithStreamingResponse:
    def __init__(self, pseudo_ipv4: AsyncPseudoIPV4Resource) -> None:
        self._pseudo_ipv4 = pseudo_ipv4

        self.edit = async_to_streamed_response_wrapper(
            pseudo_ipv4.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            pseudo_ipv4.get,
        )
