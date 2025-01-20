# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .widgets import (
    WidgetsResource,
    AsyncWidgetsResource,
    WidgetsResourceWithRawResponse,
    AsyncWidgetsResourceWithRawResponse,
    WidgetsResourceWithStreamingResponse,
    AsyncWidgetsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TurnstileResource", "AsyncTurnstileResource"]


class TurnstileResource(SyncAPIResource):
    @cached_property
    def widgets(self) -> WidgetsResource:
        return WidgetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TurnstileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TurnstileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TurnstileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TurnstileResourceWithStreamingResponse(self)


class AsyncTurnstileResource(AsyncAPIResource):
    @cached_property
    def widgets(self) -> AsyncWidgetsResource:
        return AsyncWidgetsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTurnstileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTurnstileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTurnstileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTurnstileResourceWithStreamingResponse(self)


class TurnstileResourceWithRawResponse:
    def __init__(self, turnstile: TurnstileResource) -> None:
        self._turnstile = turnstile

    @cached_property
    def widgets(self) -> WidgetsResourceWithRawResponse:
        return WidgetsResourceWithRawResponse(self._turnstile.widgets)


class AsyncTurnstileResourceWithRawResponse:
    def __init__(self, turnstile: AsyncTurnstileResource) -> None:
        self._turnstile = turnstile

    @cached_property
    def widgets(self) -> AsyncWidgetsResourceWithRawResponse:
        return AsyncWidgetsResourceWithRawResponse(self._turnstile.widgets)


class TurnstileResourceWithStreamingResponse:
    def __init__(self, turnstile: TurnstileResource) -> None:
        self._turnstile = turnstile

    @cached_property
    def widgets(self) -> WidgetsResourceWithStreamingResponse:
        return WidgetsResourceWithStreamingResponse(self._turnstile.widgets)


class AsyncTurnstileResourceWithStreamingResponse:
    def __init__(self, turnstile: AsyncTurnstileResource) -> None:
        self._turnstile = turnstile

    @cached_property
    def widgets(self) -> AsyncWidgetsResourceWithStreamingResponse:
        return AsyncWidgetsResourceWithStreamingResponse(self._turnstile.widgets)
