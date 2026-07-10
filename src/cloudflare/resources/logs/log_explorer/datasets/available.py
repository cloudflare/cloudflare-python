# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.logs.log_explorer.datasets.available_dataset import AvailableDataset

__all__ = ["AvailableResource", "AsyncAvailableResource"]


class AvailableResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvailableResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AvailableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvailableResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AvailableResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[AvailableDataset]:
        """Returns all dataset types that this account or zone can create.

        Each entry
        includes the dataset schema and timestamp field.

        The schema shows all possible fields for a dataset. However, not all fields may
        be available for your account or zone. When creating or updating a dataset, only
        fields available to your account or zone can be enabled. If you request a field
        that is not available, you will receive an error.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets/available",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=SyncSinglePage[AvailableDataset],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AvailableDataset,
        )


class AsyncAvailableResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvailableResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvailableResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvailableResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAvailableResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AvailableDataset, AsyncSinglePage[AvailableDataset]]:
        """Returns all dataset types that this account or zone can create.

        Each entry
        includes the dataset schema and timestamp field.

        The schema shows all possible fields for a dataset. However, not all fields may
        be available for your account or zone. When creating or updating a dataset, only
        fields available to your account or zone can be enabled. If you request a field
        that is not available, you will receive an error.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

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
                "/{account_or_zone}/{account_or_zone_id}/logs/explorer/datasets/available",
                account_or_zone=account_or_zone,
                account_or_zone_id=account_or_zone_id,
            ),
            page=AsyncSinglePage[AvailableDataset],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AvailableDataset,
        )


class AvailableResourceWithRawResponse:
    def __init__(self, available: AvailableResource) -> None:
        self._available = available

        self.list = to_raw_response_wrapper(
            available.list,
        )


class AsyncAvailableResourceWithRawResponse:
    def __init__(self, available: AsyncAvailableResource) -> None:
        self._available = available

        self.list = async_to_raw_response_wrapper(
            available.list,
        )


class AvailableResourceWithStreamingResponse:
    def __init__(self, available: AvailableResource) -> None:
        self._available = available

        self.list = to_streamed_response_wrapper(
            available.list,
        )


class AsyncAvailableResourceWithStreamingResponse:
    def __init__(self, available: AsyncAvailableResource) -> None:
        self._available = available

        self.list = async_to_streamed_response_wrapper(
            available.list,
        )
