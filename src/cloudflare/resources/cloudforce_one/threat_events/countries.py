# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events.country_list_response import CountryListResponse

__all__ = ["CountriesResource", "AsyncCountriesResource"]


class CountriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CountriesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryListResponse:
        """
        Retrieves countries information for all countries

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryListResponse,
        )


class AsyncCountriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCountriesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CountryListResponse:
        """
        Retrieves countries information for all countries

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/countries",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryListResponse,
        )


class CountriesResourceWithRawResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.list = to_raw_response_wrapper(
            countries.list,
        )


class AsyncCountriesResourceWithRawResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.list = async_to_raw_response_wrapper(
            countries.list,
        )


class CountriesResourceWithStreamingResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.list = to_streamed_response_wrapper(
            countries.list,
        )


class AsyncCountriesResourceWithStreamingResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.list = async_to_streamed_response_wrapper(
            countries.list,
        )
