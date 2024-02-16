# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.stream import (
    CaptionUpdateResponse,
    CaptionDeleteResponse,
    CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse,
)

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.stream import caption_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Captions", "AsyncCaptions"]


class Captions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CaptionsWithRawResponse:
        return CaptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CaptionsWithStreamingResponse:
        return CaptionsWithStreamingResponse(self)

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
    ) -> CaptionUpdateResponse:
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
        return cast(
            CaptionUpdateResponse,
            self._put(
                f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
                body=maybe_transform({"file": file}, caption_update_params.CaptionUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CaptionUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
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
    ) -> CaptionDeleteResponse:
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
        return cast(
            CaptionDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CaptionDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def stream_subtitles_captions_list_captions_or_subtitles(
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
    ) -> CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse],
                ResultWrapper[CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse],
            ),
        )


class AsyncCaptions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCaptionsWithRawResponse:
        return AsyncCaptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCaptionsWithStreamingResponse:
        return AsyncCaptionsWithStreamingResponse(self)

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
    ) -> CaptionUpdateResponse:
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
        return cast(
            CaptionUpdateResponse,
            await self._put(
                f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
                body=maybe_transform({"file": file}, caption_update_params.CaptionUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CaptionUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
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
    ) -> CaptionDeleteResponse:
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
        return cast(
            CaptionDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CaptionDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def stream_subtitles_captions_list_captions_or_subtitles(
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
    ) -> CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse],
                ResultWrapper[CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse],
            ),
        )


class CaptionsWithRawResponse:
    def __init__(self, captions: Captions) -> None:
        self._captions = captions

        self.update = to_raw_response_wrapper(
            captions.update,
        )
        self.delete = to_raw_response_wrapper(
            captions.delete,
        )
        self.stream_subtitles_captions_list_captions_or_subtitles = to_raw_response_wrapper(
            captions.stream_subtitles_captions_list_captions_or_subtitles,
        )


class AsyncCaptionsWithRawResponse:
    def __init__(self, captions: AsyncCaptions) -> None:
        self._captions = captions

        self.update = async_to_raw_response_wrapper(
            captions.update,
        )
        self.delete = async_to_raw_response_wrapper(
            captions.delete,
        )
        self.stream_subtitles_captions_list_captions_or_subtitles = async_to_raw_response_wrapper(
            captions.stream_subtitles_captions_list_captions_or_subtitles,
        )


class CaptionsWithStreamingResponse:
    def __init__(self, captions: Captions) -> None:
        self._captions = captions

        self.update = to_streamed_response_wrapper(
            captions.update,
        )
        self.delete = to_streamed_response_wrapper(
            captions.delete,
        )
        self.stream_subtitles_captions_list_captions_or_subtitles = to_streamed_response_wrapper(
            captions.stream_subtitles_captions_list_captions_or_subtitles,
        )


class AsyncCaptionsWithStreamingResponse:
    def __init__(self, captions: AsyncCaptions) -> None:
        self._captions = captions

        self.update = async_to_streamed_response_wrapper(
            captions.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            captions.delete,
        )
        self.stream_subtitles_captions_list_captions_or_subtitles = async_to_streamed_response_wrapper(
            captions.stream_subtitles_captions_list_captions_or_subtitles,
        )
