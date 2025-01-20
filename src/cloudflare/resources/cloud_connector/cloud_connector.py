# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CloudConnectorResource", "AsyncCloudConnectorResource"]


class CloudConnectorResource(SyncAPIResource):
    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CloudConnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CloudConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudConnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CloudConnectorResourceWithStreamingResponse(self)


class AsyncCloudConnectorResource(AsyncAPIResource):
    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloudConnectorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudConnectorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCloudConnectorResourceWithStreamingResponse(self)


class CloudConnectorResourceWithRawResponse:
    def __init__(self, cloud_connector: CloudConnectorResource) -> None:
        self._cloud_connector = cloud_connector

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._cloud_connector.rules)


class AsyncCloudConnectorResourceWithRawResponse:
    def __init__(self, cloud_connector: AsyncCloudConnectorResource) -> None:
        self._cloud_connector = cloud_connector

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._cloud_connector.rules)


class CloudConnectorResourceWithStreamingResponse:
    def __init__(self, cloud_connector: CloudConnectorResource) -> None:
        self._cloud_connector = cloud_connector

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._cloud_connector.rules)


class AsyncCloudConnectorResourceWithStreamingResponse:
    def __init__(self, cloud_connector: AsyncCloudConnectorResource) -> None:
        self._cloud_connector = cloud_connector

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._cloud_connector.rules)
