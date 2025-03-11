# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import date
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.radar.ranking import domain_get_params
from ....types.radar.ranking.domain_get_response import DomainGetResponse

__all__ = ["DomainResource", "AsyncDomainResource"]


class DomainResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DomainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DomainResourceWithStreamingResponse(self)

    def get(
        self,
        domain: str,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        include_top_locations: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        ranking_type: Literal["POPULAR", "TRENDING_RISE", "TRENDING_STEADY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainGetResponse:
        """Retrieves domain rank details.

        Cloudflare provides an ordered rank for the top
        100 domains, but for the remainder it only provides ranking buckets like top 200
        thousand, top one million, etc.. These are available through Radar datasets
        endpoints.

        Args:
          domain: Domain name.

          date: Array of dates to filter the results.

          format: Format in which results will be returned.

          include_top_locations: Includes top locations in the response.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          ranking_type: Ranking type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        return self._get(
            f"/radar/ranking/domain/{domain}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "include_top_locations": include_top_locations,
                        "limit": limit,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    domain_get_params.DomainGetParams,
                ),
                post_parser=ResultWrapper[DomainGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )


class AsyncDomainResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDomainResourceWithStreamingResponse(self)

    async def get(
        self,
        domain: str,
        *,
        date: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        include_top_locations: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        ranking_type: Literal["POPULAR", "TRENDING_RISE", "TRENDING_STEADY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainGetResponse:
        """Retrieves domain rank details.

        Cloudflare provides an ordered rank for the top
        100 domains, but for the remainder it only provides ranking buckets like top 200
        thousand, top one million, etc.. These are available through Radar datasets
        endpoints.

        Args:
          domain: Domain name.

          date: Array of dates to filter the results.

          format: Format in which results will be returned.

          include_top_locations: Includes top locations in the response.

          limit: Limits the number of objects returned in the response.

          name: Array of names used to label the series in the response.

          ranking_type: Ranking type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        return await self._get(
            f"/radar/ranking/domain/{domain}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "format": format,
                        "include_top_locations": include_top_locations,
                        "limit": limit,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    domain_get_params.DomainGetParams,
                ),
                post_parser=ResultWrapper[DomainGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )


class DomainResourceWithRawResponse:
    def __init__(self, domain: DomainResource) -> None:
        self._domain = domain

        self.get = to_raw_response_wrapper(
            domain.get,
        )


class AsyncDomainResourceWithRawResponse:
    def __init__(self, domain: AsyncDomainResource) -> None:
        self._domain = domain

        self.get = async_to_raw_response_wrapper(
            domain.get,
        )


class DomainResourceWithStreamingResponse:
    def __init__(self, domain: DomainResource) -> None:
        self._domain = domain

        self.get = to_streamed_response_wrapper(
            domain.get,
        )


class AsyncDomainResourceWithStreamingResponse:
    def __init__(self, domain: AsyncDomainResource) -> None:
        self._domain = domain

        self.get = async_to_streamed_response_wrapper(
            domain.get,
        )
