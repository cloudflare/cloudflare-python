# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.browser_rendering.devtools.browser import live_view_create_params
from .....types.browser_rendering.devtools.browser.live_view_create_response import LiveViewCreateResponse

__all__ = ["LiveViewResource", "AsyncLiveViewResource"]


class LiveViewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiveViewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LiveViewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveViewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LiveViewResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        account_id: str,
        expires_in_ms: float | Omit = omit,
        guardrails: live_view_create_params.Guardrails | Omit = omit,
        mode: Literal["devtools", "tab", "full"] | Omit = omit,
        target_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveViewCreateResponse:
        """Generates time-limited URLs to view a remote browser session.

        Set
        `guardrails: { mode: 'readonly' }` to create a view-only link.

        Args:
          account_id: Account ID.

          session_id: Browser session ID

          expires_in_ms: How long the live view URLs remain valid, in milliseconds. Default: 5 minutes.
              Max: 60 minutes.

          guardrails: Connection guardrails. Use `{ mode: 'readonly' }` to generate a view-only link.

          mode: UI mode: 'devtools' (Chrome DevTools), 'tab' (single tab view), 'full'
              (multi-tab browser)

          target_id: Target ID (page) to connect to. If omitted, auto-resolves to the first active
              page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/live_view",
                account_id=account_id,
                session_id=session_id,
            ),
            body=maybe_transform(
                {
                    "expires_in_ms": expires_in_ms,
                    "guardrails": guardrails,
                    "mode": mode,
                    "target_id": target_id,
                },
                live_view_create_params.LiveViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveViewCreateResponse,
        )


class AsyncLiveViewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiveViewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLiveViewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveViewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLiveViewResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        account_id: str,
        expires_in_ms: float | Omit = omit,
        guardrails: live_view_create_params.Guardrails | Omit = omit,
        mode: Literal["devtools", "tab", "full"] | Omit = omit,
        target_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LiveViewCreateResponse:
        """Generates time-limited URLs to view a remote browser session.

        Set
        `guardrails: { mode: 'readonly' }` to create a view-only link.

        Args:
          account_id: Account ID.

          session_id: Browser session ID

          expires_in_ms: How long the live view URLs remain valid, in milliseconds. Default: 5 minutes.
              Max: 60 minutes.

          guardrails: Connection guardrails. Use `{ mode: 'readonly' }` to generate a view-only link.

          mode: UI mode: 'devtools' (Chrome DevTools), 'tab' (single tab view), 'full'
              (multi-tab browser)

          target_id: Target ID (page) to connect to. If omitted, auto-resolves to the first active
              page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/live_view",
                account_id=account_id,
                session_id=session_id,
            ),
            body=await async_maybe_transform(
                {
                    "expires_in_ms": expires_in_ms,
                    "guardrails": guardrails,
                    "mode": mode,
                    "target_id": target_id,
                },
                live_view_create_params.LiveViewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveViewCreateResponse,
        )


class LiveViewResourceWithRawResponse:
    def __init__(self, live_view: LiveViewResource) -> None:
        self._live_view = live_view

        self.create = to_raw_response_wrapper(
            live_view.create,
        )


class AsyncLiveViewResourceWithRawResponse:
    def __init__(self, live_view: AsyncLiveViewResource) -> None:
        self._live_view = live_view

        self.create = async_to_raw_response_wrapper(
            live_view.create,
        )


class LiveViewResourceWithStreamingResponse:
    def __init__(self, live_view: LiveViewResource) -> None:
        self._live_view = live_view

        self.create = to_streamed_response_wrapper(
            live_view.create,
        )


class AsyncLiveViewResourceWithStreamingResponse:
    def __init__(self, live_view: AsyncLiveViewResource) -> None:
        self._live_view = live_view

        self.create = async_to_streamed_response_wrapper(
            live_view.create,
        )
