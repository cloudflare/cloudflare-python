# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.waiting_rooms.events import DetailWaitingRoomPreviewActiveEventDetailsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_waiting_room_preview_active_event_details(self, client: Cloudflare) -> None:
        detail = client.waiting_rooms.events.details.waiting_room_preview_active_event_details(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(DetailWaitingRoomPreviewActiveEventDetailsResponse, detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_waiting_room_preview_active_event_details(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.details.with_raw_response.waiting_room_preview_active_event_details(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailWaitingRoomPreviewActiveEventDetailsResponse, detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_waiting_room_preview_active_event_details(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.details.with_streaming_response.waiting_room_preview_active_event_details(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailWaitingRoomPreviewActiveEventDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_waiting_room_preview_active_event_details(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.events.details.with_raw_response.waiting_room_preview_active_event_details(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_waiting_room_preview_active_event_details(self, async_client: AsyncCloudflare) -> None:
        detail = await async_client.waiting_rooms.events.details.waiting_room_preview_active_event_details(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(DetailWaitingRoomPreviewActiveEventDetailsResponse, detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_waiting_room_preview_active_event_details(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.waiting_rooms.events.details.with_raw_response.waiting_room_preview_active_event_details(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailWaitingRoomPreviewActiveEventDetailsResponse, detail, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_waiting_room_preview_active_event_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.waiting_rooms.events.details.with_streaming_response.waiting_room_preview_active_event_details(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailWaitingRoomPreviewActiveEventDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_waiting_room_preview_active_event_details(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.events.details.with_raw_response.waiting_room_preview_active_event_details(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )
