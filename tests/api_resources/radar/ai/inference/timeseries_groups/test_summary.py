# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.ai.inference.timeseries_groups import (
    SummaryTaskResponse,
    SummaryModelResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_model(self, client: Cloudflare) -> None:
        summary = client.radar.ai.inference.timeseries_groups.summary.model()
        assert_matches_type(SummaryModelResponse, summary, path=["response"])

    @parametrize
    def test_method_model_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.ai.inference.timeseries_groups.summary.model(
            agg_interval="15m",
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            name=["main_series"],
        )
        assert_matches_type(SummaryModelResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_model(self, client: Cloudflare) -> None:
        response = client.radar.ai.inference.timeseries_groups.summary.with_raw_response.model()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryModelResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_model(self, client: Cloudflare) -> None:
        with client.radar.ai.inference.timeseries_groups.summary.with_streaming_response.model() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryModelResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_task(self, client: Cloudflare) -> None:
        summary = client.radar.ai.inference.timeseries_groups.summary.task()
        assert_matches_type(SummaryTaskResponse, summary, path=["response"])

    @parametrize
    def test_method_task_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.ai.inference.timeseries_groups.summary.task(
            agg_interval="15m",
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            name=["main_series"],
        )
        assert_matches_type(SummaryTaskResponse, summary, path=["response"])

    @parametrize
    def test_raw_response_task(self, client: Cloudflare) -> None:
        response = client.radar.ai.inference.timeseries_groups.summary.with_raw_response.task()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryTaskResponse, summary, path=["response"])

    @parametrize
    def test_streaming_response_task(self, client: Cloudflare) -> None:
        with client.radar.ai.inference.timeseries_groups.summary.with_streaming_response.task() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryTaskResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_model(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.ai.inference.timeseries_groups.summary.model()
        assert_matches_type(SummaryModelResponse, summary, path=["response"])

    @parametrize
    async def test_method_model_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.ai.inference.timeseries_groups.summary.model(
            agg_interval="15m",
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            name=["main_series"],
        )
        assert_matches_type(SummaryModelResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_model(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.inference.timeseries_groups.summary.with_raw_response.model()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryModelResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_model(self, async_client: AsyncCloudflare) -> None:
        async with (
            async_client.radar.ai.inference.timeseries_groups.summary.with_streaming_response.model()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryModelResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_task(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.ai.inference.timeseries_groups.summary.task()
        assert_matches_type(SummaryTaskResponse, summary, path=["response"])

    @parametrize
    async def test_method_task_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.ai.inference.timeseries_groups.summary.task(
            agg_interval="15m",
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            name=["main_series"],
        )
        assert_matches_type(SummaryTaskResponse, summary, path=["response"])

    @parametrize
    async def test_raw_response_task(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ai.inference.timeseries_groups.summary.with_raw_response.task()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryTaskResponse, summary, path=["response"])

    @parametrize
    async def test_streaming_response_task(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ai.inference.timeseries_groups.summary.with_streaming_response.task() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryTaskResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True
