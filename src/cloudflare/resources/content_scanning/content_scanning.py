# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .payloads import (
    PayloadsResource,
    AsyncPayloadsResource,
    PayloadsResourceWithRawResponse,
    AsyncPayloadsResourceWithRawResponse,
    PayloadsResourceWithStreamingResponse,
    AsyncPayloadsResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options

__all__ = ["ContentScanningResource", "AsyncContentScanningResource"]


class ContentScanningResource(SyncAPIResource):
    @cached_property
    def payloads(self) -> PayloadsResource:
        return PayloadsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContentScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ContentScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ContentScanningResourceWithStreamingResponse(self)

    def disable(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Disable Content Scanning

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/content-upload-scan/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def enable(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Enable Content Scanning

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/content-upload-scan/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncContentScanningResource(AsyncAPIResource):
    @cached_property
    def payloads(self) -> AsyncPayloadsResource:
        return AsyncPayloadsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContentScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncContentScanningResourceWithStreamingResponse(self)

    async def disable(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Disable Content Scanning

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/content-upload-scan/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def enable(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Enable Content Scanning

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/content-upload-scan/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class ContentScanningResourceWithRawResponse:
    def __init__(self, content_scanning: ContentScanningResource) -> None:
        self._content_scanning = content_scanning

        self.disable = to_raw_response_wrapper(
            content_scanning.disable,
        )
        self.enable = to_raw_response_wrapper(
            content_scanning.enable,
        )

    @cached_property
    def payloads(self) -> PayloadsResourceWithRawResponse:
        return PayloadsResourceWithRawResponse(self._content_scanning.payloads)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._content_scanning.settings)


class AsyncContentScanningResourceWithRawResponse:
    def __init__(self, content_scanning: AsyncContentScanningResource) -> None:
        self._content_scanning = content_scanning

        self.disable = async_to_raw_response_wrapper(
            content_scanning.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            content_scanning.enable,
        )

    @cached_property
    def payloads(self) -> AsyncPayloadsResourceWithRawResponse:
        return AsyncPayloadsResourceWithRawResponse(self._content_scanning.payloads)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._content_scanning.settings)


class ContentScanningResourceWithStreamingResponse:
    def __init__(self, content_scanning: ContentScanningResource) -> None:
        self._content_scanning = content_scanning

        self.disable = to_streamed_response_wrapper(
            content_scanning.disable,
        )
        self.enable = to_streamed_response_wrapper(
            content_scanning.enable,
        )

    @cached_property
    def payloads(self) -> PayloadsResourceWithStreamingResponse:
        return PayloadsResourceWithStreamingResponse(self._content_scanning.payloads)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._content_scanning.settings)


class AsyncContentScanningResourceWithStreamingResponse:
    def __init__(self, content_scanning: AsyncContentScanningResource) -> None:
        self._content_scanning = content_scanning

        self.disable = async_to_streamed_response_wrapper(
            content_scanning.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            content_scanning.enable,
        )

    @cached_property
    def payloads(self) -> AsyncPayloadsResourceWithStreamingResponse:
        return AsyncPayloadsResourceWithStreamingResponse(self._content_scanning.payloads)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._content_scanning.settings)
