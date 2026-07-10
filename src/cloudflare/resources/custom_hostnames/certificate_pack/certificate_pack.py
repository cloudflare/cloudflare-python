# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .certificates import (
    CertificatesResource,
    AsyncCertificatesResource,
    CertificatesResourceWithRawResponse,
    AsyncCertificatesResourceWithRawResponse,
    CertificatesResourceWithStreamingResponse,
    AsyncCertificatesResourceWithStreamingResponse,
)

__all__ = ["CertificatePackResource", "AsyncCertificatePackResource"]


class CertificatePackResource(SyncAPIResource):
    @cached_property
    def certificates(self) -> CertificatesResource:
        return CertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CertificatePackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CertificatePackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatePackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CertificatePackResourceWithStreamingResponse(self)


class AsyncCertificatePackResource(AsyncAPIResource):
    @cached_property
    def certificates(self) -> AsyncCertificatesResource:
        return AsyncCertificatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCertificatePackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCertificatePackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatePackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCertificatePackResourceWithStreamingResponse(self)


class CertificatePackResourceWithRawResponse:
    def __init__(self, certificate_pack: CertificatePackResource) -> None:
        self._certificate_pack = certificate_pack

    @cached_property
    def certificates(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self._certificate_pack.certificates)


class AsyncCertificatePackResourceWithRawResponse:
    def __init__(self, certificate_pack: AsyncCertificatePackResource) -> None:
        self._certificate_pack = certificate_pack

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self._certificate_pack.certificates)


class CertificatePackResourceWithStreamingResponse:
    def __init__(self, certificate_pack: CertificatePackResource) -> None:
        self._certificate_pack = certificate_pack

    @cached_property
    def certificates(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self._certificate_pack.certificates)


class AsyncCertificatePackResourceWithStreamingResponse:
    def __init__(self, certificate_pack: AsyncCertificatePackResource) -> None:
        self._certificate_pack = certificate_pack

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self._certificate_pack.certificates)
