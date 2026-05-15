# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.access import saml_certificate_list_params
from ....types.zero_trust.access.saml_certificate_get_response import SAMLCertificateGetResponse
from ....types.zero_trust.access.saml_certificate_list_response import SAMLCertificateListResponse
from ....types.zero_trust.access.saml_certificate_rotate_response import SAMLCertificateRotateResponse

__all__ = ["SAMLCertificatesResource", "AsyncSAMLCertificatesResource"]


class SAMLCertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SAMLCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SAMLCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SAMLCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SAMLCertificatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        id: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[SAMLCertificateListResponse]:
        """
        Returns a paginated list of the organization's SAML encryption certificate sets.
        Each certificate set includes the current and (if present) previous
        certificates.

        Args:
          account_id: Identifier.

          id: Filter by SAML certificate set UID. Accepts a comma-separated list of UIDs.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/access/saml_certificates", account_id=account_id),
            page=SyncV4PagePaginationArray[SAMLCertificateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "page": page,
                        "per_page": per_page,
                    },
                    saml_certificate_list_params.SAMLCertificateListParams,
                ),
            ),
            model=SAMLCertificateListResponse,
        )

    def get(
        self,
        saml_cert_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SAMLCertificateGetResponse]:
        """
        Retrieves a specific SAML encryption certificate set by its UID, including both
        current and previous certificates if available.

        Args:
          account_id: Identifier.

          saml_cert_set_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not saml_cert_set_id:
            raise ValueError(f"Expected a non-empty value for `saml_cert_set_id` but received {saml_cert_set_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/access/saml_certificates/{saml_cert_set_id}",
                account_id=account_id,
                saml_cert_set_id=saml_cert_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SAMLCertificateGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SAMLCertificateGetResponse]], ResultWrapper[SAMLCertificateGetResponse]),
        )

    def get_pem(
        self,
        saml_cert_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Downloads the current SAML encryption certificate's public key in PEM format for
        the specified certificate set. This endpoint is useful for providing the
        certificate to Identity Providers for SAML assertion encryption configuration.

        Args:
          account_id: Identifier.

          saml_cert_set_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not saml_cert_set_id:
            raise ValueError(f"Expected a non-empty value for `saml_cert_set_id` but received {saml_cert_set_id!r}")
        extra_headers = {"Accept": "application/x-pem-file", **(extra_headers or {})}
        return self._get(
            path_template(
                "/accounts/{account_id}/access/saml_certificates/{saml_cert_set_id}/pem",
                account_id=account_id,
                saml_cert_set_id=saml_cert_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def rotate(
        self,
        saml_cert_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SAMLCertificateRotateResponse]:
        """
        Rotates the SAML encryption certificates within the specified certificate set.
        This generates a new certificate and moves the current certificate to the
        previous slot. If a previous certificate exists, it will be deactivated and
        removed.

        This endpoint ensures zero-downtime rotation by maintaining both current and
        previous certificates during the transition period, allowing IdPs time to update
        their configurations. Automated rotation happens 30 days before a current
        certificate's expiration.

        Args:
          account_id: Identifier.

          saml_cert_set_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not saml_cert_set_id:
            raise ValueError(f"Expected a non-empty value for `saml_cert_set_id` but received {saml_cert_set_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/access/saml_certificates/{saml_cert_set_id}/rotate",
                account_id=account_id,
                saml_cert_set_id=saml_cert_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SAMLCertificateRotateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SAMLCertificateRotateResponse]], ResultWrapper[SAMLCertificateRotateResponse]),
        )


class AsyncSAMLCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSAMLCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSAMLCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSAMLCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSAMLCertificatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        id: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SAMLCertificateListResponse, AsyncV4PagePaginationArray[SAMLCertificateListResponse]]:
        """
        Returns a paginated list of the organization's SAML encryption certificate sets.
        Each certificate set includes the current and (if present) previous
        certificates.

        Args:
          account_id: Identifier.

          id: Filter by SAML certificate set UID. Accepts a comma-separated list of UIDs.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/access/saml_certificates", account_id=account_id),
            page=AsyncV4PagePaginationArray[SAMLCertificateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "page": page,
                        "per_page": per_page,
                    },
                    saml_certificate_list_params.SAMLCertificateListParams,
                ),
            ),
            model=SAMLCertificateListResponse,
        )

    async def get(
        self,
        saml_cert_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SAMLCertificateGetResponse]:
        """
        Retrieves a specific SAML encryption certificate set by its UID, including both
        current and previous certificates if available.

        Args:
          account_id: Identifier.

          saml_cert_set_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not saml_cert_set_id:
            raise ValueError(f"Expected a non-empty value for `saml_cert_set_id` but received {saml_cert_set_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/access/saml_certificates/{saml_cert_set_id}",
                account_id=account_id,
                saml_cert_set_id=saml_cert_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SAMLCertificateGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SAMLCertificateGetResponse]], ResultWrapper[SAMLCertificateGetResponse]),
        )

    async def get_pem(
        self,
        saml_cert_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Downloads the current SAML encryption certificate's public key in PEM format for
        the specified certificate set. This endpoint is useful for providing the
        certificate to Identity Providers for SAML assertion encryption configuration.

        Args:
          account_id: Identifier.

          saml_cert_set_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not saml_cert_set_id:
            raise ValueError(f"Expected a non-empty value for `saml_cert_set_id` but received {saml_cert_set_id!r}")
        extra_headers = {"Accept": "application/x-pem-file", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/accounts/{account_id}/access/saml_certificates/{saml_cert_set_id}/pem",
                account_id=account_id,
                saml_cert_set_id=saml_cert_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def rotate(
        self,
        saml_cert_set_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SAMLCertificateRotateResponse]:
        """
        Rotates the SAML encryption certificates within the specified certificate set.
        This generates a new certificate and moves the current certificate to the
        previous slot. If a previous certificate exists, it will be deactivated and
        removed.

        This endpoint ensures zero-downtime rotation by maintaining both current and
        previous certificates during the transition period, allowing IdPs time to update
        their configurations. Automated rotation happens 30 days before a current
        certificate's expiration.

        Args:
          account_id: Identifier.

          saml_cert_set_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not saml_cert_set_id:
            raise ValueError(f"Expected a non-empty value for `saml_cert_set_id` but received {saml_cert_set_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/access/saml_certificates/{saml_cert_set_id}/rotate",
                account_id=account_id,
                saml_cert_set_id=saml_cert_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SAMLCertificateRotateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SAMLCertificateRotateResponse]], ResultWrapper[SAMLCertificateRotateResponse]),
        )


