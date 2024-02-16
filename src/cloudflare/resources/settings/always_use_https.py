# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.settings import AlwaysUseHTTPSGetResponse, AlwaysUseHTTPSUpdateResponse, always_use_https_update_params

__all__ = ["AlwaysUseHTTPS", "AsyncAlwaysUseHTTPS"]


class AlwaysUseHTTPS(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlwaysUseHTTPSWithRawResponse:
        return AlwaysUseHTTPSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlwaysUseHTTPSWithStreamingResponse:
        return AlwaysUseHTTPSWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AlwaysUseHTTPSUpdateResponse]:
        """
        Reply to all requests for URLs that use "http" with a 301 redirect to the
        equivalent "https" URL. If you only want to redirect for a subset of requests,
        consider creating an "Always use HTTPS" page rule.

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
            f"/zones/{zone_id}/settings/always_use_https",
            body=maybe_transform({"value": value}, always_use_https_update_params.AlwaysUseHTTPSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlwaysUseHTTPSUpdateResponse]], ResultWrapper[AlwaysUseHTTPSUpdateResponse]),
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
    ) -> Optional[AlwaysUseHTTPSGetResponse]:
        """
        Reply to all requests for URLs that use "http" with a 301 redirect to the
        equivalent "https" URL. If you only want to redirect for a subset of requests,
        consider creating an "Always use HTTPS" page rule.

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
            f"/zones/{zone_id}/settings/always_use_https",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlwaysUseHTTPSGetResponse]], ResultWrapper[AlwaysUseHTTPSGetResponse]),
        )


class AsyncAlwaysUseHTTPS(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlwaysUseHTTPSWithRawResponse:
        return AsyncAlwaysUseHTTPSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlwaysUseHTTPSWithStreamingResponse:
        return AsyncAlwaysUseHTTPSWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AlwaysUseHTTPSUpdateResponse]:
        """
        Reply to all requests for URLs that use "http" with a 301 redirect to the
        equivalent "https" URL. If you only want to redirect for a subset of requests,
        consider creating an "Always use HTTPS" page rule.

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
            f"/zones/{zone_id}/settings/always_use_https",
            body=maybe_transform({"value": value}, always_use_https_update_params.AlwaysUseHTTPSUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlwaysUseHTTPSUpdateResponse]], ResultWrapper[AlwaysUseHTTPSUpdateResponse]),
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
    ) -> Optional[AlwaysUseHTTPSGetResponse]:
        """
        Reply to all requests for URLs that use "http" with a 301 redirect to the
        equivalent "https" URL. If you only want to redirect for a subset of requests,
        consider creating an "Always use HTTPS" page rule.

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
            f"/zones/{zone_id}/settings/always_use_https",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AlwaysUseHTTPSGetResponse]], ResultWrapper[AlwaysUseHTTPSGetResponse]),
        )


class AlwaysUseHTTPSWithRawResponse:
    def __init__(self, always_use_https: AlwaysUseHTTPS) -> None:
        self._always_use_https = always_use_https

        self.update = to_raw_response_wrapper(
            always_use_https.update,
        )
        self.get = to_raw_response_wrapper(
            always_use_https.get,
        )


class AsyncAlwaysUseHTTPSWithRawResponse:
    def __init__(self, always_use_https: AsyncAlwaysUseHTTPS) -> None:
        self._always_use_https = always_use_https

        self.update = async_to_raw_response_wrapper(
            always_use_https.update,
        )
        self.get = async_to_raw_response_wrapper(
            always_use_https.get,
        )


class AlwaysUseHTTPSWithStreamingResponse:
    def __init__(self, always_use_https: AlwaysUseHTTPS) -> None:
        self._always_use_https = always_use_https

        self.update = to_streamed_response_wrapper(
            always_use_https.update,
        )
        self.get = to_streamed_response_wrapper(
            always_use_https.get,
        )


class AsyncAlwaysUseHTTPSWithStreamingResponse:
    def __init__(self, always_use_https: AsyncAlwaysUseHTTPS) -> None:
        self._always_use_https = always_use_https

        self.update = async_to_streamed_response_wrapper(
            always_use_https.update,
        )
        self.get = async_to_streamed_response_wrapper(
            always_use_https.get,
        )
