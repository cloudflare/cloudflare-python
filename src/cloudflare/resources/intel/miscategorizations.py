# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.intel import miscategorization_create_params
from ..._base_client import make_request_options
from ...types.intel.miscategorization_create_response import MiscategorizationCreateResponse

__all__ = ["MiscategorizationsResource", "AsyncMiscategorizationsResource"]


class MiscategorizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MiscategorizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MiscategorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MiscategorizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MiscategorizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        content_adds: Iterable[int] | NotGiven = NOT_GIVEN,
        content_removes: Iterable[int] | NotGiven = NOT_GIVEN,
        indicator_type: Literal["domain", "ipv4", "ipv6", "url"] | NotGiven = NOT_GIVEN,
        ip: Optional[str] | NotGiven = NOT_GIVEN,
        security_adds: Iterable[int] | NotGiven = NOT_GIVEN,
        security_removes: Iterable[int] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MiscategorizationCreateResponse:
        """
        Allows you to submit requests to change a domain’s category.

        Args:
          account_id: Identifier

          content_adds: Content category IDs to add.

          content_removes: Content category IDs to remove.

          ip: Provide only if indicator_type is `ipv4` or `ipv6`.

          security_adds: Security category IDs to add.

          security_removes: Security category IDs to remove.

          url: Provide only if indicator_type is `domain` or `url`. Example if indicator_type
              is `domain`: `example.com`. Example if indicator_type is `url`:
              `https://example.com/news/`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/intel/miscategorization",
            body=maybe_transform(
                {
                    "content_adds": content_adds,
                    "content_removes": content_removes,
                    "indicator_type": indicator_type,
                    "ip": ip,
                    "security_adds": security_adds,
                    "security_removes": security_removes,
                    "url": url,
                },
                miscategorization_create_params.MiscategorizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MiscategorizationCreateResponse,
        )


class AsyncMiscategorizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMiscategorizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMiscategorizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMiscategorizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMiscategorizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        content_adds: Iterable[int] | NotGiven = NOT_GIVEN,
        content_removes: Iterable[int] | NotGiven = NOT_GIVEN,
        indicator_type: Literal["domain", "ipv4", "ipv6", "url"] | NotGiven = NOT_GIVEN,
        ip: Optional[str] | NotGiven = NOT_GIVEN,
        security_adds: Iterable[int] | NotGiven = NOT_GIVEN,
        security_removes: Iterable[int] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MiscategorizationCreateResponse:
        """
        Allows you to submit requests to change a domain’s category.

        Args:
          account_id: Identifier

          content_adds: Content category IDs to add.

          content_removes: Content category IDs to remove.

          ip: Provide only if indicator_type is `ipv4` or `ipv6`.

          security_adds: Security category IDs to add.

          security_removes: Security category IDs to remove.

          url: Provide only if indicator_type is `domain` or `url`. Example if indicator_type
              is `domain`: `example.com`. Example if indicator_type is `url`:
              `https://example.com/news/`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/intel/miscategorization",
            body=await async_maybe_transform(
                {
                    "content_adds": content_adds,
                    "content_removes": content_removes,
                    "indicator_type": indicator_type,
                    "ip": ip,
                    "security_adds": security_adds,
                    "security_removes": security_removes,
                    "url": url,
                },
                miscategorization_create_params.MiscategorizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MiscategorizationCreateResponse,
        )


class MiscategorizationsResourceWithRawResponse:
    def __init__(self, miscategorizations: MiscategorizationsResource) -> None:
        self._miscategorizations = miscategorizations

        self.create = to_raw_response_wrapper(
            miscategorizations.create,
        )


class AsyncMiscategorizationsResourceWithRawResponse:
    def __init__(self, miscategorizations: AsyncMiscategorizationsResource) -> None:
        self._miscategorizations = miscategorizations

        self.create = async_to_raw_response_wrapper(
            miscategorizations.create,
        )


class MiscategorizationsResourceWithStreamingResponse:
    def __init__(self, miscategorizations: MiscategorizationsResource) -> None:
        self._miscategorizations = miscategorizations

        self.create = to_streamed_response_wrapper(
            miscategorizations.create,
        )


class AsyncMiscategorizationsResourceWithStreamingResponse:
    def __init__(self, miscategorizations: AsyncMiscategorizationsResource) -> None:
        self._miscategorizations = miscategorizations

        self.create = async_to_streamed_response_wrapper(
            miscategorizations.create,
        )
