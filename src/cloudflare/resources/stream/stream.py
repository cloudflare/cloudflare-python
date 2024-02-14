# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .audio_tracks import AudioTracks, AsyncAudioTracks

from ..._compat import cached_property

from .videos import Videos, AsyncVideos

from .clips import Clips, AsyncClips

from .copies import Copies, AsyncCopies

from .direct_uploads import DirectUploads, AsyncDirectUploads

from .keys import Keys, AsyncKeys

from .live_inputs.live_inputs import LiveInputs, AsyncLiveInputs

from .watermarks import Watermarks, AsyncWatermarks

from .webhooks import Webhooks, AsyncWebhooks

from .captions import Captions, AsyncCaptions

from .downloads import Downloads, AsyncDownloads

from .embeds import Embeds, AsyncEmbeds

from .tokens import Tokens, AsyncTokens

from ...types import StreamUpdateResponse, StreamGetResponse, StreamStreamVideosListVideosResponse

from typing import Type, List, Union

from datetime import datetime

from typing_extensions import Literal

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
from ...types import stream_update_params
from ...types import stream_stream_videos_list_videos_params
from .audio_tracks import (
    AudioTracks,
    AsyncAudioTracks,
    AudioTracksWithRawResponse,
    AsyncAudioTracksWithRawResponse,
    AudioTracksWithStreamingResponse,
    AsyncAudioTracksWithStreamingResponse,
)
from .videos import (
    Videos,
    AsyncVideos,
    VideosWithRawResponse,
    AsyncVideosWithRawResponse,
    VideosWithStreamingResponse,
    AsyncVideosWithStreamingResponse,
)
from .clips import (
    Clips,
    AsyncClips,
    ClipsWithRawResponse,
    AsyncClipsWithRawResponse,
    ClipsWithStreamingResponse,
    AsyncClipsWithStreamingResponse,
)
from .copies import (
    Copies,
    AsyncCopies,
    CopiesWithRawResponse,
    AsyncCopiesWithRawResponse,
    CopiesWithStreamingResponse,
    AsyncCopiesWithStreamingResponse,
)
from .direct_uploads import (
    DirectUploads,
    AsyncDirectUploads,
    DirectUploadsWithRawResponse,
    AsyncDirectUploadsWithRawResponse,
    DirectUploadsWithStreamingResponse,
    AsyncDirectUploadsWithStreamingResponse,
)
from .keys import (
    Keys,
    AsyncKeys,
    KeysWithRawResponse,
    AsyncKeysWithRawResponse,
    KeysWithStreamingResponse,
    AsyncKeysWithStreamingResponse,
)
from .live_inputs import (
    LiveInputs,
    AsyncLiveInputs,
    LiveInputsWithRawResponse,
    AsyncLiveInputsWithRawResponse,
    LiveInputsWithStreamingResponse,
    AsyncLiveInputsWithStreamingResponse,
)
from .watermarks import (
    Watermarks,
    AsyncWatermarks,
    WatermarksWithRawResponse,
    AsyncWatermarksWithRawResponse,
    WatermarksWithStreamingResponse,
    AsyncWatermarksWithStreamingResponse,
)
from .webhooks import (
    Webhooks,
    AsyncWebhooks,
    WebhooksWithRawResponse,
    AsyncWebhooksWithRawResponse,
    WebhooksWithStreamingResponse,
    AsyncWebhooksWithStreamingResponse,
)
from .captions import (
    Captions,
    AsyncCaptions,
    CaptionsWithRawResponse,
    AsyncCaptionsWithRawResponse,
    CaptionsWithStreamingResponse,
    AsyncCaptionsWithStreamingResponse,
)
from .downloads import (
    Downloads,
    AsyncDownloads,
    DownloadsWithRawResponse,
    AsyncDownloadsWithRawResponse,
    DownloadsWithStreamingResponse,
    AsyncDownloadsWithStreamingResponse,
)
from .embeds import (
    Embeds,
    AsyncEmbeds,
    EmbedsWithRawResponse,
    AsyncEmbedsWithRawResponse,
    EmbedsWithStreamingResponse,
    AsyncEmbedsWithStreamingResponse,
)
from .tokens import (
    Tokens,
    AsyncTokens,
    TokensWithRawResponse,
    AsyncTokensWithRawResponse,
    TokensWithStreamingResponse,
    AsyncTokensWithStreamingResponse,
)
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Stream", "AsyncStream"]


