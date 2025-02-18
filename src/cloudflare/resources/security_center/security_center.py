# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .insights.insights import (
    InsightsResource,
    AsyncInsightsResource,
    InsightsResourceWithRawResponse,
    AsyncInsightsResourceWithRawResponse,
    InsightsResourceWithStreamingResponse,
    AsyncInsightsResourceWithStreamingResponse,
)

__all__ = ["SecurityCenterResource", "AsyncSecurityCenterResource"]


class SecurityCenterResource(SyncAPIResource):
    @cached_property
    def insights(self) -> InsightsResource:
        return InsightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecurityCenterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SecurityCenterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityCenterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SecurityCenterResourceWithStreamingResponse(self)


class AsyncSecurityCenterResource(AsyncAPIResource):
    @cached_property
    def insights(self) -> AsyncInsightsResource:
        return AsyncInsightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecurityCenterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecurityCenterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityCenterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSecurityCenterResourceWithStreamingResponse(self)


class SecurityCenterResourceWithRawResponse:
    def __init__(self, security_center: SecurityCenterResource) -> None:
        self._security_center = security_center

    @cached_property
    def insights(self) -> InsightsResourceWithRawResponse:
        return InsightsResourceWithRawResponse(self._security_center.insights)


class AsyncSecurityCenterResourceWithRawResponse:
    def __init__(self, security_center: AsyncSecurityCenterResource) -> None:
        self._security_center = security_center

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithRawResponse:
        return AsyncInsightsResourceWithRawResponse(self._security_center.insights)


class SecurityCenterResourceWithStreamingResponse:
    def __init__(self, security_center: SecurityCenterResource) -> None:
        self._security_center = security_center

    @cached_property
    def insights(self) -> InsightsResourceWithStreamingResponse:
        return InsightsResourceWithStreamingResponse(self._security_center.insights)


class AsyncSecurityCenterResourceWithStreamingResponse:
    def __init__(self, security_center: AsyncSecurityCenterResource) -> None:
        self._security_center = security_center

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithStreamingResponse:
        return AsyncInsightsResourceWithStreamingResponse(self._security_center.insights)
