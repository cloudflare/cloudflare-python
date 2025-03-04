# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .cloudflare_source import (
    CloudflareSourceResource,
    AsyncCloudflareSourceResource,
    CloudflareSourceResourceWithRawResponse,
    AsyncCloudflareSourceResourceWithRawResponse,
    CloudflareSourceResourceWithStreamingResponse,
    AsyncCloudflareSourceResourceWithStreamingResponse,
)
from .....types.zero_trust.networks import subnet_list_params
from .....types.zero_trust.networks.subnet_list_response import SubnetListResponse

__all__ = ["SubnetsResource", "AsyncSubnetsResource"]


class SubnetsResource(SyncAPIResource):
    @cached_property
    def cloudflare_source(self) -> CloudflareSourceResource:
        return CloudflareSourceResource(self._client)

    @cached_property
    def with_raw_response(self) -> SubnetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SubnetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubnetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SubnetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        address_family: Literal["v4", "v6"] | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        existed_at: str | NotGiven = NOT_GIVEN,
        is_default_network: bool | NotGiven = NOT_GIVEN,
        is_deleted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        subnet_types: Literal["cloudflare_source", "warp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[SubnetListResponse]:
        """
        Lists and filters subnets in an account.

        Args:
          account_id: Cloudflare account ID

          address_family: If set, only include subnets in the given address family - `v4` or `v6`

          comment: If set, only list subnets with the given comment.

          existed_at: If provided, include only resources that were created (and not deleted) before
              this time. URL encoded.

          is_default_network: If `true`, only include default subnets. If `false`, exclude default subnets
              subnets. If not set, all subnets will be included.

          is_deleted: If `true`, only include deleted subnets. If `false`, exclude deleted subnets. If
              not set, all subnets will be included.

          name: If set, only list subnets with the given name

          network: If set, only list the subnet whose network exactly matches the given CIDR.

          page: Page number of paginated results.

          per_page: Number of results to display.

          sort_order: Sort order of the results. `asc` means oldest to newest, `desc` means newest to
              oldest. If not set, they will not be in any particular order.

          subnet_types: If set, the types of subnets to include, separated by comma.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/zerotrust/subnets",
            page=SyncV4PagePaginationArray[SubnetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "address_family": address_family,
                        "comment": comment,
                        "existed_at": existed_at,
                        "is_default_network": is_default_network,
                        "is_deleted": is_deleted,
                        "name": name,
                        "network": network,
                        "page": page,
                        "per_page": per_page,
                        "sort_order": sort_order,
                        "subnet_types": subnet_types,
                    },
                    subnet_list_params.SubnetListParams,
                ),
            ),
            model=SubnetListResponse,
        )


class AsyncSubnetsResource(AsyncAPIResource):
    @cached_property
    def cloudflare_source(self) -> AsyncCloudflareSourceResource:
        return AsyncCloudflareSourceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSubnetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubnetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubnetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSubnetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        address_family: Literal["v4", "v6"] | NotGiven = NOT_GIVEN,
        comment: str | NotGiven = NOT_GIVEN,
        existed_at: str | NotGiven = NOT_GIVEN,
        is_default_network: bool | NotGiven = NOT_GIVEN,
        is_deleted: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        network: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        subnet_types: Literal["cloudflare_source", "warp"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SubnetListResponse, AsyncV4PagePaginationArray[SubnetListResponse]]:
        """
        Lists and filters subnets in an account.

        Args:
          account_id: Cloudflare account ID

          address_family: If set, only include subnets in the given address family - `v4` or `v6`

          comment: If set, only list subnets with the given comment.

          existed_at: If provided, include only resources that were created (and not deleted) before
              this time. URL encoded.

          is_default_network: If `true`, only include default subnets. If `false`, exclude default subnets
              subnets. If not set, all subnets will be included.

          is_deleted: If `true`, only include deleted subnets. If `false`, exclude deleted subnets. If
              not set, all subnets will be included.

          name: If set, only list subnets with the given name

          network: If set, only list the subnet whose network exactly matches the given CIDR.

          page: Page number of paginated results.

          per_page: Number of results to display.

          sort_order: Sort order of the results. `asc` means oldest to newest, `desc` means newest to
              oldest. If not set, they will not be in any particular order.

          subnet_types: If set, the types of subnets to include, separated by comma.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/zerotrust/subnets",
            page=AsyncV4PagePaginationArray[SubnetListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "address_family": address_family,
                        "comment": comment,
                        "existed_at": existed_at,
                        "is_default_network": is_default_network,
                        "is_deleted": is_deleted,
                        "name": name,
                        "network": network,
                        "page": page,
                        "per_page": per_page,
                        "sort_order": sort_order,
                        "subnet_types": subnet_types,
                    },
                    subnet_list_params.SubnetListParams,
                ),
            ),
            model=SubnetListResponse,
        )


class SubnetsResourceWithRawResponse:
    def __init__(self, subnets: SubnetsResource) -> None:
        self._subnets = subnets

        self.list = to_raw_response_wrapper(
            subnets.list,
        )

    @cached_property
    def cloudflare_source(self) -> CloudflareSourceResourceWithRawResponse:
        return CloudflareSourceResourceWithRawResponse(self._subnets.cloudflare_source)


class AsyncSubnetsResourceWithRawResponse:
    def __init__(self, subnets: AsyncSubnetsResource) -> None:
        self._subnets = subnets

        self.list = async_to_raw_response_wrapper(
            subnets.list,
        )

    @cached_property
    def cloudflare_source(self) -> AsyncCloudflareSourceResourceWithRawResponse:
        return AsyncCloudflareSourceResourceWithRawResponse(self._subnets.cloudflare_source)


class SubnetsResourceWithStreamingResponse:
    def __init__(self, subnets: SubnetsResource) -> None:
        self._subnets = subnets

        self.list = to_streamed_response_wrapper(
            subnets.list,
        )

    @cached_property
    def cloudflare_source(self) -> CloudflareSourceResourceWithStreamingResponse:
        return CloudflareSourceResourceWithStreamingResponse(self._subnets.cloudflare_source)


class AsyncSubnetsResourceWithStreamingResponse:
    def __init__(self, subnets: AsyncSubnetsResource) -> None:
        self._subnets = subnets

        self.list = async_to_streamed_response_wrapper(
            subnets.list,
        )

    @cached_property
    def cloudflare_source(self) -> AsyncCloudflareSourceResourceWithStreamingResponse:
        return AsyncCloudflareSourceResourceWithStreamingResponse(self._subnets.cloudflare_source)
