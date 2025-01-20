# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, Optional, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.brand_protection import brand_protection_submit_params, brand_protection_url_info_params
from ..types.brand_protection.info import Info
from ..types.brand_protection.submit import Submit

__all__ = ["BrandProtectionResource", "AsyncBrandProtectionResource"]


class BrandProtectionResource(SyncAPIResource):
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
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Submit]:
        """
        Submit suspicious URL for scanning

        Args:
          account_id: Identifier

          url: URL(s) to filter submissions results by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/brand-protection/submit",
            body=maybe_transform({"url": url}, brand_protection_submit_params.BrandProtectionSubmitParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Submit]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Submit]], ResultWrapper[Submit]),
        )

    def url_info(
        self,
        *,
        account_id: str,
        url: List[str] | NotGiven = NOT_GIVEN,
        url_id: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Info]:
        """
        Gets phishing details about a URL.

        Args:
          account_id: Identifier

          url: Submission URL(s) to filter submission results by.

          url_id: Submission ID(s) to filter submission results by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/brand-protection/url-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "url_id": url_id,
                    },
                    brand_protection_url_info_params.BrandProtectionURLInfoParams,
                ),
                post_parser=ResultWrapper[Optional[Info]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Info]], ResultWrapper[Info]),
        )


class AsyncBrandProtectionResource(AsyncAPIResource):
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
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Submit]:
        """
        Submit suspicious URL for scanning

        Args:
          account_id: Identifier

          url: URL(s) to filter submissions results by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/brand-protection/submit",
            body=await async_maybe_transform({"url": url}, brand_protection_submit_params.BrandProtectionSubmitParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Submit]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Submit]], ResultWrapper[Submit]),
        )

    async def url_info(
        self,
        *,
        account_id: str,
        url: List[str] | NotGiven = NOT_GIVEN,
        url_id: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Info]:
        """
        Gets phishing details about a URL.

        Args:
          account_id: Identifier

          url: Submission URL(s) to filter submission results by.

          url_id: Submission ID(s) to filter submission results by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/brand-protection/url-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "url_id": url_id,
                    },
                    brand_protection_url_info_params.BrandProtectionURLInfoParams,
                ),
                post_parser=ResultWrapper[Optional[Info]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Info]], ResultWrapper[Info]),
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


class AsyncBrandProtectionResourceWithRawResponse:
    def __init__(self, brand_protection: AsyncBrandProtectionResource) -> None:
        self._brand_protection = brand_protection

        self.submit = async_to_raw_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = async_to_raw_response_wrapper(
            brand_protection.url_info,
        )


class BrandProtectionResourceWithStreamingResponse:
    def __init__(self, brand_protection: BrandProtectionResource) -> None:
        self._brand_protection = brand_protection

        self.submit = to_streamed_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = to_streamed_response_wrapper(
            brand_protection.url_info,
        )


class AsyncBrandProtectionResourceWithStreamingResponse:
    def __init__(self, brand_protection: AsyncBrandProtectionResource) -> None:
        self._brand_protection = brand_protection

        self.submit = async_to_streamed_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = async_to_streamed_response_wrapper(
            brand_protection.url_info,
        )
