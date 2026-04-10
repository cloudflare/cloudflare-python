# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .page import (
    PageResource,
    AsyncPageResource,
    PageResourceWithRawResponse,
    AsyncPageResourceWithRawResponse,
    PageResourceWithStreamingResponse,
    AsyncPageResourceWithStreamingResponse,
)
from .targets import (
    TargetsResource,
    AsyncTargetsResource,
    TargetsResourceWithRawResponse,
    AsyncTargetsResourceWithRawResponse,
    TargetsResourceWithStreamingResponse,
    AsyncTargetsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.browser_rendering.devtools import browser_create_params, browser_launch_params, browser_connect_params
from .....types.browser_rendering.devtools.browser_create_response import BrowserCreateResponse
from .....types.browser_rendering.devtools.browser_delete_response import BrowserDeleteResponse
from .....types.browser_rendering.devtools.browser_version_response import BrowserVersionResponse
from .....types.browser_rendering.devtools.browser_protocol_response import BrowserProtocolResponse

__all__ = ["BrowserResource", "AsyncBrowserResource"]


class BrowserResource(SyncAPIResource):
    @cached_property
    def page(self) -> PageResource:
        return PageResource(self._client)

    @cached_property
    def targets(self) -> TargetsResource:
        return TargetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BrowserResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        keep_alive: float | Omit = omit,
        lab: bool | Omit = omit,
        recording: bool | Omit = omit,
        targets: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserCreateResponse:
        """
        Get a browser session ID.

        Args:
          account_id: Account ID.

          keep_alive: Keep-alive time in milliseconds.

          lab: Use experimental browser.

          targets: Include browser targets in response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/browser-rendering/devtools/browser",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "keep_alive": keep_alive,
                        "lab": lab,
                        "recording": recording,
                        "targets": targets,
                    },
                    browser_create_params.BrowserCreateParams,
                ),
            ),
            cast_to=BrowserCreateResponse,
        )

    def delete(
        self,
        session_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserDeleteResponse:
        """
        Closes an existing browser session.

        Args:
          account_id: Account ID.

          session_id: Browser session ID to close.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._delete(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserDeleteResponse,
        )

    def connect(
        self,
        session_id: str,
        *,
        account_id: str,
        keep_alive: float | Omit = omit,
        lab: bool | Omit = omit,
        recording: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Establishes a WebSocket connection to an existing browser session.

        Args:
          account_id: Account ID.

          session_id: Browser session ID to connect to.

          keep_alive: Keep-alive time in ms (only valid when acquiring new session).

          lab: Use experimental browser.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "keep_alive": keep_alive,
                        "lab": lab,
                        "recording": recording,
                    },
                    browser_connect_params.BrowserConnectParams,
                ),
            ),
            cast_to=NoneType,
        )

    def launch(
        self,
        *,
        account_id: str,
        keep_alive: float | Omit = omit,
        lab: bool | Omit = omit,
        recording: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Acquires and establishes a WebSocket connection to a browser session.

        Args:
          account_id: Account ID.

          keep_alive: Keep-alive time in ms (only valid when acquiring new session).

          lab: Use experimental browser.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "keep_alive": keep_alive,
                        "lab": lab,
                        "recording": recording,
                    },
                    browser_launch_params.BrowserLaunchParams,
                ),
            ),
            cast_to=NoneType,
        )

    def protocol(
        self,
        session_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserProtocolResponse:
        """
        Returns the complete Chrome DevTools Protocol schema including all domains,
        commands, events, and types. This schema describes the entire CDP API surface.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/protocol",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserProtocolResponse,
        )

    def version(
        self,
        session_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserVersionResponse:
        """
        Get browser version metadata.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserVersionResponse,
        )


