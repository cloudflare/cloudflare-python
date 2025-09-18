# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.browser_rendering import pdf_create_params

__all__ = ["PDFResource", "AsyncPDFResource"]


class PDFResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PDFResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PDFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PDFResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PDFResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        cache_ttl: float | Omit = omit,
        action_timeout: float | Omit = omit,
        add_script_tag: Iterable[pdf_create_params.AddScriptTag] | Omit = omit,
        add_style_tag: Iterable[pdf_create_params.AddStyleTag] | Omit = omit,
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
        authenticate: pdf_create_params.Authenticate | Omit = omit,
        best_attempt: bool | Omit = omit,
        cookies: Iterable[pdf_create_params.Cookie] | Omit = omit,
        emulate_media_type: str | Omit = omit,
        goto_options: pdf_create_params.GotoOptions | Omit = omit,
        html: str | Omit = omit,
        pdf_options: pdf_create_params.PDFOptions | Omit = omit,
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
        set_extra_http_headers: Dict[str, str] | Omit = omit,
        set_java_script_enabled: bool | Omit = omit,
        url: str | Omit = omit,
        user_agent: str | Omit = omit,
        viewport: pdf_create_params.Viewport | Omit = omit,
        wait_for_selector: pdf_create_params.WaitForSelector | Omit = omit,
        wait_for_timeout: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Fetches rendered PDF from provided URL or HTML.

        Check available options like
        `gotoOptions` and `waitFor*` to control page load behaviour.

        Args:
          account_id: Account ID.

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

          goto_options: Check [options](https://pptr.dev/api/puppeteer.gotooptions).

          html: Set the content of the page, eg: `<h1>Hello World!!</h1>`. Either `html` or
              `url` must be set.

          pdf_options: Check [options](https://pptr.dev/api/puppeteer.pdfoptions).

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
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/browser-rendering/pdf",
            body=maybe_transform(
                {
                    "action_timeout": action_timeout,
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
                    "pdf_options": pdf_options,
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
                pdf_create_params.PDFCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cache_ttl": cache_ttl}, pdf_create_params.PDFCreateParams),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncPDFResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPDFResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPDFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPDFResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPDFResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        cache_ttl: float | Omit = omit,
        action_timeout: float | Omit = omit,
        add_script_tag: Iterable[pdf_create_params.AddScriptTag] | Omit = omit,
        add_style_tag: Iterable[pdf_create_params.AddStyleTag] | Omit = omit,
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
        authenticate: pdf_create_params.Authenticate | Omit = omit,
        best_attempt: bool | Omit = omit,
        cookies: Iterable[pdf_create_params.Cookie] | Omit = omit,
        emulate_media_type: str | Omit = omit,
        goto_options: pdf_create_params.GotoOptions | Omit = omit,
        html: str | Omit = omit,
        pdf_options: pdf_create_params.PDFOptions | Omit = omit,
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
        set_extra_http_headers: Dict[str, str] | Omit = omit,
        set_java_script_enabled: bool | Omit = omit,
        url: str | Omit = omit,
        user_agent: str | Omit = omit,
        viewport: pdf_create_params.Viewport | Omit = omit,
        wait_for_selector: pdf_create_params.WaitForSelector | Omit = omit,
        wait_for_timeout: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Fetches rendered PDF from provided URL or HTML.

        Check available options like
        `gotoOptions` and `waitFor*` to control page load behaviour.

        Args:
          account_id: Account ID.

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

          goto_options: Check [options](https://pptr.dev/api/puppeteer.gotooptions).

          html: Set the content of the page, eg: `<h1>Hello World!!</h1>`. Either `html` or
              `url` must be set.

          pdf_options: Check [options](https://pptr.dev/api/puppeteer.pdfoptions).

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
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/browser-rendering/pdf",
            body=await async_maybe_transform(
                {
                    "action_timeout": action_timeout,
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
                    "pdf_options": pdf_options,
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
                pdf_create_params.PDFCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cache_ttl": cache_ttl}, pdf_create_params.PDFCreateParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class PDFResourceWithRawResponse:
    def __init__(self, pdf: PDFResource) -> None:
        self._pdf = pdf

        self.create = to_custom_raw_response_wrapper(
            pdf.create,
            BinaryAPIResponse,
        )


class AsyncPDFResourceWithRawResponse:
    def __init__(self, pdf: AsyncPDFResource) -> None:
        self._pdf = pdf

        self.create = async_to_custom_raw_response_wrapper(
            pdf.create,
            AsyncBinaryAPIResponse,
        )


class PDFResourceWithStreamingResponse:
    def __init__(self, pdf: PDFResource) -> None:
        self._pdf = pdf

        self.create = to_custom_streamed_response_wrapper(
            pdf.create,
            StreamedBinaryAPIResponse,
        )


class AsyncPDFResourceWithStreamingResponse:
    def __init__(self, pdf: AsyncPDFResource) -> None:
        self._pdf = pdf

        self.create = async_to_custom_streamed_response_wrapper(
            pdf.create,
            AsyncStreamedBinaryAPIResponse,
        )
