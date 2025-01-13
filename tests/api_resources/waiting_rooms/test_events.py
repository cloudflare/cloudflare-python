# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.waiting_rooms import (
    Event,
    EventDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.create(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.create(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.update(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.update(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.update(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.update(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.update(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.update(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.update(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[Event], event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[Event], event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Event], event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.list(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.list(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.delete(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(EventDeleteResponse, event, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.delete(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventDeleteResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.delete(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventDeleteResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.delete(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.delete(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.delete(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.edit(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.edit(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.edit(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.edit(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.edit(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.edit(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.edit(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        event = client.waiting_rooms.events.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.with_raw_response.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.with_streaming_response.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.get(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.get(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.waiting_rooms.events.with_raw_response.get(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.create(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.create(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.create(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.update(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.update(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.update(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.update(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.update(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.update(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.update(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Event], event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[Event], event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Event], event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.list(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.list(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.list(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.delete(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(EventDeleteResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.delete(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventDeleteResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.delete(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventDeleteResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.delete(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.delete(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.delete(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.edit(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.edit(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.edit(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.edit(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            event_end_time="2021-09-28T17:00:00.000Z",
            event_start_time="2021-09-28T15:30:00.000Z",
            name="production_webinar_event",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.edit(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.edit(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.edit(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                event_end_time="2021-09-28T17:00:00.000Z",
                event_start_time="2021-09-28T15:30:00.000Z",
                name="production_webinar_event",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        event = await async_client.waiting_rooms.events.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.with_raw_response.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.with_streaming_response.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.get(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.get(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.waiting_rooms.events.with_raw_response.get(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )
