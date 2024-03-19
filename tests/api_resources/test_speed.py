# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    ObservatoryTrend,
    ObservatorySchedule,
    SpeedDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeed:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        speed = client.speed.delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedDeleteResponse], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        speed = client.speed.delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedDeleteResponse], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.speed.with_raw_response.delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = response.parse()
        assert_matches_type(Optional[SpeedDeleteResponse], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.speed.with_streaming_response.delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = response.parse()
            assert_matches_type(Optional[SpeedDeleteResponse], speed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.with_raw_response.delete(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_schedule_get(self, client: Cloudflare) -> None:
        speed = client.speed.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ObservatorySchedule], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_schedule_get_with_all_params(self, client: Cloudflare) -> None:
        speed = client.speed.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[ObservatorySchedule], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_schedule_get(self, client: Cloudflare) -> None:
        response = client.speed.with_raw_response.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = response.parse()
        assert_matches_type(Optional[ObservatorySchedule], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_schedule_get(self, client: Cloudflare) -> None:
        with client.speed.with_streaming_response.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = response.parse()
            assert_matches_type(Optional[ObservatorySchedule], speed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_schedule_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.with_raw_response.schedule_get(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.with_raw_response.schedule_get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_trends_list(self, client: Cloudflare) -> None:
        speed = client.speed.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        )
        assert_matches_type(Optional[ObservatoryTrend], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_trends_list(self, client: Cloudflare) -> None:
        response = client.speed.with_raw_response.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = response.parse()
        assert_matches_type(Optional[ObservatoryTrend], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_trends_list(self, client: Cloudflare) -> None:
        with client.speed.with_streaming_response.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = response.parse()
            assert_matches_type(Optional[ObservatoryTrend], speed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_trends_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.with_raw_response.trends_list(
                "example.com",
                zone_id="",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="us-central1",
                tz="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.with_raw_response.trends_list(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="us-central1",
                tz="string",
            )


class TestAsyncSpeed:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        speed = await async_client.speed.delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedDeleteResponse], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        speed = await async_client.speed.delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedDeleteResponse], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.with_raw_response.delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = await response.parse()
        assert_matches_type(Optional[SpeedDeleteResponse], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.with_streaming_response.delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = await response.parse()
            assert_matches_type(Optional[SpeedDeleteResponse], speed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.with_raw_response.delete(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_schedule_get(self, async_client: AsyncCloudflare) -> None:
        speed = await async_client.speed.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ObservatorySchedule], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_schedule_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        speed = await async_client.speed.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[ObservatorySchedule], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_schedule_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.with_raw_response.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = await response.parse()
        assert_matches_type(Optional[ObservatorySchedule], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_schedule_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.with_streaming_response.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = await response.parse()
            assert_matches_type(Optional[ObservatorySchedule], speed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_schedule_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.with_raw_response.schedule_get(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.with_raw_response.schedule_get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_trends_list(self, async_client: AsyncCloudflare) -> None:
        speed = await async_client.speed.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        )
        assert_matches_type(Optional[ObservatoryTrend], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_trends_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.with_raw_response.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = await response.parse()
        assert_matches_type(Optional[ObservatoryTrend], speed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_trends_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.with_streaming_response.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = await response.parse()
            assert_matches_type(Optional[ObservatoryTrend], speed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_trends_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.with_raw_response.trends_list(
                "example.com",
                zone_id="",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="us-central1",
                tz="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.with_raw_response.trends_list(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="us-central1",
                tz="string",
            )
