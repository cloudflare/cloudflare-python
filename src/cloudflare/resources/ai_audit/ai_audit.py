# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .robots import (
    RobotsResource,
    AsyncRobotsResource,
    RobotsResourceWithRawResponse,
    AsyncRobotsResourceWithRawResponse,
    RobotsResourceWithStreamingResponse,
    AsyncRobotsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AIAuditResource", "AsyncAIAuditResource"]


class AIAuditResource(SyncAPIResource):
    @cached_property
    def robots(self) -> RobotsResource:
        return RobotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AIAuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AIAuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIAuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AIAuditResourceWithStreamingResponse(self)


class AsyncAIAuditResource(AsyncAPIResource):
    @cached_property
    def robots(self) -> AsyncRobotsResource:
        return AsyncRobotsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAIAuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIAuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIAuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAIAuditResourceWithStreamingResponse(self)


class AIAuditResourceWithRawResponse:
    def __init__(self, ai_audit: AIAuditResource) -> None:
        self._ai_audit = ai_audit

    @cached_property
    def robots(self) -> RobotsResourceWithRawResponse:
        return RobotsResourceWithRawResponse(self._ai_audit.robots)


class AsyncAIAuditResourceWithRawResponse:
    def __init__(self, ai_audit: AsyncAIAuditResource) -> None:
        self._ai_audit = ai_audit

    @cached_property
    def robots(self) -> AsyncRobotsResourceWithRawResponse:
        return AsyncRobotsResourceWithRawResponse(self._ai_audit.robots)


class AIAuditResourceWithStreamingResponse:
    def __init__(self, ai_audit: AIAuditResource) -> None:
        self._ai_audit = ai_audit

    @cached_property
    def robots(self) -> RobotsResourceWithStreamingResponse:
        return RobotsResourceWithStreamingResponse(self._ai_audit.robots)


class AsyncAIAuditResourceWithStreamingResponse:
    def __init__(self, ai_audit: AsyncAIAuditResource) -> None:
        self._ai_audit = ai_audit

    @cached_property
    def robots(self) -> AsyncRobotsResourceWithStreamingResponse:
        return AsyncRobotsResourceWithStreamingResponse(self._ai_audit.robots)