class AsyncBrowserResource(AsyncAPIResource):
    @cached_property
    def page(self) -> AsyncPageResource:
        return AsyncPageResource(self._client)

    @cached_property
    def targets(self) -> AsyncTargetsResource:
        return AsyncTargetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrowserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBrowserResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        keep_alive: float | Omit = omit,
        lab: bool | Omit = omit,
        recording: bool | Omit = omit,
        targets: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserCreateResponse:
        """
        Get a browser session ID.

        Args:
          account_id: Account ID.

          keep_alive: Keep-alive time in milliseconds.

          lab: Use experimental browser.

          targets: Include browser targets in response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/browser-rendering/devtools/browser",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "keep_alive": keep_alive,
                        "lab": lab,
                        "recording": recording,
                        "targets": targets,
                    },
                    browser_create_params.BrowserCreateParams,
                ),
            ),
            cast_to=BrowserCreateResponse,
        )

    async def delete(
        self,
        session_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserDeleteResponse:
        """
        Closes an existing browser session.

        Args:
          account_id: Account ID.

          session_id: Browser session ID to close.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserDeleteResponse,
        )

    async def connect(
        self,
        session_id: str,
        *,
        account_id: str,
        keep_alive: float | Omit = omit,
        lab: bool | Omit = omit,
        recording: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Establishes a WebSocket connection to an existing browser session.

        Args:
          account_id: Account ID.

          session_id: Browser session ID to connect to.

          keep_alive: Keep-alive time in ms (only valid when acquiring new session).

          lab: Use experimental browser.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "keep_alive": keep_alive,
                        "lab": lab,
                        "recording": recording,
                    },
                    browser_connect_params.BrowserConnectParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def launch(
        self,
        *,
        account_id: str,
        keep_alive: float | Omit = omit,
        lab: bool | Omit = omit,
        recording: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Acquires and establishes a WebSocket connection to a browser session.

        Args:
          account_id: Account ID.

          keep_alive: Keep-alive time in ms (only valid when acquiring new session).

          lab: Use experimental browser.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "keep_alive": keep_alive,
                        "lab": lab,
                        "recording": recording,
                    },
                    browser_launch_params.BrowserLaunchParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def protocol(
        self,
        session_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserProtocolResponse:
        """
        Returns the complete Chrome DevTools Protocol schema including all domains,
        commands, events, and types. This schema describes the entire CDP API surface.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/protocol",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserProtocolResponse,
        )

    async def version(
        self,
        session_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserVersionResponse:
        """
        Get browser version metadata.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserVersionResponse,
        )


class BrowserResourceWithRawResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

        self.create = to_raw_response_wrapper(
            browser.create,
        )
        self.delete = to_raw_response_wrapper(
            browser.delete,
        )
        self.connect = to_raw_response_wrapper(
            browser.connect,
        )
        self.launch = to_raw_response_wrapper(
            browser.launch,
        )
        self.protocol = to_raw_response_wrapper(
            browser.protocol,
        )
        self.version = to_raw_response_wrapper(
            browser.version,
        )

    @cached_property
    def page(self) -> PageResourceWithRawResponse:
        return PageResourceWithRawResponse(self._browser.page)

    @cached_property
    def targets(self) -> TargetsResourceWithRawResponse:
        return TargetsResourceWithRawResponse(self._browser.targets)


class AsyncBrowserResourceWithRawResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

        self.create = async_to_raw_response_wrapper(
            browser.create,
        )
        self.delete = async_to_raw_response_wrapper(
            browser.delete,
        )
        self.connect = async_to_raw_response_wrapper(
            browser.connect,
        )
        self.launch = async_to_raw_response_wrapper(
            browser.launch,
        )
        self.protocol = async_to_raw_response_wrapper(
            browser.protocol,
        )
        self.version = async_to_raw_response_wrapper(
            browser.version,
        )

    @cached_property
    def page(self) -> AsyncPageResourceWithRawResponse:
        return AsyncPageResourceWithRawResponse(self._browser.page)

    @cached_property
    def targets(self) -> AsyncTargetsResourceWithRawResponse:
        return AsyncTargetsResourceWithRawResponse(self._browser.targets)


class BrowserResourceWithStreamingResponse:
    def __init__(self, browser: BrowserResource) -> None:
        self._browser = browser

        self.create = to_streamed_response_wrapper(
            browser.create,
        )
        self.delete = to_streamed_response_wrapper(
            browser.delete,
        )
        self.connect = to_streamed_response_wrapper(
            browser.connect,
        )
        self.launch = to_streamed_response_wrapper(
            browser.launch,
        )
        self.protocol = to_streamed_response_wrapper(
            browser.protocol,
        )
        self.version = to_streamed_response_wrapper(
            browser.version,
        )

    @cached_property
    def page(self) -> PageResourceWithStreamingResponse:
        return PageResourceWithStreamingResponse(self._browser.page)

    @cached_property
    def targets(self) -> TargetsResourceWithStreamingResponse:
        return TargetsResourceWithStreamingResponse(self._browser.targets)


class AsyncBrowserResourceWithStreamingResponse:
    def __init__(self, browser: AsyncBrowserResource) -> None:
        self._browser = browser

        self.create = async_to_streamed_response_wrapper(
            browser.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            browser.delete,
        )
        self.connect = async_to_streamed_response_wrapper(
            browser.connect,
        )
        self.launch = async_to_streamed_response_wrapper(
            browser.launch,
        )
        self.protocol = async_to_streamed_response_wrapper(
            browser.protocol,
        )
        self.version = async_to_streamed_response_wrapper(
            browser.version,
        )

    @cached_property
    def page(self) -> AsyncPageResourceWithStreamingResponse:
        return AsyncPageResourceWithStreamingResponse(self._browser.page)

    @cached_property
    def targets(self) -> AsyncTargetsResourceWithStreamingResponse:
        return AsyncTargetsResourceWithStreamingResponse(self._browser.targets)
