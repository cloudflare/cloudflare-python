# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import (
    ClientCertificateUpdateResponse,
    ClientCertificateDeleteResponse,
    ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse,
    ClientCertificateClientCertificateForAZoneListClientCertificatesResponse,
    ClientCertificateGetResponse,
)

from typing import Type, Optional

from typing_extensions import Literal

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
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import client_certificate_client_certificate_for_a_zone_create_client_certificate_params
from ..types import client_certificate_client_certificate_for_a_zone_list_client_certificates_params
from .._wrappers import ResultWrapper
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

__all__ = ["ClientCertificates", "AsyncClientCertificates"]


class ClientCertificates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientCertificatesWithRawResponse:
        return ClientCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientCertificatesWithStreamingResponse:
        return ClientCertificatesWithStreamingResponse(self)

    def update(
        self,
        client_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientCertificateUpdateResponse:
        """
        If a API Shield mTLS Client Certificate is in a pending_revocation state, you
        may reactivate it with this endpoint.

        Args:
          zone_id: Identifier

          client_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not client_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `client_certificate_id` but received {client_certificate_id!r}"
            )
        return self._patch(
            f"/zones/{zone_id}/client_certificates/{client_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ClientCertificateUpdateResponse], ResultWrapper[ClientCertificateUpdateResponse]),
        )

    def delete(
        self,
        client_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientCertificateDeleteResponse:
        """
        Set a API Shield mTLS Client Certificate to pending_revocation status for
        processing to revoked status.

        Args:
          zone_id: Identifier

          client_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not client_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `client_certificate_id` but received {client_certificate_id!r}"
            )
        return self._delete(
            f"/zones/{zone_id}/client_certificates/{client_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ClientCertificateDeleteResponse], ResultWrapper[ClientCertificateDeleteResponse]),
        )

    def client_certificate_for_a_zone_create_client_certificate(
        self,
        zone_id: str,
        *,
        csr: str,
        validity_days: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse:
        """
        Create a new API Shield mTLS Client Certificate

        Args:
          zone_id: Identifier

          csr: The Certificate Signing Request (CSR). Must be newline-encoded.

          validity_days: The number of days the Client Certificate will be valid after the issued_on date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/client_certificates",
            body=maybe_transform(
                {
                    "csr": csr,
                    "validity_days": validity_days,
                },
                client_certificate_client_certificate_for_a_zone_create_client_certificate_params.ClientCertificateClientCertificateForAZoneCreateClientCertificateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse],
                ResultWrapper[ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse],
            ),
        )

    def client_certificate_for_a_zone_list_client_certificates(
        self,
        zone_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["all", "active", "pending_reactivation", "pending_revocation", "revoked"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse]:
        """
        List all of your Zone's API Shield mTLS Client Certificates by Status and/or
        using Pagination

        Args:
          zone_id: Identifier

          limit: Limit to the number of records returned.

          offset: Offset the results

          page: Page number of paginated results.

          per_page: Number of records per page.

          status: Client Certitifcate Status to filter results by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/client_certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    client_certificate_client_certificate_for_a_zone_list_client_certificates_params.ClientCertificateClientCertificateForAZoneListClientCertificatesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse]],
                ResultWrapper[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
            ),
        )

    def get(
        self,
        client_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientCertificateGetResponse:
        """
        Get Details for a single mTLS API Shield Client Certificate

        Args:
          zone_id: Identifier

          client_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not client_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `client_certificate_id` but received {client_certificate_id!r}"
            )
        return self._get(
            f"/zones/{zone_id}/client_certificates/{client_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ClientCertificateGetResponse], ResultWrapper[ClientCertificateGetResponse]),
        )


class AsyncClientCertificates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientCertificatesWithRawResponse:
        return AsyncClientCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientCertificatesWithStreamingResponse:
        return AsyncClientCertificatesWithStreamingResponse(self)

    async def update(
        self,
        client_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientCertificateUpdateResponse:
        """
        If a API Shield mTLS Client Certificate is in a pending_revocation state, you
        may reactivate it with this endpoint.

        Args:
          zone_id: Identifier

          client_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not client_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `client_certificate_id` but received {client_certificate_id!r}"
            )
        return await self._patch(
            f"/zones/{zone_id}/client_certificates/{client_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ClientCertificateUpdateResponse], ResultWrapper[ClientCertificateUpdateResponse]),
        )

    async def delete(
        self,
        client_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientCertificateDeleteResponse:
        """
        Set a API Shield mTLS Client Certificate to pending_revocation status for
        processing to revoked status.

        Args:
          zone_id: Identifier

          client_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not client_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `client_certificate_id` but received {client_certificate_id!r}"
            )
        return await self._delete(
            f"/zones/{zone_id}/client_certificates/{client_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ClientCertificateDeleteResponse], ResultWrapper[ClientCertificateDeleteResponse]),
        )

    async def client_certificate_for_a_zone_create_client_certificate(
        self,
        zone_id: str,
        *,
        csr: str,
        validity_days: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse:
        """
        Create a new API Shield mTLS Client Certificate

        Args:
          zone_id: Identifier

          csr: The Certificate Signing Request (CSR). Must be newline-encoded.

          validity_days: The number of days the Client Certificate will be valid after the issued_on date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/client_certificates",
            body=maybe_transform(
                {
                    "csr": csr,
                    "validity_days": validity_days,
                },
                client_certificate_client_certificate_for_a_zone_create_client_certificate_params.ClientCertificateClientCertificateForAZoneCreateClientCertificateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse],
                ResultWrapper[ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse],
            ),
        )

    async def client_certificate_for_a_zone_list_client_certificates(
        self,
        zone_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["all", "active", "pending_reactivation", "pending_revocation", "revoked"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse]:
        """
        List all of your Zone's API Shield mTLS Client Certificates by Status and/or
        using Pagination

        Args:
          zone_id: Identifier

          limit: Limit to the number of records returned.

          offset: Offset the results

          page: Page number of paginated results.

          per_page: Number of records per page.

          status: Client Certitifcate Status to filter results by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/client_certificates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    client_certificate_client_certificate_for_a_zone_list_client_certificates_params.ClientCertificateClientCertificateForAZoneListClientCertificatesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse]],
                ResultWrapper[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
            ),
        )

    async def get(
        self,
        client_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClientCertificateGetResponse:
        """
        Get Details for a single mTLS API Shield Client Certificate

        Args:
          zone_id: Identifier

          client_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not client_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `client_certificate_id` but received {client_certificate_id!r}"
            )
        return await self._get(
            f"/zones/{zone_id}/client_certificates/{client_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ClientCertificateGetResponse], ResultWrapper[ClientCertificateGetResponse]),
        )


