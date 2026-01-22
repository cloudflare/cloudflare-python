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
from ...types.origin_tls_client_auth import zone_certificate_create_params
from ...types.origin_tls_client_auth.zone_certificate_get_response import ZoneCertificateGetResponse
from ...types.origin_tls_client_auth.zone_certificate_list_response import ZoneCertificateListResponse
from ...types.origin_tls_client_auth.zone_certificate_create_response import ZoneCertificateCreateResponse
from ...types.origin_tls_client_auth.zone_certificate_delete_response import ZoneCertificateDeleteResponse

__all__ = ["ZoneCertificatesResource", "AsyncZoneCertificatesResource"]


class ZoneCertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZoneCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ZoneCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZoneCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ZoneCertificatesResourceWithStreamingResponse(self)

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
    ) -> Optional[ZoneCertificateCreateResponse]:
        """
        Upload your own certificate you want Cloudflare to use for edge-to-origin
        communication to override the shared certificate. Please note that it is
        important to keep only one certificate active. Also, make sure to enable
        zone-level authenticated origin pulls by making a PUT call to settings endpoint
        to see the uploaded certificate in use.

        Args:
          zone_id: Identifier.

          certificate: The zone's leaf certificate.

          private_key: The zone's private key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/origin_tls_client_auth",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "private_key": private_key,
                },
                zone_certificate_create_params.ZoneCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneCertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneCertificateCreateResponse]], ResultWrapper[ZoneCertificateCreateResponse]),
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
    ) -> SyncSinglePage[ZoneCertificateListResponse]:
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
            f"/zones/{zone_id}/origin_tls_client_auth",
            page=SyncSinglePage[ZoneCertificateListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ZoneCertificateListResponse,
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
    ) -> Optional[ZoneCertificateDeleteResponse]:
        """
        Delete Certificate

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
            f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneCertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneCertificateDeleteResponse]], ResultWrapper[ZoneCertificateDeleteResponse]),
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
    ) -> Optional[ZoneCertificateGetResponse]:
        """
        Get Certificate Details

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
            f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneCertificateGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneCertificateGetResponse]], ResultWrapper[ZoneCertificateGetResponse]),
        )


class AsyncZoneCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZoneCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZoneCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZoneCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncZoneCertificatesResourceWithStreamingResponse(self)

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
    ) -> Optional[ZoneCertificateCreateResponse]:
        """
        Upload your own certificate you want Cloudflare to use for edge-to-origin
        communication to override the shared certificate. Please note that it is
        important to keep only one certificate active. Also, make sure to enable
        zone-level authenticated origin pulls by making a PUT call to settings endpoint
        to see the uploaded certificate in use.

        Args:
          zone_id: Identifier.

          certificate: The zone's leaf certificate.

          private_key: The zone's private key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/origin_tls_client_auth",
            body=await async_maybe_transform(
                {
                    "certificate": certificate,
                    "private_key": private_key,
                },
                zone_certificate_create_params.ZoneCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneCertificateCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneCertificateCreateResponse]], ResultWrapper[ZoneCertificateCreateResponse]),
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
    ) -> AsyncPaginator[ZoneCertificateListResponse, AsyncSinglePage[ZoneCertificateListResponse]]:
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
            f"/zones/{zone_id}/origin_tls_client_auth",
            page=AsyncSinglePage[ZoneCertificateListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ZoneCertificateListResponse,
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
    ) -> Optional[ZoneCertificateDeleteResponse]:
        """
        Delete Certificate

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
            f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneCertificateDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneCertificateDeleteResponse]], ResultWrapper[ZoneCertificateDeleteResponse]),
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
    ) -> Optional[ZoneCertificateGetResponse]:
        """
        Get Certificate Details

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
            f"/zones/{zone_id}/origin_tls_client_auth/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ZoneCertificateGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneCertificateGetResponse]], ResultWrapper[ZoneCertificateGetResponse]),
        )


class ZoneCertificatesResourceWithRawResponse:
    def __init__(self, zone_certificates: ZoneCertificatesResource) -> None:
        self._zone_certificates = zone_certificates

        self.create = to_raw_response_wrapper(
            zone_certificates.create,
        )
        self.list = to_raw_response_wrapper(
            zone_certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            zone_certificates.delete,
        )
        self.get = to_raw_response_wrapper(
            zone_certificates.get,
        )


class AsyncZoneCertificatesResourceWithRawResponse:
    def __init__(self, zone_certificates: AsyncZoneCertificatesResource) -> None:
        self._zone_certificates = zone_certificates

        self.create = async_to_raw_response_wrapper(
            zone_certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            zone_certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            zone_certificates.delete,
        )
        self.get = async_to_raw_response_wrapper(
            zone_certificates.get,
        )


class ZoneCertificatesResourceWithStreamingResponse:
    def __init__(self, zone_certificates: ZoneCertificatesResource) -> None:
        self._zone_certificates = zone_certificates

        self.create = to_streamed_response_wrapper(
            zone_certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            zone_certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            zone_certificates.delete,
        )
        self.get = to_streamed_response_wrapper(
            zone_certificates.get,
        )


class AsyncZoneCertificatesResourceWithStreamingResponse:
    def __init__(self, zone_certificates: AsyncZoneCertificatesResource) -> None:
        self._zone_certificates = zone_certificates

        self.create = async_to_streamed_response_wrapper(
            zone_certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            zone_certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            zone_certificates.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            zone_certificates.get,
        )
