# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.url_scanner import screenshot_get_params

__all__ = ["ScreenshotResource", "AsyncScreenshotResource"]


class ScreenshotResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScreenshotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ScreenshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenshotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ScreenshotResourceWithStreamingResponse(self)

    def get(
        self,
        scan_id: str,
        *,
        account_id: str,
        resolution: Literal["desktop", "mobile", "tablet"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Get scan's screenshot by resolution (desktop/mobile/tablet).

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          resolution: Target device type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/urlscanner/v2/screenshots/{scan_id}.png",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"resolution": resolution}, screenshot_get_params.ScreenshotGetParams),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncScreenshotResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScreenshotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenshotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenshotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncScreenshotResourceWithStreamingResponse(self)

    async def get(
        self,
        scan_id: str,
        *,
        account_id: str,
        resolution: Literal["desktop", "mobile", "tablet"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Get scan's screenshot by resolution (desktop/mobile/tablet).

        Args:
          account_id: Account Id.

          scan_id: Scan uuid.

          resolution: Target device type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        extra_headers = {"Accept": "image/png", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/urlscanner/v2/screenshots/{scan_id}.png",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"resolution": resolution}, screenshot_get_params.ScreenshotGetParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ScreenshotResourceWithRawResponse:
    def __init__(self, screenshot: ScreenshotResource) -> None:
        self._screenshot = screenshot

        self.get = to_custom_raw_response_wrapper(
            screenshot.get,
            BinaryAPIResponse,
        )


class AsyncScreenshotResourceWithRawResponse:
    def __init__(self, screenshot: AsyncScreenshotResource) -> None:
        self._screenshot = screenshot

        self.get = async_to_custom_raw_response_wrapper(
            screenshot.get,
            AsyncBinaryAPIResponse,
        )


class ScreenshotResourceWithStreamingResponse:
    def __init__(self, screenshot: ScreenshotResource) -> None:
        self._screenshot = screenshot

        self.get = to_custom_streamed_response_wrapper(
            screenshot.get,
            StreamedBinaryAPIResponse,
        )


class AsyncScreenshotResourceWithStreamingResponse:
    def __init__(self, screenshot: AsyncScreenshotResource) -> None:
        self._screenshot = screenshot

        self.get = async_to_custom_streamed_response_wrapper(
            screenshot.get,
            AsyncStreamedBinaryAPIResponse,
        )
