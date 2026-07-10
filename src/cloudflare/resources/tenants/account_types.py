# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.tenants.account_type_list_response import AccountTypeListResponse

__all__ = ["AccountTypesResource", "AsyncAccountTypesResource"]


class AccountTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccountTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccountTypesResourceWithStreamingResponse(self)

    def list(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[AccountTypeListResponse]:
        """
        List of account types available for the Tenant to provision accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get_api_list(
            path_template("/tenants/{tenant_id}/account_types", tenant_id=tenant_id),
            page=SyncSinglePage[AccountTypeListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
        )


class AsyncAccountTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccountTypesResourceWithStreamingResponse(self)

    def list(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AccountTypeListResponse, AsyncSinglePage[AccountTypeListResponse]]:
        """
        List of account types available for the Tenant to provision accounts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get_api_list(
            path_template("/tenants/{tenant_id}/account_types", tenant_id=tenant_id),
            page=AsyncSinglePage[AccountTypeListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=str,
        )


class AccountTypesResourceWithRawResponse:
    def __init__(self, account_types: AccountTypesResource) -> None:
        self._account_types = account_types

        self.list = to_raw_response_wrapper(
            account_types.list,
        )


class AsyncAccountTypesResourceWithRawResponse:
    def __init__(self, account_types: AsyncAccountTypesResource) -> None:
        self._account_types = account_types

        self.list = async_to_raw_response_wrapper(
            account_types.list,
        )


class AccountTypesResourceWithStreamingResponse:
    def __init__(self, account_types: AccountTypesResource) -> None:
        self._account_types = account_types

        self.list = to_streamed_response_wrapper(
            account_types.list,
        )


class AsyncAccountTypesResourceWithStreamingResponse:
    def __init__(self, account_types: AsyncAccountTypesResource) -> None:
        self._account_types = account_types

        self.list = async_to_streamed_response_wrapper(
            account_types.list,
        )
