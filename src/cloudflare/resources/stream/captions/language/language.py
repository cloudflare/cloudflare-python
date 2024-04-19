# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .vtt import (
    Vtt,
    AsyncVtt,
    VttWithRawResponse,
    AsyncVttWithRawResponse,
    VttWithStreamingResponse,
    AsyncVttWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import (
    make_request_options,
)
from .....types.stream import Caption
from .....types.stream.captions import LanguageDeleteResponse, language_delete_params, language_update_params

__all__ = ["Language", "AsyncLanguage"]


class Language(SyncAPIResource):
    @cached_property
    def vtt(self) -> Vtt:
        return Vtt(self._client)

    @cached_property
    def with_raw_response(self) -> LanguageWithRawResponse:
        return LanguageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LanguageWithStreamingResponse:
        return LanguageWithStreamingResponse(self)

    def update(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        file: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Uploads the caption or subtitle file to the endpoint for a specific BCP47
        language. One caption or subtitle file per language is allowed.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          file: The WebVTT file containing the caption or subtitle content.

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
        return self._put(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            body=maybe_transform({"file": file}, language_update_params.LanguageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )

    def delete(
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
        Removes the captions or subtitles from a video.

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
        return self._delete(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            body=maybe_transform(body, language_delete_params.LanguageDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LanguageDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def get(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Lists the captions or subtitles for provided language.

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
        return self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )


class AsyncLanguage(AsyncAPIResource):
    @cached_property
    def vtt(self) -> AsyncVtt:
        return AsyncVtt(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLanguageWithRawResponse:
        return AsyncLanguageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLanguageWithStreamingResponse:
        return AsyncLanguageWithStreamingResponse(self)

    async def update(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        file: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Uploads the caption or subtitle file to the endpoint for a specific BCP47
        language. One caption or subtitle file per language is allowed.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          file: The WebVTT file containing the caption or subtitle content.

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
        return await self._put(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            body=await async_maybe_transform({"file": file}, language_update_params.LanguageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )

    async def delete(
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
        Removes the captions or subtitles from a video.

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
        return await self._delete(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            body=await async_maybe_transform(body, language_delete_params.LanguageDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LanguageDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def get(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Lists the captions or subtitles for provided language.

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
        return await self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )


class LanguageWithRawResponse:
    def __init__(self, language: Language) -> None:
        self._language = language

        self.update = to_raw_response_wrapper(
            language.update,
        )
        self.delete = to_raw_response_wrapper(
            language.delete,
        )
        self.get = to_raw_response_wrapper(
            language.get,
        )

    @cached_property
    def vtt(self) -> VttWithRawResponse:
        return VttWithRawResponse(self._language.vtt)


class AsyncLanguageWithRawResponse:
    def __init__(self, language: AsyncLanguage) -> None:
        self._language = language

        self.update = async_to_raw_response_wrapper(
            language.update,
        )
        self.delete = async_to_raw_response_wrapper(
            language.delete,
        )
        self.get = async_to_raw_response_wrapper(
            language.get,
        )

    @cached_property
    def vtt(self) -> AsyncVttWithRawResponse:
        return AsyncVttWithRawResponse(self._language.vtt)


class LanguageWithStreamingResponse:
    def __init__(self, language: Language) -> None:
        self._language = language

        self.update = to_streamed_response_wrapper(
            language.update,
        )
        self.delete = to_streamed_response_wrapper(
            language.delete,
        )
        self.get = to_streamed_response_wrapper(
            language.get,
        )

    @cached_property
    def vtt(self) -> VttWithStreamingResponse:
        return VttWithStreamingResponse(self._language.vtt)


class AsyncLanguageWithStreamingResponse:
    def __init__(self, language: AsyncLanguage) -> None:
        self._language = language

        self.update = async_to_streamed_response_wrapper(
            language.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            language.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            language.get,
        )

    @cached_property
    def vtt(self) -> AsyncVttWithStreamingResponse:
        return AsyncVttWithStreamingResponse(self._language.vtt)
