# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .....types.zero_trust.access.applications.ca import CA

__all__ = ["CAsResource", "AsyncCAsResource"]


class CAsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CAsResourceWithRawResponse:
        return CAsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CAsResourceWithStreamingResponse:
        return CAsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[CA]:
        """
        Lists short-lived certificate CAs and their public keys.

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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/ca",
            page=SyncSinglePage[CA],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CA,
        )


class AsyncCAsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCAsResourceWithRawResponse:
        return AsyncCAsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCAsResourceWithStreamingResponse:
        return AsyncCAsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CA, AsyncSinglePage[CA]]:
        """
        Lists short-lived certificate CAs and their public keys.

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
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/ca",
            page=AsyncSinglePage[CA],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=CA,
        )


class CAsResourceWithRawResponse:
    def __init__(self, cas: CAsResource) -> None:
        self._cas = cas

        self.list = to_raw_response_wrapper(
            cas.list,
        )


class AsyncCAsResourceWithRawResponse:
    def __init__(self, cas: AsyncCAsResource) -> None:
        self._cas = cas

        self.list = async_to_raw_response_wrapper(
            cas.list,
        )


class CAsResourceWithStreamingResponse:
    def __init__(self, cas: CAsResource) -> None:
        self._cas = cas

        self.list = to_streamed_response_wrapper(
            cas.list,
        )


class AsyncCAsResourceWithStreamingResponse:
    def __init__(self, cas: AsyncCAsResource) -> None:
        self._cas = cas

        self.list = async_to_streamed_response_wrapper(
            cas.list,
        )
