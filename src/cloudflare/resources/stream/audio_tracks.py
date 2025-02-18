# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.stream import audio_track_copy_params, audio_track_edit_params
from ...types.stream.audio import Audio
from ...types.stream.audio_track_delete_response import AudioTrackDeleteResponse

__all__ = ["AudioTracksResource", "AsyncAudioTracksResource"]


class AudioTracksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AudioTracksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AudioTracksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudioTracksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AudioTracksResourceWithStreamingResponse(self)

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
    ) -> str:
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
        return self._delete(
            f"/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AudioTrackDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
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
    ) -> Optional[Audio]:
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
                post_parser=ResultWrapper[Optional[Audio]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Audio]], ResultWrapper[Audio]),
        )

    def edit(
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
    ) -> Optional[Audio]:
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
                audio_track_edit_params.AudioTrackEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Audio]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Audio]], ResultWrapper[Audio]),
        )

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
    ) -> SyncSinglePage[Audio]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/stream/{identifier}/audio",
            page=SyncSinglePage[Audio],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Audio,
        )


class AsyncAudioTracksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAudioTracksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAudioTracksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudioTracksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAudioTracksResourceWithStreamingResponse(self)

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
    ) -> str:
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
        return await self._delete(
            f"/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AudioTrackDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
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
    ) -> Optional[Audio]:
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
            body=await async_maybe_transform(
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
                post_parser=ResultWrapper[Optional[Audio]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Audio]], ResultWrapper[Audio]),
        )

    async def edit(
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
    ) -> Optional[Audio]:
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
            body=await async_maybe_transform(
                {
                    "default": default,
                    "label": label,
                },
                audio_track_edit_params.AudioTrackEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Audio]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Audio]], ResultWrapper[Audio]),
        )

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
    ) -> AsyncPaginator[Audio, AsyncSinglePage[Audio]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/stream/{identifier}/audio",
            page=AsyncSinglePage[Audio],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Audio,
        )


class AudioTracksResourceWithRawResponse:
    def __init__(self, audio_tracks: AudioTracksResource) -> None:
        self._audio_tracks = audio_tracks

        self.delete = to_raw_response_wrapper(
            audio_tracks.delete,
        )
        self.copy = to_raw_response_wrapper(
            audio_tracks.copy,
        )
        self.edit = to_raw_response_wrapper(
            audio_tracks.edit,
        )
        self.get = to_raw_response_wrapper(
            audio_tracks.get,
        )


class AsyncAudioTracksResourceWithRawResponse:
    def __init__(self, audio_tracks: AsyncAudioTracksResource) -> None:
        self._audio_tracks = audio_tracks

        self.delete = async_to_raw_response_wrapper(
            audio_tracks.delete,
        )
        self.copy = async_to_raw_response_wrapper(
            audio_tracks.copy,
        )
        self.edit = async_to_raw_response_wrapper(
            audio_tracks.edit,
        )
        self.get = async_to_raw_response_wrapper(
            audio_tracks.get,
        )


class AudioTracksResourceWithStreamingResponse:
    def __init__(self, audio_tracks: AudioTracksResource) -> None:
        self._audio_tracks = audio_tracks

        self.delete = to_streamed_response_wrapper(
            audio_tracks.delete,
        )
        self.copy = to_streamed_response_wrapper(
            audio_tracks.copy,
        )
        self.edit = to_streamed_response_wrapper(
            audio_tracks.edit,
        )
        self.get = to_streamed_response_wrapper(
            audio_tracks.get,
        )


class AsyncAudioTracksResourceWithStreamingResponse:
    def __init__(self, audio_tracks: AsyncAudioTracksResource) -> None:
        self._audio_tracks = audio_tracks

        self.delete = async_to_streamed_response_wrapper(
            audio_tracks.delete,
        )
        self.copy = async_to_streamed_response_wrapper(
            audio_tracks.copy,
        )
        self.edit = async_to_streamed_response_wrapper(
            audio_tracks.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            audio_tracks.get,
        )
