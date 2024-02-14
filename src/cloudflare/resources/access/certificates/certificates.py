# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .settings import Settings, AsyncSettings

from ...._compat import cached_property

from ....types.access import (
    CertificateUpdateResponse,
    CertificateDeleteResponse,
    CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse,
    CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse,
    CertificateGetResponse,
)

from typing import Type, List, Optional

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
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.access import certificate_update_params
from ....types.access import certificate_access_m_tls_authentication_add_an_m_tls_certificate_params
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Certificates", "AsyncCertificates"]


class Certificates(SyncAPIResource):
    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def with_raw_response(self) -> CertificatesWithRawResponse:
        return CertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatesWithStreamingResponse:
        return CertificatesWithStreamingResponse(self)

    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        associated_hostnames: List[str],
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateUpdateResponse:
        """
        Updates a configured mTLS certificate.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          associated_hostnames: The hostnames of the applications that will use this certificate.

          name: The name of the certificate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}",
            body=maybe_transform(
                {
                    "associated_hostnames": associated_hostnames,
                    "name": name,
                },
                certificate_update_params.CertificateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificateUpdateResponse], ResultWrapper[CertificateUpdateResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateDeleteResponse:
        """
        Deletes an mTLS certificate.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificateDeleteResponse], ResultWrapper[CertificateDeleteResponse]),
        )

    def access_m_tls_authentication_add_an_m_tls_certificate(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        certificate: str,
        name: str,
        associated_hostnames: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse:
        """
        Adds a new mTLS root certificate to Access.

        Args:
          account_or_zone_id: Identifier

          certificate: The certificate content.

          name: The name of the certificate.

          associated_hostnames: The hostnames of the applications that will use this certificate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "name": name,
                    "associated_hostnames": associated_hostnames,
                },
                certificate_access_m_tls_authentication_add_an_m_tls_certificate_params.CertificateAccessMTLSAuthenticationAddAnMTLSCertificateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse],
                ResultWrapper[CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse],
            ),
        )

    def access_m_tls_authentication_list_m_tls_certificates(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse]:
        """
        Lists all mTLS root certificates.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse]],
                ResultWrapper[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse],
            ),
        )

    def get(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateGetResponse:
        """
        Fetches a single mTLS certificate.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificateGetResponse], ResultWrapper[CertificateGetResponse]),
        )


class AsyncCertificates(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCertificatesWithRawResponse:
        return AsyncCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatesWithStreamingResponse:
        return AsyncCertificatesWithStreamingResponse(self)

    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        associated_hostnames: List[str],
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateUpdateResponse:
        """
        Updates a configured mTLS certificate.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          associated_hostnames: The hostnames of the applications that will use this certificate.

          name: The name of the certificate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}",
            body=maybe_transform(
                {
                    "associated_hostnames": associated_hostnames,
                    "name": name,
                },
                certificate_update_params.CertificateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificateUpdateResponse], ResultWrapper[CertificateUpdateResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateDeleteResponse:
        """
        Deletes an mTLS certificate.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificateDeleteResponse], ResultWrapper[CertificateDeleteResponse]),
        )

    async def access_m_tls_authentication_add_an_m_tls_certificate(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        certificate: str,
        name: str,
        associated_hostnames: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse:
        """
        Adds a new mTLS root certificate to Access.

        Args:
          account_or_zone_id: Identifier

          certificate: The certificate content.

          name: The name of the certificate.

          associated_hostnames: The hostnames of the applications that will use this certificate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "name": name,
                    "associated_hostnames": associated_hostnames,
                },
                certificate_access_m_tls_authentication_add_an_m_tls_certificate_params.CertificateAccessMTLSAuthenticationAddAnMTLSCertificateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse],
                ResultWrapper[CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse],
            ),
        )

    async def access_m_tls_authentication_list_m_tls_certificates(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse]:
        """
        Lists all mTLS root certificates.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse]],
                ResultWrapper[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse],
            ),
        )

    async def get(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CertificateGetResponse:
        """
        Fetches a single mTLS certificate.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/certificates/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificateGetResponse], ResultWrapper[CertificateGetResponse]),
        )


class CertificatesWithRawResponse:
    def __init__(self, certificates: Certificates) -> None:
        self._certificates = certificates

        self.update = to_raw_response_wrapper(
            certificates.update,
        )
        self.delete = to_raw_response_wrapper(
            certificates.delete,
        )
        self.access_m_tls_authentication_add_an_m_tls_certificate = to_raw_response_wrapper(
            certificates.access_m_tls_authentication_add_an_m_tls_certificate,
        )
        self.access_m_tls_authentication_list_m_tls_certificates = to_raw_response_wrapper(
            certificates.access_m_tls_authentication_list_m_tls_certificates,
        )
        self.get = to_raw_response_wrapper(
            certificates.get,
        )

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._certificates.settings)


class AsyncCertificatesWithRawResponse:
    def __init__(self, certificates: AsyncCertificates) -> None:
        self._certificates = certificates

        self.update = async_to_raw_response_wrapper(
            certificates.update,
        )
        self.delete = async_to_raw_response_wrapper(
            certificates.delete,
        )
        self.access_m_tls_authentication_add_an_m_tls_certificate = async_to_raw_response_wrapper(
            certificates.access_m_tls_authentication_add_an_m_tls_certificate,
        )
        self.access_m_tls_authentication_list_m_tls_certificates = async_to_raw_response_wrapper(
            certificates.access_m_tls_authentication_list_m_tls_certificates,
        )
        self.get = async_to_raw_response_wrapper(
            certificates.get,
        )

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._certificates.settings)


class CertificatesWithStreamingResponse:
    def __init__(self, certificates: Certificates) -> None:
        self._certificates = certificates

        self.update = to_streamed_response_wrapper(
            certificates.update,
        )
        self.delete = to_streamed_response_wrapper(
            certificates.delete,
        )
        self.access_m_tls_authentication_add_an_m_tls_certificate = to_streamed_response_wrapper(
            certificates.access_m_tls_authentication_add_an_m_tls_certificate,
        )
        self.access_m_tls_authentication_list_m_tls_certificates = to_streamed_response_wrapper(
            certificates.access_m_tls_authentication_list_m_tls_certificates,
        )
        self.get = to_streamed_response_wrapper(
            certificates.get,
        )

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._certificates.settings)


class AsyncCertificatesWithStreamingResponse:
    def __init__(self, certificates: AsyncCertificates) -> None:
        self._certificates = certificates

        self.update = async_to_streamed_response_wrapper(
            certificates.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            certificates.delete,
        )
        self.access_m_tls_authentication_add_an_m_tls_certificate = async_to_streamed_response_wrapper(
            certificates.access_m_tls_authentication_add_an_m_tls_certificate,
        )
        self.access_m_tls_authentication_list_m_tls_certificates = async_to_streamed_response_wrapper(
            certificates.access_m_tls_authentication_list_m_tls_certificates,
        )
        self.get = async_to_streamed_response_wrapper(
            certificates.get,
        )

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._certificates.settings)
