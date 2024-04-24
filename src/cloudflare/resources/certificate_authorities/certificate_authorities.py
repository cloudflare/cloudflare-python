# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .hostname_associations import (
    HostnameAssociationsResource,
    AsyncHostnameAssociationsResource,
    HostnameAssociationsResourceWithRawResponse,
    AsyncHostnameAssociationsResourceWithRawResponse,
    HostnameAssociationsResourceWithStreamingResponse,
    AsyncHostnameAssociationsResourceWithStreamingResponse,
)

__all__ = ["CertificateAuthoritiesResource", "AsyncCertificateAuthoritiesResource"]


class CertificateAuthoritiesResource(SyncAPIResource):
    @cached_property
    def hostname_associations(self) -> HostnameAssociationsResource:
        return HostnameAssociationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CertificateAuthoritiesResourceWithRawResponse:
        return CertificateAuthoritiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificateAuthoritiesResourceWithStreamingResponse:
        return CertificateAuthoritiesResourceWithStreamingResponse(self)


class AsyncCertificateAuthoritiesResource(AsyncAPIResource):
    @cached_property
    def hostname_associations(self) -> AsyncHostnameAssociationsResource:
        return AsyncHostnameAssociationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCertificateAuthoritiesResourceWithRawResponse:
        return AsyncCertificateAuthoritiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificateAuthoritiesResourceWithStreamingResponse:
        return AsyncCertificateAuthoritiesResourceWithStreamingResponse(self)


class CertificateAuthoritiesResourceWithRawResponse:
    def __init__(self, certificate_authorities: CertificateAuthoritiesResource) -> None:
        self._certificate_authorities = certificate_authorities

    @cached_property
    def hostname_associations(self) -> HostnameAssociationsResourceWithRawResponse:
        return HostnameAssociationsResourceWithRawResponse(self._certificate_authorities.hostname_associations)


class AsyncCertificateAuthoritiesResourceWithRawResponse:
    def __init__(self, certificate_authorities: AsyncCertificateAuthoritiesResource) -> None:
        self._certificate_authorities = certificate_authorities

    @cached_property
    def hostname_associations(self) -> AsyncHostnameAssociationsResourceWithRawResponse:
        return AsyncHostnameAssociationsResourceWithRawResponse(self._certificate_authorities.hostname_associations)


class CertificateAuthoritiesResourceWithStreamingResponse:
    def __init__(self, certificate_authorities: CertificateAuthoritiesResource) -> None:
        self._certificate_authorities = certificate_authorities

    @cached_property
    def hostname_associations(self) -> HostnameAssociationsResourceWithStreamingResponse:
        return HostnameAssociationsResourceWithStreamingResponse(self._certificate_authorities.hostname_associations)


class AsyncCertificateAuthoritiesResourceWithStreamingResponse:
    def __init__(self, certificate_authorities: AsyncCertificateAuthoritiesResource) -> None:
        self._certificate_authorities = certificate_authorities

    @cached_property
    def hostname_associations(self) -> AsyncHostnameAssociationsResourceWithStreamingResponse:
        return AsyncHostnameAssociationsResourceWithStreamingResponse(
            self._certificate_authorities.hostname_associations
        )
