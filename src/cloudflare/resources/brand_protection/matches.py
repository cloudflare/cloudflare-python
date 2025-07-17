# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.brand_protection import match_get_params, match_download_params
from ...types.brand_protection.match_get_response import MatchGetResponse
from ...types.brand_protection.match_download_response import MatchDownloadResponse

__all__ = ["MatchesResource", "AsyncMatchesResource"]


class MatchesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MatchesResourceWithStreamingResponse(self)

    def download(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        include_domain_id: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MatchDownloadResponse:
        """
        Return matches as CSV for string queries based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/brand-protection/matches/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "include_domain_id": include_domain_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    match_download_params.MatchDownloadParams,
                ),
            ),
            cast_to=MatchDownloadResponse,
        )

    def get(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        include_domain_id: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MatchGetResponse:
        """
        Return matches for string queries based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/brand-protection/matches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "include_domain_id": include_domain_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    match_get_params.MatchGetParams,
                ),
            ),
            cast_to=MatchGetResponse,
        )


class AsyncMatchesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMatchesResourceWithStreamingResponse(self)

    async def download(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        include_domain_id: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MatchDownloadResponse:
        """
        Return matches as CSV for string queries based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/brand-protection/matches/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "include_domain_id": include_domain_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    match_download_params.MatchDownloadParams,
                ),
            ),
            cast_to=MatchDownloadResponse,
        )

    async def get(
        self,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        include_domain_id: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MatchGetResponse:
        """
        Return matches for string queries based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/brand-protection/matches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "include_domain_id": include_domain_id,
                        "limit": limit,
                        "offset": offset,
                    },
                    match_get_params.MatchGetParams,
                ),
            ),
            cast_to=MatchGetResponse,
        )


class MatchesResourceWithRawResponse:
    def __init__(self, matches: MatchesResource) -> None:
        self._matches = matches

        self.download = to_raw_response_wrapper(
            matches.download,
        )
        self.get = to_raw_response_wrapper(
            matches.get,
        )


class AsyncMatchesResourceWithRawResponse:
    def __init__(self, matches: AsyncMatchesResource) -> None:
        self._matches = matches

        self.download = async_to_raw_response_wrapper(
            matches.download,
        )
        self.get = async_to_raw_response_wrapper(
            matches.get,
        )


class MatchesResourceWithStreamingResponse:
    def __init__(self, matches: MatchesResource) -> None:
        self._matches = matches

        self.download = to_streamed_response_wrapper(
            matches.download,
        )
        self.get = to_streamed_response_wrapper(
            matches.get,
        )


class AsyncMatchesResourceWithStreamingResponse:
    def __init__(self, matches: AsyncMatchesResource) -> None:
        self._matches = matches

        self.download = async_to_streamed_response_wrapper(
            matches.download,
        )
        self.get = async_to_streamed_response_wrapper(
            matches.get,
        )
