# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.origin_ca_certificates.origin_ca_certificate import OriginCACertificate

from .._wrappers import ResultWrapper

from .._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, List

from .._base_client import make_request_options, AsyncPaginator

from ..types.shared.certificate_request_type import CertificateRequestType

from ..types.ssl.request_validity import RequestValidity

from ..pagination import SyncSinglePage, AsyncSinglePage

from ..types.origin_ca_certificates.origin_ca_certificate_delete_response import OriginCACertificateDeleteResponse

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types.origin_ca_certificates import origin_ca_certificate_create_params
from ..types.origin_ca_certificates import origin_ca_certificate_list_params
from ..types import shared
from ..types.ssl import RequestValidity
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["OriginCACertificatesResource", "AsyncOriginCACertificatesResource"]


class OriginCACertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginCACertificatesResourceWithRawResponse:
        return OriginCACertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginCACertificatesResourceWithStreamingResponse:
        return OriginCACertificatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        csr: str | NotGiven = NOT_GIVEN,
        hostnames: List[str] | NotGiven = NOT_GIVEN,
        request_type: CertificateRequestType | NotGiven = NOT_GIVEN,
        requested_validity: RequestValidity | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginCACertificate]:
        """Create an Origin CA certificate.

        Use your Origin CA Key as your User Service Key
        when calling this endpoint ([see above](#requests)).

        Args:
          csr: The Certificate Signing Request (CSR). Must be newline-encoded.

          hostnames: Array of hostnames or wildcard names (e.g., \\**.example.com) bound to the
              certificate.

          request_type: Signature type desired on certificate ("origin-rsa" (rsa), "origin-ecc" (ecdsa),
              or "keyless-certificate" (for Keyless SSL servers).

          requested_validity: The number of days for which the certificate should be valid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/certificates",
            body=maybe_transform(
                {
                    "csr": csr,
                    "hostnames": hostnames,
                    "request_type": request_type,
                    "requested_validity": requested_validity,
                },
                origin_ca_certificate_create_params.OriginCACertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCACertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCACertificate]], ResultWrapper[OriginCACertificate]),
        )

    def list(
        self,
        *,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[OriginCACertificate]:
        """List all existing Origin CA certificates for a given zone.

        Use your Origin CA
        Key as your User Service Key when calling this endpoint
        ([see above](#requests)).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/certificates",
            page=SyncSinglePage[OriginCACertificate],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"zone_id": zone_id}, origin_ca_certificate_list_params.OriginCACertificateListParams
                ),
            ),
            model=OriginCACertificate,
        )

    def delete(
        self,
        certificate_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginCACertificateDeleteResponse]:
        """Revoke an existing Origin CA certificate by its serial number.

        Use your Origin
        CA Key as your User Service Key when calling this endpoint
        ([see above](#requests)).

        Args:
          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return self._delete(
            f"/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCACertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCACertificateDeleteResponse]], ResultWrapper[OriginCACertificateDeleteResponse]
            ),
        )

    def get(
        self,
        certificate_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginCACertificate]:
        """Get an existing Origin CA certificate by its serial number.

        Use your Origin CA
        Key as your User Service Key when calling this endpoint
        ([see above](#requests)).

        Args:
          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return self._get(
            f"/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCACertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCACertificate]], ResultWrapper[OriginCACertificate]),
        )


class AsyncOriginCACertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginCACertificatesResourceWithRawResponse:
        return AsyncOriginCACertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginCACertificatesResourceWithStreamingResponse:
        return AsyncOriginCACertificatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        csr: str | NotGiven = NOT_GIVEN,
        hostnames: List[str] | NotGiven = NOT_GIVEN,
        request_type: CertificateRequestType | NotGiven = NOT_GIVEN,
        requested_validity: RequestValidity | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginCACertificate]:
        """Create an Origin CA certificate.

        Use your Origin CA Key as your User Service Key
        when calling this endpoint ([see above](#requests)).

        Args:
          csr: The Certificate Signing Request (CSR). Must be newline-encoded.

          hostnames: Array of hostnames or wildcard names (e.g., \\**.example.com) bound to the
              certificate.

          request_type: Signature type desired on certificate ("origin-rsa" (rsa), "origin-ecc" (ecdsa),
              or "keyless-certificate" (for Keyless SSL servers).

          requested_validity: The number of days for which the certificate should be valid.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/certificates",
            body=await async_maybe_transform(
                {
                    "csr": csr,
                    "hostnames": hostnames,
                    "request_type": request_type,
                    "requested_validity": requested_validity,
                },
                origin_ca_certificate_create_params.OriginCACertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCACertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCACertificate]], ResultWrapper[OriginCACertificate]),
        )

    def list(
        self,
        *,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OriginCACertificate, AsyncSinglePage[OriginCACertificate]]:
        """List all existing Origin CA certificates for a given zone.

        Use your Origin CA
        Key as your User Service Key when calling this endpoint
        ([see above](#requests)).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/certificates",
            page=AsyncSinglePage[OriginCACertificate],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"zone_id": zone_id}, origin_ca_certificate_list_params.OriginCACertificateListParams
                ),
            ),
            model=OriginCACertificate,
        )

    async def delete(
        self,
        certificate_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginCACertificateDeleteResponse]:
        """Revoke an existing Origin CA certificate by its serial number.

        Use your Origin
        CA Key as your User Service Key when calling this endpoint
        ([see above](#requests)).

        Args:
          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return await self._delete(
            f"/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCACertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCACertificateDeleteResponse]], ResultWrapper[OriginCACertificateDeleteResponse]
            ),
        )

    async def get(
        self,
        certificate_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginCACertificate]:
        """Get an existing Origin CA certificate by its serial number.

        Use your Origin CA
        Key as your User Service Key when calling this endpoint
        ([see above](#requests)).

        Args:
          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return await self._get(
            f"/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginCACertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OriginCACertificate]], ResultWrapper[OriginCACertificate]),
        )


class OriginCACertificatesResourceWithRawResponse:
    def __init__(self, origin_ca_certificates: OriginCACertificatesResource) -> None:
        self._origin_ca_certificates = origin_ca_certificates

        self.create = to_raw_response_wrapper(
            origin_ca_certificates.create,
        )
        self.list = to_raw_response_wrapper(
            origin_ca_certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            origin_ca_certificates.delete,
        )
        self.get = to_raw_response_wrapper(
            origin_ca_certificates.get,
        )


class AsyncOriginCACertificatesResourceWithRawResponse:
    def __init__(self, origin_ca_certificates: AsyncOriginCACertificatesResource) -> None:
        self._origin_ca_certificates = origin_ca_certificates

        self.create = async_to_raw_response_wrapper(
            origin_ca_certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            origin_ca_certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            origin_ca_certificates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            origin_ca_certificates.get,
        )


class OriginCACertificatesResourceWithStreamingResponse:
    def __init__(self, origin_ca_certificates: OriginCACertificatesResource) -> None:
        self._origin_ca_certificates = origin_ca_certificates

        self.create = to_streamed_response_wrapper(
            origin_ca_certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            origin_ca_certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            origin_ca_certificates.delete,
        )
        self.get = to_streamed_response_wrapper(
            origin_ca_certificates.get,
        )


class AsyncOriginCACertificatesResourceWithStreamingResponse:
    def __init__(self, origin_ca_certificates: AsyncOriginCACertificatesResource) -> None:
        self._origin_ca_certificates = origin_ca_certificates

        self.create = async_to_streamed_response_wrapper(
            origin_ca_certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            origin_ca_certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            origin_ca_certificates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            origin_ca_certificates.get,
        )
