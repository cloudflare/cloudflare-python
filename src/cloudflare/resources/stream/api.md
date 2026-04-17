# Stream

Types:

```python
from cloudflare.types.stream import AllowedOrigins, Video
```

Methods:

- <code title="post /accounts/{account_id}/stream">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/stream_create_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/stream">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/stream_list_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video.py">SyncSinglePage[Video]</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">delete</a>(identifier, \*, account_id) -> None</code>
- <code title="post /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">edit</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/stream_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video.py">Optional[Video]</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}">client.stream.<a href="./src/cloudflare/resources/stream/stream.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/video.py">Optional[Video]</a></code>

## AudioTracks

Types:

```python
from cloudflare.types.stream import Audio, AudioTrackDeleteResponse, AudioTrackGetResponse
```

Methods:

- <code title="delete /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">delete</a>(audio_identifier, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/audio_track_delete_response.py">str</a></code>
- <code title="post /accounts/{account_id}/stream/{identifier}/audio/copy">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">copy</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/audio_track_copy_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/audio.py">Optional[Audio]</a></code>
- <code title="patch /accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">edit</a>(audio_identifier, \*, account_id, identifier, \*\*<a href="src/cloudflare/types/stream/audio_track_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/audio.py">Optional[Audio]</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/audio">client.stream.audio_tracks.<a href="./src/cloudflare/resources/stream/audio_tracks.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/audio_track_get_response.py">Optional[AudioTrackGetResponse]</a></code>

## Videos

Types:

```python
from cloudflare.types.stream import VideoStorageUsageResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/storage-usage">client.stream.videos.<a href="./src/cloudflare/resources/stream/videos.py">storage_usage</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/video_storage_usage_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video_storage_usage_response.py">Optional[VideoStorageUsageResponse]</a></code>

## Clip

Types:

```python
from cloudflare.types.stream import Clip
```

Methods:

- <code title="post /accounts/{account_id}/stream/clip">client.stream.clip.<a href="./src/cloudflare/resources/stream/clip.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/clip_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video.py">Optional[Video]</a></code>

## Copy

Methods:

- <code title="post /accounts/{account_id}/stream/copy">client.stream.copy.<a href="./src/cloudflare/resources/stream/copy.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/copy_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/video.py">Optional[Video]</a></code>

## DirectUpload

Types:

```python
from cloudflare.types.stream import DirectUploadCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/direct_upload">client.stream.direct_upload.<a href="./src/cloudflare/resources/stream/direct_upload.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/direct_upload_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/direct_upload_create_response.py">Optional[DirectUploadCreateResponse]</a></code>

## Keys

Types:

```python
from cloudflare.types.stream import Keys, KeyDeleteResponse, KeyGetResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/keys">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/key_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/keys.py">Optional[Keys]</a></code>
- <code title="delete /accounts/{account_id}/stream/keys/{identifier}">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/key_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/keys">client.stream.keys.<a href="./src/cloudflare/resources/stream/keys.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/key_get_response.py">SyncSinglePage[KeyGetResponse]</a></code>

## LiveInputs

Types:

```python
from cloudflare.types.stream import LiveInput, LiveInputListResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/live_inputs">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input.py">Optional[LiveInput]</a></code>
- <code title="put /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">update</a>(live_input_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input.py">Optional[LiveInput]</a></code>
- <code title="get /accounts/{account_id}/stream/live_inputs">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/live_input_list_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_input_list_response.py">Optional[LiveInputListResponse]</a></code>
- <code title="delete /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">delete</a>(live_input_identifier, \*, account_id) -> None</code>
- <code title="get /accounts/{account_id}/stream/live_inputs/{live_input_identifier}">client.stream.live_inputs.<a href="./src/cloudflare/resources/stream/live_inputs/live_inputs.py">get</a>(live_input_identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/live_input.py">Optional[LiveInput]</a></code>

### Outputs

Types:

```python
from cloudflare.types.stream.live_inputs import Output
```

Methods:

- <code title="post /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">create</a>(live_input_identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/live_inputs/output_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_inputs/output.py">Optional[Output]</a></code>
- <code title="put /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">update</a>(output_identifier, \*, account_id, live_input_identifier, \*\*<a href="src/cloudflare/types/stream/live_inputs/output_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/live_inputs/output.py">Optional[Output]</a></code>
- <code title="get /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">list</a>(live_input_identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/live_inputs/output.py">SyncSinglePage[Output]</a></code>
- <code title="delete /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}">client.stream.live_inputs.outputs.<a href="./src/cloudflare/resources/stream/live_inputs/outputs.py">delete</a>(output_identifier, \*, account_id, live_input_identifier) -> None</code>

## Watermarks

Types:

```python
from cloudflare.types.stream import Watermark, WatermarkDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/watermarks">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/watermark_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/watermark.py">Optional[Watermark]</a></code>
- <code title="get /accounts/{account_id}/stream/watermarks">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">list</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/watermark.py">SyncSinglePage[Watermark]</a></code>
- <code title="delete /accounts/{account_id}/stream/watermarks/{identifier}">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/watermark_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/watermarks/{identifier}">client.stream.watermarks.<a href="./src/cloudflare/resources/stream/watermarks.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/watermark.py">Optional[Watermark]</a></code>

## Webhooks

Types:

```python
from cloudflare.types.stream import WebhookUpdateResponse, WebhookDeleteResponse, WebhookGetResponse
```

Methods:

- <code title="put /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">update</a>(\*, account_id, \*\*<a href="src/cloudflare/types/stream/webhook_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/webhook_update_response.py">Optional[WebhookUpdateResponse]</a></code>
- <code title="delete /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">delete</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/webhook_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/webhook">client.stream.webhooks.<a href="./src/cloudflare/resources/stream/webhooks.py">get</a>(\*, account_id) -> <a href="./src/cloudflare/types/stream/webhook_get_response.py">Optional[WebhookGetResponse]</a></code>

## Captions

Types:

```python
from cloudflare.types.stream import Caption
```

Methods:

- <code title="get /accounts/{account_id}/stream/{identifier}/captions">client.stream.captions.<a href="./src/cloudflare/resources/stream/captions/captions.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/caption.py">SyncSinglePage[Caption]</a></code>

### Language

Types:

```python
from cloudflare.types.stream.captions import LanguageDeleteResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/captions/{language}/generate">client.stream.captions.language.<a href="./src/cloudflare/resources/stream/captions/language/language.py">create</a>(language, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/caption.py">Optional[Caption]</a></code>
- <code title="put /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.language.<a href="./src/cloudflare/resources/stream/captions/language/language.py">update</a>(language, \*, account_id, identifier, \*\*<a href="src/cloudflare/types/stream/captions/language_update_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/caption.py">Optional[Caption]</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.language.<a href="./src/cloudflare/resources/stream/captions/language/language.py">delete</a>(language, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/captions/language_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/captions/{language}">client.stream.captions.language.<a href="./src/cloudflare/resources/stream/captions/language/language.py">get</a>(language, \*, account_id, identifier) -> <a href="./src/cloudflare/types/stream/caption.py">Optional[Caption]</a></code>

#### Vtt

Types:

```python
from cloudflare.types.stream.captions.language import VttGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/{identifier}/captions/{language}/vtt">client.stream.captions.language.vtt.<a href="./src/cloudflare/resources/stream/captions/language/vtt.py">get</a>(language, \*, account_id, identifier) -> str</code>

## Downloads

Types:

```python
from cloudflare.types.stream import (
    DownloadCreateResponse,
    DownloadDeleteResponse,
    DownloadGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">create</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_create_response.py">Optional[DownloadCreateResponse]</a></code>
- <code title="delete /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">delete</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_delete_response.py">str</a></code>
- <code title="get /accounts/{account_id}/stream/{identifier}/downloads">client.stream.downloads.<a href="./src/cloudflare/resources/stream/downloads.py">get</a>(identifier, \*, account_id) -> <a href="./src/cloudflare/types/stream/download_get_response.py">Optional[DownloadGetResponse]</a></code>

## Embed

Types:

```python
from cloudflare.types.stream import EmbedGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/stream/{identifier}/embed">client.stream.embed.<a href="./src/cloudflare/resources/stream/embed.py">get</a>(identifier, \*, account_id) -> str</code>

## Token

Types:

```python
from cloudflare.types.stream import TokenCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/stream/{identifier}/token">client.stream.token.<a href="./src/cloudflare/resources/stream/token.py">create</a>(identifier, \*, account_id, \*\*<a href="src/cloudflare/types/stream/token_create_params.py">params</a>) -> <a href="./src/cloudflare/types/stream/token_create_response.py">Optional[TokenCreateResponse]</a></code>
