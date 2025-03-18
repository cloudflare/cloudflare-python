# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .eligible import (
    EligibleResource,
    AsyncEligibleResource,
    EligibleResourceWithRawResponse,
    AsyncEligibleResourceWithRawResponse,
    EligibleResourceWithStreamingResponse,
    AsyncEligibleResourceWithStreamingResponse,
)
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from .pagerduty import (
    PagerdutyResource,
    AsyncPagerdutyResource,
    PagerdutyResourceWithRawResponse,
    AsyncPagerdutyResourceWithRawResponse,
    PagerdutyResourceWithStreamingResponse,
    AsyncPagerdutyResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DestinationsResource", "AsyncDestinationsResource"]


class DestinationsResource(SyncAPIResource):
    @cached_property
    def eligible(self) -> EligibleResource:
        return EligibleResource(self._client)

    @cached_property
    def pagerduty(self) -> PagerdutyResource:
        return PagerdutyResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> DestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DestinationsResourceWithStreamingResponse(self)


class AsyncDestinationsResource(AsyncAPIResource):
    @cached_property
    def eligible(self) -> AsyncEligibleResource:
        return AsyncEligibleResource(self._client)

    @cached_property
    def pagerduty(self) -> AsyncPagerdutyResource:
        return AsyncPagerdutyResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDestinationsResourceWithStreamingResponse(self)


class DestinationsResourceWithRawResponse:
    def __init__(self, destinations: DestinationsResource) -> None:
        self._destinations = destinations

    @cached_property
    def eligible(self) -> EligibleResourceWithRawResponse:
        return EligibleResourceWithRawResponse(self._destinations.eligible)

    @cached_property
    def pagerduty(self) -> PagerdutyResourceWithRawResponse:
        return PagerdutyResourceWithRawResponse(self._destinations.pagerduty)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._destinations.webhooks)


class AsyncDestinationsResourceWithRawResponse:
    def __init__(self, destinations: AsyncDestinationsResource) -> None:
        self._destinations = destinations

    @cached_property
    def eligible(self) -> AsyncEligibleResourceWithRawResponse:
        return AsyncEligibleResourceWithRawResponse(self._destinations.eligible)

    @cached_property
    def pagerduty(self) -> AsyncPagerdutyResourceWithRawResponse:
        return AsyncPagerdutyResourceWithRawResponse(self._destinations.pagerduty)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._destinations.webhooks)


class DestinationsResourceWithStreamingResponse:
    def __init__(self, destinations: DestinationsResource) -> None:
        self._destinations = destinations

    @cached_property
    def eligible(self) -> EligibleResourceWithStreamingResponse:
        return EligibleResourceWithStreamingResponse(self._destinations.eligible)

    @cached_property
    def pagerduty(self) -> PagerdutyResourceWithStreamingResponse:
        return PagerdutyResourceWithStreamingResponse(self._destinations.pagerduty)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._destinations.webhooks)


class AsyncDestinationsResourceWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinationsResource) -> None:
        self._destinations = destinations

    @cached_property
    def eligible(self) -> AsyncEligibleResourceWithStreamingResponse:
        return AsyncEligibleResourceWithStreamingResponse(self._destinations.eligible)

    @cached_property
    def pagerduty(self) -> AsyncPagerdutyResourceWithStreamingResponse:
        return AsyncPagerdutyResourceWithStreamingResponse(self._destinations.pagerduty)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._destinations.webhooks)
