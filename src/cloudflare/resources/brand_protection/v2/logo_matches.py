# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.brand_protection.v2 import logo_match_get_params
from ....types.brand_protection.v2.logo_match_get_response import LogoMatchGetResponse

__all__ = ["LogoMatchesResource", "AsyncLogoMatchesResource"]


class LogoMatchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogoMatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LogoMatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogoMatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LogoMatchesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        account_id: str | None = None,
        query_id: str,
        download: str | Omit = omit,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["matchedAt", "domain", "similarityScore", "registrar"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoMatchGetResponse:
        """
        Get paginated list of logo matches for a specific brand protection logo query

        Args:
          order: Sort order. Options: 'asc' (ascending) or 'desc' (descending)

          order_by: Column to sort by. Options: 'matchedAt', 'domain', 'similarityScore', or
              'registrar'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/matches", account_id=account_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query_id": query_id,
                        "download": download,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "order_by": order_by,
                    },
                    logo_match_get_params.LogoMatchGetParams,
                ),
            ),
            cast_to=LogoMatchGetResponse,
        )


class AsyncLogoMatchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogoMatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogoMatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogoMatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLogoMatchesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        account_id: str | None = None,
        query_id: str,
        download: str | Omit = omit,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: Literal["matchedAt", "domain", "similarityScore", "registrar"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoMatchGetResponse:
        """
        Get paginated list of logo matches for a specific brand protection logo query

        Args:
          order: Sort order. Options: 'asc' (ascending) or 'desc' (descending)

          order_by: Column to sort by. Options: 'matchedAt', 'domain', 'similarityScore', or
              'registrar'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/matches", account_id=account_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query_id": query_id,
                        "download": download,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "order_by": order_by,
                    },
                    logo_match_get_params.LogoMatchGetParams,
                ),
            ),
            cast_to=LogoMatchGetResponse,
        )


class LogoMatchesResourceWithRawResponse:
    def __init__(self, logo_matches: LogoMatchesResource) -> None:
        self._logo_matches = logo_matches

        self.get = to_raw_response_wrapper(
            logo_matches.get,
        )


class AsyncLogoMatchesResourceWithRawResponse:
    def __init__(self, logo_matches: AsyncLogoMatchesResource) -> None:
        self._logo_matches = logo_matches

        self.get = async_to_raw_response_wrapper(
            logo_matches.get,
        )


class LogoMatchesResourceWithStreamingResponse:
    def __init__(self, logo_matches: LogoMatchesResource) -> None:
        self._logo_matches = logo_matches

        self.get = to_streamed_response_wrapper(
            logo_matches.get,
        )


class AsyncLogoMatchesResourceWithStreamingResponse:
    def __init__(self, logo_matches: AsyncLogoMatchesResource) -> None:
        self._logo_matches = logo_matches

        self.get = async_to_streamed_response_wrapper(
            logo_matches.get,
        )
