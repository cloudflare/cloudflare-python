# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.waiting_rooms import (
    EventGetResponse,
    EventDeleteResponse,
    EventUpdateResponse,
    EventWaitingRoomListEventsResponse,
    EventWaitingRoomCreateEventResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Event is prequeueing / Queue all enabled {{/waitTimeKnown}}",
            description="Production event - DO NOT MODIFY",
            disable_session_renewal=True,
            new_users_per_minute=200,
            prequeue_start_time="2021-09-28T15:00:00.000Z",
            queueing_method="random",
            session_duration=1,
            shuffle_at_event_start=True,
            suspended=True,
            total_active_users=200,
        )
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventUpdateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.events.with_raw_response.update(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(EventDeleteResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventDeleteResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventDeleteResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.events.with_raw_response.delete(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.get(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(EventGetResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.get(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventGetResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.get(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventGetResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.events.with_raw_response.get(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_waiting_room_create_event(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.waiting_room_create_event(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(EventWaitingRoomCreateEventResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_waiting_room_create_event_with_all_params(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.waiting_room_create_event(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Event is prequeueing / Queue all enabled {{/waitTimeKnown}}",
            description="Production event - DO NOT MODIFY",
            disable_session_renewal=True,
            new_users_per_minute=200,
            prequeue_start_time="2021-09-28T15:00:00.000Z",
            queueing_method="random",
            session_duration=1,
            shuffle_at_event_start=True,
            suspended=True,
            total_active_users=200,
        )
        assert_matches_type(EventWaitingRoomCreateEventResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_waiting_room_create_event(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.waiting_room_create_event(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventWaitingRoomCreateEventResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_waiting_room_create_event(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.waiting_room_create_event(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventWaitingRoomCreateEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_waiting_room_create_event(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.events.with_raw_response.waiting_room_create_event(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_waiting_room_list_events(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.waiting_room_list_events(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EventWaitingRoomListEventsResponse], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_waiting_room_list_events(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.waiting_room_list_events(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Optional[EventWaitingRoomListEventsResponse], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_waiting_room_list_events(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.waiting_room_list_events(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Optional[EventWaitingRoomListEventsResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_waiting_room_list_events(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.events.with_raw_response.waiting_room_list_events(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Event is prequeueing / Queue all enabled {{/waitTimeKnown}}",
            description="Production event - DO NOT MODIFY",
            disable_session_renewal=True,
            new_users_per_minute=200,
            prequeue_start_time="2021-09-28T15:00:00.000Z",
            queueing_method="random",
            session_duration=1,
            shuffle_at_event_start=True,
            suspended=True,
            total_active_users=200,
        )
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventUpdateResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventUpdateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.update(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(EventDeleteResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventDeleteResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventDeleteResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.delete(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.get(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(EventGetResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.get(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventGetResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.get(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventGetResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.get(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_waiting_room_create_event(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.waiting_room_create_event(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(EventWaitingRoomCreateEventResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_waiting_room_create_event_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.waiting_room_create_event(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
            custom_page_html="{{#waitTimeKnown}} {{waitTime}} mins {{/waitTimeKnown}} {{^waitTimeKnown}} Event is prequeueing / Queue all enabled {{/waitTimeKnown}}",
            description="Production event - DO NOT MODIFY",
            disable_session_renewal=True,
            new_users_per_minute=200,
            prequeue_start_time="2021-09-28T15:00:00.000Z",
            queueing_method="random",
            session_duration=1,
            shuffle_at_event_start=True,
            suspended=True,
            total_active_users=200,
        )
        assert_matches_type(EventWaitingRoomCreateEventResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_waiting_room_create_event(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.waiting_room_create_event(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventWaitingRoomCreateEventResponse, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_waiting_room_create_event(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.waiting_room_create_event(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventWaitingRoomCreateEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_waiting_room_create_event(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.waiting_room_create_event(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_waiting_room_list_events(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.waiting_room_list_events(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EventWaitingRoomListEventsResponse], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_waiting_room_list_events(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.waiting_room_list_events(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(Optional[EventWaitingRoomListEventsResponse], event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_waiting_room_list_events(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.waiting_room_list_events(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Optional[EventWaitingRoomListEventsResponse], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_waiting_room_list_events(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.waiting_room_list_events(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
            )
