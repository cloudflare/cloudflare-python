# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.speed import (
    Schedule,
    ScheduleCreateResponse,
    ScheduleDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedule:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        schedule = client.speed.schedule.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        schedule = client.speed.schedule.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.speed.schedule.with_raw_response.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.speed.schedule.with_streaming_response.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.schedule.with_raw_response.create(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.schedule.with_raw_response.create(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        schedule = client.speed.schedule.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ScheduleDeleteResponse], schedule, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        schedule = client.speed.schedule.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[ScheduleDeleteResponse], schedule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.speed.schedule.with_raw_response.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(Optional[ScheduleDeleteResponse], schedule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.speed.schedule.with_streaming_response.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(Optional[ScheduleDeleteResponse], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.schedule.with_raw_response.delete(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.schedule.with_raw_response.delete(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        schedule = client.speed.schedule.get(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Schedule], schedule, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        schedule = client.speed.schedule.get(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[Schedule], schedule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.speed.schedule.with_raw_response.get(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(Optional[Schedule], schedule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.speed.schedule.with_streaming_response.get(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(Optional[Schedule], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.schedule.with_raw_response.get(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.schedule.with_raw_response.get(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSchedule:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.speed.schedule.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.speed.schedule.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.schedule.with_raw_response.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.schedule.with_streaming_response.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(Optional[ScheduleCreateResponse], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.schedule.with_raw_response.create(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.schedule.with_raw_response.create(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.speed.schedule.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ScheduleDeleteResponse], schedule, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.speed.schedule.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[ScheduleDeleteResponse], schedule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.schedule.with_raw_response.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(Optional[ScheduleDeleteResponse], schedule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.schedule.with_streaming_response.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(Optional[ScheduleDeleteResponse], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.schedule.with_raw_response.delete(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.schedule.with_raw_response.delete(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.speed.schedule.get(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Schedule], schedule, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        schedule = await async_client.speed.schedule.get(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[Schedule], schedule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.schedule.with_raw_response.get(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(Optional[Schedule], schedule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.schedule.with_streaming_response.get(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(Optional[Schedule], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.schedule.with_raw_response.get(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.schedule.with_raw_response.get(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
