# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.stream import (
    AudioTrackUpdateResponse,
    AudioTrackListResponse,
    AudioTrackDeleteResponse,
    AudioTrackCopyResponse,
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
from ...types.stream import audio_track_update_params
from ...types.stream import audio_track_copy_params
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

__all__ = ["AudioTracks", "AsyncAudioTracks"]


class AudioTracks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AudioTracksWithRawResponse:
        return AudioTracksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudioTracksWithStreamingResponse:
        return AudioTracksWithStreamingResponse(self)

    def update(
        self,
        audio_identifier: str,
        *,
        account_id: str,
        identifier: str,
        default: bool | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTrackUpdateResponse:
        """Edits additional audio tracks on a video.

        Editing the default status of an audio
        track to `true` will mark all other audio tracks on the video default status to
        `false`.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          audio_identifier: The unique identifier for an additional audio track.

          default: Denotes whether the audio track will be played by default in a player.

          label: A string to uniquely identify the track amongst other audio track labels for the
              specified video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not audio_identifier:
            raise ValueError(f"Expected a non-empty value for `audio_identifier` but received {audio_identifier!r}")
        return self._patch(
            f"/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}",
            body=maybe_transform(
                {
                    "default": default,
                    "label": label,
                },
                audio_track_update_params.AudioTrackUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AudioTrackUpdateResponse], ResultWrapper[AudioTrackUpdateResponse]),
        )

    def list(
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
    ) -> AudioTrackListResponse:
        """Lists additional audio tracks on a video.

        Note this API will not return
        information for audio attached to the video upload.

        Args:
          account_id: The account identifier tag.

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
            f"/accounts/{account_id}/stream/{identifier}/audio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AudioTrackListResponse], ResultWrapper[AudioTrackListResponse]),
        )

    def delete(
        self,
        audio_identifier: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTrackDeleteResponse:
        """Deletes additional audio tracks on a video.

        Deleting a default audio track is
        not allowed. You must assign another audio track as default prior to deletion.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          audio_identifier: The unique identifier for an additional audio track.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not audio_identifier:
            raise ValueError(f"Expected a non-empty value for `audio_identifier` but received {audio_identifier!r}")
        return cast(
            AudioTrackDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AudioTrackDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def copy(
        self,
        identifier: str,
        *,
        account_id: str,
        label: str,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTrackCopyResponse:
        """
        Adds an additional audio track to a video using the provided audio track URL.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          label: A string to uniquely identify the track amongst other audio track labels for the
              specified video.

          url: An audio track URL. The server must be publicly routable and support `HTTP HEAD`
              requests and `HTTP GET` range requests. The server should respond to `HTTP HEAD`
              requests with a `content-range` header that includes the size of the file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._post(
            f"/accounts/{account_id}/stream/{identifier}/audio/copy",
            body=maybe_transform(
                {
                    "label": label,
                    "url": url,
                },
                audio_track_copy_params.AudioTrackCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AudioTrackCopyResponse], ResultWrapper[AudioTrackCopyResponse]),
        )


class AsyncAudioTracks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAudioTracksWithRawResponse:
        return AsyncAudioTracksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudioTracksWithStreamingResponse:
        return AsyncAudioTracksWithStreamingResponse(self)

    async def update(
        self,
        audio_identifier: str,
        *,
        account_id: str,
        identifier: str,
        default: bool | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTrackUpdateResponse:
        """Edits additional audio tracks on a video.

        Editing the default status of an audio
        track to `true` will mark all other audio tracks on the video default status to
        `false`.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          audio_identifier: The unique identifier for an additional audio track.

          default: Denotes whether the audio track will be played by default in a player.

          label: A string to uniquely identify the track amongst other audio track labels for the
              specified video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not audio_identifier:
            raise ValueError(f"Expected a non-empty value for `audio_identifier` but received {audio_identifier!r}")
        return await self._patch(
            f"/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}",
            body=maybe_transform(
                {
                    "default": default,
                    "label": label,
                },
                audio_track_update_params.AudioTrackUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AudioTrackUpdateResponse], ResultWrapper[AudioTrackUpdateResponse]),
        )

    async def list(
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
    ) -> AudioTrackListResponse:
        """Lists additional audio tracks on a video.

        Note this API will not return
        information for audio attached to the video upload.

        Args:
          account_id: The account identifier tag.

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
            f"/accounts/{account_id}/stream/{identifier}/audio",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AudioTrackListResponse], ResultWrapper[AudioTrackListResponse]),
        )

    async def delete(
        self,
        audio_identifier: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTrackDeleteResponse:
        """Deletes additional audio tracks on a video.

        Deleting a default audio track is
        not allowed. You must assign another audio track as default prior to deletion.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          audio_identifier: The unique identifier for an additional audio track.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not audio_identifier:
            raise ValueError(f"Expected a non-empty value for `audio_identifier` but received {audio_identifier!r}")
        return cast(
            AudioTrackDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AudioTrackDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def copy(
        self,
        identifier: str,
        *,
        account_id: str,
        label: str,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudioTrackCopyResponse:
        """
        Adds an additional audio track to a video using the provided audio track URL.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          label: A string to uniquely identify the track amongst other audio track labels for the
              specified video.

          url: An audio track URL. The server must be publicly routable and support `HTTP HEAD`
              requests and `HTTP GET` range requests. The server should respond to `HTTP HEAD`
              requests with a `content-range` header that includes the size of the file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._post(
            f"/accounts/{account_id}/stream/{identifier}/audio/copy",
            body=maybe_transform(
                {
                    "label": label,
                    "url": url,
                },
                audio_track_copy_params.AudioTrackCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AudioTrackCopyResponse], ResultWrapper[AudioTrackCopyResponse]),
        )


class AudioTracksWithRawResponse:
    def __init__(self, audio_tracks: AudioTracks) -> None:
        self._audio_tracks = audio_tracks

        self.update = to_raw_response_wrapper(
            audio_tracks.update,
        )
        self.list = to_raw_response_wrapper(
            audio_tracks.list,
        )
        self.delete = to_raw_response_wrapper(
            audio_tracks.delete,
        )
        self.copy = to_raw_response_wrapper(
            audio_tracks.copy,
        )


class AsyncAudioTracksWithRawResponse:
    def __init__(self, audio_tracks: AsyncAudioTracks) -> None:
        self._audio_tracks = audio_tracks

        self.update = async_to_raw_response_wrapper(
            audio_tracks.update,
        )
        self.list = async_to_raw_response_wrapper(
            audio_tracks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            audio_tracks.delete,
        )
        self.copy = async_to_raw_response_wrapper(
            audio_tracks.copy,
        )


class AudioTracksWithStreamingResponse:
    def __init__(self, audio_tracks: AudioTracks) -> None:
        self._audio_tracks = audio_tracks

        self.update = to_streamed_response_wrapper(
            audio_tracks.update,
        )
        self.list = to_streamed_response_wrapper(
            audio_tracks.list,
        )
        self.delete = to_streamed_response_wrapper(
            audio_tracks.delete,
        )
        self.copy = to_streamed_response_wrapper(
            audio_tracks.copy,
        )


class AsyncAudioTracksWithStreamingResponse:
    def __init__(self, audio_tracks: AsyncAudioTracks) -> None:
        self._audio_tracks = audio_tracks

        self.update = async_to_streamed_response_wrapper(
            audio_tracks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            audio_tracks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            audio_tracks.delete,
        )
        self.copy = async_to_streamed_response_wrapper(
            audio_tracks.copy,
        )
