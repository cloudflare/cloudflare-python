# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...types.dls import region_list_params
from ...pagination import SyncCursorPagination, AsyncCursorPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.dls.region_get_response import RegionGetResponse
from ...types.dls.region_list_response import RegionListResponse

__all__ = ["RegionsResource", "AsyncRegionsResource"]


class RegionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        per_page: int | Omit = omit,
        type: Literal["managed", "custom"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[RegionListResponse]:
        """
        List the DLS regions (managed and custom) available to an account.

        Args:
          account_id: Identifier of a Cloudflare account.

          cursor: Opaque token for cursor-based pagination. Omit for the first page. Pass the
              value from a previous response to fetch the next page.

          type: Filter regions by type. Omit to return all regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dls/regions", account_id=account_id),
            page=SyncCursorPagination[RegionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                        "type": type,
                    },
                    region_list_params.RegionListParams,
                ),
            ),
            model=RegionListResponse,
        )

    def get(
        self,
        region_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegionGetResponse:
        """
        Retrieve a single DLS region (managed or custom) by ID or region key.

        Args:
          account_id: Identifier of a Cloudflare account.

          region_id: UUID of the region (custom or managed) or region_key of a managed region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not region_id:
            raise ValueError(f"Expected a non-empty value for `region_id` but received {region_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/dls/regions/{region_id}", account_id=account_id, region_id=region_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegionGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegionGetResponse], ResultWrapper[RegionGetResponse]),
        )


class AsyncRegionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        per_page: int | Omit = omit,
        type: Literal["managed", "custom"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RegionListResponse, AsyncCursorPagination[RegionListResponse]]:
        """
        List the DLS regions (managed and custom) available to an account.

        Args:
          account_id: Identifier of a Cloudflare account.

          cursor: Opaque token for cursor-based pagination. Omit for the first page. Pass the
              value from a previous response to fetch the next page.

          type: Filter regions by type. Omit to return all regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/dls/regions", account_id=account_id),
            page=AsyncCursorPagination[RegionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                        "type": type,
                    },
                    region_list_params.RegionListParams,
                ),
            ),
            model=RegionListResponse,
        )

    async def get(
        self,
        region_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegionGetResponse:
        """
        Retrieve a single DLS region (managed or custom) by ID or region key.

        Args:
          account_id: Identifier of a Cloudflare account.

          region_id: UUID of the region (custom or managed) or region_key of a managed region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not region_id:
            raise ValueError(f"Expected a non-empty value for `region_id` but received {region_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/dls/regions/{region_id}", account_id=account_id, region_id=region_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegionGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegionGetResponse], ResultWrapper[RegionGetResponse]),
        )


class RegionsResourceWithRawResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.list = to_raw_response_wrapper(
            regions.list,
        )
        self.get = to_raw_response_wrapper(
            regions.get,
        )


class AsyncRegionsResourceWithRawResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.list = async_to_raw_response_wrapper(
            regions.list,
        )
        self.get = async_to_raw_response_wrapper(
            regions.get,
        )


class RegionsResourceWithStreamingResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.list = to_streamed_response_wrapper(
            regions.list,
        )
        self.get = to_streamed_response_wrapper(
            regions.get,
        )


class AsyncRegionsResourceWithStreamingResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.list = async_to_streamed_response_wrapper(
            regions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            regions.get,
        )