class Stream(SyncAPIResource):
    @cached_property
    def audio_tracks(self) -> AudioTracks:
        return AudioTracks(self._client)

    @cached_property
    def videos(self) -> Videos:
        return Videos(self._client)

    @cached_property
    def clips(self) -> Clips:
        return Clips(self._client)

    @cached_property
    def copies(self) -> Copies:
        return Copies(self._client)

    @cached_property
    def direct_uploads(self) -> DirectUploads:
        return DirectUploads(self._client)

    @cached_property
    def keys(self) -> Keys:
        return Keys(self._client)

    @cached_property
    def live_inputs(self) -> LiveInputs:
        return LiveInputs(self._client)

    @cached_property
    def watermarks(self) -> Watermarks:
        return Watermarks(self._client)

    @cached_property
    def webhooks(self) -> Webhooks:
        return Webhooks(self._client)

    @cached_property
    def captions(self) -> Captions:
        return Captions(self._client)

    @cached_property
    def downloads(self) -> Downloads:
        return Downloads(self._client)

    @cached_property
    def embeds(self) -> Embeds:
        return Embeds(self._client)

    @cached_property
    def tokens(self) -> Tokens:
        return Tokens(self._client)

    @cached_property
    def with_raw_response(self) -> StreamWithRawResponse:
        return StreamWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamWithStreamingResponse:
        return StreamWithStreamingResponse(self)

    def update(
        self,
        identifier: str,
        *,
        account_id: str,
        allowed_origins: List[str] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        scheduled_deletion: Union[str, datetime] | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        upload_expiry: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StreamUpdateResponse:
        """
        Edit details for a single video.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          max_duration_seconds: The maximum duration in seconds for a video upload. Can be set for a video that
              is not yet uploaded to limit its duration. Uploads that exceed the specified
              duration will fail during processing. A value of `-1` means the value is
              unknown.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing videos.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          scheduled_deletion: Indicates the date and time at which the video will be deleted. Omit the field
              to indicate no change, or include with a `null` value to remove an existing
              scheduled deletion. If specified, must be at least 30 days from upload time.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          upload_expiry: The date and time when the video upload URL is no longer valid for direct user
              uploads.

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
            f"/accounts/{account_id}/stream/{identifier}",
            body=maybe_transform(
                {
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "max_duration_seconds": max_duration_seconds,
                    "meta": meta,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "upload_expiry": upload_expiry,
                },
                stream_update_params.StreamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[StreamUpdateResponse], ResultWrapper[StreamUpdateResponse]),
        )

    def delete(
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
    ) -> None:
        """
        Deletes a video and its copies from Cloudflare Stream.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/stream/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> StreamGetResponse:
        """
        Fetches details for a single video.

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
            f"/accounts/{account_id}/stream/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[StreamGetResponse], ResultWrapper[StreamGetResponse]),
        )

    def stream_videos_initiate_video_uploads_using_tus(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Initiates a video upload using the TUS protocol.

        On success, the server responds
        with a status code 201 (created) and includes a `location` header to indicate
        where the content should be uploaded. Refer to https://tus.io for protocol
        details.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/accounts/{account_id}/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def stream_videos_list_videos(
        self,
        account_id: str,
        *,
        asc: bool | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_counts: bool | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["pendingupload", "downloading", "queued", "inprogress", "ready", "error"]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StreamStreamVideosListVideosResponse:
        """Lists up to 1000 videos from a single request.

        For a specific range, refer to
        the optional parameters.

        Args:
          account_id: The account identifier tag.

          asc: Lists videos in ascending order of creation.

          creator: A user-defined identifier for the media creator.

          end: Lists videos created before the specified date.

          include_counts: Includes the total number of videos associated with the submitted query
              parameters.

          search: Searches over the `name` key in the `meta` field. This field can be set with or
              after the upload request.

          start: Lists videos created after the specified date.

          status: Specifies the processing status for all quality levels for a video.

          type: Specifies whether the video is `vod` or `live`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asc": asc,
                        "creator": creator,
                        "end": end,
                        "include_counts": include_counts,
                        "search": search,
                        "start": start,
                        "status": status,
                        "type": type,
                    },
                    stream_stream_videos_list_videos_params.StreamStreamVideosListVideosParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[StreamStreamVideosListVideosResponse], ResultWrapper[StreamStreamVideosListVideosResponse]
            ),
        )


