# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.brand_protection import logo_match_get_params, logo_match_download_params
from ...types.brand_protection.logo_match_get_response import LogoMatchGetResponse
from ...types.brand_protection.logo_match_download_response import LogoMatchDownloadResponse

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

    def download(
        self,
        *,
        account_id: str,
        limit: str | Omit = omit,
        logo_id: SequenceNotStr[str] | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoMatchDownloadResponse:
        """
        Return matches as CSV for logo queries based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/brand-protection/logo-matches/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "logo_id": logo_id,
                        "offset": offset,
                    },
                    logo_match_download_params.LogoMatchDownloadParams,
                ),
            ),
            cast_to=LogoMatchDownloadResponse,
        )

    def get(
        self,
        *,
        account_id: str,
        limit: str | Omit = omit,
        logo_id: SequenceNotStr[str] | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoMatchGetResponse:
        """
        Return matches for logo queries based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/brand-protection/logo-matches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "logo_id": logo_id,
                        "offset": offset,
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

    async def download(
        self,
        *,
        account_id: str,
        limit: str | Omit = omit,
        logo_id: SequenceNotStr[str] | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoMatchDownloadResponse:
        """
        Return matches as CSV for logo queries based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/brand-protection/logo-matches/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "logo_id": logo_id,
                        "offset": offset,
                    },
                    logo_match_download_params.LogoMatchDownloadParams,
                ),
            ),
            cast_to=LogoMatchDownloadResponse,
        )

    async def get(
        self,
        *,
        account_id: str,
        limit: str | Omit = omit,
        logo_id: SequenceNotStr[str] | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoMatchGetResponse:
        """
        Return matches for logo queries based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/brand-protection/logo-matches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "logo_id": logo_id,
                        "offset": offset,
                    },
                    logo_match_get_params.LogoMatchGetParams,
                ),
            ),
            cast_to=LogoMatchGetResponse,
        )


class LogoMatchesResourceWithRawResponse:
    def __init__(self, logo_matches: LogoMatchesResource) -> None:
        self._logo_matches = logo_matches

        self.download = to_raw_response_wrapper(
            logo_matches.download,
        )
        self.get = to_raw_response_wrapper(
            logo_matches.get,
        )


class AsyncLogoMatchesResourceWithRawResponse:
    def __init__(self, logo_matches: AsyncLogoMatchesResource) -> None:
        self._logo_matches = logo_matches

        self.download = async_to_raw_response_wrapper(
            logo_matches.download,
        )
        self.get = async_to_raw_response_wrapper(
            logo_matches.get,
        )


class LogoMatchesResourceWithStreamingResponse:
    def __init__(self, logo_matches: LogoMatchesResource) -> None:
        self._logo_matches = logo_matches

        self.download = to_streamed_response_wrapper(
            logo_matches.download,
        )
        self.get = to_streamed_response_wrapper(
            logo_matches.get,
        )


class AsyncLogoMatchesResourceWithStreamingResponse:
    def __init__(self, logo_matches: AsyncLogoMatchesResource) -> None:
        self._logo_matches = logo_matches

        self.download = async_to_streamed_response_wrapper(
            logo_matches.download,
        )
        self.get = async_to_streamed_response_wrapper(
            logo_matches.get,
        )
