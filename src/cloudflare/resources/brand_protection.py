# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..types import (
    IntelPhishingURLInfo,
    IntelPhishingURLSubmit,
    brand_protection_submit_params,
    brand_protection_url_info_params,
)
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
from .._base_client import (
    make_request_options,
)

__all__ = ["BrandProtection", "AsyncBrandProtection"]


class BrandProtection(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandProtectionWithRawResponse:
        return BrandProtectionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandProtectionWithStreamingResponse:
        return BrandProtectionWithStreamingResponse(self)

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
    ) -> IntelPhishingURLSubmit:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IntelPhishingURLSubmit], ResultWrapper[IntelPhishingURLSubmit]),
        )

    def url_info(
        self,
        *,
        account_id: str,
        url: str | NotGiven = NOT_GIVEN,
        url_id_param: brand_protection_url_info_params.URLIDParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntelPhishingURLInfo:
        """
        Get results for a URL scan

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
            f"/accounts/{account_id}/brand-protection/url-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "url_id_param": url_id_param,
                    },
                    brand_protection_url_info_params.BrandProtectionURLInfoParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IntelPhishingURLInfo], ResultWrapper[IntelPhishingURLInfo]),
        )


class AsyncBrandProtection(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandProtectionWithRawResponse:
        return AsyncBrandProtectionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandProtectionWithStreamingResponse:
        return AsyncBrandProtectionWithStreamingResponse(self)

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
    ) -> IntelPhishingURLSubmit:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IntelPhishingURLSubmit], ResultWrapper[IntelPhishingURLSubmit]),
        )

    async def url_info(
        self,
        *,
        account_id: str,
        url: str | NotGiven = NOT_GIVEN,
        url_id_param: brand_protection_url_info_params.URLIDParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntelPhishingURLInfo:
        """
        Get results for a URL scan

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
            f"/accounts/{account_id}/brand-protection/url-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "url_id_param": url_id_param,
                    },
                    brand_protection_url_info_params.BrandProtectionURLInfoParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IntelPhishingURLInfo], ResultWrapper[IntelPhishingURLInfo]),
        )


class BrandProtectionWithRawResponse:
    def __init__(self, brand_protection: BrandProtection) -> None:
        self._brand_protection = brand_protection

        self.submit = to_raw_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = to_raw_response_wrapper(
            brand_protection.url_info,
        )


class AsyncBrandProtectionWithRawResponse:
    def __init__(self, brand_protection: AsyncBrandProtection) -> None:
        self._brand_protection = brand_protection

        self.submit = async_to_raw_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = async_to_raw_response_wrapper(
            brand_protection.url_info,
        )


class BrandProtectionWithStreamingResponse:
    def __init__(self, brand_protection: BrandProtection) -> None:
        self._brand_protection = brand_protection

        self.submit = to_streamed_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = to_streamed_response_wrapper(
            brand_protection.url_info,
        )


class AsyncBrandProtectionWithStreamingResponse:
    def __init__(self, brand_protection: AsyncBrandProtection) -> None:
        self._brand_protection = brand_protection

        self.submit = async_to_streamed_response_wrapper(
            brand_protection.submit,
        )
        self.url_info = async_to_streamed_response_wrapper(
            brand_protection.url_info,
        )
