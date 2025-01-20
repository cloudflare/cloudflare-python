# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .bulks import (
    BulksResource,
    AsyncBulksResource,
    BulksResourceWithRawResponse,
    AsyncBulksResourceWithRawResponse,
    BulksResourceWithStreamingResponse,
    AsyncBulksResourceWithStreamingResponse,
)
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
from ....types.intel import domain_get_params
from ...._base_client import make_request_options
from ....types.intel.domain import Domain

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def bulks(self) -> BulksResource:
        return BulksResource(self._client)

    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DomainsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Domain]:
        """
        Gets security details and statistics about a domain.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain": domain}, domain_get_params.DomainGetParams),
                post_parser=ResultWrapper[Optional[Domain]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Domain]], ResultWrapper[Domain]),
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def bulks(self) -> AsyncBulksResource:
        return AsyncBulksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDomainsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Domain]:
        """
        Gets security details and statistics about a domain.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"domain": domain}, domain_get_params.DomainGetParams),
                post_parser=ResultWrapper[Optional[Domain]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Domain]], ResultWrapper[Domain]),
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.get = to_raw_response_wrapper(
            domains.get,
        )

    @cached_property
    def bulks(self) -> BulksResourceWithRawResponse:
        return BulksResourceWithRawResponse(self._domains.bulks)


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.get = async_to_raw_response_wrapper(
            domains.get,
        )

    @cached_property
    def bulks(self) -> AsyncBulksResourceWithRawResponse:
        return AsyncBulksResourceWithRawResponse(self._domains.bulks)


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.get = to_streamed_response_wrapper(
            domains.get,
        )

    @cached_property
    def bulks(self) -> BulksResourceWithStreamingResponse:
        return BulksResourceWithStreamingResponse(self._domains.bulks)


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.get = async_to_streamed_response_wrapper(
            domains.get,
        )

    @cached_property
    def bulks(self) -> AsyncBulksResourceWithStreamingResponse:
        return AsyncBulksResourceWithStreamingResponse(self._domains.bulks)
