# WaitingRooms

Types:

```python
from cloudflare.types.waiting_rooms import (
    AdditionalRoutes,
    CookieAttributes,
    Query,
    WaitingRoom,
    WaitingRoomDeleteResponse,
)
```

Methods:

- <code title="post /zones/{zone_id}/waiting_rooms">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">create</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/waiting_room_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">WaitingRoom</a></code>
- <code title="put /zones/{zone_id}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">update</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/waiting_room_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">WaitingRoom</a></code>
- <code title="get /{accounts_or_zones}/{account_or_zone_id}/waiting_rooms">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">list</a>(\*, account_id, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/waiting_room_list_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">SyncV4PagePaginationArray[WaitingRoom]</a></code>
- <code title="delete /zones/{zone_id}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">delete</a>(waiting_room_id, \*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room_delete_response.py">WaitingRoomDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">edit</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/waiting_room_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">WaitingRoom</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}">client.waiting_rooms.<a href="./src/cloudflare/resources/waiting_rooms/waiting_rooms.py">get</a>(waiting_room_id, \*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room.py">WaitingRoom</a></code>

## Page

Types:

```python
from cloudflare.types.waiting_rooms import PagePreviewResponse
```

Methods:

- <code title="post /zones/{zone_id}/waiting_rooms/preview">client.waiting_rooms.page.<a href="./src/cloudflare/resources/waiting_rooms/page.py">preview</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/page_preview_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/page_preview_response.py">PagePreviewResponse</a></code>

## Events

Types:

```python
from cloudflare.types.waiting_rooms import Event, EventDeleteResponse
```

Methods:

- <code title="post /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">create</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">Event</a></code>
- <code title="put /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">update</a>(event_id, \*, zone_id, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">Event</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">list</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_list_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">SyncV4PagePaginationArray[Event]</a></code>
- <code title="delete /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">delete</a>(event_id, \*, zone_id, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/event_delete_response.py">EventDeleteResponse</a></code>
- <code title="patch /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">edit</a>(event_id, \*, zone_id, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/event_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">Event</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}">client.waiting_rooms.events.<a href="./src/cloudflare/resources/waiting_rooms/events/events.py">get</a>(event_id, \*, zone_id, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/event.py">Event</a></code>

### Details

Types:

```python
from cloudflare.types.waiting_rooms.events import EventQuery, DetailGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}/details">client.waiting_rooms.events.details.<a href="./src/cloudflare/resources/waiting_rooms/events/details.py">get</a>(event_id, \*, zone_id, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/events/detail_get_response.py">DetailGetResponse</a></code>

## Rules

Types:

```python
from cloudflare.types.waiting_rooms import WaitingRoomRule
```

Methods:

- <code title="post /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">create</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_create_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room_rule.py">SyncSinglePage[WaitingRoomRule]</a></code>
- <code title="put /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">update</a>(waiting_room_id, \*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room_rule.py">SyncSinglePage[WaitingRoomRule]</a></code>
- <code title="delete /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">delete</a>(rule_id, \*, zone_id, waiting_room_id) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room_rule.py">SyncSinglePage[WaitingRoomRule]</a></code>
- <code title="patch /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">edit</a>(rule_id, \*, zone_id, waiting_room_id, \*\*<a href="src/cloudflare/types/waiting_rooms/rule_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room_rule.py">SyncSinglePage[WaitingRoomRule]</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules">client.waiting_rooms.rules.<a href="./src/cloudflare/resources/waiting_rooms/rules.py">get</a>(waiting_room_id, \*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/waiting_room_rule.py">SyncSinglePage[WaitingRoomRule]</a></code>

## Statuses

Types:

```python
from cloudflare.types.waiting_rooms import StatusGetResponse
```

Methods:

- <code title="get /zones/{zone_id}/waiting_rooms/{waiting_room_id}/status">client.waiting_rooms.statuses.<a href="./src/cloudflare/resources/waiting_rooms/statuses.py">get</a>(waiting_room_id, \*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/status_get_response.py">StatusGetResponse</a></code>

## Settings

Types:

```python
from cloudflare.types.waiting_rooms import (
    Setting,
    SettingUpdateResponse,
    SettingEditResponse,
    SettingGetResponse,
)
```

Methods:

- <code title="put /zones/{zone_id}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/setting_update_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/setting_update_response.py">SettingUpdateResponse</a></code>
- <code title="patch /zones/{zone_id}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">edit</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/waiting_rooms/setting_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/waiting_rooms/setting_edit_response.py">SettingEditResponse</a></code>
- <code title="get /zones/{zone_id}/waiting_rooms/settings">client.waiting_rooms.settings.<a href="./src/cloudflare/resources/waiting_rooms/settings.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/waiting_rooms/setting_get_response.py">SettingGetResponse</a></code>
