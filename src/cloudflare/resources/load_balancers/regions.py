# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.load_balancers import RegionGetResponse, RegionLoadBalancerRegionsListRegionsResponse

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.load_balancers import region_load_balancer_regions_list_regions_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Regions", "AsyncRegions"]


class Regions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegionsWithRawResponse:
        return RegionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionsWithStreamingResponse:
        return RegionsWithStreamingResponse(self)

    def get(
        self,
        region_code: Literal[
            "WNAM", "ENAM", "WEU", "EEU", "NSAM", "SSAM", "OC", "ME", "NAF", "SAF", "SAS", "SEAS", "NEAS"
        ],
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          region_code: A list of Cloudflare regions. WNAM: Western North America, ENAM: Eastern North
              America, WEU: Western Europe, EEU: Eastern Europe, NSAM: Northern South America,
              SSAM: Southern South America, OC: Oceania, ME: Middle East, NAF: North Africa,
              SAF: South Africa, SAS: Southern Asia, SEAS: South East Asia, NEAS: North East
              Asia).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not region_code:
            raise ValueError(f"Expected a non-empty value for `region_code` but received {region_code!r}")
        return cast(
            RegionGetResponse,
            self._get(
                f"/accounts/{account_identifier}/load_balancers/regions/{region_code}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RegionGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def load_balancer_regions_list_regions(
        self,
        account_identifier: str,
        *,
        country_code_a2: str | NotGiven = NOT_GIVEN,
        subdivision_code: str | NotGiven = NOT_GIVEN,
        subdivision_code_a2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionLoadBalancerRegionsListRegionsResponse:
        """
        List all region mappings.

        Args:
          account_identifier: Identifier

          country_code_a2: Two-letter alpha-2 country code followed in ISO 3166-1.

          subdivision_code: Two-letter subdivision code followed in ISO 3166-2.

          subdivision_code_a2: Two-letter subdivision code followed in ISO 3166-2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return cast(
            RegionLoadBalancerRegionsListRegionsResponse,
            self._get(
                f"/accounts/{account_identifier}/load_balancers/regions",
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
                        region_load_balancer_regions_list_regions_params.RegionLoadBalancerRegionsListRegionsParams,
                    ),
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RegionLoadBalancerRegionsListRegionsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncRegions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegionsWithRawResponse:
        return AsyncRegionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionsWithStreamingResponse:
        return AsyncRegionsWithStreamingResponse(self)

    async def get(
        self,
        region_code: Literal[
            "WNAM", "ENAM", "WEU", "EEU", "NSAM", "SSAM", "OC", "ME", "NAF", "SAF", "SAS", "SEAS", "NEAS"
        ],
        *,
        account_identifier: str,
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
          account_identifier: Identifier

          region_code: A list of Cloudflare regions. WNAM: Western North America, ENAM: Eastern North
              America, WEU: Western Europe, EEU: Eastern Europe, NSAM: Northern South America,
              SSAM: Southern South America, OC: Oceania, ME: Middle East, NAF: North Africa,
              SAF: South Africa, SAS: Southern Asia, SEAS: South East Asia, NEAS: North East
              Asia).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not region_code:
            raise ValueError(f"Expected a non-empty value for `region_code` but received {region_code!r}")
        return cast(
            RegionGetResponse,
            await self._get(
                f"/accounts/{account_identifier}/load_balancers/regions/{region_code}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RegionGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def load_balancer_regions_list_regions(
        self,
        account_identifier: str,
        *,
        country_code_a2: str | NotGiven = NOT_GIVEN,
        subdivision_code: str | NotGiven = NOT_GIVEN,
        subdivision_code_a2: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegionLoadBalancerRegionsListRegionsResponse:
        """
        List all region mappings.

        Args:
          account_identifier: Identifier

          country_code_a2: Two-letter alpha-2 country code followed in ISO 3166-1.

          subdivision_code: Two-letter subdivision code followed in ISO 3166-2.

          subdivision_code_a2: Two-letter subdivision code followed in ISO 3166-2.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return cast(
            RegionLoadBalancerRegionsListRegionsResponse,
            await self._get(
                f"/accounts/{account_identifier}/load_balancers/regions",
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
                        region_load_balancer_regions_list_regions_params.RegionLoadBalancerRegionsListRegionsParams,
                    ),
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RegionLoadBalancerRegionsListRegionsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RegionsWithRawResponse:
    def __init__(self, regions: Regions) -> None:
        self._regions = regions

        self.get = to_raw_response_wrapper(
            regions.get,
        )
        self.load_balancer_regions_list_regions = to_raw_response_wrapper(
            regions.load_balancer_regions_list_regions,
        )


class AsyncRegionsWithRawResponse:
    def __init__(self, regions: AsyncRegions) -> None:
        self._regions = regions

        self.get = async_to_raw_response_wrapper(
            regions.get,
        )
        self.load_balancer_regions_list_regions = async_to_raw_response_wrapper(
            regions.load_balancer_regions_list_regions,
        )


class RegionsWithStreamingResponse:
    def __init__(self, regions: Regions) -> None:
        self._regions = regions

        self.get = to_streamed_response_wrapper(
            regions.get,
        )
        self.load_balancer_regions_list_regions = to_streamed_response_wrapper(
            regions.load_balancer_regions_list_regions,
        )


class AsyncRegionsWithStreamingResponse:
    def __init__(self, regions: AsyncRegions) -> None:
        self._regions = regions

        self.get = async_to_streamed_response_wrapper(
            regions.get,
        )
        self.load_balancer_regions_list_regions = async_to_streamed_response_wrapper(
            regions.load_balancer_regions_list_regions,
        )
