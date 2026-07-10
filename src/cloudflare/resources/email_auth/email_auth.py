# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .spf.spf import (
    SPFResource,
    AsyncSPFResource,
    SPFResourceWithRawResponse,
    AsyncSPFResourceWithRawResponse,
    SPFResourceWithStreamingResponse,
    AsyncSPFResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .dmarc_reports import (
    DMARCReportsResource,
    AsyncDMARCReportsResource,
    DMARCReportsResourceWithRawResponse,
    AsyncDMARCReportsResourceWithRawResponse,
    DMARCReportsResourceWithStreamingResponse,
    AsyncDMARCReportsResourceWithStreamingResponse,
)

__all__ = ["EmailAuthResource", "AsyncEmailAuthResource"]


class EmailAuthResource(SyncAPIResource):
    @cached_property
    def dmarc_reports(self) -> DMARCReportsResource:
        return DMARCReportsResource(self._client)

    @cached_property
    def spf(self) -> SPFResource:
        return SPFResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EmailAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EmailAuthResourceWithStreamingResponse(self)


class AsyncEmailAuthResource(AsyncAPIResource):
    @cached_property
    def dmarc_reports(self) -> AsyncDMARCReportsResource:
        return AsyncDMARCReportsResource(self._client)

    @cached_property
    def spf(self) -> AsyncSPFResource:
        return AsyncSPFResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEmailAuthResourceWithStreamingResponse(self)


class EmailAuthResourceWithRawResponse:
    def __init__(self, email_auth: EmailAuthResource) -> None:
        self._email_auth = email_auth

    @cached_property
    def dmarc_reports(self) -> DMARCReportsResourceWithRawResponse:
        return DMARCReportsResourceWithRawResponse(self._email_auth.dmarc_reports)

    @cached_property
    def spf(self) -> SPFResourceWithRawResponse:
        return SPFResourceWithRawResponse(self._email_auth.spf)


class AsyncEmailAuthResourceWithRawResponse:
    def __init__(self, email_auth: AsyncEmailAuthResource) -> None:
        self._email_auth = email_auth

    @cached_property
    def dmarc_reports(self) -> AsyncDMARCReportsResourceWithRawResponse:
        return AsyncDMARCReportsResourceWithRawResponse(self._email_auth.dmarc_reports)

    @cached_property
    def spf(self) -> AsyncSPFResourceWithRawResponse:
        return AsyncSPFResourceWithRawResponse(self._email_auth.spf)


class EmailAuthResourceWithStreamingResponse:
    def __init__(self, email_auth: EmailAuthResource) -> None:
        self._email_auth = email_auth

    @cached_property
    def dmarc_reports(self) -> DMARCReportsResourceWithStreamingResponse:
        return DMARCReportsResourceWithStreamingResponse(self._email_auth.dmarc_reports)

    @cached_property
    def spf(self) -> SPFResourceWithStreamingResponse:
        return SPFResourceWithStreamingResponse(self._email_auth.spf)


class AsyncEmailAuthResourceWithStreamingResponse:
    def __init__(self, email_auth: AsyncEmailAuthResource) -> None:
        self._email_auth = email_auth

    @cached_property
    def dmarc_reports(self) -> AsyncDMARCReportsResourceWithStreamingResponse:
        return AsyncDMARCReportsResourceWithStreamingResponse(self._email_auth.dmarc_reports)

    @cached_property
    def spf(self) -> AsyncSPFResourceWithStreamingResponse:
        return AsyncSPFResourceWithStreamingResponse(self._email_auth.spf)
