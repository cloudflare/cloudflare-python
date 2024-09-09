# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.waiting_rooms import StatusGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        status = client.waiting_rooms.statuses.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.statuses.with_raw_response.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.waiting_rooms.statuses.with_streaming_response.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusGetResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.waiting_rooms.statuses.with_raw_response.get(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.statuses.with_raw_response.get(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncStatuses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        status = await async_client.waiting_rooms.statuses.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.statuses.with_raw_response.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusGetResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.statuses.with_streaming_response.get(
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusGetResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.waiting_rooms.statuses.with_raw_response.get(
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.statuses.with_raw_response.get(
                waiting_room_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
