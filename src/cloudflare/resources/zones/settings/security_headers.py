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
from ....types.zones.settings import ZonesSecurityHeader, security_header_edit_params

__all__ = ["SecurityHeaders", "AsyncSecurityHeaders"]


class SecurityHeaders(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecurityHeadersWithRawResponse:
        return SecurityHeadersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityHeadersWithStreamingResponse:
        return SecurityHeadersWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: security_header_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesSecurityHeader]:
        """
        Cloudflare security header for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/security_header",
            body=maybe_transform({"value": value}, security_header_edit_params.SecurityHeaderEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesSecurityHeader]], ResultWrapper[ZonesSecurityHeader]),
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
    ) -> Optional[ZonesSecurityHeader]:
        """
        Cloudflare security header for a zone.

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
            f"/zones/{zone_id}/settings/security_header",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesSecurityHeader]], ResultWrapper[ZonesSecurityHeader]),
        )


class AsyncSecurityHeaders(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecurityHeadersWithRawResponse:
        return AsyncSecurityHeadersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityHeadersWithStreamingResponse:
        return AsyncSecurityHeadersWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: security_header_edit_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesSecurityHeader]:
        """
        Cloudflare security header for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/security_header",
            body=await async_maybe_transform({"value": value}, security_header_edit_params.SecurityHeaderEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesSecurityHeader]], ResultWrapper[ZonesSecurityHeader]),
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
    ) -> Optional[ZonesSecurityHeader]:
        """
        Cloudflare security header for a zone.

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
            f"/zones/{zone_id}/settings/security_header",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesSecurityHeader]], ResultWrapper[ZonesSecurityHeader]),
        )


class SecurityHeadersWithRawResponse:
    def __init__(self, security_headers: SecurityHeaders) -> None:
        self._security_headers = security_headers

        self.edit = to_raw_response_wrapper(
            security_headers.edit,
        )
        self.get = to_raw_response_wrapper(
            security_headers.get,
        )


class AsyncSecurityHeadersWithRawResponse:
    def __init__(self, security_headers: AsyncSecurityHeaders) -> None:
        self._security_headers = security_headers

        self.edit = async_to_raw_response_wrapper(
            security_headers.edit,
        )
        self.get = async_to_raw_response_wrapper(
            security_headers.get,
        )


class SecurityHeadersWithStreamingResponse:
    def __init__(self, security_headers: SecurityHeaders) -> None:
        self._security_headers = security_headers

        self.edit = to_streamed_response_wrapper(
            security_headers.edit,
        )
        self.get = to_streamed_response_wrapper(
            security_headers.get,
        )


class AsyncSecurityHeadersWithStreamingResponse:
    def __init__(self, security_headers: AsyncSecurityHeaders) -> None:
        self._security_headers = security_headers

        self.edit = async_to_streamed_response_wrapper(
            security_headers.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            security_headers.get,
        )
