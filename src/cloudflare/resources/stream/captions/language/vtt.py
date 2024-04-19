# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import (
    make_request_options,
)

__all__ = ["Vtt", "AsyncVtt"]


class Vtt(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VttWithRawResponse:
        return VttWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VttWithStreamingResponse:
        return VttWithStreamingResponse(self)

    def get(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Return WebVTT captions for a provided language.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        extra_headers = {"Accept": "text/vtt", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}/vtt",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncVtt(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVttWithRawResponse:
        return AsyncVttWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVttWithStreamingResponse:
        return AsyncVttWithStreamingResponse(self)

    async def get(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Return WebVTT captions for a provided language.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        extra_headers = {"Accept": "text/vtt", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}/vtt",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class VttWithRawResponse:
    def __init__(self, vtt: Vtt) -> None:
        self._vtt = vtt

        self.get = to_raw_response_wrapper(
            vtt.get,
        )


class AsyncVttWithRawResponse:
    def __init__(self, vtt: AsyncVtt) -> None:
        self._vtt = vtt

        self.get = async_to_raw_response_wrapper(
            vtt.get,
        )


class VttWithStreamingResponse:
    def __init__(self, vtt: Vtt) -> None:
        self._vtt = vtt

        self.get = to_streamed_response_wrapper(
            vtt.get,
        )


class AsyncVttWithStreamingResponse:
    def __init__(self, vtt: AsyncVtt) -> None:
        self._vtt = vtt

        self.get = async_to_streamed_response_wrapper(
            vtt.get,
        )
