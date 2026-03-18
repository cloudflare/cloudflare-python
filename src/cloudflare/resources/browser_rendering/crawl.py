# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Type, Iterable, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
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
from ...types.browser_rendering import crawl_get_params, crawl_create_params
from ...types.browser_rendering.crawl_get_response import CrawlGetResponse
from ...types.browser_rendering.crawl_create_response import CrawlCreateResponse
from ...types.browser_rendering.crawl_delete_response import CrawlDeleteResponse

__all__ = ["CrawlResource", "AsyncCrawlResource"]


class CrawlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CrawlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CrawlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CrawlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CrawlResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        url: str,
        cache_ttl: float | Omit = omit,
        action_timeout: float | Omit = omit,
        add_script_tag: Iterable[crawl_create_params.Variant0AddScriptTag] | Omit = omit,
        add_style_tag: Iterable[crawl_create_params.Variant0AddStyleTag] | Omit = omit,
        allow_request_pattern: SequenceNotStr[str] | Omit = omit,
        allow_resource_types: List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ]
        | Omit = omit,
        authenticate: crawl_create_params.Variant0Authenticate | Omit = omit,
        best_attempt: bool | Omit = omit,
        cookies: Iterable[crawl_create_params.Variant0Cookie] | Omit = omit,
        crawl_purposes: List[Literal["search", "ai-input", "ai-train"]] | Omit = omit,
        depth: float | Omit = omit,
        emulate_media_type: str | Omit = omit,
        formats: List[Literal["html", "markdown", "json"]] | Omit = omit,
        goto_options: crawl_create_params.Variant0GotoOptions | Omit = omit,
        json_options: crawl_create_params.Variant0JsonOptions | Omit = omit,
        limit: float | Omit = omit,
        max_age: float | Omit = omit,
        modified_since: int | Omit = omit,
        options: crawl_create_params.Variant0Options | Omit = omit,
        reject_request_pattern: SequenceNotStr[str] | Omit = omit,
        reject_resource_types: List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ]
        | Omit = omit,
        render: Literal[True] | Omit = omit,
        set_extra_http_headers: Dict[str, str] | Omit = omit,
        set_java_script_enabled: bool | Omit = omit,
        source: Literal["sitemaps", "links", "all"] | Omit = omit,
        viewport: crawl_create_params.Variant0Viewport | Omit = omit,
        wait_for_selector: crawl_create_params.Variant0WaitForSelector | Omit = omit,
        wait_for_timeout: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Starts a crawl job for the provided URL and its children.

        Check available
        options like `gotoOptions` and `waitFor*` to control page load behaviour.

        Args:
          account_id: Account ID.

          url: URL to navigate to, eg. `https://example.com`.

          cache_ttl: Cache TTL default is 5s. Set to 0 to disable.

          action_timeout: The maximum duration allowed for the browser action to complete after the page
              has loaded (such as taking screenshots, extracting content, or generating PDFs).
              If this time limit is exceeded, the action stops and returns a timeout error.

          add_script_tag: Adds a `<script>` tag into the page with the desired URL or content.

          add_style_tag: Adds a `<link rel="stylesheet">` tag into the page with the desired URL or a
              `<style type="text/css">` tag with the content.

          allow_request_pattern: Only allow requests that match the provided regex patterns, eg. '/^.\\**\\..(css)'.

          allow_resource_types: Only allow requests that match the provided resource types, eg. 'image' or
              'script'.

          authenticate: Provide credentials for HTTP authentication.

          best_attempt: Attempt to proceed when 'awaited' events fail or timeout.

          cookies: Check [options](https://pptr.dev/api/puppeteer.page.setcookie).

          crawl_purposes: List of crawl purposes to respect Content-Signal directives in robots.txt.
              Allowed values: 'search', 'ai-input', 'ai-train'. Learn more:
              https://contentsignals.org/. Default: ['search', 'ai-input', 'ai-train'].

          depth: Maximum number of levels deep the crawler will traverse from the starting URL.

          formats: Formats to return. Default is `html`.

          goto_options: Check [options](https://pptr.dev/api/puppeteer.gotooptions).

          json_options: Options for JSON extraction.

          limit: Maximum number of URLs to crawl.

          max_age: Maximum age of a resource that can be returned from cache in seconds. Default is
              1 day.

          modified_since: Unix timestamp (seconds since epoch) indicating to only crawl pages that were
              modified since this time. For sitemap URLs with a lastmod field, this is
              compared directly. For other URLs, the crawler will use If-Modified-Since header
              when fetching. URLs without modification information (no lastmod in sitemap and
              no Last-Modified header support) will be crawled. Note: This works in
              conjunction with maxAge - both filters must pass for a cached resource to be
              used. Must be within the last year and not in the future.

          options: Additional options for the crawler.

          reject_request_pattern: Block undesired requests that match the provided regex patterns, eg.
              '/^.\\**\\..(css)'.

          reject_resource_types: Block undesired requests that match the provided resource types, eg. 'image' or
              'script'.

          render: Whether to render the page or fetch static content. True by default.

          source: Source of links to crawl. 'sitemaps' - only crawl URLs from sitemaps, 'links' -
              only crawl URLs scraped from pages, 'all' - crawl both sitemap and scraped links
              (default).

          viewport: Check [options](https://pptr.dev/api/puppeteer.page.setviewport).

          wait_for_selector: Wait for the selector to appear in page. Check
              [options](https://pptr.dev/api/puppeteer.page.waitforselector).

          wait_for_timeout: Waits for a specified timeout before continuing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        render: Literal[False],
        url: str,
        cache_ttl: float | Omit = omit,
        crawl_purposes: List[Literal["search", "ai-input", "ai-train"]] | Omit = omit,
        depth: float | Omit = omit,
        formats: List[Literal["html", "markdown", "json"]] | Omit = omit,
        json_options: crawl_create_params.Variant1JsonOptions | Omit = omit,
        limit: float | Omit = omit,
        max_age: float | Omit = omit,
        modified_since: int | Omit = omit,
        options: crawl_create_params.Variant1Options | Omit = omit,
        source: Literal["sitemaps", "links", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Starts a crawl job for the provided URL and its children.

        Check available
        options like `gotoOptions` and `waitFor*` to control page load behaviour.

        Args:
          account_id: Account ID.

          render: Whether to render the page or fetch static content. True by default.

          url: URL to navigate to, eg. `https://example.com`.

          cache_ttl: Cache TTL default is 5s. Set to 0 to disable.

          crawl_purposes: List of crawl purposes to respect Content-Signal directives in robots.txt.
              Allowed values: 'search', 'ai-input', 'ai-train'. Learn more:
              https://contentsignals.org/. Default: ['search', 'ai-input', 'ai-train'].

          depth: Maximum number of levels deep the crawler will traverse from the starting URL.

          formats: Formats to return. Default is `html`.

          json_options: Options for JSON extraction.

          limit: Maximum number of URLs to crawl.

          max_age: Maximum age of a resource that can be returned from cache in seconds. Default is
              1 day.

          modified_since: Unix timestamp (seconds since epoch) indicating to only crawl pages that were
              modified since this time. For sitemap URLs with a lastmod field, this is
              compared directly. For other URLs, the crawler will use If-Modified-Since header
              when fetching. URLs without modification information (no lastmod in sitemap and
              no Last-Modified header support) will be crawled. Note: This works in
              conjunction with maxAge - both filters must pass for a cached resource to be
              used. Must be within the last year and not in the future.

          options: Additional options for the crawler.

          source: Source of links to crawl. 'sitemaps' - only crawl URLs from sitemaps, 'links' -
              only crawl URLs scraped from pages, 'all' - crawl both sitemap and scraped links
              (default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "url"], ["account_id", "render", "url"])
    def create(
        self,
        *,
        account_id: str,
        url: str,
        cache_ttl: float | Omit = omit,
        action_timeout: float | Omit = omit,
        add_script_tag: Iterable[crawl_create_params.Variant0AddScriptTag] | Omit = omit,
        add_style_tag: Iterable[crawl_create_params.Variant0AddStyleTag] | Omit = omit,
        allow_request_pattern: SequenceNotStr[str] | Omit = omit,
        allow_resource_types: List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ]
        | Omit = omit,
        authenticate: crawl_create_params.Variant0Authenticate | Omit = omit,
        best_attempt: bool | Omit = omit,
        cookies: Iterable[crawl_create_params.Variant0Cookie] | Omit = omit,
        crawl_purposes: List[Literal["search", "ai-input", "ai-train"]] | Omit = omit,
        depth: float | Omit = omit,
        emulate_media_type: str | Omit = omit,
        formats: List[Literal["html", "markdown", "json"]] | Omit = omit,
        goto_options: crawl_create_params.Variant0GotoOptions | Omit = omit,
        json_options: crawl_create_params.Variant0JsonOptions | crawl_create_params.Variant1JsonOptions | Omit = omit,
        limit: float | Omit = omit,
        max_age: float | Omit = omit,
        modified_since: int | Omit = omit,
        options: crawl_create_params.Variant0Options | crawl_create_params.Variant1Options | Omit = omit,
        reject_request_pattern: SequenceNotStr[str] | Omit = omit,
        reject_resource_types: List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ]
        | Omit = omit,
        render: Literal[True] | Literal[False] | Omit = omit,
        set_extra_http_headers: Dict[str, str] | Omit = omit,
        set_java_script_enabled: bool | Omit = omit,
        source: Literal["sitemaps", "links", "all"] | Omit = omit,
        viewport: crawl_create_params.Variant0Viewport | Omit = omit,
        wait_for_selector: crawl_create_params.Variant0WaitForSelector | Omit = omit,
        wait_for_timeout: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/browser-rendering/crawl",
            body=maybe_transform(
                {
                    "url": url,
                    "action_timeout": action_timeout,
                    "add_script_tag": add_script_tag,
                    "add_style_tag": add_style_tag,
                    "allow_request_pattern": allow_request_pattern,
                    "allow_resource_types": allow_resource_types,
                    "authenticate": authenticate,
                    "best_attempt": best_attempt,
                    "cookies": cookies,
                    "crawl_purposes": crawl_purposes,
                    "depth": depth,
                    "emulate_media_type": emulate_media_type,
                    "formats": formats,
                    "goto_options": goto_options,
                    "json_options": json_options,
                    "limit": limit,
                    "max_age": max_age,
                    "modified_since": modified_since,
                    "options": options,
                    "reject_request_pattern": reject_request_pattern,
                    "reject_resource_types": reject_resource_types,
                    "render": render,
                    "set_extra_http_headers": set_extra_http_headers,
                    "set_java_script_enabled": set_java_script_enabled,
                    "source": source,
                    "viewport": viewport,
                    "wait_for_selector": wait_for_selector,
                    "wait_for_timeout": wait_for_timeout,
                },
                crawl_create_params.CrawlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cache_ttl": cache_ttl}, crawl_create_params.CrawlCreateParams),
                post_parser=ResultWrapper[CrawlCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def delete(
        self,
        job_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlDeleteResponse:
        """
        Cancels an ongoing crawl job by setting its status to cancelled and stopping all
        queued URLs.

        Args:
          account_id: Account ID.

          job_id: The ID of the crawl job to cancel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/accounts/{account_id}/browser-rendering/crawl/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CrawlDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CrawlDeleteResponse], ResultWrapper[CrawlDeleteResponse]),
        )

    def get(
        self,
        job_id: str,
        *,
        account_id: str,
        cache_ttl: float | Omit = omit,
        cursor: float | Omit = omit,
        limit: float | Omit = omit,
        status: Literal["queued", "errored", "completed", "disallowed", "skipped", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlGetResponse:
        """
        Returns the result of a crawl job.

        Args:
          account_id: Account ID.

          job_id: Crawl job ID.

          cache_ttl: Cache TTL default is 5s. Set to 0 to disable.

          cursor: Cursor for pagination.

          limit: Limit for pagination.

          status: Filter by URL status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/accounts/{account_id}/browser-rendering/crawl/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cache_ttl": cache_ttl,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    crawl_get_params.CrawlGetParams,
                ),
                post_parser=ResultWrapper[CrawlGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CrawlGetResponse], ResultWrapper[CrawlGetResponse]),
        )


class AsyncCrawlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCrawlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCrawlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCrawlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCrawlResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        url: str,
        cache_ttl: float | Omit = omit,
        action_timeout: float | Omit = omit,
        add_script_tag: Iterable[crawl_create_params.Variant0AddScriptTag] | Omit = omit,
        add_style_tag: Iterable[crawl_create_params.Variant0AddStyleTag] | Omit = omit,
        allow_request_pattern: SequenceNotStr[str] | Omit = omit,
        allow_resource_types: List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ]
        | Omit = omit,
        authenticate: crawl_create_params.Variant0Authenticate | Omit = omit,
        best_attempt: bool | Omit = omit,
        cookies: Iterable[crawl_create_params.Variant0Cookie] | Omit = omit,
        crawl_purposes: List[Literal["search", "ai-input", "ai-train"]] | Omit = omit,
        depth: float | Omit = omit,
        emulate_media_type: str | Omit = omit,
        formats: List[Literal["html", "markdown", "json"]] | Omit = omit,
        goto_options: crawl_create_params.Variant0GotoOptions | Omit = omit,
        json_options: crawl_create_params.Variant0JsonOptions | Omit = omit,
        limit: float | Omit = omit,
        max_age: float | Omit = omit,
        modified_since: int | Omit = omit,
        options: crawl_create_params.Variant0Options | Omit = omit,
        reject_request_pattern: SequenceNotStr[str] | Omit = omit,
        reject_resource_types: List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ]
        | Omit = omit,
        render: Literal[True] | Omit = omit,
        set_extra_http_headers: Dict[str, str] | Omit = omit,
        set_java_script_enabled: bool | Omit = omit,
        source: Literal["sitemaps", "links", "all"] | Omit = omit,
        viewport: crawl_create_params.Variant0Viewport | Omit = omit,
        wait_for_selector: crawl_create_params.Variant0WaitForSelector | Omit = omit,
        wait_for_timeout: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Starts a crawl job for the provided URL and its children.

        Check available
        options like `gotoOptions` and `waitFor*` to control page load behaviour.

        Args:
          account_id: Account ID.

          url: URL to navigate to, eg. `https://example.com`.

          cache_ttl: Cache TTL default is 5s. Set to 0 to disable.

          action_timeout: The maximum duration allowed for the browser action to complete after the page
              has loaded (such as taking screenshots, extracting content, or generating PDFs).
              If this time limit is exceeded, the action stops and returns a timeout error.

          add_script_tag: Adds a `<script>` tag into the page with the desired URL or content.

          add_style_tag: Adds a `<link rel="stylesheet">` tag into the page with the desired URL or a
              `<style type="text/css">` tag with the content.

          allow_request_pattern: Only allow requests that match the provided regex patterns, eg. '/^.\\**\\..(css)'.

          allow_resource_types: Only allow requests that match the provided resource types, eg. 'image' or
              'script'.

          authenticate: Provide credentials for HTTP authentication.

          best_attempt: Attempt to proceed when 'awaited' events fail or timeout.

          cookies: Check [options](https://pptr.dev/api/puppeteer.page.setcookie).

          crawl_purposes: List of crawl purposes to respect Content-Signal directives in robots.txt.
              Allowed values: 'search', 'ai-input', 'ai-train'. Learn more:
              https://contentsignals.org/. Default: ['search', 'ai-input', 'ai-train'].

          depth: Maximum number of levels deep the crawler will traverse from the starting URL.

          formats: Formats to return. Default is `html`.

          goto_options: Check [options](https://pptr.dev/api/puppeteer.gotooptions).

          json_options: Options for JSON extraction.

          limit: Maximum number of URLs to crawl.

          max_age: Maximum age of a resource that can be returned from cache in seconds. Default is
              1 day.

          modified_since: Unix timestamp (seconds since epoch) indicating to only crawl pages that were
              modified since this time. For sitemap URLs with a lastmod field, this is
              compared directly. For other URLs, the crawler will use If-Modified-Since header
              when fetching. URLs without modification information (no lastmod in sitemap and
              no Last-Modified header support) will be crawled. Note: This works in
              conjunction with maxAge - both filters must pass for a cached resource to be
              used. Must be within the last year and not in the future.

          options: Additional options for the crawler.

          reject_request_pattern: Block undesired requests that match the provided regex patterns, eg.
              '/^.\\**\\..(css)'.

          reject_resource_types: Block undesired requests that match the provided resource types, eg. 'image' or
              'script'.

          render: Whether to render the page or fetch static content. True by default.

          source: Source of links to crawl. 'sitemaps' - only crawl URLs from sitemaps, 'links' -
              only crawl URLs scraped from pages, 'all' - crawl both sitemap and scraped links
              (default).

          viewport: Check [options](https://pptr.dev/api/puppeteer.page.setviewport).

          wait_for_selector: Wait for the selector to appear in page. Check
              [options](https://pptr.dev/api/puppeteer.page.waitforselector).

          wait_for_timeout: Waits for a specified timeout before continuing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        render: Literal[False],
        url: str,
        cache_ttl: float | Omit = omit,
        crawl_purposes: List[Literal["search", "ai-input", "ai-train"]] | Omit = omit,
        depth: float | Omit = omit,
        formats: List[Literal["html", "markdown", "json"]] | Omit = omit,
        json_options: crawl_create_params.Variant1JsonOptions | Omit = omit,
        limit: float | Omit = omit,
        max_age: float | Omit = omit,
        modified_since: int | Omit = omit,
        options: crawl_create_params.Variant1Options | Omit = omit,
        source: Literal["sitemaps", "links", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Starts a crawl job for the provided URL and its children.

        Check available
        options like `gotoOptions` and `waitFor*` to control page load behaviour.

        Args:
          account_id: Account ID.

          render: Whether to render the page or fetch static content. True by default.

          url: URL to navigate to, eg. `https://example.com`.

          cache_ttl: Cache TTL default is 5s. Set to 0 to disable.

          crawl_purposes: List of crawl purposes to respect Content-Signal directives in robots.txt.
              Allowed values: 'search', 'ai-input', 'ai-train'. Learn more:
              https://contentsignals.org/. Default: ['search', 'ai-input', 'ai-train'].

          depth: Maximum number of levels deep the crawler will traverse from the starting URL.

          formats: Formats to return. Default is `html`.

          json_options: Options for JSON extraction.

          limit: Maximum number of URLs to crawl.

          max_age: Maximum age of a resource that can be returned from cache in seconds. Default is
              1 day.

          modified_since: Unix timestamp (seconds since epoch) indicating to only crawl pages that were
              modified since this time. For sitemap URLs with a lastmod field, this is
              compared directly. For other URLs, the crawler will use If-Modified-Since header
              when fetching. URLs without modification information (no lastmod in sitemap and
              no Last-Modified header support) will be crawled. Note: This works in
              conjunction with maxAge - both filters must pass for a cached resource to be
              used. Must be within the last year and not in the future.

          options: Additional options for the crawler.

          source: Source of links to crawl. 'sitemaps' - only crawl URLs from sitemaps, 'links' -
              only crawl URLs scraped from pages, 'all' - crawl both sitemap and scraped links
              (default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "url"], ["account_id", "render", "url"])
    async def create(
        self,
        *,
        account_id: str,
        url: str,
        cache_ttl: float | Omit = omit,
        action_timeout: float | Omit = omit,
        add_script_tag: Iterable[crawl_create_params.Variant0AddScriptTag] | Omit = omit,
        add_style_tag: Iterable[crawl_create_params.Variant0AddStyleTag] | Omit = omit,
        allow_request_pattern: SequenceNotStr[str] | Omit = omit,
        allow_resource_types: List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ]
        | Omit = omit,
        authenticate: crawl_create_params.Variant0Authenticate | Omit = omit,
        best_attempt: bool | Omit = omit,
        cookies: Iterable[crawl_create_params.Variant0Cookie] | Omit = omit,
        crawl_purposes: List[Literal["search", "ai-input", "ai-train"]] | Omit = omit,
        depth: float | Omit = omit,
        emulate_media_type: str | Omit = omit,
        formats: List[Literal["html", "markdown", "json"]] | Omit = omit,
        goto_options: crawl_create_params.Variant0GotoOptions | Omit = omit,
        json_options: crawl_create_params.Variant0JsonOptions | crawl_create_params.Variant1JsonOptions | Omit = omit,
        limit: float | Omit = omit,
        max_age: float | Omit = omit,
        modified_since: int | Omit = omit,
        options: crawl_create_params.Variant0Options | crawl_create_params.Variant1Options | Omit = omit,
        reject_request_pattern: SequenceNotStr[str] | Omit = omit,
        reject_resource_types: List[
            Literal[
                "document",
                "stylesheet",
                "image",
                "media",
                "font",
                "script",
                "texttrack",
                "xhr",
                "fetch",
                "prefetch",
                "eventsource",
                "websocket",
                "manifest",
                "signedexchange",
                "ping",
                "cspviolationreport",
                "preflight",
                "other",
            ]
        ]
        | Omit = omit,
        render: Literal[True] | Literal[False] | Omit = omit,
        set_extra_http_headers: Dict[str, str] | Omit = omit,
        set_java_script_enabled: bool | Omit = omit,
        source: Literal["sitemaps", "links", "all"] | Omit = omit,
        viewport: crawl_create_params.Variant0Viewport | Omit = omit,
        wait_for_selector: crawl_create_params.Variant0WaitForSelector | Omit = omit,
        wait_for_timeout: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/browser-rendering/crawl",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "action_timeout": action_timeout,
                    "add_script_tag": add_script_tag,
                    "add_style_tag": add_style_tag,
                    "allow_request_pattern": allow_request_pattern,
                    "allow_resource_types": allow_resource_types,
                    "authenticate": authenticate,
                    "best_attempt": best_attempt,
                    "cookies": cookies,
                    "crawl_purposes": crawl_purposes,
                    "depth": depth,
                    "emulate_media_type": emulate_media_type,
                    "formats": formats,
                    "goto_options": goto_options,
                    "json_options": json_options,
                    "limit": limit,
                    "max_age": max_age,
                    "modified_since": modified_since,
                    "options": options,
                    "reject_request_pattern": reject_request_pattern,
                    "reject_resource_types": reject_resource_types,
                    "render": render,
                    "set_extra_http_headers": set_extra_http_headers,
                    "set_java_script_enabled": set_java_script_enabled,
                    "source": source,
                    "viewport": viewport,
                    "wait_for_selector": wait_for_selector,
                    "wait_for_timeout": wait_for_timeout,
                },
                crawl_create_params.CrawlCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cache_ttl": cache_ttl}, crawl_create_params.CrawlCreateParams),
                post_parser=ResultWrapper[CrawlCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def delete(
        self,
        job_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlDeleteResponse:
        """
        Cancels an ongoing crawl job by setting its status to cancelled and stopping all
        queued URLs.

        Args:
          account_id: Account ID.

          job_id: The ID of the crawl job to cancel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/browser-rendering/crawl/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[CrawlDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[CrawlDeleteResponse], ResultWrapper[CrawlDeleteResponse]),
        )

    async def get(
        self,
        job_id: str,
        *,
        account_id: str,
        cache_ttl: float | Omit = omit,
        cursor: float | Omit = omit,
        limit: float | Omit = omit,
        status: Literal["queued", "errored", "completed", "disallowed", "skipped", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CrawlGetResponse:
        """
        Returns the result of a crawl job.

        Args:
          account_id: Account ID.

          job_id: Crawl job ID.

          cache_ttl: Cache TTL default is 5s. Set to 0 to disable.

          cursor: Cursor for pagination.

          limit: Limit for pagination.

          status: Filter by URL status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/accounts/{account_id}/browser-rendering/crawl/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cache_ttl": cache_ttl,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    crawl_get_params.CrawlGetParams,
                ),
                post_parser=ResultWrapper[CrawlGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[CrawlGetResponse], ResultWrapper[CrawlGetResponse]),
        )


class CrawlResourceWithRawResponse:
    def __init__(self, crawl: CrawlResource) -> None:
        self._crawl = crawl

        self.create = to_raw_response_wrapper(
            crawl.create,
        )
        self.delete = to_raw_response_wrapper(
            crawl.delete,
        )
        self.get = to_raw_response_wrapper(
            crawl.get,
        )


class AsyncCrawlResourceWithRawResponse:
    def __init__(self, crawl: AsyncCrawlResource) -> None:
        self._crawl = crawl

        self.create = async_to_raw_response_wrapper(
            crawl.create,
        )
        self.delete = async_to_raw_response_wrapper(
            crawl.delete,
        )
        self.get = async_to_raw_response_wrapper(
            crawl.get,
        )


class CrawlResourceWithStreamingResponse:
    def __init__(self, crawl: CrawlResource) -> None:
        self._crawl = crawl

        self.create = to_streamed_response_wrapper(
            crawl.create,
        )
        self.delete = to_streamed_response_wrapper(
            crawl.delete,
        )
        self.get = to_streamed_response_wrapper(
            crawl.get,
        )


class AsyncCrawlResourceWithStreamingResponse:
    def __init__(self, crawl: AsyncCrawlResource) -> None:
        self._crawl = crawl

        self.create = async_to_streamed_response_wrapper(
            crawl.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            crawl.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            crawl.get,
        )
