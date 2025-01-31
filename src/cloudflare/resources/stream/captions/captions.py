# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from .language.language import (
    LanguageResource,
    AsyncLanguageResource,
    LanguageResourceWithRawResponse,
    AsyncLanguageResourceWithRawResponse,
    LanguageResourceWithStreamingResponse,
    AsyncLanguageResourceWithStreamingResponse,
)
from ....types.stream.caption import Caption

__all__ = ["CaptionsResource", "AsyncCaptionsResource"]


class CaptionsResource(SyncAPIResource):
    @cached_property
    def language(self) -> LanguageResource:
        return LanguageResource(self._client)

    @cached_property
    def with_raw_response(self) -> CaptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CaptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CaptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CaptionsResourceWithStreamingResponse(self)

    def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Caption]:
        """
        Lists the available captions or subtitles for a specific video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/stream/{identifier}/captions",
            page=SyncSinglePage[Caption],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Caption,
        )


class AsyncCaptionsResource(AsyncAPIResource):
    @cached_property
    def language(self) -> AsyncLanguageResource:
        return AsyncLanguageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCaptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCaptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCaptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCaptionsResourceWithStreamingResponse(self)

    def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Caption, AsyncSinglePage[Caption]]:
        """
        Lists the available captions or subtitles for a specific video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/stream/{identifier}/captions",
            page=AsyncSinglePage[Caption],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Caption,
        )


class CaptionsResourceWithRawResponse:
    def __init__(self, captions: CaptionsResource) -> None:
        self._captions = captions

        self.get = to_raw_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> LanguageResourceWithRawResponse:
        return LanguageResourceWithRawResponse(self._captions.language)


class AsyncCaptionsResourceWithRawResponse:
    def __init__(self, captions: AsyncCaptionsResource) -> None:
        self._captions = captions

        self.get = async_to_raw_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> AsyncLanguageResourceWithRawResponse:
        return AsyncLanguageResourceWithRawResponse(self._captions.language)


class CaptionsResourceWithStreamingResponse:
    def __init__(self, captions: CaptionsResource) -> None:
        self._captions = captions

        self.get = to_streamed_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> LanguageResourceWithStreamingResponse:
        return LanguageResourceWithStreamingResponse(self._captions.language)


class AsyncCaptionsResourceWithStreamingResponse:
    def __init__(self, captions: AsyncCaptionsResource) -> None:
        self._captions = captions

        self.get = async_to_streamed_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> AsyncLanguageResourceWithStreamingResponse:
        return AsyncLanguageResourceWithStreamingResponse(self._captions.language)
