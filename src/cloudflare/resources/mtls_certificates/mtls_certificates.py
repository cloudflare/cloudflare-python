# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...types import (
    MTLSCertificateListResponse,
    TLSCertificatesAndHostnamesCertificateObjectPost,
    TLSCertificatesAndHostnamesComponentsSchemasCertificateObject,
    mtls_certificate_create_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .associations import (
    Associations,
    AsyncAssociations,
    AssociationsWithRawResponse,
    AsyncAssociationsWithRawResponse,
    AssociationsWithStreamingResponse,
    AsyncAssociationsWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["MTLSCertificates", "AsyncMTLSCertificates"]


class MTLSCertificates(SyncAPIResource):
    @cached_property
    def associations(self) -> Associations:
        return Associations(self._client)

    @cached_property
    def with_raw_response(self) -> MTLSCertificatesWithRawResponse:
        return MTLSCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MTLSCertificatesWithStreamingResponse:
        return MTLSCertificatesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        ca: bool,
        certificates: str,
        name: str | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesCertificateObjectPost:
        """
        Upload a certificate that you want to use with mTLS-enabled Cloudflare services.

        Args:
          account_id: Identifier

          ca: Indicates whether the certificate is a CA or leaf certificate.

          certificates: The uploaded root CA certificate.

          name: Optional unique name for the certificate. Only used for human readability.

          private_key: The private key for the certificate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/mtls_certificates",
            body=maybe_transform(
                {
                    "ca": ca,
                    "certificates": certificates,
                    "name": name,
                    "private_key": private_key,
                },
                mtls_certificate_create_params.MTLSCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesCertificateObjectPost],
                ResultWrapper[TLSCertificatesAndHostnamesCertificateObjectPost],
            ),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MTLSCertificateListResponse]:
        """
        Lists all mTLS certificates.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/mtls_certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[MTLSCertificateListResponse]], ResultWrapper[MTLSCertificateListResponse]),
        )

    def delete(
        self,
        mtls_certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesComponentsSchemasCertificateObject:
        """
        Deletes the mTLS certificate unless the certificate is in use by one or more
        Cloudflare services.

        Args:
          account_id: Identifier

          mtls_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not mtls_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `mtls_certificate_id` but received {mtls_certificate_id!r}"
            )
        return self._delete(
            f"/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesComponentsSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesComponentsSchemasCertificateObject],
            ),
        )

    def get(
        self,
        mtls_certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesComponentsSchemasCertificateObject:
        """
        Fetches a single mTLS certificate.

        Args:
          account_id: Identifier

          mtls_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not mtls_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `mtls_certificate_id` but received {mtls_certificate_id!r}"
            )
        return self._get(
            f"/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesComponentsSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesComponentsSchemasCertificateObject],
            ),
        )


class AsyncMTLSCertificates(AsyncAPIResource):
    @cached_property
    def associations(self) -> AsyncAssociations:
        return AsyncAssociations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMTLSCertificatesWithRawResponse:
        return AsyncMTLSCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMTLSCertificatesWithStreamingResponse:
        return AsyncMTLSCertificatesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        ca: bool,
        certificates: str,
        name: str | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesCertificateObjectPost:
        """
        Upload a certificate that you want to use with mTLS-enabled Cloudflare services.

        Args:
          account_id: Identifier

          ca: Indicates whether the certificate is a CA or leaf certificate.

          certificates: The uploaded root CA certificate.

          name: Optional unique name for the certificate. Only used for human readability.

          private_key: The private key for the certificate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/mtls_certificates",
            body=await async_maybe_transform(
                {
                    "ca": ca,
                    "certificates": certificates,
                    "name": name,
                    "private_key": private_key,
                },
                mtls_certificate_create_params.MTLSCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesCertificateObjectPost],
                ResultWrapper[TLSCertificatesAndHostnamesCertificateObjectPost],
            ),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MTLSCertificateListResponse]:
        """
        Lists all mTLS certificates.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/mtls_certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[MTLSCertificateListResponse]], ResultWrapper[MTLSCertificateListResponse]),
        )

    async def delete(
        self,
        mtls_certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesComponentsSchemasCertificateObject:
        """
        Deletes the mTLS certificate unless the certificate is in use by one or more
        Cloudflare services.

        Args:
          account_id: Identifier

          mtls_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not mtls_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `mtls_certificate_id` but received {mtls_certificate_id!r}"
            )
        return await self._delete(
            f"/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesComponentsSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesComponentsSchemasCertificateObject],
            ),
        )

    async def get(
        self,
        mtls_certificate_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TLSCertificatesAndHostnamesComponentsSchemasCertificateObject:
        """
        Fetches a single mTLS certificate.

        Args:
          account_id: Identifier

          mtls_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not mtls_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `mtls_certificate_id` but received {mtls_certificate_id!r}"
            )
        return await self._get(
            f"/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TLSCertificatesAndHostnamesComponentsSchemasCertificateObject],
                ResultWrapper[TLSCertificatesAndHostnamesComponentsSchemasCertificateObject],
            ),
        )


class MTLSCertificatesWithRawResponse:
    def __init__(self, mtls_certificates: MTLSCertificates) -> None:
        self._mtls_certificates = mtls_certificates

        self.create = to_raw_response_wrapper(
            mtls_certificates.create,
        )
        self.list = to_raw_response_wrapper(
            mtls_certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            mtls_certificates.delete,
        )
        self.get = to_raw_response_wrapper(
            mtls_certificates.get,
        )

    @cached_property
    def associations(self) -> AssociationsWithRawResponse:
        return AssociationsWithRawResponse(self._mtls_certificates.associations)


class AsyncMTLSCertificatesWithRawResponse:
    def __init__(self, mtls_certificates: AsyncMTLSCertificates) -> None:
        self._mtls_certificates = mtls_certificates

        self.create = async_to_raw_response_wrapper(
            mtls_certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            mtls_certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mtls_certificates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            mtls_certificates.get,
        )

    @cached_property
    def associations(self) -> AsyncAssociationsWithRawResponse:
        return AsyncAssociationsWithRawResponse(self._mtls_certificates.associations)


class MTLSCertificatesWithStreamingResponse:
    def __init__(self, mtls_certificates: MTLSCertificates) -> None:
        self._mtls_certificates = mtls_certificates

        self.create = to_streamed_response_wrapper(
            mtls_certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            mtls_certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            mtls_certificates.delete,
        )
        self.get = to_streamed_response_wrapper(
            mtls_certificates.get,
        )

    @cached_property
    def associations(self) -> AssociationsWithStreamingResponse:
        return AssociationsWithStreamingResponse(self._mtls_certificates.associations)


class AsyncMTLSCertificatesWithStreamingResponse:
    def __init__(self, mtls_certificates: AsyncMTLSCertificates) -> None:
        self._mtls_certificates = mtls_certificates

        self.create = async_to_streamed_response_wrapper(
            mtls_certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            mtls_certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mtls_certificates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            mtls_certificates.get,
        )

    @cached_property
    def associations(self) -> AsyncAssociationsWithStreamingResponse:
        return AsyncAssociationsWithStreamingResponse(self._mtls_certificates.associations)
