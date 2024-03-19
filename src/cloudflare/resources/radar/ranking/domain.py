# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
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
from ...._base_client import (
    make_request_options,
)
from ....types.radar.ranking import DomainGetResponse, domain_get_params

__all__ = ["Domain", "AsyncDomain"]


class Domain(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainWithRawResponse:
        return DomainWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainWithStreamingResponse:
        return DomainWithStreamingResponse(self)

    def get(
        self,
        domain: str,
        *,
        date: List[Optional[str]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
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
        """Gets Domains Rank details.

        Cloudflare provides an ordered rank for the top 100
        domains, but for the remainder it only provides ranking buckets like top 200
        thousand, top one million, etc.. These are available through Radar datasets
        endpoints.

        Args:
          date: Array of dates to filter the ranking.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          name: Array of names that will be used to name the series in responses.

          ranking_type: The ranking type.

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
                        "limit": limit,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    domain_get_params.DomainGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )


class AsyncDomain(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainWithRawResponse:
        return AsyncDomainWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainWithStreamingResponse:
        return AsyncDomainWithStreamingResponse(self)

    async def get(
        self,
        domain: str,
        *,
        date: List[Optional[str]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
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
        """Gets Domains Rank details.

        Cloudflare provides an ordered rank for the top 100
        domains, but for the remainder it only provides ranking buckets like top 200
        thousand, top one million, etc.. These are available through Radar datasets
        endpoints.

        Args:
          date: Array of dates to filter the ranking.

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          name: Array of names that will be used to name the series in responses.

          ranking_type: The ranking type.

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
                        "limit": limit,
                        "name": name,
                        "ranking_type": ranking_type,
                    },
                    domain_get_params.DomainGetParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )


class DomainWithRawResponse:
    def __init__(self, domain: Domain) -> None:
        self._domain = domain

        self.get = to_raw_response_wrapper(
            domain.get,
        )


class AsyncDomainWithRawResponse:
    def __init__(self, domain: AsyncDomain) -> None:
        self._domain = domain

        self.get = async_to_raw_response_wrapper(
            domain.get,
        )


class DomainWithStreamingResponse:
    def __init__(self, domain: Domain) -> None:
        self._domain = domain

        self.get = to_streamed_response_wrapper(
            domain.get,
        )


class AsyncDomainWithStreamingResponse:
    def __init__(self, domain: AsyncDomain) -> None:
        self._domain = domain

        self.get = async_to_streamed_response_wrapper(
            domain.get,
        )
