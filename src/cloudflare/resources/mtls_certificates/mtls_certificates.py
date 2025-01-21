# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from ...pagination import SyncSinglePage, AsyncSinglePage
from .associations import (
    AssociationsResource,
    AsyncAssociationsResource,
    AssociationsResourceWithRawResponse,
    AsyncAssociationsResourceWithRawResponse,
    AssociationsResourceWithStreamingResponse,
    AsyncAssociationsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.mtls_certificates import mtls_certificate_create_params
from ...types.mtls_certificates.mtls_certificate import MTLSCertificate
from ...types.mtls_certificates.mtls_certificate_create_response import MTLSCertificateCreateResponse

__all__ = ["MTLSCertificatesResource", "AsyncMTLSCertificatesResource"]


class MTLSCertificatesResource(SyncAPIResource):
    @cached_property
    def associations(self) -> AssociationsResource:
        return AssociationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MTLSCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MTLSCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MTLSCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MTLSCertificatesResourceWithStreamingResponse(self)

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
    ) -> Optional[MTLSCertificateCreateResponse]:
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
                post_parser=ResultWrapper[Optional[MTLSCertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MTLSCertificateCreateResponse]], ResultWrapper[MTLSCertificateCreateResponse]),
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
    ) -> SyncSinglePage[MTLSCertificate]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/mtls_certificates",
            page=SyncSinglePage[MTLSCertificate],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MTLSCertificate,
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
    ) -> Optional[MTLSCertificate]:
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
                post_parser=ResultWrapper[Optional[MTLSCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MTLSCertificate]], ResultWrapper[MTLSCertificate]),
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
    ) -> Optional[MTLSCertificate]:
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
                post_parser=ResultWrapper[Optional[MTLSCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MTLSCertificate]], ResultWrapper[MTLSCertificate]),
        )


class AsyncMTLSCertificatesResource(AsyncAPIResource):
    @cached_property
    def associations(self) -> AsyncAssociationsResource:
        return AsyncAssociationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMTLSCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMTLSCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMTLSCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMTLSCertificatesResourceWithStreamingResponse(self)

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
    ) -> Optional[MTLSCertificateCreateResponse]:
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
                post_parser=ResultWrapper[Optional[MTLSCertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MTLSCertificateCreateResponse]], ResultWrapper[MTLSCertificateCreateResponse]),
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
    ) -> AsyncPaginator[MTLSCertificate, AsyncSinglePage[MTLSCertificate]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/mtls_certificates",
            page=AsyncSinglePage[MTLSCertificate],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MTLSCertificate,
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
    ) -> Optional[MTLSCertificate]:
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
                post_parser=ResultWrapper[Optional[MTLSCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MTLSCertificate]], ResultWrapper[MTLSCertificate]),
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
    ) -> Optional[MTLSCertificate]:
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
                post_parser=ResultWrapper[Optional[MTLSCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MTLSCertificate]], ResultWrapper[MTLSCertificate]),
        )


class MTLSCertificatesResourceWithRawResponse:
    def __init__(self, mtls_certificates: MTLSCertificatesResource) -> None:
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
    def associations(self) -> AssociationsResourceWithRawResponse:
        return AssociationsResourceWithRawResponse(self._mtls_certificates.associations)


class AsyncMTLSCertificatesResourceWithRawResponse:
    def __init__(self, mtls_certificates: AsyncMTLSCertificatesResource) -> None:
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
    def associations(self) -> AsyncAssociationsResourceWithRawResponse:
        return AsyncAssociationsResourceWithRawResponse(self._mtls_certificates.associations)


class MTLSCertificatesResourceWithStreamingResponse:
    def __init__(self, mtls_certificates: MTLSCertificatesResource) -> None:
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
    def associations(self) -> AssociationsResourceWithStreamingResponse:
        return AssociationsResourceWithStreamingResponse(self._mtls_certificates.associations)


class AsyncMTLSCertificatesResourceWithStreamingResponse:
    def __init__(self, mtls_certificates: AsyncMTLSCertificatesResource) -> None:
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
    def associations(self) -> AsyncAssociationsResourceWithStreamingResponse:
        return AsyncAssociationsResourceWithStreamingResponse(self._mtls_certificates.associations)