class AsyncStream(AsyncAPIResource):
    @cached_property
    def audio_tracks(self) -> AsyncAudioTracks:
        return AsyncAudioTracks(self._client)

    @cached_property
    def videos(self) -> AsyncVideos:
        return AsyncVideos(self._client)

    @cached_property
    def clips(self) -> AsyncClips:
        return AsyncClips(self._client)

    @cached_property
    def copies(self) -> AsyncCopies:
        return AsyncCopies(self._client)

    @cached_property
    def direct_uploads(self) -> AsyncDirectUploads:
        return AsyncDirectUploads(self._client)

    @cached_property
    def keys(self) -> AsyncKeys:
        return AsyncKeys(self._client)

    @cached_property
    def live_inputs(self) -> AsyncLiveInputs:
        return AsyncLiveInputs(self._client)

    @cached_property
    def watermarks(self) -> AsyncWatermarks:
        return AsyncWatermarks(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooks:
        return AsyncWebhooks(self._client)

    @cached_property
    def captions(self) -> AsyncCaptions:
        return AsyncCaptions(self._client)

    @cached_property
    def downloads(self) -> AsyncDownloads:
        return AsyncDownloads(self._client)

    @cached_property
    def embeds(self) -> AsyncEmbeds:
        return AsyncEmbeds(self._client)

    @cached_property
    def tokens(self) -> AsyncTokens:
        return AsyncTokens(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStreamWithRawResponse:
        return AsyncStreamWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamWithStreamingResponse:
        return AsyncStreamWithStreamingResponse(self)

    async def update(
        self,
        identifier: str,
        *,
        account_id: str,
        allowed_origins: List[str] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        scheduled_deletion: Union[str, datetime] | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        upload_expiry: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StreamUpdateResponse:
        """
        Edit details for a single video.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          max_duration_seconds: The maximum duration in seconds for a video upload. Can be set for a video that
              is not yet uploaded to limit its duration. Uploads that exceed the specified
              duration will fail during processing. A value of `-1` means the value is
              unknown.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing videos.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          scheduled_deletion: Indicates the date and time at which the video will be deleted. Omit the field
              to indicate no change, or include with a `null` value to remove an existing
              scheduled deletion. If specified, must be at least 30 days from upload time.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          upload_expiry: The date and time when the video upload URL is no longer valid for direct user
              uploads.

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
            f"/accounts/{account_id}/stream/{identifier}",
            body=maybe_transform(
                {
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "max_duration_seconds": max_duration_seconds,
                    "meta": meta,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "upload_expiry": upload_expiry,
                },
                stream_update_params.StreamUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[StreamUpdateResponse], ResultWrapper[StreamUpdateResponse]),
        )

    async def delete(
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
    ) -> None:
        """
        Deletes a video and its copies from Cloudflare Stream.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/stream/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

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
    ) -> StreamGetResponse:
        """
        Fetches details for a single video.

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
            f"/accounts/{account_id}/stream/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[StreamGetResponse], ResultWrapper[StreamGetResponse]),
        )

    async def stream_videos_initiate_video_uploads_using_tus(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Initiates a video upload using the TUS protocol.

        On success, the server responds
        with a status code 201 (created) and includes a `location` header to indicate
        where the content should be uploaded. Refer to https://tus.io for protocol
        details.

        Args:
          account_id: The account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/accounts/{account_id}/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def stream_videos_list_videos(
        self,
        account_id: str,
        *,
        asc: bool | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_counts: bool | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["pendingupload", "downloading", "queued", "inprogress", "ready", "error"]
        | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StreamStreamVideosListVideosResponse:
        """Lists up to 1000 videos from a single request.

        For a specific range, refer to
        the optional parameters.

        Args:
          account_id: The account identifier tag.

          asc: Lists videos in ascending order of creation.

          creator: A user-defined identifier for the media creator.

          end: Lists videos created before the specified date.

          include_counts: Includes the total number of videos associated with the submitted query
              parameters.

          search: Searches over the `name` key in the `meta` field. This field can be set with or
              after the upload request.

          start: Lists videos created after the specified date.

          status: Specifies the processing status for all quality levels for a video.

          type: Specifies whether the video is `vod` or `live`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asc": asc,
                        "creator": creator,
                        "end": end,
                        "include_counts": include_counts,
                        "search": search,
                        "start": start,
                        "status": status,
                        "type": type,
                    },
                    stream_stream_videos_list_videos_params.StreamStreamVideosListVideosParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[StreamStreamVideosListVideosResponse], ResultWrapper[StreamStreamVideosListVideosResponse]
            ),
        )


