# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.addressing.service_list_response import ServiceListResponse

__all__ = ["ServicesResource", "AsyncServicesResource"]


class ServicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ServicesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[ServiceListResponse]:
        """
        Bring-Your-Own IP (BYOIP) prefixes onboarded to Cloudflare must be bound to a
        service running on the Cloudflare network to enable a Cloudflare product on the
        IP addresses. This endpoint can be used as a reference of available services on
        the Cloudflare network, and their service IDs.

        Args:
          account_id: Identifier of a Cloudflare account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/services",
            page=SyncSinglePage[ServiceListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ServiceListResponse,
        )


class AsyncServicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncServicesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ServiceListResponse, AsyncSinglePage[ServiceListResponse]]:
        """
        Bring-Your-Own IP (BYOIP) prefixes onboarded to Cloudflare must be bound to a
        service running on the Cloudflare network to enable a Cloudflare product on the
        IP addresses. This endpoint can be used as a reference of available services on
        the Cloudflare network, and their service IDs.

        Args:
          account_id: Identifier of a Cloudflare account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/services",
            page=AsyncSinglePage[ServiceListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ServiceListResponse,
        )


class ServicesResourceWithRawResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.list = to_raw_response_wrapper(
            services.list,
        )


class AsyncServicesResourceWithRawResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.list = async_to_raw_response_wrapper(
            services.list,
        )


class ServicesResourceWithStreamingResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.list = to_streamed_response_wrapper(
            services.list,
        )


class AsyncServicesResourceWithStreamingResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.list = async_to_streamed_response_wrapper(
            services.list,
        )
