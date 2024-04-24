# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .clip import (
    ClipResource,
    AsyncClipResource,
    ClipResourceWithRawResponse,
    AsyncClipResourceWithRawResponse,
    ClipResourceWithStreamingResponse,
    AsyncClipResourceWithStreamingResponse,
)
from .copy import (
    CopyResource,
    AsyncCopyResource,
    CopyResourceWithRawResponse,
    AsyncCopyResourceWithRawResponse,
    CopyResourceWithStreamingResponse,
    AsyncCopyResourceWithStreamingResponse,
)
from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from .embed import (
    EmbedResource,
    AsyncEmbedResource,
    EmbedResourceWithRawResponse,
    AsyncEmbedResourceWithRawResponse,
    EmbedResourceWithStreamingResponse,
    AsyncEmbedResourceWithStreamingResponse,
)
from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from .videos import (
    VideosResource,
    AsyncVideosResource,
    VideosResourceWithRawResponse,
    AsyncVideosResourceWithRawResponse,
    VideosResourceWithStreamingResponse,
    AsyncVideosResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .captions import (
    CaptionsResource,
    AsyncCaptionsResource,
    CaptionsResourceWithRawResponse,
    AsyncCaptionsResourceWithRawResponse,
    CaptionsResourceWithStreamingResponse,
    AsyncCaptionsResourceWithStreamingResponse,
)
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .downloads import (
    DownloadsResource,
    AsyncDownloadsResource,
    DownloadsResourceWithRawResponse,
    AsyncDownloadsResourceWithRawResponse,
    DownloadsResourceWithStreamingResponse,
    AsyncDownloadsResourceWithStreamingResponse,
)
from .watermarks import (
    WatermarksResource,
    AsyncWatermarksResource,
    WatermarksResourceWithRawResponse,
    AsyncWatermarksResourceWithRawResponse,
    WatermarksResourceWithStreamingResponse,
    AsyncWatermarksResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .live_inputs import (
    LiveInputsResource,
    AsyncLiveInputsResource,
    LiveInputsResourceWithRawResponse,
    AsyncLiveInputsResourceWithRawResponse,
    LiveInputsResourceWithStreamingResponse,
    AsyncLiveInputsResourceWithStreamingResponse,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from .audio_tracks import (
    AudioTracksResource,
    AsyncAudioTracksResource,
    AudioTracksResourceWithRawResponse,
    AsyncAudioTracksResourceWithRawResponse,
    AudioTracksResourceWithStreamingResponse,
    AsyncAudioTracksResourceWithStreamingResponse,
)
from .direct_upload import (
    DirectUploadResource,
    AsyncDirectUploadResource,
    DirectUploadResourceWithRawResponse,
    AsyncDirectUploadResourceWithRawResponse,
    DirectUploadResourceWithStreamingResponse,
    AsyncDirectUploadResourceWithStreamingResponse,
)
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.stream import stream_list_params, stream_create_params
from .captions.captions import CaptionsResource, AsyncCaptionsResource
from ...types.stream.video import Video
from .live_inputs.live_inputs import LiveInputsResource, AsyncLiveInputsResource

__all__ = ["StreamResource", "AsyncStreamResource"]


class StreamResource(SyncAPIResource):
    @cached_property
    def audio_tracks(self) -> AudioTracksResource:
        return AudioTracksResource(self._client)

    @cached_property
    def videos(self) -> VideosResource:
        return VideosResource(self._client)

    @cached_property
    def clip(self) -> ClipResource:
        return ClipResource(self._client)

    @cached_property
    def copy(self) -> CopyResource:
        return CopyResource(self._client)

    @cached_property
    def direct_upload(self) -> DirectUploadResource:
        return DirectUploadResource(self._client)

    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def live_inputs(self) -> LiveInputsResource:
        return LiveInputsResource(self._client)

    @cached_property
    def watermarks(self) -> WatermarksResource:
        return WatermarksResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def captions(self) -> CaptionsResource:
        return CaptionsResource(self._client)

    @cached_property
    def downloads(self) -> DownloadsResource:
        return DownloadsResource(self._client)

    @cached_property
    def embed(self) -> EmbedResource:
        return EmbedResource(self._client)

    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def with_raw_response(self) -> StreamResourceWithRawResponse:
        return StreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StreamResourceWithStreamingResponse:
        return StreamResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: object,
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
            body=maybe_transform(body, stream_create_params.StreamCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        account_id: str,
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
    ) -> SyncSinglePage[Video]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/stream",
            page=SyncSinglePage[Video],
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
                    stream_list_params.StreamListParams,
                ),
            ),
            model=Video,
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
    ) -> Optional[Video]:
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
                post_parser=ResultWrapper[Optional[Video]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Video]], ResultWrapper[Video]),
        )


