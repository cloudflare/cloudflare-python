# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date, parse_datetime
from cloudflare.types.radar import (
    RankingTopResponse,
    RankingTimeseriesGroupsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRanking:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_timeseries_groups(self, client: Cloudflare) -> None:
        ranking = client.radar.ranking.timeseries_groups()
        assert_matches_type(RankingTimeseriesGroupsResponse, ranking, path=["response"])

    @parametrize
    def test_method_timeseries_groups_with_all_params(self, client: Cloudflare) -> None:
        ranking = client.radar.ranking.timeseries_groups(
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            domain_category=["string"],
            domains=["string"],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
            ranking_type="POPULAR",
        )
        assert_matches_type(RankingTimeseriesGroupsResponse, ranking, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups(self, client: Cloudflare) -> None:
        response = client.radar.ranking.with_raw_response.timeseries_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ranking = response.parse()
        assert_matches_type(RankingTimeseriesGroupsResponse, ranking, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups(self, client: Cloudflare) -> None:
        with client.radar.ranking.with_streaming_response.timeseries_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ranking = response.parse()
            assert_matches_type(RankingTimeseriesGroupsResponse, ranking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_top(self, client: Cloudflare) -> None:
        ranking = client.radar.ranking.top()
        assert_matches_type(RankingTopResponse, ranking, path=["response"])

    @parametrize
    def test_method_top_with_all_params(self, client: Cloudflare) -> None:
        ranking = client.radar.ranking.top(
            date=[parse_date("2019-12-27")],
            domain_category=["string"],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
            ranking_type="POPULAR",
        )
        assert_matches_type(RankingTopResponse, ranking, path=["response"])

    @parametrize
    def test_raw_response_top(self, client: Cloudflare) -> None:
        response = client.radar.ranking.with_raw_response.top()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ranking = response.parse()
        assert_matches_type(RankingTopResponse, ranking, path=["response"])

    @parametrize
    def test_streaming_response_top(self, client: Cloudflare) -> None:
        with client.radar.ranking.with_streaming_response.top() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ranking = response.parse()
            assert_matches_type(RankingTopResponse, ranking, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRanking:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        ranking = await async_client.radar.ranking.timeseries_groups()
        assert_matches_type(RankingTimeseriesGroupsResponse, ranking, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ranking = await async_client.radar.ranking.timeseries_groups(
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            domain_category=["string"],
            domains=["string"],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
            ranking_type="POPULAR",
        )
        assert_matches_type(RankingTimeseriesGroupsResponse, ranking, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ranking.with_raw_response.timeseries_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ranking = await response.parse()
        assert_matches_type(RankingTimeseriesGroupsResponse, ranking, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ranking.with_streaming_response.timeseries_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ranking = await response.parse()
            assert_matches_type(RankingTimeseriesGroupsResponse, ranking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_top(self, async_client: AsyncCloudflare) -> None:
        ranking = await async_client.radar.ranking.top()
        assert_matches_type(RankingTopResponse, ranking, path=["response"])

    @parametrize
    async def test_method_top_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ranking = await async_client.radar.ranking.top(
            date=[parse_date("2019-12-27")],
            domain_category=["string"],
            format="JSON",
            limit=5,
            location=["string"],
            name=["main_series"],
            ranking_type="POPULAR",
        )
        assert_matches_type(RankingTopResponse, ranking, path=["response"])

    @parametrize
    async def test_raw_response_top(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ranking.with_raw_response.top()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ranking = await response.parse()
        assert_matches_type(RankingTopResponse, ranking, path=["response"])

    @parametrize
    async def test_streaming_response_top(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ranking.with_streaming_response.top() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ranking = await response.parse()
            assert_matches_type(RankingTopResponse, ranking, path=["response"])

        assert cast(Any, response.is_closed) is True
