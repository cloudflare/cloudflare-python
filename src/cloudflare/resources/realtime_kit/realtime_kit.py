# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .apps import (
    AppsResource,
    AsyncAppsResource,
    AppsResourceWithRawResponse,
    AsyncAppsResourceWithRawResponse,
    AppsResourceWithStreamingResponse,
    AsyncAppsResourceWithStreamingResponse,
)
from .presets import (
    PresetsResource,
    AsyncPresetsResource,
    PresetsResourceWithRawResponse,
    AsyncPresetsResourceWithRawResponse,
    PresetsResourceWithStreamingResponse,
    AsyncPresetsResourceWithStreamingResponse,
)
from .meetings import (
    MeetingsResource,
    AsyncMeetingsResource,
    MeetingsResourceWithRawResponse,
    AsyncMeetingsResourceWithRawResponse,
    MeetingsResourceWithStreamingResponse,
    AsyncMeetingsResourceWithStreamingResponse,
)
from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
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
from .analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)
from .recordings import (
    RecordingsResource,
    AsyncRecordingsResource,
    RecordingsResourceWithRawResponse,
    AsyncRecordingsResourceWithRawResponse,
    RecordingsResourceWithStreamingResponse,
    AsyncRecordingsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .livestreams import (
    LivestreamsResource,
    AsyncLivestreamsResource,
    LivestreamsResourceWithRawResponse,
    AsyncLivestreamsResourceWithRawResponse,
    LivestreamsResourceWithStreamingResponse,
    AsyncLivestreamsResourceWithStreamingResponse,
)
from .active_session import (
    ActiveSessionResource,
    AsyncActiveSessionResource,
    ActiveSessionResourceWithRawResponse,
    AsyncActiveSessionResourceWithRawResponse,
    ActiveSessionResourceWithStreamingResponse,
    AsyncActiveSessionResourceWithStreamingResponse,
)

__all__ = ["RealtimeKitResource", "AsyncRealtimeKitResource"]


class RealtimeKitResource(SyncAPIResource):
    @cached_property
    def apps(self) -> AppsResource:
        return AppsResource(self._client)

    @cached_property
    def meetings(self) -> MeetingsResource:
        return MeetingsResource(self._client)

    @cached_property
    def presets(self) -> PresetsResource:
        return PresetsResource(self._client)

    @cached_property
    def sessions(self) -> SessionsResource:
        return SessionsResource(self._client)

    @cached_property
    def recordings(self) -> RecordingsResource:
        return RecordingsResource(self._client)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def active_session(self) -> ActiveSessionResource:
        return ActiveSessionResource(self._client)

    @cached_property
    def livestreams(self) -> LivestreamsResource:
        return LivestreamsResource(self._client)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RealtimeKitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RealtimeKitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RealtimeKitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RealtimeKitResourceWithStreamingResponse(self)


class AsyncRealtimeKitResource(AsyncAPIResource):
    @cached_property
    def apps(self) -> AsyncAppsResource:
        return AsyncAppsResource(self._client)

    @cached_property
    def meetings(self) -> AsyncMeetingsResource:
        return AsyncMeetingsResource(self._client)

    @cached_property
    def presets(self) -> AsyncPresetsResource:
        return AsyncPresetsResource(self._client)

    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        return AsyncSessionsResource(self._client)

    @cached_property
    def recordings(self) -> AsyncRecordingsResource:
        return AsyncRecordingsResource(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def active_session(self) -> AsyncActiveSessionResource:
        return AsyncActiveSessionResource(self._client)

    @cached_property
    def livestreams(self) -> AsyncLivestreamsResource:
        return AsyncLivestreamsResource(self._client)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRealtimeKitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRealtimeKitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRealtimeKitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRealtimeKitResourceWithStreamingResponse(self)


class RealtimeKitResourceWithRawResponse:
    def __init__(self, realtime_kit: RealtimeKitResource) -> None:
        self._realtime_kit = realtime_kit

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self._realtime_kit.apps)

    @cached_property
    def meetings(self) -> MeetingsResourceWithRawResponse:
        return MeetingsResourceWithRawResponse(self._realtime_kit.meetings)

    @cached_property
    def presets(self) -> PresetsResourceWithRawResponse:
        return PresetsResourceWithRawResponse(self._realtime_kit.presets)

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        return SessionsResourceWithRawResponse(self._realtime_kit.sessions)

    @cached_property
    def recordings(self) -> RecordingsResourceWithRawResponse:
        return RecordingsResourceWithRawResponse(self._realtime_kit.recordings)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._realtime_kit.webhooks)

    @cached_property
    def active_session(self) -> ActiveSessionResourceWithRawResponse:
        return ActiveSessionResourceWithRawResponse(self._realtime_kit.active_session)

    @cached_property
    def livestreams(self) -> LivestreamsResourceWithRawResponse:
        return LivestreamsResourceWithRawResponse(self._realtime_kit.livestreams)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._realtime_kit.analytics)