class SAMLCertificatesResourceWithRawResponse:
    def __init__(self, saml_certificates: SAMLCertificatesResource) -> None:
        self._saml_certificates = saml_certificates

        self.list = to_raw_response_wrapper(
            saml_certificates.list,
        )
        self.get = to_raw_response_wrapper(
            saml_certificates.get,
        )
        self.get_pem = to_custom_raw_response_wrapper(
            saml_certificates.get_pem,
            BinaryAPIResponse,
        )
        self.rotate = to_raw_response_wrapper(
            saml_certificates.rotate,
        )


class AsyncSAMLCertificatesResourceWithRawResponse:
    def __init__(self, saml_certificates: AsyncSAMLCertificatesResource) -> None:
        self._saml_certificates = saml_certificates

        self.list = async_to_raw_response_wrapper(
            saml_certificates.list,
        )
        self.get = async_to_raw_response_wrapper(
            saml_certificates.get,
        )
        self.get_pem = async_to_custom_raw_response_wrapper(
            saml_certificates.get_pem,
            AsyncBinaryAPIResponse,
        )
        self.rotate = async_to_raw_response_wrapper(
            saml_certificates.rotate,
        )


class SAMLCertificatesResourceWithStreamingResponse:
    def __init__(self, saml_certificates: SAMLCertificatesResource) -> None:
        self._saml_certificates = saml_certificates

        self.list = to_streamed_response_wrapper(
            saml_certificates.list,
        )
        self.get = to_streamed_response_wrapper(
            saml_certificates.get,
        )
        self.get_pem = to_custom_streamed_response_wrapper(
            saml_certificates.get_pem,
            StreamedBinaryAPIResponse,
        )
        self.rotate = to_streamed_response_wrapper(
            saml_certificates.rotate,
        )


class AsyncSAMLCertificatesResourceWithStreamingResponse:
    def __init__(self, saml_certificates: AsyncSAMLCertificatesResource) -> None:
        self._saml_certificates = saml_certificates

        self.list = async_to_streamed_response_wrapper(
            saml_certificates.list,
        )
        self.get = async_to_streamed_response_wrapper(
            saml_certificates.get,
        )
        self.get_pem = async_to_custom_streamed_response_wrapper(
            saml_certificates.get_pem,
            AsyncStreamedBinaryAPIResponse,
        )
        self.rotate = async_to_streamed_response_wrapper(
            saml_certificates.rotate,
        )
