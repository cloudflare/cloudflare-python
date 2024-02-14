# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.speed_api import ScheduleCreateResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.speed_api import schedule_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedule:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        schedule = client.speed_api.schedule.create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        schedule = client.speed_api.schedule.create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.speed_api.schedule.with_raw_response.create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.speed_api.schedule.with_streaming_response.create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.schedule.with_raw_response.create(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed_api.schedule.with_raw_response.create(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSchedule:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.speed_api.schedule.create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.speed_api.schedule.create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.schedule.with_raw_response.create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.schedule.with_streaming_response.create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.schedule.with_raw_response.create(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed_api.schedule.with_raw_response.create(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
