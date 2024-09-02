# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.origin_tls_client_auth.hostnames.certificate_create_response import CertificateCreateResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ...._base_client import make_request_options, AsyncPaginator

from ....types.origin_tls_client_auth.authenticated_origin_pull import AuthenticatedOriginPull

from ....pagination import SyncSinglePage, AsyncSinglePage

from ....types.origin_tls_client_auth.hostnames.certificate_delete_response import CertificateDeleteResponse

from ....types.origin_tls_client_auth.hostnames.certificate_get_response import CertificateGetResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.origin_tls_client_auth.hostnames import certificate_create_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CertificatesResource", "AsyncCertificatesResource"]


class CertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self)

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
    ) -> Optional[CertificateCreateResponse]:
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
                post_parser=ResultWrapper[Optional[CertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateCreateResponse]], ResultWrapper[CertificateCreateResponse]),
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
    ) -> SyncSinglePage[AuthenticatedOriginPull]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates",
            page=SyncSinglePage[AuthenticatedOriginPull],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AuthenticatedOriginPull,
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
    ) -> Optional[CertificateDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[CertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateDeleteResponse]], ResultWrapper[CertificateDeleteResponse]),
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
    ) -> Optional[CertificateGetResponse]:
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
                post_parser=ResultWrapper[Optional[CertificateGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateGetResponse]], ResultWrapper[CertificateGetResponse]),
        )


class AsyncCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self)

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
    ) -> Optional[CertificateCreateResponse]:
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
                post_parser=ResultWrapper[Optional[CertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateCreateResponse]], ResultWrapper[CertificateCreateResponse]),
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
    ) -> AsyncPaginator[AuthenticatedOriginPull, AsyncSinglePage[AuthenticatedOriginPull]]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates",
            page=AsyncSinglePage[AuthenticatedOriginPull],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AuthenticatedOriginPull,
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
    ) -> Optional[CertificateDeleteResponse]:
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
                post_parser=ResultWrapper[Optional[CertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateDeleteResponse]], ResultWrapper[CertificateDeleteResponse]),
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
    ) -> Optional[CertificateGetResponse]:
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
                post_parser=ResultWrapper[Optional[CertificateGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateGetResponse]], ResultWrapper[CertificateGetResponse]),
        )


class CertificatesResourceWithRawResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
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


class AsyncCertificatesResourceWithRawResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
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


class CertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
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


class AsyncCertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
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
