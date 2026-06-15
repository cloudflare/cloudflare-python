# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.intel.domains import bulk_get_params
from ....types.intel.domains.bulk_get_response import BulkGetResponse

__all__ = ["BulksResource", "AsyncBulksResource"]


class BulksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BulksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BulksResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str,
        domain: SequenceNotStr[str] | Omit = omit,
        include_ranking: bool | Omit = omit,
        skip_ranking: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BulkGetResponse]:
        """
        Returns security details and statistics about multiple domains in a single
        request.

        **Behavior change — domain ranking is becoming opt-in.** This endpoint
        previously included domain ranking data in every response and accepted a
        `skip_ranking=true` query parameter to opt out. That parameter is being
        deprecated and ranking will no longer be returned by default. Callers that want
        ranking data must pass `include_ranking=true`. The `skip_ranking` parameter will
        be silently ignored once the change ships.

        Args:
          account_id: Identifier.

          domain: Accepts multiple values like `?domain=cloudflare.com&domain=example.com`.

          include_ranking: Whether to include domain ranking data in the response. Defaults to `false` —
              ranking lookups are expensive at bulk scale and most callers do not need them.
              Set to `true` to opt in. This parameter replaces the deprecated `skip_ranking`
              (see below).

          skip_ranking: **Deprecated.** Previously controlled whether the ranking lookup was skipped
              (defaulted to `false`, meaning ranking ran). The endpoint's default behavior is
              being flipped — ranking is now opt-in via `include_ranking=true` — and this
              parameter will be silently ignored. Remove it from your callers and use
              `include_ranking` instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/intel/domain/bulk", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "include_ranking": include_ranking,
                        "skip_ranking": skip_ranking,
                    },
                    bulk_get_params.BulkGetParams,
                ),
                post_parser=ResultWrapper[Optional[BulkGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BulkGetResponse]], ResultWrapper[BulkGetResponse]),
        )


class AsyncBulksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBulksResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str,
        domain: SequenceNotStr[str] | Omit = omit,
        include_ranking: bool | Omit = omit,
        skip_ranking: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[BulkGetResponse]:
        """
        Returns security details and statistics about multiple domains in a single
        request.

        **Behavior change — domain ranking is becoming opt-in.** This endpoint
        previously included domain ranking data in every response and accepted a
        `skip_ranking=true` query parameter to opt out. That parameter is being
        deprecated and ranking will no longer be returned by default. Callers that want
        ranking data must pass `include_ranking=true`. The `skip_ranking` parameter will
        be silently ignored once the change ships.

        Args:
          account_id: Identifier.

          domain: Accepts multiple values like `?domain=cloudflare.com&domain=example.com`.

          include_ranking: Whether to include domain ranking data in the response. Defaults to `false` —
              ranking lookups are expensive at bulk scale and most callers do not need them.
              Set to `true` to opt in. This parameter replaces the deprecated `skip_ranking`
              (see below).

          skip_ranking: **Deprecated.** Previously controlled whether the ranking lookup was skipped
              (defaulted to `false`, meaning ranking ran). The endpoint's default behavior is
              being flipped — ranking is now opt-in via `include_ranking=true` — and this
              parameter will be silently ignored. Remove it from your callers and use
              `include_ranking` instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/intel/domain/bulk", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "include_ranking": include_ranking,
                        "skip_ranking": skip_ranking,
                    },
                    bulk_get_params.BulkGetParams,
                ),
                post_parser=ResultWrapper[Optional[BulkGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[BulkGetResponse]], ResultWrapper[BulkGetResponse]),
        )


class BulksResourceWithRawResponse:
    def __init__(self, bulks: BulksResource) -> None:
        self._bulks = bulks

        self.get = to_raw_response_wrapper(
            bulks.get,
        )


class AsyncBulksResourceWithRawResponse:
    def __init__(self, bulks: AsyncBulksResource) -> None:
        self._bulks = bulks

        self.get = async_to_raw_response_wrapper(
            bulks.get,
        )


class BulksResourceWithStreamingResponse:
    def __init__(self, bulks: BulksResource) -> None:
        self._bulks = bulks

        self.get = to_streamed_response_wrapper(
            bulks.get,
        )


class AsyncBulksResourceWithStreamingResponse:
    def __init__(self, bulks: AsyncBulksResource) -> None:
        self._bulks = bulks

        self.get = async_to_streamed_response_wrapper(
            bulks.get,
        )
