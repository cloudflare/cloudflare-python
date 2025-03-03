# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Type, Iterable, cast
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
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.browser_rendering import scrape_create_params
from ...types.browser_rendering.scrape_create_response import ScrapeCreateResponse

__all__ = ["ScrapeResource", "AsyncScrapeResource"]


class ScrapeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScrapeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ScrapeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScrapeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ScrapeResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        elements: Iterable[scrape_create_params.Element],
        cache_ttl: float | NotGiven = NOT_GIVEN,
        add_script_tag: Iterable[scrape_create_params.AddScriptTag] | NotGiven = NOT_GIVEN,
        add_style_tag: Iterable[scrape_create_params.AddStyleTag] | NotGiven = NOT_GIVEN,
        allow_request_pattern: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        authenticate: scrape_create_params.Authenticate | NotGiven = NOT_GIVEN,
        best_attempt: bool | NotGiven = NOT_GIVEN,
        cookies: Iterable[scrape_create_params.Cookie] | NotGiven = NOT_GIVEN,
        emulate_media_type: str | NotGiven = NOT_GIVEN,
        goto_options: scrape_create_params.GotoOptions | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        reject_request_pattern: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        set_extra_http_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        set_java_script_enabled: bool | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        user_agent: str | NotGiven = NOT_GIVEN,
        viewport: scrape_create_params.Viewport | NotGiven = NOT_GIVEN,
        wait_for_selector: scrape_create_params.WaitForSelector | NotGiven = NOT_GIVEN,
        wait_for_timeout: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScrapeCreateResponse:
        """
        Get meta attributes like height, width, text and others of selected elements.

        Args:
          account_id: Account ID.

          cache_ttl: Cache TTL default is 5s. Set to 0 to disable.

          add_script_tag: Adds a `<script>` tag into the page with the desired URL or content.

          add_style_tag: Adds a `<link rel="stylesheet">` tag into the page with the desired URL or a
              `<style type="text/css">` tag with the content.

          allow_request_pattern: Only allow requests that match the provided regex patterns, eg. '/^.\\**\\..(css)'.

          allow_resource_types: Only allow requests that match the provided resource types, eg. 'image' or
              'script'.

          authenticate: Provide credentials for HTTP authentication.

          best_attempt: Attempt to proceed when 'awaited' events fail or timeout.

          cookies: Check [options](https://pptr.dev/api/puppeteer.page.setcookie).

          goto_options: Check [options](https://pptr.dev/api/puppeteer.gotooptions).

          html: Set the content of the page, eg: `<h1>Hello World!!</h1>`. Either `html` or
              `url` must be set.

          reject_request_pattern: Block undesired requests that match the provided regex patterns, eg.
              '/^.\\**\\..(css)'.

          reject_resource_types: Block undesired requests that match the provided resource types, eg. 'image' or
              'script'.

          url: URL to navigate to, eg. `https://example.com`.

          viewport: Check [options](https://pptr.dev/api/puppeteer.page.setviewport).

          wait_for_selector: Wait for the selector to appear in page. Check
              [options](https://pptr.dev/api/puppeteer.page.waitforselector).

          wait_for_timeout: Waits for a specified timeout before continuing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/browser-rendering/scrape",
            body=maybe_transform(
                {
                    "elements": elements,
                    "add_script_tag": add_script_tag,
                    "add_style_tag": add_style_tag,
                    "allow_request_pattern": allow_request_pattern,
                    "allow_resource_types": allow_resource_types,
                    "authenticate": authenticate,
                    "best_attempt": best_attempt,
                    "cookies": cookies,
                    "emulate_media_type": emulate_media_type,
                    "goto_options": goto_options,
                    "html": html,
                    "reject_request_pattern": reject_request_pattern,
                    "reject_resource_types": reject_resource_types,
                    "set_extra_http_headers": set_extra_http_headers,
                    "set_java_script_enabled": set_java_script_enabled,
                    "url": url,
                    "user_agent": user_agent,
                    "viewport": viewport,
                    "wait_for_selector": wait_for_selector,
                    "wait_for_timeout": wait_for_timeout,
                },
                scrape_create_params.ScrapeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cache_ttl": cache_ttl}, scrape_create_params.ScrapeCreateParams),
                post_parser=ResultWrapper[ScrapeCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScrapeCreateResponse], ResultWrapper[ScrapeCreateResponse]),
        )


class AsyncScrapeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScrapeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScrapeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScrapeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncScrapeResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        elements: Iterable[scrape_create_params.Element],
        cache_ttl: float | NotGiven = NOT_GIVEN,
        add_script_tag: Iterable[scrape_create_params.AddScriptTag] | NotGiven = NOT_GIVEN,
        add_style_tag: Iterable[scrape_create_params.AddStyleTag] | NotGiven = NOT_GIVEN,
        allow_request_pattern: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        authenticate: scrape_create_params.Authenticate | NotGiven = NOT_GIVEN,
        best_attempt: bool | NotGiven = NOT_GIVEN,
        cookies: Iterable[scrape_create_params.Cookie] | NotGiven = NOT_GIVEN,
        emulate_media_type: str | NotGiven = NOT_GIVEN,
        goto_options: scrape_create_params.GotoOptions | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        reject_request_pattern: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        set_extra_http_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        set_java_script_enabled: bool | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        user_agent: str | NotGiven = NOT_GIVEN,
        viewport: scrape_create_params.Viewport | NotGiven = NOT_GIVEN,
        wait_for_selector: scrape_create_params.WaitForSelector | NotGiven = NOT_GIVEN,
        wait_for_timeout: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScrapeCreateResponse:
        """
        Get meta attributes like height, width, text and others of selected elements.

        Args:
          account_id: Account ID.

          cache_ttl: Cache TTL default is 5s. Set to 0 to disable.

          add_script_tag: Adds a `<script>` tag into the page with the desired URL or content.

          add_style_tag: Adds a `<link rel="stylesheet">` tag into the page with the desired URL or a
              `<style type="text/css">` tag with the content.

          allow_request_pattern: Only allow requests that match the provided regex patterns, eg. '/^.\\**\\..(css)'.

          allow_resource_types: Only allow requests that match the provided resource types, eg. 'image' or
              'script'.

          authenticate: Provide credentials for HTTP authentication.

          best_attempt: Attempt to proceed when 'awaited' events fail or timeout.

          cookies: Check [options](https://pptr.dev/api/puppeteer.page.setcookie).

          goto_options: Check [options](https://pptr.dev/api/puppeteer.gotooptions).

          html: Set the content of the page, eg: `<h1>Hello World!!</h1>`. Either `html` or
              `url` must be set.

          reject_request_pattern: Block undesired requests that match the provided regex patterns, eg.
              '/^.\\**\\..(css)'.

          reject_resource_types: Block undesired requests that match the provided resource types, eg. 'image' or
              'script'.

          url: URL to navigate to, eg. `https://example.com`.

          viewport: Check [options](https://pptr.dev/api/puppeteer.page.setviewport).

          wait_for_selector: Wait for the selector to appear in page. Check
              [options](https://pptr.dev/api/puppeteer.page.waitforselector).

          wait_for_timeout: Waits for a specified timeout before continuing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/browser-rendering/scrape",
            body=await async_maybe_transform(
                {
                    "elements": elements,
                    "add_script_tag": add_script_tag,
                    "add_style_tag": add_style_tag,
                    "allow_request_pattern": allow_request_pattern,
                    "allow_resource_types": allow_resource_types,
                    "authenticate": authenticate,
                    "best_attempt": best_attempt,
                    "cookies": cookies,
                    "emulate_media_type": emulate_media_type,
                    "goto_options": goto_options,
                    "html": html,
                    "reject_request_pattern": reject_request_pattern,
                    "reject_resource_types": reject_resource_types,
                    "set_extra_http_headers": set_extra_http_headers,
                    "set_java_script_enabled": set_java_script_enabled,
                    "url": url,
                    "user_agent": user_agent,
                    "viewport": viewport,
                    "wait_for_selector": wait_for_selector,
                    "wait_for_timeout": wait_for_timeout,
                },
                scrape_create_params.ScrapeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cache_ttl": cache_ttl}, scrape_create_params.ScrapeCreateParams),
                post_parser=ResultWrapper[ScrapeCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ScrapeCreateResponse], ResultWrapper[ScrapeCreateResponse]),
        )


class ScrapeResourceWithRawResponse:
    def __init__(self, scrape: ScrapeResource) -> None:
        self._scrape = scrape

        self.create = to_raw_response_wrapper(
            scrape.create,
        )


class AsyncScrapeResourceWithRawResponse:
    def __init__(self, scrape: AsyncScrapeResource) -> None:
        self._scrape = scrape

        self.create = async_to_raw_response_wrapper(
            scrape.create,
        )


class ScrapeResourceWithStreamingResponse:
    def __init__(self, scrape: ScrapeResource) -> None:
        self._scrape = scrape

        self.create = to_streamed_response_wrapper(
            scrape.create,
        )


class AsyncScrapeResourceWithStreamingResponse:
    def __init__(self, scrape: AsyncScrapeResource) -> None:
        self._scrape = scrape

        self.create = async_to_streamed_response_wrapper(
            scrape.create,
        )
