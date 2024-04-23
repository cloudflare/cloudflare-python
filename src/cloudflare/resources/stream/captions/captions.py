# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .language import (
    Language,
    AsyncLanguage,
    LanguageWithRawResponse,
    AsyncLanguageWithRawResponse,
    LanguageWithStreamingResponse,
    AsyncLanguageWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from .language.language import Language, AsyncLanguage
from ....types.stream.caption_get_response import CaptionGetResponse

__all__ = ["Captions", "AsyncCaptions"]


class Captions(SyncAPIResource):
    @cached_property
    def language(self) -> Language:
        return Language(self._client)

    @cached_property
    def with_raw_response(self) -> CaptionsWithRawResponse:
        return CaptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CaptionsWithStreamingResponse:
        return CaptionsWithStreamingResponse(self)

    def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CaptionGetResponse]:
        """
        Lists the available captions or subtitles for a specific video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CaptionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CaptionGetResponse]], ResultWrapper[CaptionGetResponse]),
        )


class AsyncCaptions(AsyncAPIResource):
    @cached_property
    def language(self) -> AsyncLanguage:
        return AsyncLanguage(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCaptionsWithRawResponse:
        return AsyncCaptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCaptionsWithStreamingResponse:
        return AsyncCaptionsWithStreamingResponse(self)

    async def get(
        self,
        identifier: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CaptionGetResponse]:
        """
        Lists the available captions or subtitles for a specific video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CaptionGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CaptionGetResponse]], ResultWrapper[CaptionGetResponse]),
        )


class CaptionsWithRawResponse:
    def __init__(self, captions: Captions) -> None:
        self._captions = captions

        self.get = to_raw_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> LanguageWithRawResponse:
        return LanguageWithRawResponse(self._captions.language)


class AsyncCaptionsWithRawResponse:
    def __init__(self, captions: AsyncCaptions) -> None:
        self._captions = captions

        self.get = async_to_raw_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> AsyncLanguageWithRawResponse:
        return AsyncLanguageWithRawResponse(self._captions.language)


class CaptionsWithStreamingResponse:
    def __init__(self, captions: Captions) -> None:
        self._captions = captions

        self.get = to_streamed_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> LanguageWithStreamingResponse:
        return LanguageWithStreamingResponse(self._captions.language)


class AsyncCaptionsWithStreamingResponse:
    def __init__(self, captions: AsyncCaptions) -> None:
        self._captions = captions

        self.get = async_to_streamed_response_wrapper(
            captions.get,
        )

    @cached_property
    def language(self) -> AsyncLanguageWithStreamingResponse:
        return AsyncLanguageWithStreamingResponse(self._captions.language)
