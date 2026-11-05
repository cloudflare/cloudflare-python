# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access.mfa.authenticator_catalog_list_response import AuthenticatorCatalogListResponse

__all__ = ["AuthenticatorCatalogResource", "AsyncAuthenticatorCatalogResource"]


class AuthenticatorCatalogResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticatorCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AuthenticatorCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticatorCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AuthenticatorCatalogResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[AuthenticatorCatalogListResponse]:
        """
        Returns a list of Authenticator Device AAGUIDs for MFA configuration.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/access/authenticator_device_aaguids", account_id=account_id),
            page=SyncSinglePage[AuthenticatorCatalogListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AuthenticatorCatalogListResponse,
        )


class AsyncAuthenticatorCatalogResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthenticatorCatalogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthenticatorCatalogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticatorCatalogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAuthenticatorCatalogResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuthenticatorCatalogListResponse, AsyncSinglePage[AuthenticatorCatalogListResponse]]:
        """
        Returns a list of Authenticator Device AAGUIDs for MFA configuration.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/access/authenticator_device_aaguids", account_id=account_id),
            page=AsyncSinglePage[AuthenticatorCatalogListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AuthenticatorCatalogListResponse,
        )


class AuthenticatorCatalogResourceWithRawResponse:
    def __init__(self, authenticator_catalog: AuthenticatorCatalogResource) -> None:
        self._authenticator_catalog = authenticator_catalog

        self.list = to_raw_response_wrapper(
            authenticator_catalog.list,
        )


class AsyncAuthenticatorCatalogResourceWithRawResponse:
    def __init__(self, authenticator_catalog: AsyncAuthenticatorCatalogResource) -> None:
        self._authenticator_catalog = authenticator_catalog

        self.list = async_to_raw_response_wrapper(
            authenticator_catalog.list,
        )


class AuthenticatorCatalogResourceWithStreamingResponse:
    def __init__(self, authenticator_catalog: AuthenticatorCatalogResource) -> None:
        self._authenticator_catalog = authenticator_catalog

        self.list = to_streamed_response_wrapper(
            authenticator_catalog.list,
        )


class AsyncAuthenticatorCatalogResourceWithStreamingResponse:
    def __init__(self, authenticator_catalog: AsyncAuthenticatorCatalogResource) -> None:
        self._authenticator_catalog = authenticator_catalog

        self.list = async_to_streamed_response_wrapper(
            authenticator_catalog.list,
        )
