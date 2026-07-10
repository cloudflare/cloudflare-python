# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncV4PagePagination, AsyncV4PagePagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.dex.devices import isp_list_params
from .....types.zero_trust.dex.devices.isps import ISPs

__all__ = ["ISPsResource", "AsyncISPsResource"]


class ISPsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ISPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ISPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ISPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ISPsResourceWithStreamingResponse(self)

    def list(
        self,
        device_id: str,
        *,
        account_id: str,
        per_page: int,
        cursor: str | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        page: int | Omit = omit,
        sort_by: Literal["time_start"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePagination[Optional[ISPs]]:
        """
        List ISP information observed for a specific device during traceroute tests.

        Args:
          account_id: Unique identifier linked to an account.

          device_id: API Resource UUID tag.

          per_page: Number of items per page

          cursor: Cursor for cursor-based pagination. Mutually exclusive with page.

          from_: Start time for the query in ISO 8601 format.

          page: Page number of paginated results. Mutually exclusive with cursor.

          sort_by: The field to sort results by.

          sort_order: The order to sort results.

          to: End time for the query in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/dex/devices/{device_id}/isps", account_id=account_id, device_id=device_id
            ),
            page=SyncV4PagePagination[Optional[ISPs]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "per_page": per_page,
                        "cursor": cursor,
                        "from_": from_,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "to": to,
                    },
                    isp_list_params.ISPListParams,
                ),
            ),
            model=ISPs,
        )


class AsyncISPsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncISPsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncISPsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncISPsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncISPsResourceWithStreamingResponse(self)

    def list(
        self,
        device_id: str,
        *,
        account_id: str,
        per_page: int,
        cursor: str | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        page: int | Omit = omit,
        sort_by: Literal["time_start"] | Omit = omit,
        sort_order: Literal["ASC", "DESC"] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Optional[ISPs], AsyncV4PagePagination[Optional[ISPs]]]:
        """
        List ISP information observed for a specific device during traceroute tests.

        Args:
          account_id: Unique identifier linked to an account.

          device_id: API Resource UUID tag.

          per_page: Number of items per page

          cursor: Cursor for cursor-based pagination. Mutually exclusive with page.

          from_: Start time for the query in ISO 8601 format.

          page: Page number of paginated results. Mutually exclusive with cursor.

          sort_by: The field to sort results by.

          sort_order: The order to sort results.

          to: End time for the query in ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/dex/devices/{device_id}/isps", account_id=account_id, device_id=device_id
            ),
            page=AsyncV4PagePagination[Optional[ISPs]],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "per_page": per_page,
                        "cursor": cursor,
                        "from_": from_,
                        "page": page,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "to": to,
                    },
                    isp_list_params.ISPListParams,
                ),
            ),
            model=ISPs,
        )


class ISPsResourceWithRawResponse:
    def __init__(self, isps: ISPsResource) -> None:
        self._isps = isps

        self.list = to_raw_response_wrapper(
            isps.list,
        )


class AsyncISPsResourceWithRawResponse:
    def __init__(self, isps: AsyncISPsResource) -> None:
        self._isps = isps

        self.list = async_to_raw_response_wrapper(
            isps.list,
        )


class ISPsResourceWithStreamingResponse:
    def __init__(self, isps: ISPsResource) -> None:
        self._isps = isps

        self.list = to_streamed_response_wrapper(
            isps.list,
        )


class AsyncISPsResourceWithStreamingResponse:
    def __init__(self, isps: AsyncISPsResource) -> None:
        self._isps = isps

        self.list = async_to_streamed_response_wrapper(
            isps.list,
        )
