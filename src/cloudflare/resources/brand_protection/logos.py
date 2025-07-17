# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
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
from ...types.brand_protection import logo_create_params
from ...types.brand_protection.logo_create_response import LogoCreateResponse

__all__ = ["LogosResource", "AsyncLogosResource"]


class LogosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LogosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LogosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        match_type: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        image: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogoCreateResponse:
        """
        Return new saved logo queries created from image files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/brand-protection/logos",
            body=maybe_transform({"image": image}, logo_create_params.LogoCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "match_type": match_type,
                        "tag": tag,
                        "threshold": threshold,
                    },
                    logo_create_params.LogoCreateParams,
                ),
            ),
            cast_to=LogoCreateResponse,
        )

    def delete(
        self,
        logo_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Return a success message after deleting saved logo queries by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not logo_id:
            raise ValueError(f"Expected a non-empty value for `logo_id` but received {logo_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/brand-protection/logos/{logo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLogosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLogosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        match_type: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        image: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LogoCreateResponse:
        """
        Return new saved logo queries created from image files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/brand-protection/logos",
            body=await async_maybe_transform({"image": image}, logo_create_params.LogoCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "match_type": match_type,
                        "tag": tag,
                        "threshold": threshold,
                    },
                    logo_create_params.LogoCreateParams,
                ),
            ),
            cast_to=LogoCreateResponse,
        )

    async def delete(
        self,
        logo_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Return a success message after deleting saved logo queries by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not logo_id:
            raise ValueError(f"Expected a non-empty value for `logo_id` but received {logo_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/brand-protection/logos/{logo_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LogosResourceWithRawResponse:
    def __init__(self, logos: LogosResource) -> None:
        self._logos = logos

        self.create = to_raw_response_wrapper(
            logos.create,
        )
        self.delete = to_raw_response_wrapper(
            logos.delete,
        )


class AsyncLogosResourceWithRawResponse:
    def __init__(self, logos: AsyncLogosResource) -> None:
        self._logos = logos

        self.create = async_to_raw_response_wrapper(
            logos.create,
        )
        self.delete = async_to_raw_response_wrapper(
            logos.delete,
        )


class LogosResourceWithStreamingResponse:
    def __init__(self, logos: LogosResource) -> None:
        self._logos = logos

        self.create = to_streamed_response_wrapper(
            logos.create,
        )
        self.delete = to_streamed_response_wrapper(
            logos.delete,
        )


class AsyncLogosResourceWithStreamingResponse:
    def __init__(self, logos: AsyncLogosResource) -> None:
        self._logos = logos

        self.create = async_to_streamed_response_wrapper(
            logos.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            logos.delete,
        )
