# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .routing.routing import (
    RoutingResource,
    AsyncRoutingResource,
    RoutingResourceWithRawResponse,
    AsyncRoutingResourceWithRawResponse,
    RoutingResourceWithStreamingResponse,
    AsyncRoutingResourceWithStreamingResponse,
)
from .security.security import (
    SecurityResource,
    AsyncSecurityResource,
    SecurityResourceWithRawResponse,
    AsyncSecurityResourceWithRawResponse,
    SecurityResourceWithStreamingResponse,
    AsyncSecurityResourceWithStreamingResponse,
)

__all__ = ["EmailResource", "AsyncEmailResource"]


class EmailResource(SyncAPIResource):
    @cached_property
    def routing(self) -> RoutingResource:
        return RoutingResource(self._client)

    @cached_property
    def security(self) -> SecurityResource:
        return SecurityResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EmailResourceWithStreamingResponse(self)


class AsyncEmailResource(AsyncAPIResource):
    @cached_property
    def routing(self) -> AsyncRoutingResource:
        return AsyncRoutingResource(self._client)

    @cached_property
    def security(self) -> AsyncSecurityResource:
        return AsyncSecurityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEmailResourceWithStreamingResponse(self)


class EmailResourceWithRawResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

    @cached_property
    def routing(self) -> RoutingResourceWithRawResponse:
        return RoutingResourceWithRawResponse(self._email.routing)

    @cached_property
    def security(self) -> SecurityResourceWithRawResponse:
        return SecurityResourceWithRawResponse(self._email.security)


class AsyncEmailResourceWithRawResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

    @cached_property
    def routing(self) -> AsyncRoutingResourceWithRawResponse:
        return AsyncRoutingResourceWithRawResponse(self._email.routing)

    @cached_property
    def security(self) -> AsyncSecurityResourceWithRawResponse:
        return AsyncSecurityResourceWithRawResponse(self._email.security)


class EmailResourceWithStreamingResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

    @cached_property
    def routing(self) -> RoutingResourceWithStreamingResponse:
        return RoutingResourceWithStreamingResponse(self._email.routing)

    @cached_property
    def security(self) -> SecurityResourceWithStreamingResponse:
        return SecurityResourceWithStreamingResponse(self._email.security)


class AsyncEmailResourceWithStreamingResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

    @cached_property
    def routing(self) -> AsyncRoutingResourceWithStreamingResponse:
        return AsyncRoutingResourceWithStreamingResponse(self._email.routing)

    @cached_property
    def security(self) -> AsyncSecurityResourceWithStreamingResponse:
        return AsyncSecurityResourceWithStreamingResponse(self._email.security)
