# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.quality import (
    IQISummaryResponse,
    IQITimeseriesGroupsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIQI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        iqi = client.radar.quality.iqi.summary(
            metric="BANDWIDTH",
        )
        assert_matches_type(IQISummaryResponse, iqi, path=["response"])

    @parametrize
    def test_method_summary_with_all_params(self, client: Cloudflare) -> None:
        iqi = client.radar.quality.iqi.summary(
            metric="BANDWIDTH",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(IQISummaryResponse, iqi, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:
        response = client.radar.quality.iqi.with_raw_response.summary(
            metric="BANDWIDTH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iqi = response.parse()
        assert_matches_type(IQISummaryResponse, iqi, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.radar.quality.iqi.with_streaming_response.summary(
            metric="BANDWIDTH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iqi = response.parse()
            assert_matches_type(IQISummaryResponse, iqi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries_groups(self, client: Cloudflare) -> None:
        iqi = client.radar.quality.iqi.timeseries_groups(
            metric="BANDWIDTH",
        )
        assert_matches_type(IQITimeseriesGroupsResponse, iqi, path=["response"])

    @parametrize
    def test_method_timeseries_groups_with_all_params(self, client: Cloudflare) -> None:
        iqi = client.radar.quality.iqi.timeseries_groups(
            metric="BANDWIDTH",
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            interpolation=True,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(IQITimeseriesGroupsResponse, iqi, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups(self, client: Cloudflare) -> None:
        response = client.radar.quality.iqi.with_raw_response.timeseries_groups(
            metric="BANDWIDTH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iqi = response.parse()
        assert_matches_type(IQITimeseriesGroupsResponse, iqi, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups(self, client: Cloudflare) -> None:
        with client.radar.quality.iqi.with_streaming_response.timeseries_groups(
            metric="BANDWIDTH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iqi = response.parse()
            assert_matches_type(IQITimeseriesGroupsResponse, iqi, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIQI:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        iqi = await async_client.radar.quality.iqi.summary(
            metric="BANDWIDTH",
        )
        assert_matches_type(IQISummaryResponse, iqi, path=["response"])

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCloudflare) -> None:
        iqi = await async_client.radar.quality.iqi.summary(
            metric="BANDWIDTH",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(IQISummaryResponse, iqi, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.quality.iqi.with_raw_response.summary(
            metric="BANDWIDTH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iqi = await response.parse()
        assert_matches_type(IQISummaryResponse, iqi, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.quality.iqi.with_streaming_response.summary(
            metric="BANDWIDTH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iqi = await response.parse()
            assert_matches_type(IQISummaryResponse, iqi, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        iqi = await async_client.radar.quality.iqi.timeseries_groups(
            metric="BANDWIDTH",
        )
        assert_matches_type(IQITimeseriesGroupsResponse, iqi, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_with_all_params(self, async_client: AsyncCloudflare) -> None:
        iqi = await async_client.radar.quality.iqi.timeseries_groups(
            metric="BANDWIDTH",
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            interpolation=True,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(IQITimeseriesGroupsResponse, iqi, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.quality.iqi.with_raw_response.timeseries_groups(
            metric="BANDWIDTH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        iqi = await response.parse()
        assert_matches_type(IQITimeseriesGroupsResponse, iqi, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.quality.iqi.with_streaming_response.timeseries_groups(
            metric="BANDWIDTH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            iqi = await response.parse()
            assert_matches_type(IQITimeseriesGroupsResponse, iqi, path=["response"])

        assert cast(Any, response.is_closed) is True
