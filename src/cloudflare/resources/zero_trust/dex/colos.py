# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.dex import colo_list_params

__all__ = ["ColosResource", "AsyncColosResource"]


class ColosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ColosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ColosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ColosResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        from_: str,
        to: str,
        sort_by: Literal["fleet-status-usage", "application-tests-usage"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[object]:
        """
        List Cloudflare colos that account's devices were connected to during a time
        period, sorted by usage starting from the most used colo. Colos without traffic
        are also returned and sorted alphabetically.

        Args:
          from_: Start time for connection period in ISO (RFC3339 - ISO 8601) format

          to: End time for connection period in ISO (RFC3339 - ISO 8601) format

          sort_by: Type of usage that colos should be sorted by. If unspecified, returns all
              Cloudflare colos sorted alphabetically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dex/colos",
            page=SyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "sort_by": sort_by,
                    },
                    colo_list_params.ColoListParams,
                ),
            ),
            model=object,
        )


class AsyncColosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncColosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncColosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncColosResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        from_: str,
        to: str,
        sort_by: Literal["fleet-status-usage", "application-tests-usage"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[object, AsyncSinglePage[object]]:
        """
        List Cloudflare colos that account's devices were connected to during a time
        period, sorted by usage starting from the most used colo. Colos without traffic
        are also returned and sorted alphabetically.

        Args:
          from_: Start time for connection period in ISO (RFC3339 - ISO 8601) format

          to: End time for connection period in ISO (RFC3339 - ISO 8601) format

          sort_by: Type of usage that colos should be sorted by. If unspecified, returns all
              Cloudflare colos sorted alphabetically.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dex/colos",
            page=AsyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                        "sort_by": sort_by,
                    },
                    colo_list_params.ColoListParams,
                ),
            ),
            model=object,
        )


class ColosResourceWithRawResponse:
    def __init__(self, colos: ColosResource) -> None:
        self._colos = colos

        self.list = to_raw_response_wrapper(
            colos.list,
        )


class AsyncColosResourceWithRawResponse:
    def __init__(self, colos: AsyncColosResource) -> None:
        self._colos = colos

        self.list = async_to_raw_response_wrapper(
            colos.list,
        )


class ColosResourceWithStreamingResponse:
    def __init__(self, colos: ColosResource) -> None:
        self._colos = colos

        self.list = to_streamed_response_wrapper(
            colos.list,
        )


class AsyncColosResourceWithStreamingResponse:
    def __init__(self, colos: AsyncColosResource) -> None:
        self._colos = colos

        self.list = async_to_streamed_response_wrapper(
            colos.list,
        )
