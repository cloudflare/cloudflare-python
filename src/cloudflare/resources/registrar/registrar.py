# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RegistrarResource", "AsyncRegistrarResource"]


class RegistrarResource(SyncAPIResource):
    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RegistrarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegistrarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistrarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegistrarResourceWithStreamingResponse(self)


class AsyncRegistrarResource(AsyncAPIResource):
    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRegistrarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegistrarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistrarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegistrarResourceWithStreamingResponse(self)


class RegistrarResourceWithRawResponse:
    def __init__(self, registrar: RegistrarResource) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._registrar.domains)


class AsyncRegistrarResourceWithRawResponse:
    def __init__(self, registrar: AsyncRegistrarResource) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._registrar.domains)


class RegistrarResourceWithStreamingResponse:
    def __init__(self, registrar: RegistrarResource) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._registrar.domains)


class AsyncRegistrarResourceWithStreamingResponse:
    def __init__(self, registrar: AsyncRegistrarResource) -> None:
        self._registrar = registrar

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._registrar.domains)
