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
from ....types.zones.settings import ZonesTLS1_3, tls_1_3_edit_params

__all__ = ["TLS1_3", "AsyncTLS1_3"]


class TLS1_3(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TLS1_3WithRawResponse:
        return TLS1_3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TLS1_3WithStreamingResponse:
        return TLS1_3WithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off", "zrt"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesTLS1_3]:
        """
        Changes TLS 1.3 setting.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/tls_1_3",
            body=maybe_transform({"value": value}, tls_1_3_edit_params.TLS1_3EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesTLS1_3]], ResultWrapper[ZonesTLS1_3]),
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
    ) -> Optional[ZonesTLS1_3]:
        """
        Gets TLS 1.3 setting enabled for a zone.

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
            f"/zones/{zone_id}/settings/tls_1_3",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesTLS1_3]], ResultWrapper[ZonesTLS1_3]),
        )


class AsyncTLS1_3(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTLS1_3WithRawResponse:
        return AsyncTLS1_3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTLS1_3WithStreamingResponse:
        return AsyncTLS1_3WithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off", "zrt"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesTLS1_3]:
        """
        Changes TLS 1.3 setting.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/tls_1_3",
            body=await async_maybe_transform({"value": value}, tls_1_3_edit_params.TLS1_3EditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesTLS1_3]], ResultWrapper[ZonesTLS1_3]),
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
    ) -> Optional[ZonesTLS1_3]:
        """
        Gets TLS 1.3 setting enabled for a zone.

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
            f"/zones/{zone_id}/settings/tls_1_3",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesTLS1_3]], ResultWrapper[ZonesTLS1_3]),
        )


class TLS1_3WithRawResponse:
    def __init__(self, tls_1_3: TLS1_3) -> None:
        self._tls_1_3 = tls_1_3

        self.edit = to_raw_response_wrapper(
            tls_1_3.edit,
        )
        self.get = to_raw_response_wrapper(
            tls_1_3.get,
        )


class AsyncTLS1_3WithRawResponse:
    def __init__(self, tls_1_3: AsyncTLS1_3) -> None:
        self._tls_1_3 = tls_1_3

        self.edit = async_to_raw_response_wrapper(
            tls_1_3.edit,
        )
        self.get = async_to_raw_response_wrapper(
            tls_1_3.get,
        )


class TLS1_3WithStreamingResponse:
    def __init__(self, tls_1_3: TLS1_3) -> None:
        self._tls_1_3 = tls_1_3

        self.edit = to_streamed_response_wrapper(
            tls_1_3.edit,
        )
        self.get = to_streamed_response_wrapper(
            tls_1_3.get,
        )


class AsyncTLS1_3WithStreamingResponse:
    def __init__(self, tls_1_3: AsyncTLS1_3) -> None:
        self._tls_1_3 = tls_1_3

        self.edit = async_to_streamed_response_wrapper(
            tls_1_3.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            tls_1_3.get,
        )
