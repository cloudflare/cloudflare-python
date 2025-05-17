# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ...._utils import maybe_transform
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
from ....types.radar.ai import to_markdown_create_params
from ....types.radar.ai.to_markdown_create_response import ToMarkdownCreateResponse

__all__ = ["ToMarkdownResource", "AsyncToMarkdownResource"]


class ToMarkdownResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToMarkdownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ToMarkdownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToMarkdownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ToMarkdownResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[ToMarkdownCreateResponse]:
        """
        Convert Files into Markdown

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai/tomarkdown",
            page=SyncSinglePage[ToMarkdownCreateResponse],
            body=maybe_transform(body, to_markdown_create_params.ToMarkdownCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ToMarkdownCreateResponse,
            method="post",
        )


class AsyncToMarkdownResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToMarkdownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToMarkdownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToMarkdownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncToMarkdownResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ToMarkdownCreateResponse, AsyncSinglePage[ToMarkdownCreateResponse]]:
        """
        Convert Files into Markdown

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/ai/tomarkdown",
            page=AsyncSinglePage[ToMarkdownCreateResponse],
            body=maybe_transform(body, to_markdown_create_params.ToMarkdownCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ToMarkdownCreateResponse,
            method="post",
        )


class ToMarkdownResourceWithRawResponse:
    def __init__(self, to_markdown: ToMarkdownResource) -> None:
        self._to_markdown = to_markdown

        self.create = to_raw_response_wrapper(
            to_markdown.create,
        )


class AsyncToMarkdownResourceWithRawResponse:
    def __init__(self, to_markdown: AsyncToMarkdownResource) -> None:
        self._to_markdown = to_markdown

        self.create = async_to_raw_response_wrapper(
            to_markdown.create,
        )


class ToMarkdownResourceWithStreamingResponse:
    def __init__(self, to_markdown: ToMarkdownResource) -> None:
        self._to_markdown = to_markdown

        self.create = to_streamed_response_wrapper(
            to_markdown.create,
        )


class AsyncToMarkdownResourceWithStreamingResponse:
    def __init__(self, to_markdown: AsyncToMarkdownResource) -> None:
        self._to_markdown = to_markdown

        self.create = async_to_streamed_response_wrapper(
            to_markdown.create,
        )
