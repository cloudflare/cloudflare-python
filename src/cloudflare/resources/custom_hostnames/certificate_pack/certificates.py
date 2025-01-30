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
from ...._base_client import make_request_options
from ....types.custom_hostnames.certificate_pack import certificate_update_params
from ....types.custom_hostnames.certificate_pack.certificate_delete_response import CertificateDeleteResponse
from ....types.custom_hostnames.certificate_pack.certificate_update_response import CertificateUpdateResponse

__all__ = ["CertificatesResource", "AsyncCertificatesResource"]


class CertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CertificatesResourceWithStreamingResponse(self)

    def update(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        custom_hostname_id: str,
        certificate_pack_id: str,
        custom_certificate: str,
        custom_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateUpdateResponse]:
        """
        Replace a single custom certificate within a certificate pack that contains two
        bundled certificates. The replacement must adhere to the following constraints.
        You can only replace an RSA certificate with another RSA certificate or an ECDSA
        certificate with another ECDSA certificate.

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          certificate_pack_id: Identifier

          certificate_id: Identifier

          custom_certificate: If a custom uploaded certificate is used.

          custom_key: The key for a custom uploaded certificate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return self._put(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}",
            body=maybe_transform(
                {
                    "custom_certificate": custom_certificate,
                    "custom_key": custom_key,
                },
                certificate_update_params.CertificateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CertificateUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateUpdateResponse]], ResultWrapper[CertificateUpdateResponse]),
        )

    def delete(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        custom_hostname_id: str,
        certificate_pack_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateDeleteResponse:
        """
        Delete a single custom certificate from a certificate pack that contains two
        bundled certificates. Deletion is subject to the following constraints. You
        cannot delete a certificate if it is the only remaining certificate in the pack.
        At least one certificate must remain in the pack.

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          certificate_pack_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return self._delete(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CertificateDeleteResponse,
        )


class AsyncCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCertificatesResourceWithStreamingResponse(self)

    async def update(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        custom_hostname_id: str,
        certificate_pack_id: str,
        custom_certificate: str,
        custom_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateUpdateResponse]:
        """
        Replace a single custom certificate within a certificate pack that contains two
        bundled certificates. The replacement must adhere to the following constraints.
        You can only replace an RSA certificate with another RSA certificate or an ECDSA
        certificate with another ECDSA certificate.

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          certificate_pack_id: Identifier

          certificate_id: Identifier

          custom_certificate: If a custom uploaded certificate is used.

          custom_key: The key for a custom uploaded certificate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return await self._put(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}",
            body=await async_maybe_transform(
                {
                    "custom_certificate": custom_certificate,
                    "custom_key": custom_key,
                },
                certificate_update_params.CertificateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CertificateUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificateUpdateResponse]], ResultWrapper[CertificateUpdateResponse]),
        )

    async def delete(
        self,
        certificate_id: str,
        *,
        zone_id: str,
        custom_hostname_id: str,
        certificate_pack_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateDeleteResponse:
        """
        Delete a single custom certificate from a certificate pack that contains two
        bundled certificates. Deletion is subject to the following constraints. You
        cannot delete a certificate if it is the only remaining certificate in the pack.
        At least one certificate must remain in the pack.

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          certificate_pack_id: Identifier

          certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        if not certificate_id:
            raise ValueError(f"Expected a non-empty value for `certificate_id` but received {certificate_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CertificateDeleteResponse,
        )


class CertificatesResourceWithRawResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
        self._certificates = certificates

        self.update = to_raw_response_wrapper(
            certificates.update,
        )
        self.delete = to_raw_response_wrapper(
            certificates.delete,
        )


class AsyncCertificatesResourceWithRawResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
        self._certificates = certificates

        self.update = async_to_raw_response_wrapper(
            certificates.update,
        )
        self.delete = async_to_raw_response_wrapper(
            certificates.delete,
        )


class CertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: CertificatesResource) -> None:
        self._certificates = certificates

        self.update = to_streamed_response_wrapper(
            certificates.update,
        )
        self.delete = to_streamed_response_wrapper(
            certificates.delete,
        )


class AsyncCertificatesResourceWithStreamingResponse:
    def __init__(self, certificates: AsyncCertificatesResource) -> None:
        self._certificates = certificates

        self.update = async_to_streamed_response_wrapper(
            certificates.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            certificates.delete,
        )
