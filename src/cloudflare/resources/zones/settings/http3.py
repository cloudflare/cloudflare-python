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
from ....types.zones.settings import ZonesHTTP3, http3_edit_params

__all__ = ["HTTP3", "AsyncHTTP3"]


class HTTP3(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTTP3WithRawResponse:
        return HTTP3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTP3WithStreamingResponse:
        return HTTP3WithStreamingResponse(self)

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
    ) -> Optional[ZonesHTTP3]:
        """
        Value of the HTTP3 setting.

        Args:
          zone_id: Identifier

          value: Value of the HTTP3 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/http3",
            body=maybe_transform({"value": value}, http3_edit_params.HTTP3EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesHTTP3]], ResultWrapper[ZonesHTTP3]),
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
    ) -> Optional[ZonesHTTP3]:
        """
        Value of the HTTP3 setting.

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
            f"/zones/{zone_id}/settings/http3",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesHTTP3]], ResultWrapper[ZonesHTTP3]),
        )


class AsyncHTTP3(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTTP3WithRawResponse:
        return AsyncHTTP3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTP3WithStreamingResponse:
        return AsyncHTTP3WithStreamingResponse(self)

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
    ) -> Optional[ZonesHTTP3]:
        """
        Value of the HTTP3 setting.

        Args:
          zone_id: Identifier

          value: Value of the HTTP3 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/http3",
            body=await async_maybe_transform({"value": value}, http3_edit_params.HTTP3EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesHTTP3]], ResultWrapper[ZonesHTTP3]),
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
    ) -> Optional[ZonesHTTP3]:
        """
        Value of the HTTP3 setting.

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
            f"/zones/{zone_id}/settings/http3",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesHTTP3]], ResultWrapper[ZonesHTTP3]),
        )


class HTTP3WithRawResponse:
    def __init__(self, http3: HTTP3) -> None:
        self._http3 = http3

        self.edit = to_raw_response_wrapper(
            http3.edit,
        )
        self.get = to_raw_response_wrapper(
            http3.get,
        )


class AsyncHTTP3WithRawResponse:
    def __init__(self, http3: AsyncHTTP3) -> None:
        self._http3 = http3

        self.edit = async_to_raw_response_wrapper(
            http3.edit,
        )
        self.get = async_to_raw_response_wrapper(
            http3.get,
        )


class HTTP3WithStreamingResponse:
    def __init__(self, http3: HTTP3) -> None:
        self._http3 = http3

        self.edit = to_streamed_response_wrapper(
            http3.edit,
        )
        self.get = to_streamed_response_wrapper(
            http3.get,
        )


class AsyncHTTP3WithStreamingResponse:
    def __init__(self, http3: AsyncHTTP3) -> None:
        self._http3 = http3

        self.edit = async_to_streamed_response_wrapper(
            http3.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            http3.get,
        )
