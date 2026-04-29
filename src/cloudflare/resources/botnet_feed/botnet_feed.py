# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .asn import (
    ASNResource,
    AsyncASNResource,
    ASNResourceWithRawResponse,
    AsyncASNResourceWithRawResponse,
    ASNResourceWithStreamingResponse,
    AsyncASNResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .configs.configs import (
    ConfigsResource,
    AsyncConfigsResource,
    ConfigsResourceWithRawResponse,
    AsyncConfigsResourceWithRawResponse,
    ConfigsResourceWithStreamingResponse,
    AsyncConfigsResourceWithStreamingResponse,
)

__all__ = ["BotnetFeedResource", "AsyncBotnetFeedResource"]


class BotnetFeedResource(SyncAPIResource):
    @cached_property
    def asn(self) -> ASNResource:
        return ASNResource(self._client)

    @cached_property
    def configs(self) -> ConfigsResource:
        return ConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BotnetFeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BotnetFeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotnetFeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BotnetFeedResourceWithStreamingResponse(self)


class AsyncBotnetFeedResource(AsyncAPIResource):
    @cached_property
    def asn(self) -> AsyncASNResource:
        return AsyncASNResource(self._client)

    @cached_property
    def configs(self) -> AsyncConfigsResource:
        return AsyncConfigsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBotnetFeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBotnetFeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotnetFeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBotnetFeedResourceWithStreamingResponse(self)


class BotnetFeedResourceWithRawResponse:
    def __init__(self, botnet_feed: BotnetFeedResource) -> None:
        self._botnet_feed = botnet_feed

    @cached_property
    def asn(self) -> ASNResourceWithRawResponse:
        return ASNResourceWithRawResponse(self._botnet_feed.asn)

    @cached_property
    def configs(self) -> ConfigsResourceWithRawResponse:
        return ConfigsResourceWithRawResponse(self._botnet_feed.configs)


class AsyncBotnetFeedResourceWithRawResponse:
    def __init__(self, botnet_feed: AsyncBotnetFeedResource) -> None:
        self._botnet_feed = botnet_feed

    @cached_property
    def asn(self) -> AsyncASNResourceWithRawResponse:
        return AsyncASNResourceWithRawResponse(self._botnet_feed.asn)

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithRawResponse:
        return AsyncConfigsResourceWithRawResponse(self._botnet_feed.configs)


class BotnetFeedResourceWithStreamingResponse:
    def __init__(self, botnet_feed: BotnetFeedResource) -> None:
        self._botnet_feed = botnet_feed

    @cached_property
    def asn(self) -> ASNResourceWithStreamingResponse:
        return ASNResourceWithStreamingResponse(self._botnet_feed.asn)

    @cached_property
    def configs(self) -> ConfigsResourceWithStreamingResponse:
        return ConfigsResourceWithStreamingResponse(self._botnet_feed.configs)


class AsyncBotnetFeedResourceWithStreamingResponse:
    def __init__(self, botnet_feed: AsyncBotnetFeedResource) -> None:
        self._botnet_feed = botnet_feed

    @cached_property
    def asn(self) -> AsyncASNResourceWithStreamingResponse:
        return AsyncASNResourceWithStreamingResponse(self._botnet_feed.asn)

    @cached_property
    def configs(self) -> AsyncConfigsResourceWithStreamingResponse:
        return AsyncConfigsResourceWithStreamingResponse(self._botnet_feed.configs)
