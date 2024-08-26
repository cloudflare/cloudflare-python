# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.waiting_rooms.events import DetailGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        detail = client.waiting_rooms.events.details.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.events.details.with_raw_response.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.waiting_rooms.events.details.with_streaming_response.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailGetResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.events.details.with_raw_response.get(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.events.details.with_raw_response.get(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.waiting_rooms.events.details.with_raw_response.get(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        detail = await async_client.waiting_rooms.events.details.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.events.details.with_raw_response.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailGetResponse, detail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.events.details.with_streaming_response.get(
            event_id="25756b2dfe6e378a06b033b670413757",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailGetResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.events.details.with_raw_response.get(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.events.details.with_raw_response.get(
                event_id="25756b2dfe6e378a06b033b670413757",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.waiting_rooms.events.details.with_raw_response.get(
                event_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )
