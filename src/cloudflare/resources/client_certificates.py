# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

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
from ..pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .._base_client import AsyncPaginator, make_request_options
from ..types.client_certificates import client_certificate_list_params, client_certificate_create_params
from ..types.client_certificates.client_certificate import ClientCertificate

__all__ = ["ClientCertificatesResource", "AsyncClientCertificatesResource"]


class ClientCertificatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ClientCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ClientCertificatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        csr: str,
        validity_days: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ClientCertificate]:
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
                client_certificate_create_params.ClientCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ClientCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ClientCertificate]], ResultWrapper[ClientCertificate]),
        )

    def list(
        self,
        *,
        zone_id: str,
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
    ) -> SyncV4PagePaginationArray[ClientCertificate]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/client_certificates",
            page=SyncV4PagePaginationArray[ClientCertificate],
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
                    client_certificate_list_params.ClientCertificateListParams,
                ),
            ),
            model=ClientCertificate,
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
    ) -> Optional[ClientCertificate]:
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
                post_parser=ResultWrapper[Optional[ClientCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ClientCertificate]], ResultWrapper[ClientCertificate]),
        )

    def edit(
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
    ) -> Optional[ClientCertificate]:
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
                post_parser=ResultWrapper[Optional[ClientCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ClientCertificate]], ResultWrapper[ClientCertificate]),
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
    ) -> Optional[ClientCertificate]:
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
                post_parser=ResultWrapper[Optional[ClientCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ClientCertificate]], ResultWrapper[ClientCertificate]),
        )


class AsyncClientCertificatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientCertificatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientCertificatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientCertificatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncClientCertificatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        csr: str,
        validity_days: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ClientCertificate]:
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
            body=await async_maybe_transform(
                {
                    "csr": csr,
                    "validity_days": validity_days,
                },
                client_certificate_create_params.ClientCertificateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ClientCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ClientCertificate]], ResultWrapper[ClientCertificate]),
        )

    def list(
        self,
        *,
        zone_id: str,
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
    ) -> AsyncPaginator[ClientCertificate, AsyncV4PagePaginationArray[ClientCertificate]]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/client_certificates",
            page=AsyncV4PagePaginationArray[ClientCertificate],
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
                    client_certificate_list_params.ClientCertificateListParams,
                ),
            ),
            model=ClientCertificate,
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
    ) -> Optional[ClientCertificate]:
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
                post_parser=ResultWrapper[Optional[ClientCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ClientCertificate]], ResultWrapper[ClientCertificate]),
        )

    async def edit(
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
    ) -> Optional[ClientCertificate]:
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
                post_parser=ResultWrapper[Optional[ClientCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ClientCertificate]], ResultWrapper[ClientCertificate]),
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
    ) -> Optional[ClientCertificate]:
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
                post_parser=ResultWrapper[Optional[ClientCertificate]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ClientCertificate]], ResultWrapper[ClientCertificate]),
        )


class ClientCertificatesResourceWithRawResponse:
    def __init__(self, client_certificates: ClientCertificatesResource) -> None:
        self._client_certificates = client_certificates

        self.create = to_raw_response_wrapper(
            client_certificates.create,
        )
        self.list = to_raw_response_wrapper(
            client_certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            client_certificates.delete,
        )
        self.edit = to_raw_response_wrapper(
            client_certificates.edit,
        )
        self.get = to_raw_response_wrapper(
            client_certificates.get,
        )


class AsyncClientCertificatesResourceWithRawResponse:
    def __init__(self, client_certificates: AsyncClientCertificatesResource) -> None:
        self._client_certificates = client_certificates

        self.create = async_to_raw_response_wrapper(
            client_certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            client_certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            client_certificates.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            client_certificates.edit,
        )
        self.get = async_to_raw_response_wrapper(
            client_certificates.get,
        )


class ClientCertificatesResourceWithStreamingResponse:
    def __init__(self, client_certificates: ClientCertificatesResource) -> None:
        self._client_certificates = client_certificates

        self.create = to_streamed_response_wrapper(
            client_certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            client_certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            client_certificates.delete,
        )
        self.edit = to_streamed_response_wrapper(
            client_certificates.edit,
        )
        self.get = to_streamed_response_wrapper(
            client_certificates.get,
        )


class AsyncClientCertificatesResourceWithStreamingResponse:
    def __init__(self, client_certificates: AsyncClientCertificatesResource) -> None:
        self._client_certificates = client_certificates

        self.create = async_to_streamed_response_wrapper(
            client_certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            client_certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            client_certificates.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            client_certificates.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            client_certificates.get,
        )
