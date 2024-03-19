# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.origin_tls_client_auth.hostnames import (
    CertificateListResponse,
    TLSCertificatesAndHostnamesSchemasCertificateObject,
    certificate_create_params,
)

__all__ = ["Certificates", "AsyncCertificates"]


class Certificates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CertificatesWithRawResponse:
        return CertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatesWithStreamingResponse:
        return CertificatesWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        private_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesSchemasCertificateObject:
        """Upload a certificate to be used for client authentication on a hostname.

        10
        hostname certificates per zone are allowed.

        Args:
          zone_id: Identifier

          certificate: The hostname certificate.

          private_key: The hostname certificate's private key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "private_key": private_key,
                },
                certificate_create_params.CertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesSchemasCertificateObject],
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateListResponse]:
        """
        List Certificates

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateListResponse]], ResultWrapper[CertificateListResponse]),
        )

    def delete(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesSchemasCertificateObject:
        """
        Delete Hostname Client Certificate

        Args:
          zone_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return self._delete(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesSchemasCertificateObject],
            ),
        )

    def get(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesSchemasCertificateObject:
        """
        Get the certificate by ID to be used for client authentication on a hostname.

        Args:
          zone_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return self._get(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesSchemasCertificateObject],
            ),
        )


class AsyncCertificates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCertificatesWithRawResponse:
        return AsyncCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatesWithStreamingResponse:
        return AsyncCertificatesWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        private_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesSchemasCertificateObject:
        """Upload a certificate to be used for client authentication on a hostname.

        10
        hostname certificates per zone are allowed.

        Args:
          zone_id: Identifier

          certificate: The hostname certificate.

          private_key: The hostname certificate's private key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates",
            body=await async_maybe_transform(
                {
                    "certificate": certificate,
                    "private_key": private_key,
                },
                certificate_create_params.CertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesSchemasCertificateObject],
            ),
        )

    async def list(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateListResponse]:
        """
        List Certificates

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateListResponse]], ResultWrapper[CertificateListResponse]),
        )

    async def delete(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesSchemasCertificateObject:
        """
        Delete Hostname Client Certificate

        Args:
          zone_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesSchemasCertificateObject],
            ),
        )

    async def get(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesSchemasCertificateObject:
        """
        Get the certificate by ID to be used for client authentication on a hostname.

        Args:
          zone_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return await self._get(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesSchemasCertificateObject],
            ),
        )


class CertificatesWithRawResponse:
    def __init__(self, certificates: Certificates) -> None:
        self._certificates = certificates

        self.create = to_raw_response_wrapper(
            certificates.create,
        )
        self.list = to_raw_response_wrapper(
            certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            certificates.delete,
        )
        self.get = to_raw_response_wrapper(
            certificates.get,
        )


class AsyncCertificatesWithRawResponse:
    def __init__(self, certificates: AsyncCertificates) -> None:
        self._certificates = certificates

        self.create = async_to_raw_response_wrapper(
            certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            certificates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            certificates.get,
        )


class CertificatesWithStreamingResponse:
    def __init__(self, certificates: Certificates) -> None:
        self._certificates = certificates

        self.create = to_streamed_response_wrapper(
            certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            certificates.delete,
        )
        self.get = to_streamed_response_wrapper(
            certificates.get,
        )


class AsyncCertificatesWithStreamingResponse:
    def __init__(self, certificates: AsyncCertificates) -> None:
        self._certificates = certificates

        self.create = async_to_streamed_response_wrapper(
            certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            certificates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            certificates.get,
        )
