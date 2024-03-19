# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    OriginCACertificateGetResponse,
    OriginCACertificateListResponse,
    OriginCACertificateCreateResponse,
    OriginCACertificateDeleteResponse,
    origin_ca_certificate_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["OriginCACertificates", "AsyncOriginCACertificates"]


class OriginCACertificates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginCACertificatesWithRawResponse:
        return OriginCACertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginCACertificatesWithStreamingResponse:
        return OriginCACertificatesWithStreamingResponse(self)

    def create(
        self,
        *,
        csr: str | NotGiven = NOT_GIVEN,
        hostnames: Iterable[object] | NotGiven = NOT_GIVEN,
        request_type: Literal["origin-rsa", "origin-ecc", "keyless-certificate"] | NotGiven = NOT_GIVEN,
        requested_validity: Literal[7, 30, 90, 365, 730, 1095, 5475] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OriginCACertificateCreateResponse:
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
        return cast(
            OriginCACertificateCreateResponse,
            self._post(
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginCACertificateCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginCACertificateListResponse]:
        """List all existing Origin CA certificates for a given zone.

        Use your Origin CA
        Key as your User Service Key when calling this endpoint
        ([see above](#requests)).
        """
        return self._get(
            "/certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCACertificateListResponse]], ResultWrapper[OriginCACertificateListResponse]
            ),
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
    ) -> OriginCACertificateDeleteResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OriginCACertificateDeleteResponse], ResultWrapper[OriginCACertificateDeleteResponse]),
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
    ) -> OriginCACertificateGetResponse:
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
        return cast(
            OriginCACertificateGetResponse,
            self._get(
                f"/certificates/{certificate_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginCACertificateGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncOriginCACertificates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginCACertificatesWithRawResponse:
        return AsyncOriginCACertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginCACertificatesWithStreamingResponse:
        return AsyncOriginCACertificatesWithStreamingResponse(self)

    async def create(
        self,
        *,
        csr: str | NotGiven = NOT_GIVEN,
        hostnames: Iterable[object] | NotGiven = NOT_GIVEN,
        request_type: Literal["origin-rsa", "origin-ecc", "keyless-certificate"] | NotGiven = NOT_GIVEN,
        requested_validity: Literal[7, 30, 90, 365, 730, 1095, 5475] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OriginCACertificateCreateResponse:
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
        return cast(
            OriginCACertificateCreateResponse,
            await self._post(
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginCACertificateCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginCACertificateListResponse]:
        """List all existing Origin CA certificates for a given zone.

        Use your Origin CA
        Key as your User Service Key when calling this endpoint
        ([see above](#requests)).
        """
        return await self._get(
            "/certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginCACertificateListResponse]], ResultWrapper[OriginCACertificateListResponse]
            ),
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
    ) -> OriginCACertificateDeleteResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OriginCACertificateDeleteResponse], ResultWrapper[OriginCACertificateDeleteResponse]),
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
    ) -> OriginCACertificateGetResponse:
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
        return cast(
            OriginCACertificateGetResponse,
            await self._get(
                f"/certificates/{certificate_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginCACertificateGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class OriginCACertificatesWithRawResponse:
    def __init__(self, origin_ca_certificates: OriginCACertificates) -> None:
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


class AsyncOriginCACertificatesWithRawResponse:
    def __init__(self, origin_ca_certificates: AsyncOriginCACertificates) -> None:
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


class OriginCACertificatesWithStreamingResponse:
    def __init__(self, origin_ca_certificates: OriginCACertificates) -> None:
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


class AsyncOriginCACertificatesWithStreamingResponse:
    def __init__(self, origin_ca_certificates: AsyncOriginCACertificates) -> None:
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
