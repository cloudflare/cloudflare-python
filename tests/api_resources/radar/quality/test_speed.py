# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.quality import (
    SpeedSummaryResponse,
    SpeedHistogramResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeed:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_histogram(self, client: Cloudflare) -> None:
        speed = client.radar.quality.speed.histogram()
        assert_matches_type(SpeedHistogramResponse, speed, path=["response"])

    @parametrize
    def test_method_histogram_with_all_params(self, client: Cloudflare) -> None:
        speed = client.radar.quality.speed.histogram(
            asn=["string"],
            bucket_size=0,
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            metric_group="BANDWIDTH",
            name=["main_series"],
        )
        assert_matches_type(SpeedHistogramResponse, speed, path=["response"])

    @parametrize
    def test_raw_response_histogram(self, client: Cloudflare) -> None:
        response = client.radar.quality.speed.with_raw_response.histogram()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = response.parse()
        assert_matches_type(SpeedHistogramResponse, speed, path=["response"])

    @parametrize
    def test_streaming_response_histogram(self, client: Cloudflare) -> None:
        with client.radar.quality.speed.with_streaming_response.histogram() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = response.parse()
            assert_matches_type(SpeedHistogramResponse, speed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        speed = client.radar.quality.speed.summary()
        assert_matches_type(SpeedSummaryResponse, speed, path=["response"])

    @parametrize
    def test_method_summary_with_all_params(self, client: Cloudflare) -> None:
        speed = client.radar.quality.speed.summary(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(SpeedSummaryResponse, speed, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:
        response = client.radar.quality.speed.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = response.parse()
        assert_matches_type(SpeedSummaryResponse, speed, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.radar.quality.speed.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = response.parse()
            assert_matches_type(SpeedSummaryResponse, speed, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeed:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_histogram(self, async_client: AsyncCloudflare) -> None:
        speed = await async_client.radar.quality.speed.histogram()
        assert_matches_type(SpeedHistogramResponse, speed, path=["response"])

    @parametrize
    async def test_method_histogram_with_all_params(self, async_client: AsyncCloudflare) -> None:
        speed = await async_client.radar.quality.speed.histogram(
            asn=["string"],
            bucket_size=0,
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            metric_group="BANDWIDTH",
            name=["main_series"],
        )
        assert_matches_type(SpeedHistogramResponse, speed, path=["response"])

    @parametrize
    async def test_raw_response_histogram(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.quality.speed.with_raw_response.histogram()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = await response.parse()
        assert_matches_type(SpeedHistogramResponse, speed, path=["response"])

    @parametrize
    async def test_streaming_response_histogram(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.quality.speed.with_streaming_response.histogram() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = await response.parse()
            assert_matches_type(SpeedHistogramResponse, speed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        speed = await async_client.radar.quality.speed.summary()
        assert_matches_type(SpeedSummaryResponse, speed, path=["response"])

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCloudflare) -> None:
        speed = await async_client.radar.quality.speed.summary(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(SpeedSummaryResponse, speed, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.quality.speed.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed = await response.parse()
        assert_matches_type(SpeedSummaryResponse, speed, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.quality.speed.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed = await response.parse()
            assert_matches_type(SpeedSummaryResponse, speed, path=["response"])

        assert cast(Any, response.is_closed) is True
