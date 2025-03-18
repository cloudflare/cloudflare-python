# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Iterable, cast
from typing_extensions import Literal

import httpx

from .page import (
    PageResource,
    AsyncPageResource,
    PageResourceWithRawResponse,
    AsyncPageResourceWithRawResponse,
    PageResourceWithStreamingResponse,
    AsyncPageResourceWithStreamingResponse,
)
from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .statuses import (
    StatusesResource,
    AsyncStatusesResource,
    StatusesResourceWithRawResponse,
    AsyncStatusesResourceWithRawResponse,
    StatusesResourceWithStreamingResponse,
    AsyncStatusesResourceWithStreamingResponse,
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
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .events.events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.waiting_rooms import (
    waiting_room_edit_params,
    waiting_room_list_params,
    waiting_room_create_params,
    waiting_room_update_params,
)
from ...types.waiting_rooms.waiting_room import WaitingRoom
from ...types.waiting_rooms.additional_routes_param import AdditionalRoutesParam
from ...types.waiting_rooms.cookie_attributes_param import CookieAttributesParam
from ...types.waiting_rooms.waiting_room_delete_response import WaitingRoomDeleteResponse

__all__ = ["WaitingRoomsResource", "AsyncWaitingRoomsResource"]


class WaitingRoomsResource(SyncAPIResource):
    @cached_property
    def page(self) -> PageResource:
        return PageResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def statuses(self) -> StatusesResource:
        return StatusesResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WaitingRoomsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return WaitingRoomsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WaitingRoomsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return WaitingRoomsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[AdditionalRoutesParam] | NotGiven = NOT_GIVEN,
        cookie_attributes: CookieAttributesParam | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
            "bg-BG",
            "hr-HR",
            "cs-CZ",
            "da-DK",
            "fi-FI",
            "lt-LT",
            "ms-MY",
            "nb-NO",
            "ro-RO",
            "el-GR",
            "he-IL",
            "hi-IN",
            "hu-HU",
            "sr-BA",
            "sk-SK",
            "sl-SI",
            "sv-SE",
            "tl-PH",
            "th-TH",
            "uk-UA",
            "vi-VN",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        enabled_origin_commands: List[Literal["revoke"]] | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        turnstile_action: Literal["log", "infinite_queue"] | NotGiven = NOT_GIVEN,
        turnstile_mode: Literal["off", "invisible", "visible_non_interactive", "visible_managed"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Creates a new waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          enabled_origin_commands: A list of enabled origin commands.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          turnstile_action: Which action to take when a bot is detected using Turnstile. `log` will have no
              impact on queueing behavior, simply keeping track of how many bots are detected
              in Waiting Room Analytics. `infinite_queue` will send bots to a false queueing
              state, where they will never reach your origin. `infinite_queue` requires
              Advanced Waiting Room.

          turnstile_mode: Which Turnstile widget type to use for detecting bot traffic. See
              [the Turnstile documentation](https://developers.cloudflare.com/turnstile/concepts/widget/#widget-types)
              for the definitions of these widget types. Set to `off` to disable the Turnstile
              integration entirely. Setting this to anything other than `off` or `invisible`
              requires Advanced Waiting Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/waiting_rooms",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "enabled_origin_commands": enabled_origin_commands,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                    "turnstile_action": turnstile_action,
                    "turnstile_mode": turnstile_mode,
                },
                waiting_room_create_params.WaitingRoomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoom]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    def update(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[AdditionalRoutesParam] | NotGiven = NOT_GIVEN,
        cookie_attributes: CookieAttributesParam | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
            "bg-BG",
            "hr-HR",
            "cs-CZ",
            "da-DK",
            "fi-FI",
            "lt-LT",
            "ms-MY",
            "nb-NO",
            "ro-RO",
            "el-GR",
            "he-IL",
            "hi-IN",
            "hu-HU",
            "sr-BA",
            "sk-SK",
            "sl-SI",
            "sv-SE",
            "tl-PH",
            "th-TH",
            "uk-UA",
            "vi-VN",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        enabled_origin_commands: List[Literal["revoke"]] | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        turnstile_action: Literal["log", "infinite_queue"] | NotGiven = NOT_GIVEN,
        turnstile_mode: Literal["off", "invisible", "visible_non_interactive", "visible_managed"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Updates a configured waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          enabled_origin_commands: A list of enabled origin commands.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          turnstile_action: Which action to take when a bot is detected using Turnstile. `log` will have no
              impact on queueing behavior, simply keeping track of how many bots are detected
              in Waiting Room Analytics. `infinite_queue` will send bots to a false queueing
              state, where they will never reach your origin. `infinite_queue` requires
              Advanced Waiting Room.

          turnstile_mode: Which Turnstile widget type to use for detecting bot traffic. See
              [the Turnstile documentation](https://developers.cloudflare.com/turnstile/concepts/widget/#widget-types)
              for the definitions of these widget types. Set to `off` to disable the Turnstile
              integration entirely. Setting this to anything other than `off` or `invisible`
              requires Advanced Waiting Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._put(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "enabled_origin_commands": enabled_origin_commands,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                    "turnstile_action": turnstile_action,
                    "turnstile_mode": turnstile_mode,
                },
                waiting_room_update_params.WaitingRoomUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoom]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[WaitingRoom]:
        """
        Lists waiting rooms for account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          page: Page number of paginated results.

          per_page: Maximum number of results per page. Must be a multiple of 5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/waiting_rooms",
            page=SyncV4PagePaginationArray[WaitingRoom],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    waiting_room_list_params.WaitingRoomListParams,
                ),
            ),
            model=WaitingRoom,
        )

    def delete(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoomDeleteResponse:
        """
        Deletes a waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._delete(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoomDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoomDeleteResponse], ResultWrapper[WaitingRoomDeleteResponse]),
        )

    def edit(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[AdditionalRoutesParam] | NotGiven = NOT_GIVEN,
        cookie_attributes: CookieAttributesParam | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
            "bg-BG",
            "hr-HR",
            "cs-CZ",
            "da-DK",
            "fi-FI",
            "lt-LT",
            "ms-MY",
            "nb-NO",
            "ro-RO",
            "el-GR",
            "he-IL",
            "hi-IN",
            "hu-HU",
            "sr-BA",
            "sk-SK",
            "sl-SI",
            "sv-SE",
            "tl-PH",
            "th-TH",
            "uk-UA",
            "vi-VN",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        enabled_origin_commands: List[Literal["revoke"]] | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        turnstile_action: Literal["log", "infinite_queue"] | NotGiven = NOT_GIVEN,
        turnstile_mode: Literal["off", "invisible", "visible_non_interactive", "visible_managed"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Patches a configured waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          enabled_origin_commands: A list of enabled origin commands.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          turnstile_action: Which action to take when a bot is detected using Turnstile. `log` will have no
              impact on queueing behavior, simply keeping track of how many bots are detected
              in Waiting Room Analytics. `infinite_queue` will send bots to a false queueing
              state, where they will never reach your origin. `infinite_queue` requires
              Advanced Waiting Room.

          turnstile_mode: Which Turnstile widget type to use for detecting bot traffic. See
              [the Turnstile documentation](https://developers.cloudflare.com/turnstile/concepts/widget/#widget-types)
              for the definitions of these widget types. Set to `off` to disable the Turnstile
              integration entirely. Setting this to anything other than `off` or `invisible`
              requires Advanced Waiting Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._patch(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "enabled_origin_commands": enabled_origin_commands,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                    "turnstile_action": turnstile_action,
                    "turnstile_mode": turnstile_mode,
                },
                waiting_room_edit_params.WaitingRoomEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoom]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    def get(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Fetches a single configured waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoom]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )


class AsyncWaitingRoomsResource(AsyncAPIResource):
    @cached_property
    def page(self) -> AsyncPageResource:
        return AsyncPageResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def statuses(self) -> AsyncStatusesResource:
        return AsyncStatusesResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWaitingRoomsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWaitingRoomsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWaitingRoomsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncWaitingRoomsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[AdditionalRoutesParam] | NotGiven = NOT_GIVEN,
        cookie_attributes: CookieAttributesParam | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
            "bg-BG",
            "hr-HR",
            "cs-CZ",
            "da-DK",
            "fi-FI",
            "lt-LT",
            "ms-MY",
            "nb-NO",
            "ro-RO",
            "el-GR",
            "he-IL",
            "hi-IN",
            "hu-HU",
            "sr-BA",
            "sk-SK",
            "sl-SI",
            "sv-SE",
            "tl-PH",
            "th-TH",
            "uk-UA",
            "vi-VN",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        enabled_origin_commands: List[Literal["revoke"]] | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        turnstile_action: Literal["log", "infinite_queue"] | NotGiven = NOT_GIVEN,
        turnstile_mode: Literal["off", "invisible", "visible_non_interactive", "visible_managed"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Creates a new waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          enabled_origin_commands: A list of enabled origin commands.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          turnstile_action: Which action to take when a bot is detected using Turnstile. `log` will have no
              impact on queueing behavior, simply keeping track of how many bots are detected
              in Waiting Room Analytics. `infinite_queue` will send bots to a false queueing
              state, where they will never reach your origin. `infinite_queue` requires
              Advanced Waiting Room.

          turnstile_mode: Which Turnstile widget type to use for detecting bot traffic. See
              [the Turnstile documentation](https://developers.cloudflare.com/turnstile/concepts/widget/#widget-types)
              for the definitions of these widget types. Set to `off` to disable the Turnstile
              integration entirely. Setting this to anything other than `off` or `invisible`
              requires Advanced Waiting Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/waiting_rooms",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "enabled_origin_commands": enabled_origin_commands,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                    "turnstile_action": turnstile_action,
                    "turnstile_mode": turnstile_mode,
                },
                waiting_room_create_params.WaitingRoomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoom]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    async def update(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[AdditionalRoutesParam] | NotGiven = NOT_GIVEN,
        cookie_attributes: CookieAttributesParam | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
            "bg-BG",
            "hr-HR",
            "cs-CZ",
            "da-DK",
            "fi-FI",
            "lt-LT",
            "ms-MY",
            "nb-NO",
            "ro-RO",
            "el-GR",
            "he-IL",
            "hi-IN",
            "hu-HU",
            "sr-BA",
            "sk-SK",
            "sl-SI",
            "sv-SE",
            "tl-PH",
            "th-TH",
            "uk-UA",
            "vi-VN",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        enabled_origin_commands: List[Literal["revoke"]] | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        turnstile_action: Literal["log", "infinite_queue"] | NotGiven = NOT_GIVEN,
        turnstile_mode: Literal["off", "invisible", "visible_non_interactive", "visible_managed"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Updates a configured waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          enabled_origin_commands: A list of enabled origin commands.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          turnstile_action: Which action to take when a bot is detected using Turnstile. `log` will have no
              impact on queueing behavior, simply keeping track of how many bots are detected
              in Waiting Room Analytics. `infinite_queue` will send bots to a false queueing
              state, where they will never reach your origin. `infinite_queue` requires
              Advanced Waiting Room.

          turnstile_mode: Which Turnstile widget type to use for detecting bot traffic. See
              [the Turnstile documentation](https://developers.cloudflare.com/turnstile/concepts/widget/#widget-types)
              for the definitions of these widget types. Set to `off` to disable the Turnstile
              integration entirely. Setting this to anything other than `off` or `invisible`
              requires Advanced Waiting Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._put(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "enabled_origin_commands": enabled_origin_commands,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                    "turnstile_action": turnstile_action,
                    "turnstile_mode": turnstile_mode,
                },
                waiting_room_update_params.WaitingRoomUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoom]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaitingRoom, AsyncV4PagePaginationArray[WaitingRoom]]:
        """
        Lists waiting rooms for account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          page: Page number of paginated results.

          per_page: Maximum number of results per page. Must be a multiple of 5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/waiting_rooms",
            page=AsyncV4PagePaginationArray[WaitingRoom],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    waiting_room_list_params.WaitingRoomListParams,
                ),
            ),
            model=WaitingRoom,
        )

    async def delete(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoomDeleteResponse:
        """
        Deletes a waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoomDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoomDeleteResponse], ResultWrapper[WaitingRoomDeleteResponse]),
        )

    async def edit(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        host: str,
        name: str,
        new_users_per_minute: int,
        total_active_users: int,
        additional_routes: Iterable[AdditionalRoutesParam] | NotGiven = NOT_GIVEN,
        cookie_attributes: CookieAttributesParam | NotGiven = NOT_GIVEN,
        cookie_suffix: str | NotGiven = NOT_GIVEN,
        custom_page_html: str | NotGiven = NOT_GIVEN,
        default_template_language: Literal[
            "en-US",
            "es-ES",
            "de-DE",
            "fr-FR",
            "it-IT",
            "ja-JP",
            "ko-KR",
            "pt-BR",
            "zh-CN",
            "zh-TW",
            "nl-NL",
            "pl-PL",
            "id-ID",
            "tr-TR",
            "ar-EG",
            "ru-RU",
            "fa-IR",
            "bg-BG",
            "hr-HR",
            "cs-CZ",
            "da-DK",
            "fi-FI",
            "lt-LT",
            "ms-MY",
            "nb-NO",
            "ro-RO",
            "el-GR",
            "he-IL",
            "hi-IN",
            "hu-HU",
            "sr-BA",
            "sk-SK",
            "sl-SI",
            "sv-SE",
            "tl-PH",
            "th-TH",
            "uk-UA",
            "vi-VN",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: bool | NotGiven = NOT_GIVEN,
        enabled_origin_commands: List[Literal["revoke"]] | NotGiven = NOT_GIVEN,
        json_response_enabled: bool | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        queue_all: bool | NotGiven = NOT_GIVEN,
        queueing_method: Literal["fifo", "random", "passthrough", "reject"] | NotGiven = NOT_GIVEN,
        queueing_status_code: Literal[200, 202, 429] | NotGiven = NOT_GIVEN,
        session_duration: int | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        turnstile_action: Literal["log", "infinite_queue"] | NotGiven = NOT_GIVEN,
        turnstile_mode: Literal["off", "invisible", "visible_non_interactive", "visible_managed"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Patches a configured waiting room.

        Args:
          zone_id: Identifier

          host: The host name to which the waiting room will be applied (no wildcards). Please
              do not include the scheme (http:// or https://). The host and path combination
              must be unique.

          name: A unique name to identify the waiting room. Only alphanumeric characters,
              hyphens and underscores are allowed.

          new_users_per_minute: Sets the number of new users that will be let into the route every minute. This
              value is used as baseline for the number of users that are let in per minute. So
              it is possible that there is a little more or little less traffic coming to the
              route based on the traffic patterns at that time around the world.

          total_active_users: Sets the total number of active user sessions on the route at a point in time. A
              route is a combination of host and path on which a waiting room is available.
              This value is used as a baseline for the total number of active user sessions on
              the route. It is possible to have a situation where there are more or less
              active users sessions on the route based on the traffic patterns at that time
              around the world.

          additional_routes: Only available for the Waiting Room Advanced subscription. Additional hostname
              and path combinations to which this waiting room will be applied. There is an
              implied wildcard at the end of the path. The hostname and path combination must
              be unique to this and all other waiting rooms.

          cookie_attributes: Configures cookie attributes for the waiting room cookie. This encrypted cookie
              stores a user's status in the waiting room, such as queue position.

          cookie_suffix: Appends a '\\__' + a custom suffix to the end of Cloudflare Waiting Room's cookie
              name(**cf_waitingroom). If `cookie_suffix` is "abcd", the cookie name will be
              `**cf_waitingroom_abcd`. This field is required if using `additional_routes`.

          custom_page_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          default_template_language: The language of the default page template. If no default_template_language is
              provided, then `en-US` (English) will be used.

          description: A note that you can use to add more details about the waiting room.

          disable_session_renewal: Only available for the Waiting Room Advanced subscription. Disables automatic
              renewal of session cookies. If `true`, an accepted user will have
              session_duration minutes to browse the site. After that, they will have to go
              through the waiting room again. If `false`, a user's session cookie will be
              automatically renewed on every request.

          enabled_origin_commands: A list of enabled origin commands.

          json_response_enabled: Only available for the Waiting Room Advanced subscription. If `true`, requests
              to the waiting room with the header `Accept: application/json` will receive a
              JSON response object with information on the user's status in the waiting room
              as opposed to the configured static HTML page. This JSON response object has one
              property `cfWaitingRoom` which is an object containing the following fields:

              1. `inWaitingRoom`: Boolean indicating if the user is in the waiting room
                 (always **true**).
              2. `waitTimeKnown`: Boolean indicating if the current estimated wait times are
                 accurate. If **false**, they are not available.
              3. `waitTime`: Valid only when `waitTimeKnown` is **true**. Integer indicating
                 the current estimated time in minutes the user will wait in the waiting room.
                 When `queueingMethod` is **random**, this is set to `waitTime50Percentile`.
              4. `waitTime25Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 25% of users that gain entry the fastest (25th percentile).
              5. `waitTime50Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 50% of users that gain entry the fastest (50th percentile).
                 In other words, half of the queued users are expected to let into the origin
                 website before `waitTime50Percentile` and half are expected to be let in
                 after it.
              6. `waitTime75Percentile`: Valid only when `queueingMethod` is **random** and
                 `waitTimeKnown` is **true**. Integer indicating the current estimated maximum
                 wait time for the 75% of users that gain entry the fastest (75th percentile).
              7. `waitTimeFormatted`: String displaying the `waitTime` formatted in English
                 for users. If `waitTimeKnown` is **false**, `waitTimeFormatted` will display
                 **unavailable**.
              8. `queueIsFull`: Boolean indicating if the waiting room's queue is currently
                 full and not accepting new users at the moment.
              9. `queueAll`: Boolean indicating if all users will be queued in the waiting
                 room and no one will be let into the origin website.
              10. `lastUpdated`: String displaying the timestamp as an ISO 8601 string of the
                  user's last attempt to leave the waiting room and be let into the origin
                  website. The user is able to make another attempt after
                  `refreshIntervalSeconds` past this time. If the user makes a request too
                  soon, it will be ignored and `lastUpdated` will not change.
              11. `refreshIntervalSeconds`: Integer indicating the number of seconds after
                  `lastUpdated` until the user is able to make another attempt to leave the
                  waiting room and be let into the origin website. When the `queueingMethod`
                  is `reject`, there is no specified refresh time — it will always be
                  **zero**.
              12. `queueingMethod`: The queueing method currently used by the waiting room. It
                  is either **fifo**, **random**, **passthrough**, or **reject**.
              13. `isFIFOQueue`: Boolean indicating if the waiting room uses a FIFO
                  (First-In-First-Out) queue.
              14. `isRandomQueue`: Boolean indicating if the waiting room uses a Random queue
                  where users gain access randomly.
              15. `isPassthroughQueue`: Boolean indicating if the waiting room uses a
                  passthrough queue. Keep in mind that when passthrough is enabled, this JSON
                  response will only exist when `queueAll` is **true** or `isEventPrequeueing`
                  is **true** because in all other cases requests will go directly to the
                  origin.
              16. `isRejectQueue`: Boolean indicating if the waiting room uses a reject queue.
              17. `isEventActive`: Boolean indicating if an event is currently occurring.
                  Events are able to change a waiting room's behavior during a specified
                  period of time. For additional information, look at the event properties
                  `prequeue_start_time`, `event_start_time`, and `event_end_time` in the
                  documentation for creating waiting room events. Events are considered active
                  between these start and end times, as well as during the prequeueing period
                  if it exists.
              18. `isEventPrequeueing`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if an event is currently prequeueing users before it starts.
              19. `timeUntilEventStart`: Valid only when `isEventPrequeueing` is **true**.
                  Integer indicating the number of minutes until the event starts.
              20. `timeUntilEventStartFormatted`: String displaying the `timeUntilEventStart`
                  formatted in English for users. If `isEventPrequeueing` is **false**,
                  `timeUntilEventStartFormatted` will display **unavailable**.
              21. `timeUntilEventEnd`: Valid only when `isEventActive` is **true**. Integer
                  indicating the number of minutes until the event ends.
              22. `timeUntilEventEndFormatted`: String displaying the `timeUntilEventEnd`
                  formatted in English for users. If `isEventActive` is **false**,
                  `timeUntilEventEndFormatted` will display **unavailable**.
              23. `shuffleAtEventStart`: Valid only when `isEventActive` is **true**. Boolean
                  indicating if the users in the prequeue are shuffled randomly when the event
                  starts.

              An example cURL to a waiting room could be:

                  curl -X GET "https://example.com/waitingroom" \\
                  	-H "Accept: application/json"

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **fifo** and no event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 0,
                  		"waitTime50Percentile": 0,
                  		"waitTime75Percentile": 0,
                  		"waitTimeFormatted": "10 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "fifo",
                  		"isFIFOQueue": true,
                  		"isRandomQueue": false,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": false,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 0,
                  		"timeUntilEventEndFormatted": "unavailable",
                  		"shuffleAtEventStart": false
                  	}
                  }

              If `json_response_enabled` is **true** and the request hits the waiting room, an
              example JSON response when `queueingMethod` is **random** and an event is active
              could be:

                  {
                  	"cfWaitingRoom": {
                  		"inWaitingRoom": true,
                  		"waitTimeKnown": true,
                  		"waitTime": 10,
                  		"waitTime25Percentile": 5,
                  		"waitTime50Percentile": 10,
                  		"waitTime75Percentile": 15,
                  		"waitTimeFormatted": "5 minutes to 15 minutes",
                  		"queueIsFull": false,
                  		"queueAll": false,
                  		"lastUpdated": "2020-08-03T23:46:00.000Z",
                  		"refreshIntervalSeconds": 20,
                  		"queueingMethod": "random",
                  		"isFIFOQueue": false,
                  		"isRandomQueue": true,
                  		"isPassthroughQueue": false,
                  		"isRejectQueue": false,
                  		"isEventActive": true,
                  		"isEventPrequeueing": false,
                  		"timeUntilEventStart": 0,
                  		"timeUntilEventStartFormatted": "unavailable",
                  		"timeUntilEventEnd": 15,
                  		"timeUntilEventEndFormatted": "15 minutes",
                  		"shuffleAtEventStart": true
                  	}
                  }.

          path: Sets the path within the host to enable the waiting room on. The waiting room
              will be enabled for all subpaths as well. If there are two waiting rooms on the
              same subpath, the waiting room for the most specific path will be chosen.
              Wildcards and query parameters are not supported.

          queue_all: If queue_all is `true`, all the traffic that is coming to a route will be sent
              to the waiting room. No new traffic can get to the route once this field is set
              and estimated time will become unavailable.

          queueing_method: Sets the queueing method used by the waiting room. Changing this parameter from
              the **default** queueing method is only available for the Waiting Room Advanced
              subscription. Regardless of the queueing method, if `queue_all` is enabled or an
              event is prequeueing, users in the waiting room will not be accepted to the
              origin. These users will always see a waiting room page that refreshes
              automatically. The valid queueing methods are:

              1. `fifo` **(default)**: First-In-First-Out queue where customers gain access in
                 the order they arrived.
              2. `random`: Random queue where customers gain access randomly, regardless of
                 arrival time.
              3. `passthrough`: Users will pass directly through the waiting room and into the
                 origin website. As a result, any configured limits will not be respected
                 while this is enabled. This method can be used as an alternative to disabling
                 a waiting room (with `suspended`) so that analytics are still reported. This
                 can be used if you wish to allow all traffic normally, but want to restrict
                 traffic during a waiting room event, or vice versa.
              4. `reject`: Users will be immediately rejected from the waiting room. As a
                 result, no users will reach the origin website while this is enabled. This
                 can be used if you wish to reject all traffic while performing maintenance,
                 block traffic during a specified period of time (an event), or block traffic
                 while events are not occurring. Consider a waiting room used for vaccine
                 distribution that only allows traffic during sign-up events, and otherwise
                 blocks all traffic. For this case, the waiting room uses `reject`, and its
                 events override this with `fifo`, `random`, or `passthrough`. When this
                 queueing method is enabled and neither `queueAll` is enabled nor an event is
                 prequeueing, the waiting room page **will not refresh automatically**.

          queueing_status_code: HTTP status code returned to a user while in the queue.

          session_duration: Lifetime of a cookie (in minutes) set by Cloudflare for users who get access to
              the route. If a user is not seen by Cloudflare again in that time period, they
              will be treated as a new user that visits the route.

          suspended: Suspends or allows traffic going to the waiting room. If set to `true`, the
              traffic will not go to the waiting room.

          turnstile_action: Which action to take when a bot is detected using Turnstile. `log` will have no
              impact on queueing behavior, simply keeping track of how many bots are detected
              in Waiting Room Analytics. `infinite_queue` will send bots to a false queueing
              state, where they will never reach your origin. `infinite_queue` requires
              Advanced Waiting Room.

          turnstile_mode: Which Turnstile widget type to use for detecting bot traffic. See
              [the Turnstile documentation](https://developers.cloudflare.com/turnstile/concepts/widget/#widget-types)
              for the definitions of these widget types. Set to `off` to disable the Turnstile
              integration entirely. Setting this to anything other than `off` or `invisible`
              requires Advanced Waiting Room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "name": name,
                    "new_users_per_minute": new_users_per_minute,
                    "total_active_users": total_active_users,
                    "additional_routes": additional_routes,
                    "cookie_attributes": cookie_attributes,
                    "cookie_suffix": cookie_suffix,
                    "custom_page_html": custom_page_html,
                    "default_template_language": default_template_language,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "enabled_origin_commands": enabled_origin_commands,
                    "json_response_enabled": json_response_enabled,
                    "path": path,
                    "queue_all": queue_all,
                    "queueing_method": queueing_method,
                    "queueing_status_code": queueing_status_code,
                    "session_duration": session_duration,
                    "suspended": suspended,
                    "turnstile_action": turnstile_action,
                    "turnstile_mode": turnstile_mode,
                },
                waiting_room_edit_params.WaitingRoomEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoom]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )

    async def get(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaitingRoom:
        """
        Fetches a single configured waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return await self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[WaitingRoom]._unwrapper,
            ),
            cast_to=cast(Type[WaitingRoom], ResultWrapper[WaitingRoom]),
        )


class WaitingRoomsResourceWithRawResponse:
    def __init__(self, waiting_rooms: WaitingRoomsResource) -> None:
        self._waiting_rooms = waiting_rooms

        self.create = to_raw_response_wrapper(
            waiting_rooms.create,
        )
        self.update = to_raw_response_wrapper(
            waiting_rooms.update,
        )
        self.list = to_raw_response_wrapper(
            waiting_rooms.list,
        )
        self.delete = to_raw_response_wrapper(
            waiting_rooms.delete,
        )
        self.edit = to_raw_response_wrapper(
            waiting_rooms.edit,
        )
        self.get = to_raw_response_wrapper(
            waiting_rooms.get,
        )

    @cached_property
    def page(self) -> PageResourceWithRawResponse:
        return PageResourceWithRawResponse(self._waiting_rooms.page)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._waiting_rooms.events)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._waiting_rooms.rules)

    @cached_property
    def statuses(self) -> StatusesResourceWithRawResponse:
        return StatusesResourceWithRawResponse(self._waiting_rooms.statuses)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._waiting_rooms.settings)


class AsyncWaitingRoomsResourceWithRawResponse:
    def __init__(self, waiting_rooms: AsyncWaitingRoomsResource) -> None:
        self._waiting_rooms = waiting_rooms

        self.create = async_to_raw_response_wrapper(
            waiting_rooms.create,
        )
        self.update = async_to_raw_response_wrapper(
            waiting_rooms.update,
        )
        self.list = async_to_raw_response_wrapper(
            waiting_rooms.list,
        )
        self.delete = async_to_raw_response_wrapper(
            waiting_rooms.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            waiting_rooms.edit,
        )
        self.get = async_to_raw_response_wrapper(
            waiting_rooms.get,
        )

    @cached_property
    def page(self) -> AsyncPageResourceWithRawResponse:
        return AsyncPageResourceWithRawResponse(self._waiting_rooms.page)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._waiting_rooms.events)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._waiting_rooms.rules)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithRawResponse:
        return AsyncStatusesResourceWithRawResponse(self._waiting_rooms.statuses)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._waiting_rooms.settings)


class WaitingRoomsResourceWithStreamingResponse:
    def __init__(self, waiting_rooms: WaitingRoomsResource) -> None:
        self._waiting_rooms = waiting_rooms

        self.create = to_streamed_response_wrapper(
            waiting_rooms.create,
        )
        self.update = to_streamed_response_wrapper(
            waiting_rooms.update,
        )
        self.list = to_streamed_response_wrapper(
            waiting_rooms.list,
        )
        self.delete = to_streamed_response_wrapper(
            waiting_rooms.delete,
        )
        self.edit = to_streamed_response_wrapper(
            waiting_rooms.edit,
        )
        self.get = to_streamed_response_wrapper(
            waiting_rooms.get,
        )

    @cached_property
    def page(self) -> PageResourceWithStreamingResponse:
        return PageResourceWithStreamingResponse(self._waiting_rooms.page)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._waiting_rooms.events)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._waiting_rooms.rules)

    @cached_property
    def statuses(self) -> StatusesResourceWithStreamingResponse:
        return StatusesResourceWithStreamingResponse(self._waiting_rooms.statuses)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._waiting_rooms.settings)


class AsyncWaitingRoomsResourceWithStreamingResponse:
    def __init__(self, waiting_rooms: AsyncWaitingRoomsResource) -> None:
        self._waiting_rooms = waiting_rooms

        self.create = async_to_streamed_response_wrapper(
            waiting_rooms.create,
        )
        self.update = async_to_streamed_response_wrapper(
            waiting_rooms.update,
        )
        self.list = async_to_streamed_response_wrapper(
            waiting_rooms.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            waiting_rooms.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            waiting_rooms.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            waiting_rooms.get,
        )

    @cached_property
    def page(self) -> AsyncPageResourceWithStreamingResponse:
        return AsyncPageResourceWithStreamingResponse(self._waiting_rooms.page)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._waiting_rooms.events)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._waiting_rooms.rules)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithStreamingResponse:
        return AsyncStatusesResourceWithStreamingResponse(self._waiting_rooms.statuses)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._waiting_rooms.settings)
