# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .integrations import (
    IntegrationsResource,
    AsyncIntegrationsResource,
    IntegrationsResourceWithRawResponse,
    AsyncIntegrationsResourceWithRawResponse,
    IntegrationsResourceWithStreamingResponse,
    AsyncIntegrationsResourceWithStreamingResponse,
)
from .applications.applications import (
    ApplicationsResource,
    AsyncApplicationsResource,
    ApplicationsResourceWithRawResponse,
    AsyncApplicationsResourceWithRawResponse,
    ApplicationsResourceWithStreamingResponse,
    AsyncApplicationsResourceWithStreamingResponse,
)

__all__ = ["CasbResource", "AsyncCasbResource"]


class CasbResource(SyncAPIResource):
    @cached_property
    def applications(self) -> ApplicationsResource:
        return ApplicationsResource(self._client)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        return IntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CasbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CasbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CasbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CasbResourceWithStreamingResponse(self)


class AsyncCasbResource(AsyncAPIResource):
    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        return AsyncApplicationsResource(self._client)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        return AsyncIntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCasbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCasbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCasbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCasbResourceWithStreamingResponse(self)


class CasbResourceWithRawResponse:
    def __init__(self, casb: CasbResource) -> None:
        self._casb = casb

    @cached_property
    def applications(self) -> ApplicationsResourceWithRawResponse:
        return ApplicationsResourceWithRawResponse(self._casb.applications)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self._casb.integrations)


class AsyncCasbResourceWithRawResponse:
    def __init__(self, casb: AsyncCasbResource) -> None:
        self._casb = casb

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithRawResponse:
        return AsyncApplicationsResourceWithRawResponse(self._casb.applications)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self._casb.integrations)


class CasbResourceWithStreamingResponse:
    def __init__(self, casb: CasbResource) -> None:
        self._casb = casb

    @cached_property
    def applications(self) -> ApplicationsResourceWithStreamingResponse:
        return ApplicationsResourceWithStreamingResponse(self._casb.applications)

    @cached_property
    def integrations(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self._casb.integrations)


class AsyncCasbResourceWithStreamingResponse:
    def __init__(self, casb: AsyncCasbResource) -> None:
        self._casb = casb

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithStreamingResponse:
        return AsyncApplicationsResourceWithStreamingResponse(self._casb.applications)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self._casb.integrations)
