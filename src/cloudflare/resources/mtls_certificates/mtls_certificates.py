# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...types import (
    MtlsCertificateGetResponse,
    MtlsCertificateListResponse,
    MtlsCertificateDeleteResponse,
    MtlsCertificateUpdateResponse,
    mtls_certificate_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
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

__all__ = ["MtlsCertificates", "AsyncMtlsCertificates"]


class MtlsCertificates(SyncAPIResource):
    @cached_property
    def associations(self) -> Associations:
        return Associations(self._client)

    @cached_property
    def with_raw_response(self) -> MtlsCertificatesWithRawResponse:
        return MtlsCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MtlsCertificatesWithStreamingResponse:
        return MtlsCertificatesWithStreamingResponse(self)

    def update(
        self,
        account_id: str,
        *,
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
    ) -> MtlsCertificateUpdateResponse:
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
                mtls_certificate_update_params.MtlsCertificateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MtlsCertificateUpdateResponse], ResultWrapper[MtlsCertificateUpdateResponse]),
        )

    def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MtlsCertificateListResponse]:
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
            cast_to=cast(Type[Optional[MtlsCertificateListResponse]], ResultWrapper[MtlsCertificateListResponse]),
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
    ) -> MtlsCertificateDeleteResponse:
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
            cast_to=cast(Type[MtlsCertificateDeleteResponse], ResultWrapper[MtlsCertificateDeleteResponse]),
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
    ) -> MtlsCertificateGetResponse:
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
            cast_to=cast(Type[MtlsCertificateGetResponse], ResultWrapper[MtlsCertificateGetResponse]),
        )


class AsyncMtlsCertificates(AsyncAPIResource):
    @cached_property
    def associations(self) -> AsyncAssociations:
        return AsyncAssociations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMtlsCertificatesWithRawResponse:
        return AsyncMtlsCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMtlsCertificatesWithStreamingResponse:
        return AsyncMtlsCertificatesWithStreamingResponse(self)

    async def update(
        self,
        account_id: str,
        *,
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
    ) -> MtlsCertificateUpdateResponse:
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
            body=maybe_transform(
                {
                    "ca": ca,
                    "certificates": certificates,
                    "name": name,
                    "private_key": private_key,
                },
                mtls_certificate_update_params.MtlsCertificateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MtlsCertificateUpdateResponse], ResultWrapper[MtlsCertificateUpdateResponse]),
        )

    async def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MtlsCertificateListResponse]:
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
            cast_to=cast(Type[Optional[MtlsCertificateListResponse]], ResultWrapper[MtlsCertificateListResponse]),
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
    ) -> MtlsCertificateDeleteResponse:
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
            cast_to=cast(Type[MtlsCertificateDeleteResponse], ResultWrapper[MtlsCertificateDeleteResponse]),
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
    ) -> MtlsCertificateGetResponse:
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
            cast_to=cast(Type[MtlsCertificateGetResponse], ResultWrapper[MtlsCertificateGetResponse]),
        )


class MtlsCertificatesWithRawResponse:
    def __init__(self, mtls_certificates: MtlsCertificates) -> None:
        self._mtls_certificates = mtls_certificates

        self.update = to_raw_response_wrapper(
            mtls_certificates.update,
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


class AsyncMtlsCertificatesWithRawResponse:
    def __init__(self, mtls_certificates: AsyncMtlsCertificates) -> None:
        self._mtls_certificates = mtls_certificates

        self.update = async_to_raw_response_wrapper(
            mtls_certificates.update,
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


class MtlsCertificatesWithStreamingResponse:
    def __init__(self, mtls_certificates: MtlsCertificates) -> None:
        self._mtls_certificates = mtls_certificates

        self.update = to_streamed_response_wrapper(
            mtls_certificates.update,
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


class AsyncMtlsCertificatesWithStreamingResponse:
    def __init__(self, mtls_certificates: AsyncMtlsCertificates) -> None:
        self._mtls_certificates = mtls_certificates

        self.update = async_to_streamed_response_wrapper(
            mtls_certificates.update,
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
