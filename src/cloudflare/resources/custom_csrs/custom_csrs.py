# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.custom_csrs import custom_csr_list_params, custom_csr_create_params
from ...types.custom_csrs.custom_csr_get_response import CustomCsrGetResponse
from ...types.custom_csrs.custom_csr_list_response import CustomCsrListResponse
from ...types.custom_csrs.custom_csr_create_response import CustomCsrCreateResponse
from ...types.custom_csrs.custom_csr_delete_response import CustomCsrDeleteResponse

__all__ = ["CustomCsrsResource", "AsyncCustomCsrsResource"]


class CustomCsrsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomCsrsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomCsrsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomCsrsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomCsrsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        common_name: str,
        country: str,
        locality: str,
        organization: str,
        sans: SequenceNotStr[str],
        state: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        description: str | Omit = omit,
        key_type: Literal["rsa2048", "p256v1"] | Omit = omit,
        name: str | Omit = omit,
        organizational_unit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomCsrCreateResponse]:
        """
        Generate a new custom Certificate Signing Request (CSR) for an account or zone.
        Cloudflare generates and securely stores the private key associated with the
        CSR.

        Args:
          common_name: The common name (domain) for the CSR. Must be at most 64 characters.

          country: Two-letter ISO 3166-1 alpha-2 country code.

          locality: City or locality name.

          organization: Organization name.

          sans: Subject Alternative Names for the CSR. At least one SAN is required.

          state: State or province name.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          description: Optional description for the CSR.

          key_type: Key algorithm to use for the CSR. Defaults to rsa2048 if not specified.

          name: Human-readable name for the CSR.

          organizational_unit: Organizational unit name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._post(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/custom_csrs",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            body=maybe_transform(
                {
                    "common_name": common_name,
                    "country": country,
                    "locality": locality,
                    "organization": organization,
                    "sans": sans,
                    "state": state,
                    "description": description,
                    "key_type": key_type,
                    "name": name,
                    "organizational_unit": organizational_unit,
                },
                custom_csr_create_params.CustomCsrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomCsrCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomCsrCreateResponse]], ResultWrapper[CustomCsrCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[CustomCsrListResponse]:
        """
        List all custom Certificate Signing Requests (CSRs) for an account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          page: Page number of paginated results.

          per_page: Number of custom CSRs per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/custom_csrs",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=SyncV4PagePaginationArray[CustomCsrListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    custom_csr_list_params.CustomCsrListParams,
                ),
            ),
            model=CustomCsrListResponse,
        )

    def delete(
        self,
        custom_csr_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomCsrDeleteResponse]:
        """
        Delete a custom Certificate Signing Request (CSR) and its associated private
        key.

        Args:
          custom_csr_id: Custom CSR identifier tag.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not custom_csr_id:
            raise ValueError(f"Expected a non-empty value for `custom_csr_id` but received {custom_csr_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._delete(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/custom_csrs/{custom_csr_id}",
                custom_csr_id=custom_csr_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomCsrDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomCsrDeleteResponse]], ResultWrapper[CustomCsrDeleteResponse]),
        )

    def get(
        self,
        custom_csr_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomCsrGetResponse]:
        """
        Retrieve details for a specific custom Certificate Signing Request (CSR).

        Args:
          custom_csr_id: Custom CSR identifier tag.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not custom_csr_id:
            raise ValueError(f"Expected a non-empty value for `custom_csr_id` but received {custom_csr_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/custom_csrs/{custom_csr_id}",
                custom_csr_id=custom_csr_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomCsrGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomCsrGetResponse]], ResultWrapper[CustomCsrGetResponse]),
        )


class AsyncCustomCsrsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomCsrsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomCsrsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomCsrsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomCsrsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        common_name: str,
        country: str,
        locality: str,
        organization: str,
        sans: SequenceNotStr[str],
        state: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        description: str | Omit = omit,
        key_type: Literal["rsa2048", "p256v1"] | Omit = omit,
        name: str | Omit = omit,
        organizational_unit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomCsrCreateResponse]:
        """
        Generate a new custom Certificate Signing Request (CSR) for an account or zone.
        Cloudflare generates and securely stores the private key associated with the
        CSR.

        Args:
          common_name: The common name (domain) for the CSR. Must be at most 64 characters.

          country: Two-letter ISO 3166-1 alpha-2 country code.

          locality: City or locality name.

          organization: Organization name.

          sans: Subject Alternative Names for the CSR. At least one SAN is required.

          state: State or province name.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          description: Optional description for the CSR.

          key_type: Key algorithm to use for the CSR. Defaults to rsa2048 if not specified.

          name: Human-readable name for the CSR.

          organizational_unit: Organizational unit name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/custom_csrs",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            body=await async_maybe_transform(
                {
                    "common_name": common_name,
                    "country": country,
                    "locality": locality,
                    "organization": organization,
                    "sans": sans,
                    "state": state,
                    "description": description,
                    "key_type": key_type,
                    "name": name,
                    "organizational_unit": organizational_unit,
                },
                custom_csr_create_params.CustomCsrCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomCsrCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomCsrCreateResponse]], ResultWrapper[CustomCsrCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        page: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomCsrListResponse, AsyncV4PagePaginationArray[CustomCsrListResponse]]:
        """
        List all custom Certificate Signing Requests (CSRs) for an account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          page: Page number of paginated results.

          per_page: Number of custom CSRs per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/custom_csrs",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=AsyncV4PagePaginationArray[CustomCsrListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    custom_csr_list_params.CustomCsrListParams,
                ),
            ),
            model=CustomCsrListResponse,
        )

    async def delete(
        self,
        custom_csr_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomCsrDeleteResponse]:
        """
        Delete a custom Certificate Signing Request (CSR) and its associated private
        key.

        Args:
          custom_csr_id: Custom CSR identifier tag.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not custom_csr_id:
            raise ValueError(f"Expected a non-empty value for `custom_csr_id` but received {custom_csr_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._delete(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/custom_csrs/{custom_csr_id}",
                custom_csr_id=custom_csr_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomCsrDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomCsrDeleteResponse]], ResultWrapper[CustomCsrDeleteResponse]),
        )

    async def get(
        self,
        custom_csr_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[CustomCsrGetResponse]:
        """
        Retrieve details for a specific custom Certificate Signing Request (CSR).

        Args:
          custom_csr_id: Custom CSR identifier tag.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not custom_csr_id:
            raise ValueError(f"Expected a non-empty value for `custom_csr_id` but received {custom_csr_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._get(
            path_template(
                "/{account_or_zone}/{account_or_zone_id}/custom_csrs/{custom_csr_id}",
                custom_csr_id=custom_csr_id,
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CustomCsrGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomCsrGetResponse]], ResultWrapper[CustomCsrGetResponse]),
        )


class CustomCsrsResourceWithRawResponse:
    def __init__(self, custom_csrs: CustomCsrsResource) -> None:
        self._custom_csrs = custom_csrs

        self.create = to_raw_response_wrapper(
            custom_csrs.create,
        )
        self.list = to_raw_response_wrapper(
            custom_csrs.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_csrs.delete,
        )
        self.get = to_raw_response_wrapper(
            custom_csrs.get,
        )


class AsyncCustomCsrsResourceWithRawResponse:
    def __init__(self, custom_csrs: AsyncCustomCsrsResource) -> None:
        self._custom_csrs = custom_csrs

        self.create = async_to_raw_response_wrapper(
            custom_csrs.create,
        )
        self.list = async_to_raw_response_wrapper(
            custom_csrs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_csrs.delete,
        )
        self.get = async_to_raw_response_wrapper(
            custom_csrs.get,
        )


class CustomCsrsResourceWithStreamingResponse:
    def __init__(self, custom_csrs: CustomCsrsResource) -> None:
        self._custom_csrs = custom_csrs

        self.create = to_streamed_response_wrapper(
            custom_csrs.create,
        )
        self.list = to_streamed_response_wrapper(
            custom_csrs.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_csrs.delete,
        )
        self.get = to_streamed_response_wrapper(
            custom_csrs.get,
        )


class AsyncCustomCsrsResourceWithStreamingResponse:
    def __init__(self, custom_csrs: AsyncCustomCsrsResource) -> None:
        self._custom_csrs = custom_csrs

        self.create = async_to_streamed_response_wrapper(
            custom_csrs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_csrs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_csrs.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_csrs.get,
        )