class AsyncStreamResource(AsyncAPIResource):
    @cached_property
    def audio_tracks(self) -> AsyncAudioTracksResource:
        return AsyncAudioTracksResource(self._client)

    @cached_property
    def videos(self) -> AsyncVideosResource:
        return AsyncVideosResource(self._client)

    @cached_property
    def clip(self) -> AsyncClipResource:
        return AsyncClipResource(self._client)

    @cached_property
    def copy(self) -> AsyncCopyResource:
        return AsyncCopyResource(self._client)

    @cached_property
    def direct_upload(self) -> AsyncDirectUploadResource:
        return AsyncDirectUploadResource(self._client)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def live_inputs(self) -> AsyncLiveInputsResource:
        return AsyncLiveInputsResource(self._client)

    @cached_property
    def watermarks(self) -> AsyncWatermarksResource:
        return AsyncWatermarksResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def captions(self) -> AsyncCaptionsResource:
        return AsyncCaptionsResource(self._client)

    @cached_property
    def downloads(self) -> AsyncDownloadsResource:
        return AsyncDownloadsResource(self._client)

    @cached_property
    def embed(self) -> AsyncEmbedResource:
        return AsyncEmbedResource(self._client)

    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStreamResourceWithRawResponse:
        return AsyncStreamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStreamResourceWithStreamingResponse:
        return AsyncStreamResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        body: object,
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
            body=await async_maybe_transform(body, stream_create_params.StreamCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        account_id: str,
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
    ) -> AsyncPaginator[Video, AsyncSinglePage[Video]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/stream",
            page=AsyncSinglePage[Video],
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
                    stream_list_params.StreamListParams,
                ),
            ),
            model=Video,
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
    ) -> Optional[Video]:
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
                post_parser=ResultWrapper[Optional[Video]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Video]], ResultWrapper[Video]),
        )


class StreamResourceWithRawResponse:
    def __init__(self, stream: StreamResource) -> None:
        self._stream = stream

        self.create = to_raw_response_wrapper(
            stream.create,
        )
        self.list = to_raw_response_wrapper(
            stream.list,
        )
        self.delete = to_raw_response_wrapper(
            stream.delete,
        )
        self.get = to_raw_response_wrapper(
            stream.get,
        )

    @cached_property
    def audio_tracks(self) -> AudioTracksResourceWithRawResponse:
        return AudioTracksResourceWithRawResponse(self._stream.audio_tracks)

    @cached_property
    def videos(self) -> VideosResourceWithRawResponse:
        return VideosResourceWithRawResponse(self._stream.videos)

    @cached_property
    def clip(self) -> ClipResourceWithRawResponse:
        return ClipResourceWithRawResponse(self._stream.clip)

    @cached_property
    def copy(self) -> CopyResourceWithRawResponse:
        return CopyResourceWithRawResponse(self._stream.copy)

    @cached_property
    def direct_upload(self) -> DirectUploadResourceWithRawResponse:
        return DirectUploadResourceWithRawResponse(self._stream.direct_upload)

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._stream.keys)

    @cached_property
    def live_inputs(self) -> LiveInputsResourceWithRawResponse:
        return LiveInputsResourceWithRawResponse(self._stream.live_inputs)

    @cached_property
    def watermarks(self) -> WatermarksResourceWithRawResponse:
        return WatermarksResourceWithRawResponse(self._stream.watermarks)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._stream.webhooks)

    @cached_property
    def captions(self) -> CaptionsResourceWithRawResponse:
        return CaptionsResourceWithRawResponse(self._stream.captions)

    @cached_property
    def downloads(self) -> DownloadsResourceWithRawResponse:
        return DownloadsResourceWithRawResponse(self._stream.downloads)

    @cached_property
    def embed(self) -> EmbedResourceWithRawResponse:
        return EmbedResourceWithRawResponse(self._stream.embed)

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._stream.token)


class AsyncStreamResourceWithRawResponse:
    def __init__(self, stream: AsyncStreamResource) -> None:
        self._stream = stream

        self.create = async_to_raw_response_wrapper(
            stream.create,
        )
        self.list = async_to_raw_response_wrapper(
            stream.list,
        )
        self.delete = async_to_raw_response_wrapper(
            stream.delete,
        )
        self.get = async_to_raw_response_wrapper(
            stream.get,
        )

    @cached_property
    def audio_tracks(self) -> AsyncAudioTracksResourceWithRawResponse:
        return AsyncAudioTracksResourceWithRawResponse(self._stream.audio_tracks)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithRawResponse:
        return AsyncVideosResourceWithRawResponse(self._stream.videos)

    @cached_property
    def clip(self) -> AsyncClipResourceWithRawResponse:
        return AsyncClipResourceWithRawResponse(self._stream.clip)

    @cached_property
    def copy(self) -> AsyncCopyResourceWithRawResponse:
        return AsyncCopyResourceWithRawResponse(self._stream.copy)

    @cached_property
    def direct_upload(self) -> AsyncDirectUploadResourceWithRawResponse:
        return AsyncDirectUploadResourceWithRawResponse(self._stream.direct_upload)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._stream.keys)

    @cached_property
    def live_inputs(self) -> AsyncLiveInputsResourceWithRawResponse:
        return AsyncLiveInputsResourceWithRawResponse(self._stream.live_inputs)

    @cached_property
    def watermarks(self) -> AsyncWatermarksResourceWithRawResponse:
        return AsyncWatermarksResourceWithRawResponse(self._stream.watermarks)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._stream.webhooks)

    @cached_property
    def captions(self) -> AsyncCaptionsResourceWithRawResponse:
        return AsyncCaptionsResourceWithRawResponse(self._stream.captions)

    @cached_property
    def downloads(self) -> AsyncDownloadsResourceWithRawResponse:
        return AsyncDownloadsResourceWithRawResponse(self._stream.downloads)

    @cached_property
    def embed(self) -> AsyncEmbedResourceWithRawResponse:
        return AsyncEmbedResourceWithRawResponse(self._stream.embed)

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._stream.token)