class StreamWithRawResponse:
    def __init__(self, stream: Stream) -> None:
        self._stream = stream

        self.update = to_raw_response_wrapper(
            stream.update,
        )
        self.delete = to_raw_response_wrapper(
            stream.delete,
        )
        self.get = to_raw_response_wrapper(
            stream.get,
        )
        self.stream_videos_initiate_video_uploads_using_tus = to_raw_response_wrapper(
            stream.stream_videos_initiate_video_uploads_using_tus,
        )
        self.stream_videos_list_videos = to_raw_response_wrapper(
            stream.stream_videos_list_videos,
        )

    @cached_property
    def audio_tracks(self) -> AudioTracksWithRawResponse:
        return AudioTracksWithRawResponse(self._stream.audio_tracks)

    @cached_property
    def videos(self) -> VideosWithRawResponse:
        return VideosWithRawResponse(self._stream.videos)

    @cached_property
    def clips(self) -> ClipsWithRawResponse:
        return ClipsWithRawResponse(self._stream.clips)

    @cached_property
    def copies(self) -> CopiesWithRawResponse:
        return CopiesWithRawResponse(self._stream.copies)

    @cached_property
    def direct_uploads(self) -> DirectUploadsWithRawResponse:
        return DirectUploadsWithRawResponse(self._stream.direct_uploads)

    @cached_property
    def keys(self) -> KeysWithRawResponse:
        return KeysWithRawResponse(self._stream.keys)

    @cached_property
    def live_inputs(self) -> LiveInputsWithRawResponse:
        return LiveInputsWithRawResponse(self._stream.live_inputs)

    @cached_property
    def watermarks(self) -> WatermarksWithRawResponse:
        return WatermarksWithRawResponse(self._stream.watermarks)

    @cached_property
    def webhooks(self) -> WebhooksWithRawResponse:
        return WebhooksWithRawResponse(self._stream.webhooks)

    @cached_property
    def captions(self) -> CaptionsWithRawResponse:
        return CaptionsWithRawResponse(self._stream.captions)

    @cached_property
    def downloads(self) -> DownloadsWithRawResponse:
        return DownloadsWithRawResponse(self._stream.downloads)

    @cached_property
    def embeds(self) -> EmbedsWithRawResponse:
        return EmbedsWithRawResponse(self._stream.embeds)

    @cached_property
    def tokens(self) -> TokensWithRawResponse:
        return TokensWithRawResponse(self._stream.tokens)


