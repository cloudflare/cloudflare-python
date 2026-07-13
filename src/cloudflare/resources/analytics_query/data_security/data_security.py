# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .findings import (
    FindingsResource,
    AsyncFindingsResource,
    FindingsResourceWithRawResponse,
    AsyncFindingsResourceWithRawResponse,
    FindingsResourceWithStreamingResponse,
    AsyncFindingsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .content_findings import (
    ContentFindingsResource,
    AsyncContentFindingsResource,
    ContentFindingsResourceWithRawResponse,
    AsyncContentFindingsResourceWithRawResponse,
    ContentFindingsResourceWithStreamingResponse,
    AsyncContentFindingsResourceWithStreamingResponse,
)

__all__ = ["DataSecurityResource", "AsyncDataSecurityResource"]


class DataSecurityResource(SyncAPIResource):
    @cached_property
    def content_findings(self) -> ContentFindingsResource:
        return ContentFindingsResource(self._client)

    @cached_property
    def findings(self) -> FindingsResource:
        return FindingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataSecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DataSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DataSecurityResourceWithStreamingResponse(self)


class AsyncDataSecurityResource(AsyncAPIResource):
    @cached_property
    def content_findings(self) -> AsyncContentFindingsResource:
        return AsyncContentFindingsResource(self._client)

    @cached_property
    def findings(self) -> AsyncFindingsResource:
        return AsyncFindingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataSecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDataSecurityResourceWithStreamingResponse(self)


class DataSecurityResourceWithRawResponse:
    def __init__(self, data_security: DataSecurityResource) -> None:
        self._data_security = data_security

    @cached_property
    def content_findings(self) -> ContentFindingsResourceWithRawResponse:
        return ContentFindingsResourceWithRawResponse(self._data_security.content_findings)

    @cached_property
    def findings(self) -> FindingsResourceWithRawResponse:
        return FindingsResourceWithRawResponse(self._data_security.findings)


class AsyncDataSecurityResourceWithRawResponse:
    def __init__(self, data_security: AsyncDataSecurityResource) -> None:
        self._data_security = data_security

    @cached_property
    def content_findings(self) -> AsyncContentFindingsResourceWithRawResponse:
        return AsyncContentFindingsResourceWithRawResponse(self._data_security.content_findings)

    @cached_property
    def findings(self) -> AsyncFindingsResourceWithRawResponse:
        return AsyncFindingsResourceWithRawResponse(self._data_security.findings)


class DataSecurityResourceWithStreamingResponse:
    def __init__(self, data_security: DataSecurityResource) -> None:
        self._data_security = data_security

    @cached_property
    def content_findings(self) -> ContentFindingsResourceWithStreamingResponse:
        return ContentFindingsResourceWithStreamingResponse(self._data_security.content_findings)

    @cached_property
    def findings(self) -> FindingsResourceWithStreamingResponse:
        return FindingsResourceWithStreamingResponse(self._data_security.findings)


class AsyncDataSecurityResourceWithStreamingResponse:
    def __init__(self, data_security: AsyncDataSecurityResource) -> None:
        self._data_security = data_security

    @cached_property
    def content_findings(self) -> AsyncContentFindingsResourceWithStreamingResponse:
        return AsyncContentFindingsResourceWithStreamingResponse(self._data_security.content_findings)

    @cached_property
    def findings(self) -> AsyncFindingsResourceWithStreamingResponse:
        return AsyncFindingsResourceWithStreamingResponse(self._data_security.findings)
