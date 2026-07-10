# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.organizations.organization import Organization

__all__ = ["TenantsResource", "AsyncTenantsResource"]


class TenantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TenantsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[Organization]:
        """Retrieves list of tenants the authenticated user / method has access to."""
        return self._get_api_list(
            "/user/tenants",
            page=SyncSinglePage[Organization],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Organization,
        )


class AsyncTenantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTenantsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Organization, AsyncSinglePage[Organization]]:
        """Retrieves list of tenants the authenticated user / method has access to."""
        return self._get_api_list(
            "/user/tenants",
            page=AsyncSinglePage[Organization],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Organization,
        )


class TenantsResourceWithRawResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.list = to_raw_response_wrapper(
            tenants.list,
        )


class AsyncTenantsResourceWithRawResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.list = async_to_raw_response_wrapper(
            tenants.list,
        )


class TenantsResourceWithStreamingResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.list = to_streamed_response_wrapper(
            tenants.list,
        )


class AsyncTenantsResourceWithStreamingResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.list = async_to_streamed_response_wrapper(
            tenants.list,
        )