class AsyncRealtimeKitResourceWithRawResponse:
    def __init__(self, realtime_kit: AsyncRealtimeKitResource) -> None:
        self._realtime_kit = realtime_kit

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self._realtime_kit.apps)

    @cached_property
    def meetings(self) -> AsyncMeetingsResourceWithRawResponse:
        return AsyncMeetingsResourceWithRawResponse(self._realtime_kit.meetings)

    @cached_property
    def presets(self) -> AsyncPresetsResourceWithRawResponse:
        return AsyncPresetsResourceWithRawResponse(self._realtime_kit.presets)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        return AsyncSessionsResourceWithRawResponse(self._realtime_kit.sessions)

    @cached_property
    def recordings(self) -> AsyncRecordingsResourceWithRawResponse:
        return AsyncRecordingsResourceWithRawResponse(self._realtime_kit.recordings)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._realtime_kit.webhooks)

    @cached_property
    def active_session(self) -> AsyncActiveSessionResourceWithRawResponse:
        return AsyncActiveSessionResourceWithRawResponse(self._realtime_kit.active_session)

    @cached_property
    def livestreams(self) -> AsyncLivestreamsResourceWithRawResponse:
        return AsyncLivestreamsResourceWithRawResponse(self._realtime_kit.livestreams)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._realtime_kit.analytics)


class RealtimeKitResourceWithStreamingResponse:
    def __init__(self, realtime_kit: RealtimeKitResource) -> None:
        self._realtime_kit = realtime_kit

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self._realtime_kit.apps)

    @cached_property
    def meetings(self) -> MeetingsResourceWithStreamingResponse:
        return MeetingsResourceWithStreamingResponse(self._realtime_kit.meetings)

    @cached_property
    def presets(self) -> PresetsResourceWithStreamingResponse:
        return PresetsResourceWithStreamingResponse(self._realtime_kit.presets)

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        return SessionsResourceWithStreamingResponse(self._realtime_kit.sessions)

    @cached_property
    def recordings(self) -> RecordingsResourceWithStreamingResponse:
        return RecordingsResourceWithStreamingResponse(self._realtime_kit.recordings)

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._realtime_kit.webhooks)

    @cached_property
    def active_session(self) -> ActiveSessionResourceWithStreamingResponse:
        return ActiveSessionResourceWithStreamingResponse(self._realtime_kit.active_session)

    @cached_property
    def livestreams(self) -> LivestreamsResourceWithStreamingResponse:
        return LivestreamsResourceWithStreamingResponse(self._realtime_kit.livestreams)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._realtime_kit.analytics)


class AsyncRealtimeKitResourceWithStreamingResponse:
    def __init__(self, realtime_kit: AsyncRealtimeKitResource) -> None:
        self._realtime_kit = realtime_kit

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self._realtime_kit.apps)

    @cached_property
    def meetings(self) -> AsyncMeetingsResourceWithStreamingResponse:
        return AsyncMeetingsResourceWithStreamingResponse(self._realtime_kit.meetings)

    @cached_property
    def presets(self) -> AsyncPresetsResourceWithStreamingResponse:
        return AsyncPresetsResourceWithStreamingResponse(self._realtime_kit.presets)

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        return AsyncSessionsResourceWithStreamingResponse(self._realtime_kit.sessions)

    @cached_property
    def recordings(self) -> AsyncRecordingsResourceWithStreamingResponse:
        return AsyncRecordingsResourceWithStreamingResponse(self._realtime_kit.recordings)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._realtime_kit.webhooks)

    @cached_property
    def active_session(self) -> AsyncActiveSessionResourceWithStreamingResponse:
        return AsyncActiveSessionResourceWithStreamingResponse(self._realtime_kit.active_session)

    @cached_property
    def livestreams(self) -> AsyncLivestreamsResourceWithStreamingResponse:
        return AsyncLivestreamsResourceWithStreamingResponse(self._realtime_kit.livestreams)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._realtime_kit.analytics)
