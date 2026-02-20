# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .aspa import (
    ASPAResource,
    AsyncASPAResource,
    ASPAResourceWithRawResponse,
    AsyncASPAResourceWithRawResponse,
    ASPAResourceWithStreamingResponse,
    AsyncASPAResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RPKIResource", "AsyncRPKIResource"]


class RPKIResource(SyncAPIResource):
    @cached_property
    def aspa(self) -> ASPAResource:
        return ASPAResource(self._client)

    @cached_property
    def with_raw_response(self) -> RPKIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RPKIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RPKIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RPKIResourceWithStreamingResponse(self)


class AsyncRPKIResource(AsyncAPIResource):
    @cached_property
    def aspa(self) -> AsyncASPAResource:
        return AsyncASPAResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRPKIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRPKIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRPKIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRPKIResourceWithStreamingResponse(self)


class RPKIResourceWithRawResponse:
    def __init__(self, rpki: RPKIResource) -> None:
        self._rpki = rpki

    @cached_property
    def aspa(self) -> ASPAResourceWithRawResponse:
        return ASPAResourceWithRawResponse(self._rpki.aspa)


class AsyncRPKIResourceWithRawResponse:
    def __init__(self, rpki: AsyncRPKIResource) -> None:
        self._rpki = rpki

    @cached_property
    def aspa(self) -> AsyncASPAResourceWithRawResponse:
        return AsyncASPAResourceWithRawResponse(self._rpki.aspa)


class RPKIResourceWithStreamingResponse:
    def __init__(self, rpki: RPKIResource) -> None:
        self._rpki = rpki

    @cached_property
    def aspa(self) -> ASPAResourceWithStreamingResponse:
        return ASPAResourceWithStreamingResponse(self._rpki.aspa)


class AsyncRPKIResourceWithStreamingResponse:
    def __init__(self, rpki: AsyncRPKIResource) -> None:
        self._rpki = rpki

    @cached_property
    def aspa(self) -> AsyncASPAResourceWithStreamingResponse:
        return AsyncASPAResourceWithStreamingResponse(self._rpki.aspa)
