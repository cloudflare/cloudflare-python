# RealtimeKit

## Apps

Types:

```python
from cloudflare.types.realtime_kit import AppGetResponse, AppPostResponse
```

Methods:

- <code title="get /accounts/{account_id}/realtime/kit/apps">client.realtime_kit.apps.<a href="./src/cloudflare/resources/realtime_kit/apps.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/realtime_kit/app_get_response.py">AppGetResponse</a></code>
- <code title="post /accounts/{account_id}/realtime/kit/apps">client.realtime_kit.apps.<a href="./src/cloudflare/resources/realtime_kit/apps.py">post</a>(\*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/app_post_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/app_post_response.py">AppPostResponse</a></code>

## Meetings

Types:

```python
from cloudflare.types.realtime_kit import (
    MeetingCreateResponse,
    MeetingAddParticipantResponse,
    MeetingDeleteMeetingParticipantResponse,
    MeetingEditParticipantResponse,
    MeetingGetResponse,
    MeetingGetMeetingByIDResponse,
    MeetingGetMeetingParticipantResponse,
    MeetingGetMeetingParticipantsResponse,
    MeetingRefreshParticipantTokenResponse,
    MeetingReplaceMeetingByIDResponse,
    MeetingUpdateMeetingByIDResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/meetings">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">create</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/meeting_create_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/meeting_create_response.py">MeetingCreateResponse</a></code>
- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">add_participant</a>(meeting_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/meeting_add_participant_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/meeting_add_participant_response.py">MeetingAddParticipantResponse</a></code>
- <code title="delete /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">delete_meeting_participant</a>(participant_id, \*, account_id, app_id, meeting_id) -> <a href="./src/cloudflare/types/realtime_kit/meeting_delete_meeting_participant_response.py">MeetingDeleteMeetingParticipantResponse</a></code>
- <code title="patch /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">edit_participant</a>(participant_id, \*, account_id, app_id, meeting_id, \*\*<a href="src/cloudflare/types/realtime_kit/meeting_edit_participant_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/meeting_edit_participant_response.py">MeetingEditParticipantResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/meetings">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">get</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/meeting_get_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/meeting_get_response.py">MeetingGetResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">get_meeting_by_id</a>(meeting_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/meeting_get_meeting_by_id_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/meeting_get_meeting_by_id_response.py">MeetingGetMeetingByIDResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">get_meeting_participant</a>(participant_id, \*, account_id, app_id, meeting_id) -> <a href="./src/cloudflare/types/realtime_kit/meeting_get_meeting_participant_response.py">MeetingGetMeetingParticipantResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">get_meeting_participants</a>(meeting_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/meeting_get_meeting_participants_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/meeting_get_meeting_participants_response.py">MeetingGetMeetingParticipantsResponse</a></code>
- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}/token">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">refresh_participant_token</a>(participant_id, \*, account_id, app_id, meeting_id) -> <a href="./src/cloudflare/types/realtime_kit/meeting_refresh_participant_token_response.py">MeetingRefreshParticipantTokenResponse</a></code>
- <code title="put /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">replace_meeting_by_id</a>(meeting_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/meeting_replace_meeting_by_id_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/meeting_replace_meeting_by_id_response.py">MeetingReplaceMeetingByIDResponse</a></code>
- <code title="patch /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}">client.realtime_kit.meetings.<a href="./src/cloudflare/resources/realtime_kit/meetings.py">update_meeting_by_id</a>(meeting_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/meeting_update_meeting_by_id_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/meeting_update_meeting_by_id_response.py">MeetingUpdateMeetingByIDResponse</a></code>

## Presets

Types:

```python
from cloudflare.types.realtime_kit import (
    PresetCreateResponse,
    PresetUpdateResponse,
    PresetDeleteResponse,
    PresetGetResponse,
    PresetGetPresetByIDResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/presets">client.realtime_kit.presets.<a href="./src/cloudflare/resources/realtime_kit/presets.py">create</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/preset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/preset_create_response.py">PresetCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}">client.realtime_kit.presets.<a href="./src/cloudflare/resources/realtime_kit/presets.py">update</a>(preset_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/preset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/preset_update_response.py">PresetUpdateResponse</a></code>
- <code title="delete /accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}">client.realtime_kit.presets.<a href="./src/cloudflare/resources/realtime_kit/presets.py">delete</a>(preset_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/preset_delete_response.py">PresetDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/presets">client.realtime_kit.presets.<a href="./src/cloudflare/resources/realtime_kit/presets.py">get</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/preset_get_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/preset_get_response.py">PresetGetResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}">client.realtime_kit.presets.<a href="./src/cloudflare/resources/realtime_kit/presets.py">get_preset_by_id</a>(preset_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/preset_get_preset_by_id_response.py">PresetGetPresetByIDResponse</a></code>

## Sessions

Types:

```python
from cloudflare.types.realtime_kit import (
    SessionGetParticipantDataFromPeerIDResponse,
    SessionGetSessionChatResponse,
    SessionGetSessionDetailsResponse,
    SessionGetSessionParticipantDetailsResponse,
    SessionGetSessionParticipantsResponse,
    SessionGetSessionSummaryResponse,
    SessionGetSessionTranscriptsResponse,
    SessionGetSessionsResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary">client.realtime_kit.sessions.<a href="./src/cloudflare/resources/realtime_kit/sessions.py">generate_summary_of_transcripts</a>(session_id, \*, account_id, app_id) -> None</code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/sessions/peer-report/{peer_id}">client.realtime_kit.sessions.<a href="./src/cloudflare/resources/realtime_kit/sessions.py">get_participant_data_from_peer_id</a>(peer_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/session_get_participant_data_from_peer_id_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/session_get_participant_data_from_peer_id_response.py">SessionGetParticipantDataFromPeerIDResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/chat">client.realtime_kit.sessions.<a href="./src/cloudflare/resources/realtime_kit/sessions.py">get_session_chat</a>(session_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/session_get_session_chat_response.py">SessionGetSessionChatResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}">client.realtime_kit.sessions.<a href="./src/cloudflare/resources/realtime_kit/sessions.py">get_session_details</a>(session_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/session_get_session_details_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/session_get_session_details_response.py">SessionGetSessionDetailsResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants/{participant_id}">client.realtime_kit.sessions.<a href="./src/cloudflare/resources/realtime_kit/sessions.py">get_session_participant_details</a>(participant_id, \*, account_id, app_id, session_id, \*\*<a href="src/cloudflare/types/realtime_kit/session_get_session_participant_details_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/session_get_session_participant_details_response.py">SessionGetSessionParticipantDetailsResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants">client.realtime_kit.sessions.<a href="./src/cloudflare/resources/realtime_kit/sessions.py">get_session_participants</a>(session_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/session_get_session_participants_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/session_get_session_participants_response.py">SessionGetSessionParticipantsResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary">client.realtime_kit.sessions.<a href="./src/cloudflare/resources/realtime_kit/sessions.py">get_session_summary</a>(session_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/session_get_session_summary_response.py">SessionGetSessionSummaryResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/transcript">client.realtime_kit.sessions.<a href="./src/cloudflare/resources/realtime_kit/sessions.py">get_session_transcripts</a>(session_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/session_get_session_transcripts_response.py">SessionGetSessionTranscriptsResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/sessions">client.realtime_kit.sessions.<a href="./src/cloudflare/resources/realtime_kit/sessions.py">get_sessions</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/session_get_sessions_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/session_get_sessions_response.py">SessionGetSessionsResponse</a></code>

## Recordings

Types:

```python
from cloudflare.types.realtime_kit import (
    RecordingGetActiveRecordingsResponse,
    RecordingGetOneRecordingResponse,
    RecordingGetRecordingsResponse,
    RecordingPauseResumeStopRecordingResponse,
    RecordingStartRecordingsResponse,
)
```

Methods:

- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/recordings/active-recording/{meeting_id}">client.realtime_kit.recordings.<a href="./src/cloudflare/resources/realtime_kit/recordings.py">get_active_recordings</a>(meeting_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/recording_get_active_recordings_response.py">RecordingGetActiveRecordingsResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}">client.realtime_kit.recordings.<a href="./src/cloudflare/resources/realtime_kit/recordings.py">get_one_recording</a>(recording_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/recording_get_one_recording_response.py">RecordingGetOneRecordingResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/recordings">client.realtime_kit.recordings.<a href="./src/cloudflare/resources/realtime_kit/recordings.py">get_recordings</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/recording_get_recordings_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/recording_get_recordings_response.py">RecordingGetRecordingsResponse</a></code>
- <code title="put /accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}">client.realtime_kit.recordings.<a href="./src/cloudflare/resources/realtime_kit/recordings.py">pause_resume_stop_recording</a>(recording_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/recording_pause_resume_stop_recording_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/recording_pause_resume_stop_recording_response.py">RecordingPauseResumeStopRecordingResponse</a></code>
- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/recordings">client.realtime_kit.recordings.<a href="./src/cloudflare/resources/realtime_kit/recordings.py">start_recordings</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/recording_start_recordings_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/recording_start_recordings_response.py">RecordingStartRecordingsResponse</a></code>
- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/recordings/track">client.realtime_kit.recordings.<a href="./src/cloudflare/resources/realtime_kit/recordings.py">start_track_recording</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/recording_start_track_recording_params.py">params</a>) -> None</code>

## Webhooks

Types:

```python
from cloudflare.types.realtime_kit import (
    WebhookCreateWebhookResponse,
    WebhookDeleteWebhookResponse,
    WebhookEditWebhookResponse,
    WebhookGetWebhookByIDResponse,
    WebhookGetWebhooksResponse,
    WebhookReplaceWebhookResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/webhooks">client.realtime_kit.webhooks.<a href="./src/cloudflare/resources/realtime_kit/webhooks.py">create_webhook</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/webhook_create_webhook_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/webhook_create_webhook_response.py">WebhookCreateWebhookResponse</a></code>
- <code title="delete /accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}">client.realtime_kit.webhooks.<a href="./src/cloudflare/resources/realtime_kit/webhooks.py">delete_webhook</a>(webhook_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/webhook_delete_webhook_response.py">WebhookDeleteWebhookResponse</a></code>
- <code title="patch /accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}">client.realtime_kit.webhooks.<a href="./src/cloudflare/resources/realtime_kit/webhooks.py">edit_webhook</a>(webhook_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/webhook_edit_webhook_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/webhook_edit_webhook_response.py">WebhookEditWebhookResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}">client.realtime_kit.webhooks.<a href="./src/cloudflare/resources/realtime_kit/webhooks.py">get_webhook_by_id</a>(webhook_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/webhook_get_webhook_by_id_response.py">WebhookGetWebhookByIDResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/webhooks">client.realtime_kit.webhooks.<a href="./src/cloudflare/resources/realtime_kit/webhooks.py">get_webhooks</a>(app_id, \*, account_id) -> <a href="./src/cloudflare/types/realtime_kit/webhook_get_webhooks_response.py">WebhookGetWebhooksResponse</a></code>
- <code title="put /accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}">client.realtime_kit.webhooks.<a href="./src/cloudflare/resources/realtime_kit/webhooks.py">replace_webhook</a>(webhook_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/webhook_replace_webhook_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/webhook_replace_webhook_response.py">WebhookReplaceWebhookResponse</a></code>

## ActiveSession

Types:

```python
from cloudflare.types.realtime_kit import (
    ActiveSessionCreatePollResponse,
    ActiveSessionGetActiveSessionResponse,
    ActiveSessionKickAllParticipantsResponse,
    ActiveSessionKickParticipantsResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/poll">client.realtime_kit.active_session.<a href="./src/cloudflare/resources/realtime_kit/active_session.py">create_poll</a>(meeting_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/active_session_create_poll_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/active_session_create_poll_response.py">ActiveSessionCreatePollResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session">client.realtime_kit.active_session.<a href="./src/cloudflare/resources/realtime_kit/active_session.py">get_active_session</a>(meeting_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/active_session_get_active_session_response.py">ActiveSessionGetActiveSessionResponse</a></code>
- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick-all">client.realtime_kit.active_session.<a href="./src/cloudflare/resources/realtime_kit/active_session.py">kick_all_participants</a>(meeting_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/active_session_kick_all_participants_response.py">ActiveSessionKickAllParticipantsResponse</a></code>
- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick">client.realtime_kit.active_session.<a href="./src/cloudflare/resources/realtime_kit/active_session.py">kick_participants</a>(meeting_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/active_session_kick_participants_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/active_session_kick_participants_response.py">ActiveSessionKickParticipantsResponse</a></code>

## Livestreams

Types:

```python
from cloudflare.types.realtime_kit import (
    LivestreamCreateIndependentLivestreamResponse,
    LivestreamGetActiveLivestreamsForLivestreamIDResponse,
    LivestreamGetAllLivestreamsResponse,
    LivestreamGetLivestreamAnalyticsCompleteResponse,
    LivestreamGetLivestreamSessionDetailsForSessionIDResponse,
    LivestreamGetLivestreamSessionForLivestreamIDResponse,
    LivestreamGetMeetingActiveLivestreamsResponse,
    LivestreamGetOrgAnalyticsResponse,
    LivestreamStartLivestreamingAMeetingResponse,
    LivestreamStopLivestreamingAMeetingResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/livestreams">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">create_independent_livestream</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/livestream_create_independent_livestream_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/livestream_create_independent_livestream_response.py">LivestreamCreateIndependentLivestreamResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}/active-livestream-session">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">get_active_livestreams_for_livestream_id</a>(livestream_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/livestream_get_active_livestreams_for_livestream_id_response.py">LivestreamGetActiveLivestreamsForLivestreamIDResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/livestreams">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">get_all_livestreams</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/livestream_get_all_livestreams_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/livestream_get_all_livestreams_response.py">LivestreamGetAllLivestreamsResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/analytics/livestreams/overall">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">get_livestream_analytics_complete</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/livestream_get_livestream_analytics_complete_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/livestream_get_livestream_analytics_complete_response.py">LivestreamGetLivestreamAnalyticsCompleteResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/livestreams/sessions/{livestream-session-id}">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">get_livestream_session_details_for_session_id</a>(livestream_session_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/livestream_get_livestream_session_details_for_session_id_response.py">LivestreamGetLivestreamSessionDetailsForSessionIDResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">get_livestream_session_for_livestream_id</a>(livestream_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/livestream_get_livestream_session_for_livestream_id_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/livestream_get_livestream_session_for_livestream_id_response.py">LivestreamGetLivestreamSessionForLivestreamIDResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">get_meeting_active_livestreams</a>(meeting_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/livestream_get_meeting_active_livestreams_response.py">LivestreamGetMeetingActiveLivestreamsResponse</a></code>
- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">get_org_analytics</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/livestream_get_org_analytics_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/livestream_get_org_analytics_response.py">LivestreamGetOrgAnalyticsResponse</a></code>
- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/livestreams">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">start_livestreaming_a_meeting</a>(meeting_id, \*, account_id, app_id, \*\*<a href="src/cloudflare/types/realtime_kit/livestream_start_livestreaming_a_meeting_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/livestream_start_livestreaming_a_meeting_response.py">LivestreamStartLivestreamingAMeetingResponse</a></code>
- <code title="post /accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream/stop">client.realtime_kit.livestreams.<a href="./src/cloudflare/resources/realtime_kit/livestreams.py">stop_livestreaming_a_meeting</a>(meeting_id, \*, account_id, app_id) -> <a href="./src/cloudflare/types/realtime_kit/livestream_stop_livestreaming_a_meeting_response.py">LivestreamStopLivestreamingAMeetingResponse</a></code>

## Analytics

Types:

```python
from cloudflare.types.realtime_kit import AnalyticsGetOrgAnalyticsResponse
```

Methods:

- <code title="get /accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise">client.realtime_kit.analytics.<a href="./src/cloudflare/resources/realtime_kit/analytics.py">get_org_analytics</a>(app_id, \*, account_id, \*\*<a href="src/cloudflare/types/realtime_kit/analytics_get_org_analytics_params.py">params</a>) -> <a href="./src/cloudflare/types/realtime_kit/analytics_get_org_analytics_response.py">AnalyticsGetOrgAnalyticsResponse</a></code>
