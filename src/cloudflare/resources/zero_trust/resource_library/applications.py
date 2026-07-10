# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.resource_library import application_list_params
from ....types.zero_trust.resource_library.application_get_response import ApplicationGetResponse
from ....types.zero_trust.resource_library.application_list_response import ApplicationListResponse

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        filter: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[ApplicationListResponse]:
        """
        List applications with different filters.

        Args:
          filter:
              Filter applications using key:value format. Supported filter keys:

              - name: Filter by application name (e.g., name:HR)
              - id: Filter by application ID (e.g., id:0b63249c-95bf-4cc0-a7cc-d7faaaf1dac0)
              - human_id: Filter by human-readable ID (e.g., human_id:HR)
              - hostname: Filter by hostname or support domain (e.g.,
                hostname:portal.example.com)
              - source: Filter by application source name (e.g., source:cloudflare)
              - ip_subnet: Filter by IP subnet using CIDR containment — returns applications
                where any stored subnet contains the search value (e.g., ip_subnet:10.0.1.5/32
                matches apps with 10.0.0.0/16)
              - intel_id: Filter by Intel API ID (e.g., intel_id:498). also supports multiple
                values (e.g., intel_id:498,1001)
              - category_id: Filter by category ID (e.g.,
                category_id:37f8ec03-8766-49d4-9a15-369b044c842c).
              - category_name: Filter by category name (e.g., category_name:HR).
              - supported: Filter by supported Cloudflare product (e.g., supported:ACCESS).
                Values: GATEWAY, ACCESS, CASB. .

          limit: Limit of number of results to return (max 250).

          offset: Offset of results to return.

          order_by: Order results by field name and direction (e.g., name:asc). Ignored when search
              is provided; results are ranked by relevance instead.

          search: Fuzzy search across application name and hostnames. Results are ranked by
              relevance. Must be between 2 and 200 characters. Can be combined with filter
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/resource-library/applications", account_id=account_id),
            page=SyncSinglePage[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "search": search,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=ApplicationListResponse,
        )

    def get(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationGetResponse]:
        """
        Get application by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/accounts/{account_id}/resource-library/applications/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationGetResponse]], ResultWrapper[ApplicationGetResponse]),
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        filter: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: str | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ApplicationListResponse, AsyncSinglePage[ApplicationListResponse]]:
        """
        List applications with different filters.

        Args:
          filter:
              Filter applications using key:value format. Supported filter keys:

              - name: Filter by application name (e.g., name:HR)
              - id: Filter by application ID (e.g., id:0b63249c-95bf-4cc0-a7cc-d7faaaf1dac0)
              - human_id: Filter by human-readable ID (e.g., human_id:HR)
              - hostname: Filter by hostname or support domain (e.g.,
                hostname:portal.example.com)
              - source: Filter by application source name (e.g., source:cloudflare)
              - ip_subnet: Filter by IP subnet using CIDR containment — returns applications
                where any stored subnet contains the search value (e.g., ip_subnet:10.0.1.5/32
                matches apps with 10.0.0.0/16)
              - intel_id: Filter by Intel API ID (e.g., intel_id:498). also supports multiple
                values (e.g., intel_id:498,1001)
              - category_id: Filter by category ID (e.g.,
                category_id:37f8ec03-8766-49d4-9a15-369b044c842c).
              - category_name: Filter by category name (e.g., category_name:HR).
              - supported: Filter by supported Cloudflare product (e.g., supported:ACCESS).
                Values: GATEWAY, ACCESS, CASB. .

          limit: Limit of number of results to return (max 250).

          offset: Offset of results to return.

          order_by: Order results by field name and direction (e.g., name:asc). Ignored when search
              is provided; results are ranked by relevance instead.

          search: Fuzzy search across application name and hostnames. Results are ranked by
              relevance. Must be between 2 and 200 characters. Can be combined with filter
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/resource-library/applications", account_id=account_id),
            page=AsyncSinglePage[ApplicationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "search": search,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=ApplicationListResponse,
        )

    async def get(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ApplicationGetResponse]:
        """
        Get application by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/resource-library/applications/{id}", account_id=account_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ApplicationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ApplicationGetResponse]], ResultWrapper[ApplicationGetResponse]),
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.list = to_raw_response_wrapper(
            applications.list,
        )
        self.get = to_raw_response_wrapper(
            applications.get,
        )


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.list = async_to_raw_response_wrapper(
            applications.list,
        )
        self.get = async_to_raw_response_wrapper(
            applications.get,
        )


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.list = to_streamed_response_wrapper(
            applications.list,
        )
        self.get = to_streamed_response_wrapper(
            applications.get,
        )


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.list = async_to_streamed_response_wrapper(
            applications.list,
        )
        self.get = async_to_streamed_response_wrapper(
            applications.get,
        )