class AsyncStreamWithRawResponse:
    def __init__(self, stream: AsyncStream) -> None:
        self._stream = stream

        self.update = async_to_raw_response_wrapper(
            stream.update,
        )
        self.delete = async_to_raw_response_wrapper(
            stream.delete,
        )
        self.get = async_to_raw_response_wrapper(
            stream.get,
        )
        self.stream_videos_initiate_video_uploads_using_tus = async_to_raw_response_wrapper(
            stream.stream_videos_initiate_video_uploads_using_tus,
        )
        self.stream_videos_list_videos = async_to_raw_response_wrapper(
            stream.stream_videos_list_videos,
        )

    @cached_property
    def audio_tracks(self) -> AsyncAudioTracksWithRawResponse:
        return AsyncAudioTracksWithRawResponse(self._stream.audio_tracks)

    @cached_property
    def videos(self) -> AsyncVideosWithRawResponse:
        return AsyncVideosWithRawResponse(self._stream.videos)

    @cached_property
    def clips(self) -> AsyncClipsWithRawResponse:
        return AsyncClipsWithRawResponse(self._stream.clips)

    @cached_property
    def copies(self) -> AsyncCopiesWithRawResponse:
        return AsyncCopiesWithRawResponse(self._stream.copies)

    @cached_property
    def direct_uploads(self) -> AsyncDirectUploadsWithRawResponse:
        return AsyncDirectUploadsWithRawResponse(self._stream.direct_uploads)

    @cached_property
    def keys(self) -> AsyncKeysWithRawResponse:
        return AsyncKeysWithRawResponse(self._stream.keys)

    @cached_property
    def live_inputs(self) -> AsyncLiveInputsWithRawResponse:
        return AsyncLiveInputsWithRawResponse(self._stream.live_inputs)

    @cached_property
    def watermarks(self) -> AsyncWatermarksWithRawResponse:
        return AsyncWatermarksWithRawResponse(self._stream.watermarks)

    @cached_property
    def webhooks(self) -> AsyncWebhooksWithRawResponse:
        return AsyncWebhooksWithRawResponse(self._stream.webhooks)

    @cached_property
    def captions(self) -> AsyncCaptionsWithRawResponse:
        return AsyncCaptionsWithRawResponse(self._stream.captions)

    @cached_property
    def downloads(self) -> AsyncDownloadsWithRawResponse:
        return AsyncDownloadsWithRawResponse(self._stream.downloads)

    @cached_property
    def embeds(self) -> AsyncEmbedsWithRawResponse:
        return AsyncEmbedsWithRawResponse(self._stream.embeds)

    @cached_property
    def tokens(self) -> AsyncTokensWithRawResponse:
        return AsyncTokensWithRawResponse(self._stream.tokens)


class StreamWithStreamingResponse:
    def __init__(self, stream: Stream) -> None:
        self._stream = stream

        self.update = to_streamed_response_wrapper(
            stream.update,
        )
        self.delete = to_streamed_response_wrapper(
            stream.delete,
        )
        self.get = to_streamed_response_wrapper(
            stream.get,
        )
        self.stream_videos_initiate_video_uploads_using_tus = to_streamed_response_wrapper(
            stream.stream_videos_initiate_video_uploads_using_tus,
        )
        self.stream_videos_list_videos = to_streamed_response_wrapper(
            stream.stream_videos_list_videos,
        )

    @cached_property
    def audio_tracks(self) -> AudioTracksWithStreamingResponse:
        return AudioTracksWithStreamingResponse(self._stream.audio_tracks)

    @cached_property
    def videos(self) -> VideosWithStreamingResponse:
        return VideosWithStreamingResponse(self._stream.videos)

    @cached_property
    def clips(self) -> ClipsWithStreamingResponse:
        return ClipsWithStreamingResponse(self._stream.clips)

    @cached_property
    def copies(self) -> CopiesWithStreamingResponse:
        return CopiesWithStreamingResponse(self._stream.copies)

    @cached_property
    def direct_uploads(self) -> DirectUploadsWithStreamingResponse:
        return DirectUploadsWithStreamingResponse(self._stream.direct_uploads)

    @cached_property
    def keys(self) -> KeysWithStreamingResponse:
        return KeysWithStreamingResponse(self._stream.keys)

    @cached_property
    def live_inputs(self) -> LiveInputsWithStreamingResponse:
        return LiveInputsWithStreamingResponse(self._stream.live_inputs)

    @cached_property
    def watermarks(self) -> WatermarksWithStreamingResponse:
        return WatermarksWithStreamingResponse(self._stream.watermarks)

    @cached_property
    def webhooks(self) -> WebhooksWithStreamingResponse:
        return WebhooksWithStreamingResponse(self._stream.webhooks)

    @cached_property
    def captions(self) -> CaptionsWithStreamingResponse:
        return CaptionsWithStreamingResponse(self._stream.captions)

    @cached_property
    def downloads(self) -> DownloadsWithStreamingResponse:
        return DownloadsWithStreamingResponse(self._stream.downloads)

    @cached_property
    def embeds(self) -> EmbedsWithStreamingResponse:
        return EmbedsWithStreamingResponse(self._stream.embeds)

    @cached_property
    def tokens(self) -> TokensWithStreamingResponse:
        return TokensWithStreamingResponse(self._stream.tokens)


