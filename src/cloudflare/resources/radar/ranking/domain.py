# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.radar.ranking.domain_get_response import DomainGetResponse

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options

from typing import Type, List

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.radar.ranking import domain_get_params
from typing import cast
from typing import cast

__all__ = ["DomainResource", "AsyncDomainResource"]


class DomainResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainResourceWithRawResponse:
        return DomainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainResourceWithStreamingResponse:
        return DomainResourceWithStreamingResponse(self)

    def get(
        self,
        domain: str,
        *,
        date: List[str] | NotGiven = NOT_GIVEN,
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
                post_parser=ResultWrapper[DomainGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )


class AsyncDomainResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainResourceWithRawResponse:
        return AsyncDomainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainResourceWithStreamingResponse:
        return AsyncDomainResourceWithStreamingResponse(self)

    async def get(
        self,
        domain: str,
        *,
        date: List[str] | NotGiven = NOT_GIVEN,
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
