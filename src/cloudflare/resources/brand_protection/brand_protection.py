# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .logos import (
    LogosResource,
    AsyncLogosResource,
    LogosResourceWithRawResponse,
    AsyncLogosResourceWithRawResponse,
    LogosResourceWithStreamingResponse,
    AsyncLogosResourceWithStreamingResponse,
)
from .matches import (
    MatchesResource,
    AsyncMatchesResource,
    MatchesResourceWithRawResponse,
    AsyncMatchesResourceWithRawResponse,
    MatchesResourceWithStreamingResponse,
    AsyncMatchesResourceWithStreamingResponse,
)
from .queries import (
    QueriesResource,
    AsyncQueriesResource,
    QueriesResourceWithRawResponse,
    AsyncQueriesResourceWithRawResponse,
    QueriesResourceWithStreamingResponse,
    AsyncQueriesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from .logo_matches import (
    LogoMatchesResource,
    AsyncLogoMatchesResource,
    LogoMatchesResourceWithRawResponse,
    AsyncLogoMatchesResourceWithRawResponse,
    LogoMatchesResourceWithStreamingResponse,
    AsyncLogoMatchesResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.brand_protection.brand_protection_submit_response import BrandProtectionSubmitResponse
from ...types.brand_protection.brand_protection_url_info_response import BrandProtectionURLInfoResponse

__all__ = ["BrandProtectionResource", "AsyncBrandProtectionResource"]


class BrandProtectionResource(SyncAPIResource):
    @cached_property
    def queries(self) -> QueriesResource:
        return QueriesResource(self._client)

    @cached_property
    def matches(self) -> MatchesResource:
        return MatchesResource(self._client)

    @cached_property
    def logos(self) -> LogosResource:
        return LogosResource(self._client)

    @cached_property
    def logo_matches(self) -> LogoMatchesResource:
        return LogoMatchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrandProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BrandProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BrandProtectionResourceWithStreamingResponse(self)

    def submit(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandProtectionSubmitResponse:
        """
        Return new URL submissions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/brand-protection/submit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandProtectionSubmitResponse,
        )

    def url_info(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[BrandProtectionURLInfoResponse]:
        """
        Return submitted URLs based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/brand-protection/url-info",
            page=SyncSinglePage[BrandProtectionURLInfoResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=BrandProtectionURLInfoResponse,
        )


class AsyncBrandProtectionResource(AsyncAPIResource):
    @cached_property
    def queries(self) -> AsyncQueriesResource:
        return AsyncQueriesResource(self._client)

    @cached_property
    def matches(self) -> AsyncMatchesResource:
        return AsyncMatchesResource(self._client)

    @cached_property
    def logos(self) -> AsyncLogosResource:
        return AsyncLogosResource(self._client)

    @cached_property
    def logo_matches(self) -> AsyncLogoMatchesResource:
        return AsyncLogoMatchesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrandProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBrandProtectionResourceWithStreamingResponse(self)

    async def submit(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandProtectionSubmitResponse:
        """
        Return new URL submissions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/brand-protection/submit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandProtectionSubmitResponse,
        )

    def url_info(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BrandProtectionURLInfoResponse, AsyncSinglePage[BrandProtectionURLInfoResponse]]:
        """
        Return submitted URLs based on ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/brand-protection/url-info",
            page=AsyncSinglePage[BrandProtectionURLInfoResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=BrandProtectionURLInfoResponse,
        )


class BrandProtectionResourceWithRawResponse:
    def __init__(self, brand_protection: BrandProtectionResource) -> None:
        self._brand_protection = brand_protection

        self.submit = to_raw_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = to_raw_response_wrapper(
            brand_protection.url_info,
        )

    @cached_property
    def queries(self) -> QueriesResourceWithRawResponse:
        return QueriesResourceWithRawResponse(self._brand_protection.queries)

    @cached_property
    def matches(self) -> MatchesResourceWithRawResponse:
        return MatchesResourceWithRawResponse(self._brand_protection.matches)

    @cached_property
    def logos(self) -> LogosResourceWithRawResponse:
        return LogosResourceWithRawResponse(self._brand_protection.logos)

    @cached_property
    def logo_matches(self) -> LogoMatchesResourceWithRawResponse:
        return LogoMatchesResourceWithRawResponse(self._brand_protection.logo_matches)


class AsyncBrandProtectionResourceWithRawResponse:
    def __init__(self, brand_protection: AsyncBrandProtectionResource) -> None:
        self._brand_protection = brand_protection

        self.submit = async_to_raw_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = async_to_raw_response_wrapper(
            brand_protection.url_info,
        )

    @cached_property
    def queries(self) -> AsyncQueriesResourceWithRawResponse:
        return AsyncQueriesResourceWithRawResponse(self._brand_protection.queries)

    @cached_property
    def matches(self) -> AsyncMatchesResourceWithRawResponse:
        return AsyncMatchesResourceWithRawResponse(self._brand_protection.matches)

    @cached_property
    def logos(self) -> AsyncLogosResourceWithRawResponse:
        return AsyncLogosResourceWithRawResponse(self._brand_protection.logos)

    @cached_property
    def logo_matches(self) -> AsyncLogoMatchesResourceWithRawResponse:
        return AsyncLogoMatchesResourceWithRawResponse(self._brand_protection.logo_matches)


class BrandProtectionResourceWithStreamingResponse:
    def __init__(self, brand_protection: BrandProtectionResource) -> None:
        self._brand_protection = brand_protection

        self.submit = to_streamed_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = to_streamed_response_wrapper(
            brand_protection.url_info,
        )

    @cached_property
    def queries(self) -> QueriesResourceWithStreamingResponse:
        return QueriesResourceWithStreamingResponse(self._brand_protection.queries)

    @cached_property
    def matches(self) -> MatchesResourceWithStreamingResponse:
        return MatchesResourceWithStreamingResponse(self._brand_protection.matches)

    @cached_property
    def logos(self) -> LogosResourceWithStreamingResponse:
        return LogosResourceWithStreamingResponse(self._brand_protection.logos)

    @cached_property
    def logo_matches(self) -> LogoMatchesResourceWithStreamingResponse:
        return LogoMatchesResourceWithStreamingResponse(self._brand_protection.logo_matches)


class AsyncBrandProtectionResourceWithStreamingResponse:
    def __init__(self, brand_protection: AsyncBrandProtectionResource) -> None:
        self._brand_protection = brand_protection

        self.submit = async_to_streamed_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = async_to_streamed_response_wrapper(
            brand_protection.url_info,
        )

    @cached_property
    def queries(self) -> AsyncQueriesResourceWithStreamingResponse:
        return AsyncQueriesResourceWithStreamingResponse(self._brand_protection.queries)

    @cached_property
    def matches(self) -> AsyncMatchesResourceWithStreamingResponse:
        return AsyncMatchesResourceWithStreamingResponse(self._brand_protection.matches)

    @cached_property
    def logos(self) -> AsyncLogosResourceWithStreamingResponse:
        return AsyncLogosResourceWithStreamingResponse(self._brand_protection.logos)

    @cached_property
    def logo_matches(self) -> AsyncLogoMatchesResourceWithStreamingResponse:
        return AsyncLogoMatchesResourceWithStreamingResponse(self._brand_protection.logo_matches)