class AsyncStreamWithStreamingResponse:
    def __init__(self, stream: AsyncStream) -> None:
        self._stream = stream

        self.update = async_to_streamed_response_wrapper(
            stream.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            stream.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            stream.get,
        )
        self.stream_videos_initiate_video_uploads_using_tus = async_to_streamed_response_wrapper(
            stream.stream_videos_initiate_video_uploads_using_tus,
        )
        self.stream_videos_list_videos = async_to_streamed_response_wrapper(
            stream.stream_videos_list_videos,
        )

    @cached_property
    def audio_tracks(self) -> AsyncAudioTracksWithStreamingResponse:
        return AsyncAudioTracksWithStreamingResponse(self._stream.audio_tracks)

    @cached_property
    def videos(self) -> AsyncVideosWithStreamingResponse:
        return AsyncVideosWithStreamingResponse(self._stream.videos)

    @cached_property
    def clips(self) -> AsyncClipsWithStreamingResponse:
        return AsyncClipsWithStreamingResponse(self._stream.clips)

    @cached_property
    def copies(self) -> AsyncCopiesWithStreamingResponse:
        return AsyncCopiesWithStreamingResponse(self._stream.copies)

    @cached_property
    def direct_uploads(self) -> AsyncDirectUploadsWithStreamingResponse:
        return AsyncDirectUploadsWithStreamingResponse(self._stream.direct_uploads)

    @cached_property
    def keys(self) -> AsyncKeysWithStreamingResponse:
        return AsyncKeysWithStreamingResponse(self._stream.keys)

    @cached_property
    def live_inputs(self) -> AsyncLiveInputsWithStreamingResponse:
        return AsyncLiveInputsWithStreamingResponse(self._stream.live_inputs)

    @cached_property
    def watermarks(self) -> AsyncWatermarksWithStreamingResponse:
        return AsyncWatermarksWithStreamingResponse(self._stream.watermarks)

    @cached_property
    def webhooks(self) -> AsyncWebhooksWithStreamingResponse:
        return AsyncWebhooksWithStreamingResponse(self._stream.webhooks)

    @cached_property
    def captions(self) -> AsyncCaptionsWithStreamingResponse:
        return AsyncCaptionsWithStreamingResponse(self._stream.captions)

    @cached_property
    def downloads(self) -> AsyncDownloadsWithStreamingResponse:
        return AsyncDownloadsWithStreamingResponse(self._stream.downloads)

    @cached_property
    def embeds(self) -> AsyncEmbedsWithStreamingResponse:
        return AsyncEmbedsWithStreamingResponse(self._stream.embeds)

    @cached_property
    def tokens(self) -> AsyncTokensWithStreamingResponse:
        return AsyncTokensWithStreamingResponse(self._stream.tokens)