class ClientCertificatesWithRawResponse:
    def __init__(self, client_certificates: ClientCertificates) -> None:
        self._client_certificates = client_certificates

        self.update = to_raw_response_wrapper(
            client_certificates.update,
        )
        self.delete = to_raw_response_wrapper(
            client_certificates.delete,
        )
        self.client_certificate_for_a_zone_create_client_certificate = to_raw_response_wrapper(
            client_certificates.client_certificate_for_a_zone_create_client_certificate,
        )
        self.client_certificate_for_a_zone_list_client_certificates = to_raw_response_wrapper(
            client_certificates.client_certificate_for_a_zone_list_client_certificates,
        )
        self.get = to_raw_response_wrapper(
            client_certificates.get,
        )


class AsyncClientCertificatesWithRawResponse:
    def __init__(self, client_certificates: AsyncClientCertificates) -> None:
        self._client_certificates = client_certificates

        self.update = async_to_raw_response_wrapper(
            client_certificates.update,
        )
        self.delete = async_to_raw_response_wrapper(
            client_certificates.delete,
        )
        self.client_certificate_for_a_zone_create_client_certificate = async_to_raw_response_wrapper(
            client_certificates.client_certificate_for_a_zone_create_client_certificate,
        )
        self.client_certificate_for_a_zone_list_client_certificates = async_to_raw_response_wrapper(
            client_certificates.client_certificate_for_a_zone_list_client_certificates,
        )
        self.get = async_to_raw_response_wrapper(
            client_certificates.get,
        )


class ClientCertificatesWithStreamingResponse:
    def __init__(self, client_certificates: ClientCertificates) -> None:
        self._client_certificates = client_certificates

        self.update = to_streamed_response_wrapper(
            client_certificates.update,
        )
        self.delete = to_streamed_response_wrapper(
            client_certificates.delete,
        )
        self.client_certificate_for_a_zone_create_client_certificate = to_streamed_response_wrapper(
            client_certificates.client_certificate_for_a_zone_create_client_certificate,
        )
        self.client_certificate_for_a_zone_list_client_certificates = to_streamed_response_wrapper(
            client_certificates.client_certificate_for_a_zone_list_client_certificates,
        )
        self.get = to_streamed_response_wrapper(
            client_certificates.get,
        )


class AsyncClientCertificatesWithStreamingResponse:
    def __init__(self, client_certificates: AsyncClientCertificates) -> None:
        self._client_certificates = client_certificates

        self.update = async_to_streamed_response_wrapper(
            client_certificates.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            client_certificates.delete,
        )
        self.client_certificate_for_a_zone_create_client_certificate = async_to_streamed_response_wrapper(
            client_certificates.client_certificate_for_a_zone_create_client_certificate,
        )
        self.client_certificate_for_a_zone_list_client_certificates = async_to_streamed_response_wrapper(
            client_certificates.client_certificate_for_a_zone_list_client_certificates,
        )
        self.get = async_to_streamed_response_wrapper(
            client_certificates.get,
        )
