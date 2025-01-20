# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.load_balancers import region_list_params
from ...types.load_balancers.region_get_response import RegionGetResponse
from ...types.load_balancers.region_list_response import RegionListResponse

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
        country_code_a2: str | NotGiven = NOT_GIVEN,
        subdivision_code: str | NotGiven = NOT_GIVEN,
        subdivision_code_a2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionListResponse:
        """
        List all region mappings.

        Args:
          account_id: Identifier

          country_code_a2: Two-letter alpha-2 country code followed in ISO 3166-1.

          subdivision_code: Two-letter subdivision code followed in ISO 3166-2.

          subdivision_code_a2: Two-letter subdivision code followed in ISO 3166-2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            RegionListResponse,
            self._get(
                f"/accounts/{account_id}/load_balancers/regions",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "country_code_a2": country_code_a2,
                            "subdivision_code": subdivision_code,
                            "subdivision_code_a2": subdivision_code_a2,
                        },
                        region_list_params.RegionListParams,
                    ),
                    post_parser=ResultWrapper[RegionListResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RegionListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        region_id: Literal[
            "WNAM", "ENAM", "WEU", "EEU", "NSAM", "SSAM", "OC", "ME", "NAF", "SAF", "SAS", "SEAS", "NEAS"
        ],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionGetResponse:
        """
        Get a single region mapping.

        Args:
          account_id: Identifier

          region_id: A list of Cloudflare regions. WNAM: Western North America, ENAM: Eastern North
              America, WEU: Western Europe, EEU: Eastern Europe, NSAM: Northern South America,
              SSAM: Southern South America, OC: Oceania, ME: Middle East, NAF: North Africa,
              SAF: South Africa, SAS: Southern Asia, SEAS: South East Asia, NEAS: North East
              Asia).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not region_id:
            raise ValueError(f"Expected a non-empty value for `region_id` but received {region_id!r}")
        return cast(
            RegionGetResponse,
            self._get(
                f"/accounts/{account_id}/load_balancers/regions/{region_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RegionGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RegionGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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

    async def list(
        self,
        *,
        account_id: str,
        country_code_a2: str | NotGiven = NOT_GIVEN,
        subdivision_code: str | NotGiven = NOT_GIVEN,
        subdivision_code_a2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionListResponse:
        """
        List all region mappings.

        Args:
          account_id: Identifier

          country_code_a2: Two-letter alpha-2 country code followed in ISO 3166-1.

          subdivision_code: Two-letter subdivision code followed in ISO 3166-2.

          subdivision_code_a2: Two-letter subdivision code followed in ISO 3166-2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            RegionListResponse,
            await self._get(
                f"/accounts/{account_id}/load_balancers/regions",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "country_code_a2": country_code_a2,
                            "subdivision_code": subdivision_code,
                            "subdivision_code_a2": subdivision_code_a2,
                        },
                        region_list_params.RegionListParams,
                    ),
                    post_parser=ResultWrapper[RegionListResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RegionListResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        region_id: Literal[
            "WNAM", "ENAM", "WEU", "EEU", "NSAM", "SSAM", "OC", "ME", "NAF", "SAF", "SAS", "SEAS", "NEAS"
        ],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionGetResponse:
        """
        Get a single region mapping.

        Args:
          account_id: Identifier

          region_id: A list of Cloudflare regions. WNAM: Western North America, ENAM: Eastern North
              America, WEU: Western Europe, EEU: Eastern Europe, NSAM: Northern South America,
              SSAM: Southern South America, OC: Oceania, ME: Middle East, NAF: North Africa,
              SAF: South Africa, SAS: Southern Asia, SEAS: South East Asia, NEAS: North East
              Asia).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not region_id:
            raise ValueError(f"Expected a non-empty value for `region_id` but received {region_id!r}")
        return cast(
            RegionGetResponse,
            await self._get(
                f"/accounts/{account_id}/load_balancers/regions/{region_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RegionGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RegionGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
