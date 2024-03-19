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
from ....types.zones.settings import ZonesOriginErrorPagePassThru, origin_error_page_pass_thru_edit_params

__all__ = ["OriginErrorPagePassThru", "AsyncOriginErrorPagePassThru"]


class OriginErrorPagePassThru(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginErrorPagePassThruWithRawResponse:
        return OriginErrorPagePassThruWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginErrorPagePassThruWithStreamingResponse:
        return OriginErrorPagePassThruWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesOriginErrorPagePassThru]:
        """
        Cloudflare will proxy customer error pages on any 502,504 errors on origin
        server instead of showing a default Cloudflare error page. This does not apply
        to 522 errors and is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/origin_error_page_pass_thru",
            body=maybe_transform(
                {"value": value}, origin_error_page_pass_thru_edit_params.OriginErrorPagePassThruEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOriginErrorPagePassThru]], ResultWrapper[ZonesOriginErrorPagePassThru]),
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
    ) -> Optional[ZonesOriginErrorPagePassThru]:
        """
        Cloudflare will proxy customer error pages on any 502,504 errors on origin
        server instead of showing a default Cloudflare error page. This does not apply
        to 522 errors and is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/origin_error_page_pass_thru",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOriginErrorPagePassThru]], ResultWrapper[ZonesOriginErrorPagePassThru]),
        )


class AsyncOriginErrorPagePassThru(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginErrorPagePassThruWithRawResponse:
        return AsyncOriginErrorPagePassThruWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginErrorPagePassThruWithStreamingResponse:
        return AsyncOriginErrorPagePassThruWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesOriginErrorPagePassThru]:
        """
        Cloudflare will proxy customer error pages on any 502,504 errors on origin
        server instead of showing a default Cloudflare error page. This does not apply
        to 522 errors and is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/origin_error_page_pass_thru",
            body=await async_maybe_transform(
                {"value": value}, origin_error_page_pass_thru_edit_params.OriginErrorPagePassThruEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOriginErrorPagePassThru]], ResultWrapper[ZonesOriginErrorPagePassThru]),
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
    ) -> Optional[ZonesOriginErrorPagePassThru]:
        """
        Cloudflare will proxy customer error pages on any 502,504 errors on origin
        server instead of showing a default Cloudflare error page. This does not apply
        to 522 errors and is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/origin_error_page_pass_thru",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesOriginErrorPagePassThru]], ResultWrapper[ZonesOriginErrorPagePassThru]),
        )


class OriginErrorPagePassThruWithRawResponse:
    def __init__(self, origin_error_page_pass_thru: OriginErrorPagePassThru) -> None:
        self._origin_error_page_pass_thru = origin_error_page_pass_thru

        self.edit = to_raw_response_wrapper(
            origin_error_page_pass_thru.edit,
        )
        self.get = to_raw_response_wrapper(
            origin_error_page_pass_thru.get,
        )


class AsyncOriginErrorPagePassThruWithRawResponse:
    def __init__(self, origin_error_page_pass_thru: AsyncOriginErrorPagePassThru) -> None:
        self._origin_error_page_pass_thru = origin_error_page_pass_thru

        self.edit = async_to_raw_response_wrapper(
            origin_error_page_pass_thru.edit,
        )
        self.get = async_to_raw_response_wrapper(
            origin_error_page_pass_thru.get,
        )


class OriginErrorPagePassThruWithStreamingResponse:
    def __init__(self, origin_error_page_pass_thru: OriginErrorPagePassThru) -> None:
        self._origin_error_page_pass_thru = origin_error_page_pass_thru

        self.edit = to_streamed_response_wrapper(
            origin_error_page_pass_thru.edit,
        )
        self.get = to_streamed_response_wrapper(
            origin_error_page_pass_thru.get,
        )


class AsyncOriginErrorPagePassThruWithStreamingResponse:
    def __init__(self, origin_error_page_pass_thru: AsyncOriginErrorPagePassThru) -> None:
        self._origin_error_page_pass_thru = origin_error_page_pass_thru

        self.edit = async_to_streamed_response_wrapper(
            origin_error_page_pass_thru.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            origin_error_page_pass_thru.get,
        )
