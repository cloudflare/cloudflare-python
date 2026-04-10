# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.browser_rendering.devtools.browser import target_create_params
from .....types.browser_rendering.devtools.browser.target_get_response import TargetGetResponse
from .....types.browser_rendering.devtools.browser.target_list_response import TargetListResponse
from .....types.browser_rendering.devtools.browser.target_create_response import TargetCreateResponse
from .....types.browser_rendering.devtools.browser.target_activate_response import TargetActivateResponse

__all__ = ["TargetsResource", "AsyncTargetsResource"]


class TargetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TargetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TargetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TargetsResourceWithStreamingResponse(self)

    def create(
        self,
        session_id: str,
        *,
        account_id: str,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetCreateResponse:
        """Opens a new tab in the browser.

        Optionally specify a URL to navigate to.

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
        return self._put(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/new",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, target_create_params.TargetCreateParams),
            ),
            cast_to=TargetCreateResponse,
        )

    def list(
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
    ) -> TargetListResponse:
        """
        Returns a list of all debuggable targets including tabs, pages, service workers,
        and other browser contexts.

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
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetListResponse,
        )

    def activate(
        self,
        target_id: str,
        *,
        account_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetActivateResponse:
        """
        Activates (brings to front) a specific browser target by its ID.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          target_id: Target ID to activate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        return self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/activate/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetActivateResponse,
        )

    def get(
        self,
        target_id: str,
        *,
        account_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetGetResponse:
        """
        Returns the debuggable target with the given ID.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          target_id: Target ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        return self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetGetResponse,
        )


class AsyncTargetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTargetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTargetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTargetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTargetsResourceWithStreamingResponse(self)

    async def create(
        self,
        session_id: str,
        *,
        account_id: str,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetCreateResponse:
        """Opens a new tab in the browser.

        Optionally specify a URL to navigate to.

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
        return await self._put(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/new",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url": url}, target_create_params.TargetCreateParams),
            ),
            cast_to=TargetCreateResponse,
        )

    async def list(
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
    ) -> TargetListResponse:
        """
        Returns a list of all debuggable targets including tabs, pages, service workers,
        and other browser contexts.

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
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetListResponse,
        )

    async def activate(
        self,
        target_id: str,
        *,
        account_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetActivateResponse:
        """
        Activates (brings to front) a specific browser target by its ID.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          target_id: Target ID to activate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        return await self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/activate/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetActivateResponse,
        )

    async def get(
        self,
        target_id: str,
        *,
        account_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TargetGetResponse:
        """
        Returns the debuggable target with the given ID.

        Args:
          account_id: Account ID.

          session_id: Browser session ID.

          target_id: Target ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not target_id:
            raise ValueError(f"Expected a non-empty value for `target_id` but received {target_id!r}")
        return await self._get(
            f"/accounts/{account_id}/browser-rendering/devtools/browser/{session_id}/json/list/{target_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TargetGetResponse,
        )


class TargetsResourceWithRawResponse:
    def __init__(self, targets: TargetsResource) -> None:
        self._targets = targets

        self.create = to_raw_response_wrapper(
            targets.create,
        )
        self.list = to_raw_response_wrapper(
            targets.list,
        )
        self.activate = to_raw_response_wrapper(
            targets.activate,
        )
        self.get = to_raw_response_wrapper(
            targets.get,
        )


class AsyncTargetsResourceWithRawResponse:
    def __init__(self, targets: AsyncTargetsResource) -> None:
        self._targets = targets

        self.create = async_to_raw_response_wrapper(
            targets.create,
        )
        self.list = async_to_raw_response_wrapper(
            targets.list,
        )
        self.activate = async_to_raw_response_wrapper(
            targets.activate,
        )
        self.get = async_to_raw_response_wrapper(
            targets.get,
        )


class TargetsResourceWithStreamingResponse:
    def __init__(self, targets: TargetsResource) -> None:
        self._targets = targets

        self.create = to_streamed_response_wrapper(
            targets.create,
        )
        self.list = to_streamed_response_wrapper(
            targets.list,
        )
        self.activate = to_streamed_response_wrapper(
            targets.activate,
        )
        self.get = to_streamed_response_wrapper(
            targets.get,
        )


class AsyncTargetsResourceWithStreamingResponse:
    def __init__(self, targets: AsyncTargetsResource) -> None:
        self._targets = targets

        self.create = async_to_streamed_response_wrapper(
            targets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            targets.list,
        )
        self.activate = async_to_streamed_response_wrapper(
            targets.activate,
        )
        self.get = async_to_streamed_response_wrapper(
            targets.get,
        )
