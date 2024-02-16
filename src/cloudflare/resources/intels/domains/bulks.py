# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.intels.domains import BulkDomainIntelligenceGetMultipleDomainDetailsResponse

from typing import Type, Optional

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
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.intels.domains import bulk_domain_intelligence_get_multiple_domain_details_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Bulks", "AsyncBulks"]


class Bulks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulksWithRawResponse:
        return BulksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulksWithStreamingResponse:
        return BulksWithStreamingResponse(self)

    def domain_intelligence_get_multiple_domain_details(
        self,
        account_id: str,
        *,
        domain: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BulkDomainIntelligenceGetMultipleDomainDetailsResponse]:
        """
        Get Multiple Domain Details

        Args:
          account_id: Identifier

          domain: Accepts multiple values, i.e. `?domain=cloudflare.com&domain=example.com`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/domain/bulk",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"domain": domain},
                    bulk_domain_intelligence_get_multiple_domain_details_params.BulkDomainIntelligenceGetMultipleDomainDetailsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[BulkDomainIntelligenceGetMultipleDomainDetailsResponse]],
                ResultWrapper[BulkDomainIntelligenceGetMultipleDomainDetailsResponse],
            ),
        )


class AsyncBulks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulksWithRawResponse:
        return AsyncBulksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulksWithStreamingResponse:
        return AsyncBulksWithStreamingResponse(self)

    async def domain_intelligence_get_multiple_domain_details(
        self,
        account_id: str,
        *,
        domain: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BulkDomainIntelligenceGetMultipleDomainDetailsResponse]:
        """
        Get Multiple Domain Details

        Args:
          account_id: Identifier

          domain: Accepts multiple values, i.e. `?domain=cloudflare.com&domain=example.com`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/domain/bulk",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"domain": domain},
                    bulk_domain_intelligence_get_multiple_domain_details_params.BulkDomainIntelligenceGetMultipleDomainDetailsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[BulkDomainIntelligenceGetMultipleDomainDetailsResponse]],
                ResultWrapper[BulkDomainIntelligenceGetMultipleDomainDetailsResponse],
            ),
        )


class BulksWithRawResponse:
    def __init__(self, bulks: Bulks) -> None:
        self._bulks = bulks

        self.domain_intelligence_get_multiple_domain_details = to_raw_response_wrapper(
            bulks.domain_intelligence_get_multiple_domain_details,
        )


class AsyncBulksWithRawResponse:
    def __init__(self, bulks: AsyncBulks) -> None:
        self._bulks = bulks

        self.domain_intelligence_get_multiple_domain_details = async_to_raw_response_wrapper(
            bulks.domain_intelligence_get_multiple_domain_details,
        )


class BulksWithStreamingResponse:
    def __init__(self, bulks: Bulks) -> None:
        self._bulks = bulks

        self.domain_intelligence_get_multiple_domain_details = to_streamed_response_wrapper(
            bulks.domain_intelligence_get_multiple_domain_details,
        )


class AsyncBulksWithStreamingResponse:
    def __init__(self, bulks: AsyncBulks) -> None:
        self._bulks = bulks

        self.domain_intelligence_get_multiple_domain_details = async_to_streamed_response_wrapper(
            bulks.domain_intelligence_get_multiple_domain_details,
        )
