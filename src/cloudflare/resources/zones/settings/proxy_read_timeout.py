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
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import ZonesProxyReadTimeout, ZonesProxyReadTimeoutParam, proxy_read_timeout_edit_params

__all__ = ["ProxyReadTimeout", "AsyncProxyReadTimeout"]


class ProxyReadTimeout(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxyReadTimeoutWithRawResponse:
        return ProxyReadTimeoutWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxyReadTimeoutWithStreamingResponse:
        return ProxyReadTimeoutWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: ZonesProxyReadTimeoutParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesProxyReadTimeout]:
        """
        Maximum time between two read operations from origin.

        Args:
          zone_id: Identifier

          value: Maximum time between two read operations from origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/proxy_read_timeout",
            body=maybe_transform({"value": value}, proxy_read_timeout_edit_params.ProxyReadTimeoutEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesProxyReadTimeout]], ResultWrapper[ZonesProxyReadTimeout]),
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
    ) -> Optional[ZonesProxyReadTimeout]:
        """
        Maximum time between two read operations from origin.

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
            f"/zones/{zone_id}/settings/proxy_read_timeout",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesProxyReadTimeout]], ResultWrapper[ZonesProxyReadTimeout]),
        )


class AsyncProxyReadTimeout(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxyReadTimeoutWithRawResponse:
        return AsyncProxyReadTimeoutWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxyReadTimeoutWithStreamingResponse:
        return AsyncProxyReadTimeoutWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: ZonesProxyReadTimeoutParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesProxyReadTimeout]:
        """
        Maximum time between two read operations from origin.

        Args:
          zone_id: Identifier

          value: Maximum time between two read operations from origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/proxy_read_timeout",
            body=await async_maybe_transform(
                {"value": value}, proxy_read_timeout_edit_params.ProxyReadTimeoutEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesProxyReadTimeout]], ResultWrapper[ZonesProxyReadTimeout]),
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
    ) -> Optional[ZonesProxyReadTimeout]:
        """
        Maximum time between two read operations from origin.

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
            f"/zones/{zone_id}/settings/proxy_read_timeout",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesProxyReadTimeout]], ResultWrapper[ZonesProxyReadTimeout]),
        )


class ProxyReadTimeoutWithRawResponse:
    def __init__(self, proxy_read_timeout: ProxyReadTimeout) -> None:
        self._proxy_read_timeout = proxy_read_timeout

        self.edit = to_raw_response_wrapper(
            proxy_read_timeout.edit,
        )
        self.get = to_raw_response_wrapper(
            proxy_read_timeout.get,
        )


class AsyncProxyReadTimeoutWithRawResponse:
    def __init__(self, proxy_read_timeout: AsyncProxyReadTimeout) -> None:
        self._proxy_read_timeout = proxy_read_timeout

        self.edit = async_to_raw_response_wrapper(
            proxy_read_timeout.edit,
        )
        self.get = async_to_raw_response_wrapper(
            proxy_read_timeout.get,
        )


class ProxyReadTimeoutWithStreamingResponse:
    def __init__(self, proxy_read_timeout: ProxyReadTimeout) -> None:
        self._proxy_read_timeout = proxy_read_timeout

        self.edit = to_streamed_response_wrapper(
            proxy_read_timeout.edit,
        )
        self.get = to_streamed_response_wrapper(
            proxy_read_timeout.get,
        )


class AsyncProxyReadTimeoutWithStreamingResponse:
    def __init__(self, proxy_read_timeout: AsyncProxyReadTimeout) -> None:
        self._proxy_read_timeout = proxy_read_timeout

        self.edit = async_to_streamed_response_wrapper(
            proxy_read_timeout.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            proxy_read_timeout.get,
        )
