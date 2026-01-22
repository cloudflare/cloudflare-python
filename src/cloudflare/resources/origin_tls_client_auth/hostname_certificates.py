# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ..._base_client import AsyncPaginator, make_request_options
from ...types.origin_tls_client_auth import hostname_certificate_create_params
from ...types.origin_tls_client_auth.hostname_certificate_get_response import HostnameCertificateGetResponse
from ...types.origin_tls_client_auth.hostname_certificate_list_response import HostnameCertificateListResponse
from ...types.origin_tls_client_auth.hostname_certificate_create_response import HostnameCertificateCreateResponse
from ...types.origin_tls_client_auth.hostname_certificate_delete_response import HostnameCertificateDeleteResponse

__all__ = ["HostnameCertificatesResource", "AsyncHostnameCertificatesResource"]


class HostnameCertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HostnameCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HostnameCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnameCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HostnameCertificatesResourceWithStreamingResponse(self)

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[HostnameCertificateCreateResponse]:
        """Upload a certificate to be used for client authentication on a hostname.

        10
        hostname certificates per zone are allowed.

        Args:
          zone_id: Identifier.

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
                hostname_certificate_create_params.HostnameCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HostnameCertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HostnameCertificateCreateResponse]], ResultWrapper[HostnameCertificateCreateResponse]
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[HostnameCertificateListResponse]:
        """
        List Certificates

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates",
            page=SyncSinglePage[HostnameCertificateListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=HostnameCertificateListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[HostnameCertificateDeleteResponse]:
        """
        Delete Hostname Client Certificate

        Args:
          zone_id: Identifier.

          certificate_id: Identifier.

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
                post_parser=ResultWrapper[Optional[HostnameCertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HostnameCertificateDeleteResponse]], ResultWrapper[HostnameCertificateDeleteResponse]
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[HostnameCertificateGetResponse]:
        """
        Get the certificate by ID to be used for client authentication on a hostname.

        Args:
          zone_id: Identifier.

          certificate_id: Identifier.

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
                post_parser=ResultWrapper[Optional[HostnameCertificateGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameCertificateGetResponse]], ResultWrapper[HostnameCertificateGetResponse]),
        )


class AsyncHostnameCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHostnameCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostnameCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnameCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHostnameCertificatesResourceWithStreamingResponse(self)

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[HostnameCertificateCreateResponse]:
        """Upload a certificate to be used for client authentication on a hostname.

        10
        hostname certificates per zone are allowed.

        Args:
          zone_id: Identifier.

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
                hostname_certificate_create_params.HostnameCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HostnameCertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HostnameCertificateCreateResponse]], ResultWrapper[HostnameCertificateCreateResponse]
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[HostnameCertificateListResponse, AsyncSinglePage[HostnameCertificateListResponse]]:
        """
        List Certificates

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates",
            page=AsyncSinglePage[HostnameCertificateListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=HostnameCertificateListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[HostnameCertificateDeleteResponse]:
        """
        Delete Hostname Client Certificate

        Args:
          zone_id: Identifier.

          certificate_id: Identifier.

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
                post_parser=ResultWrapper[Optional[HostnameCertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HostnameCertificateDeleteResponse]], ResultWrapper[HostnameCertificateDeleteResponse]
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[HostnameCertificateGetResponse]:
        """
        Get the certificate by ID to be used for client authentication on a hostname.

        Args:
          zone_id: Identifier.

          certificate_id: Identifier.

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
                post_parser=ResultWrapper[Optional[HostnameCertificateGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameCertificateGetResponse]], ResultWrapper[HostnameCertificateGetResponse]),
        )


class HostnameCertificatesResourceWithRawResponse:
    def __init__(self, hostname_certificates: HostnameCertificatesResource) -> None:
        self._hostname_certificates = hostname_certificates

        self.create = to_raw_response_wrapper(
            hostname_certificates.create,
        )
        self.list = to_raw_response_wrapper(
            hostname_certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            hostname_certificates.delete,
        )
        self.get = to_raw_response_wrapper(
            hostname_certificates.get,
        )


class AsyncHostnameCertificatesResourceWithRawResponse:
    def __init__(self, hostname_certificates: AsyncHostnameCertificatesResource) -> None:
        self._hostname_certificates = hostname_certificates

        self.create = async_to_raw_response_wrapper(
            hostname_certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            hostname_certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            hostname_certificates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            hostname_certificates.get,
        )


class HostnameCertificatesResourceWithStreamingResponse:
    def __init__(self, hostname_certificates: HostnameCertificatesResource) -> None:
        self._hostname_certificates = hostname_certificates

        self.create = to_streamed_response_wrapper(
            hostname_certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            hostname_certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            hostname_certificates.delete,
        )
        self.get = to_streamed_response_wrapper(
            hostname_certificates.get,
        )


class AsyncHostnameCertificatesResourceWithStreamingResponse:
    def __init__(self, hostname_certificates: AsyncHostnameCertificatesResource) -> None:
        self._hostname_certificates = hostname_certificates

        self.create = async_to_streamed_response_wrapper(
            hostname_certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            hostname_certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            hostname_certificates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            hostname_certificates.get,
        )