class StreamResourceWithStreamingResponse:
    def __init__(self, stream: StreamResource) -> None:
        self._stream = stream

        self.create = to_streamed_response_wrapper(
            stream.create,
        )
        self.list = to_streamed_response_wrapper(
            stream.list,
        )
        self.delete = to_streamed_response_wrapper(
            stream.delete,
        )
        self.get = to_streamed_response_wrapper(
            stream.get,
        )

    @cached_property
    def audio_tracks(self) -> AudioTracksResourceWithStreamingResponse:
        return AudioTracksResourceWithStreamingResponse(self._stream.audio_tracks)

    @cached_property
    def videos(self) -> VideosResourceWithStreamingResponse:
        return VideosResourceWithStreamingResponse(self._stream.videos)

    @cached_property
    def clip(self) -> ClipResourceWithStreamingResponse:
        return ClipResourceWithStreamingResponse(self._stream.clip)

    @cached_property
    def copy(self) -> CopyResourceWithStreamingResponse:
        return CopyResourceWithStreamingResponse(self._stream.copy)

    @cached_property
    def direct_upload(self) -> DirectUploadResourceWithStreamingResponse:
        return DirectUploadResourceWithStreamingResponse(self._stream.direct_upload)

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._stream.keys)

    @cached_property
    def live_inputs(self) -> LiveInputsResourceWithStreamingResponse:
        return LiveInputsResourceWithStreamingResponse(self._stream.live_inputs)

    @cached_property
    def watermarks(self) -> WatermarksResourceWithStreamingResponse:
        return WatermarksResourceWithStreamingResponse(self._stream.watermarks)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._stream.webhooks)

    @cached_property
    def captions(self) -> CaptionsResourceWithStreamingResponse:
        return CaptionsResourceWithStreamingResponse(self._stream.captions)

    @cached_property
    def downloads(self) -> DownloadsResourceWithStreamingResponse:
        return DownloadsResourceWithStreamingResponse(self._stream.downloads)

    @cached_property
    def embed(self) -> EmbedResourceWithStreamingResponse:
        return EmbedResourceWithStreamingResponse(self._stream.embed)

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._stream.token)


class AsyncStreamResourceWithStreamingResponse:
    def __init__(self, stream: AsyncStreamResource) -> None:
        self._stream = stream

        self.create = async_to_streamed_response_wrapper(
            stream.create,
        )
        self.list = async_to_streamed_response_wrapper(
            stream.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            stream.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            stream.get,
        )

    @cached_property
    def audio_tracks(self) -> AsyncAudioTracksResourceWithStreamingResponse:
        return AsyncAudioTracksResourceWithStreamingResponse(self._stream.audio_tracks)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithStreamingResponse:
        return AsyncVideosResourceWithStreamingResponse(self._stream.videos)

    @cached_property
    def clip(self) -> AsyncClipResourceWithStreamingResponse:
        return AsyncClipResourceWithStreamingResponse(self._stream.clip)

    @cached_property
    def copy(self) -> AsyncCopyResourceWithStreamingResponse:
        return AsyncCopyResourceWithStreamingResponse(self._stream.copy)

    @cached_property
    def direct_upload(self) -> AsyncDirectUploadResourceWithStreamingResponse:
        return AsyncDirectUploadResourceWithStreamingResponse(self._stream.direct_upload)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._stream.keys)

    @cached_property
    def live_inputs(self) -> AsyncLiveInputsResourceWithStreamingResponse:
        return AsyncLiveInputsResourceWithStreamingResponse(self._stream.live_inputs)

    @cached_property
    def watermarks(self) -> AsyncWatermarksResourceWithStreamingResponse:
        return AsyncWatermarksResourceWithStreamingResponse(self._stream.watermarks)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._stream.webhooks)

    @cached_property
    def captions(self) -> AsyncCaptionsResourceWithStreamingResponse:
        return AsyncCaptionsResourceWithStreamingResponse(self._stream.captions)

    @cached_property
    def downloads(self) -> AsyncDownloadsResourceWithStreamingResponse:
        return AsyncDownloadsResourceWithStreamingResponse(self._stream.downloads)

    @cached_property
    def embed(self) -> AsyncEmbedResourceWithStreamingResponse:
        return AsyncEmbedResourceWithStreamingResponse(self._stream.embed)

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._stream.token)
