# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .reports import (
    ReportsResource,
    AsyncReportsResource,
    ReportsResourceWithRawResponse,
    AsyncReportsResourceWithRawResponse,
    ReportsResourceWithStreamingResponse,
    AsyncReportsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PhishguardResource", "AsyncPhishguardResource"]


class PhishguardResource(SyncAPIResource):
    @cached_property
    def reports(self) -> ReportsResource:
        return ReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PhishguardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PhishguardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhishguardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PhishguardResourceWithStreamingResponse(self)


class AsyncPhishguardResource(AsyncAPIResource):
    @cached_property
    def reports(self) -> AsyncReportsResource:
        return AsyncReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPhishguardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhishguardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhishguardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPhishguardResourceWithStreamingResponse(self)


class PhishguardResourceWithRawResponse:
    def __init__(self, phishguard: PhishguardResource) -> None:
        self._phishguard = phishguard

    @cached_property
    def reports(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self._phishguard.reports)


class AsyncPhishguardResourceWithRawResponse:
    def __init__(self, phishguard: AsyncPhishguardResource) -> None:
        self._phishguard = phishguard

    @cached_property
    def reports(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self._phishguard.reports)


class PhishguardResourceWithStreamingResponse:
    def __init__(self, phishguard: PhishguardResource) -> None:
        self._phishguard = phishguard

    @cached_property
    def reports(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self._phishguard.reports)


class AsyncPhishguardResourceWithStreamingResponse:
    def __init__(self, phishguard: AsyncPhishguardResource) -> None:
        self._phishguard = phishguard

    @cached_property
    def reports(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self._phishguard.reports)
