# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar import (
    TCPResetsTimeoutSummaryResponse,
    TCPResetsTimeoutTimeseriesGroupsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTCPResetsTimeouts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        tcp_resets_timeout = client.radar.tcp_resets_timeouts.summary()
        assert_matches_type(TCPResetsTimeoutSummaryResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    def test_method_summary_with_all_params(self, client: Cloudflare) -> None:
        tcp_resets_timeout = client.radar.tcp_resets_timeouts.summary(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TCPResetsTimeoutSummaryResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:
        response = client.radar.tcp_resets_timeouts.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tcp_resets_timeout = response.parse()
        assert_matches_type(TCPResetsTimeoutSummaryResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.radar.tcp_resets_timeouts.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tcp_resets_timeout = response.parse()
            assert_matches_type(TCPResetsTimeoutSummaryResponse, tcp_resets_timeout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries_groups(self, client: Cloudflare) -> None:
        tcp_resets_timeout = client.radar.tcp_resets_timeouts.timeseries_groups()
        assert_matches_type(TCPResetsTimeoutTimeseriesGroupsResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    def test_method_timeseries_groups_with_all_params(self, client: Cloudflare) -> None:
        tcp_resets_timeout = client.radar.tcp_resets_timeouts.timeseries_groups(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TCPResetsTimeoutTimeseriesGroupsResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups(self, client: Cloudflare) -> None:
        response = client.radar.tcp_resets_timeouts.with_raw_response.timeseries_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tcp_resets_timeout = response.parse()
        assert_matches_type(TCPResetsTimeoutTimeseriesGroupsResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups(self, client: Cloudflare) -> None:
        with client.radar.tcp_resets_timeouts.with_streaming_response.timeseries_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tcp_resets_timeout = response.parse()
            assert_matches_type(TCPResetsTimeoutTimeseriesGroupsResponse, tcp_resets_timeout, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTCPResetsTimeouts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        tcp_resets_timeout = await async_client.radar.tcp_resets_timeouts.summary()
        assert_matches_type(TCPResetsTimeoutSummaryResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCloudflare) -> None:
        tcp_resets_timeout = await async_client.radar.tcp_resets_timeouts.summary(
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TCPResetsTimeoutSummaryResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.tcp_resets_timeouts.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tcp_resets_timeout = await response.parse()
        assert_matches_type(TCPResetsTimeoutSummaryResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.tcp_resets_timeouts.with_streaming_response.summary() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tcp_resets_timeout = await response.parse()
            assert_matches_type(TCPResetsTimeoutSummaryResponse, tcp_resets_timeout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        tcp_resets_timeout = await async_client.radar.tcp_resets_timeouts.timeseries_groups()
        assert_matches_type(TCPResetsTimeoutTimeseriesGroupsResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_with_all_params(self, async_client: AsyncCloudflare) -> None:
        tcp_resets_timeout = await async_client.radar.tcp_resets_timeouts.timeseries_groups(
            agg_interval="15m",
            asn=["string"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(TCPResetsTimeoutTimeseriesGroupsResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.tcp_resets_timeouts.with_raw_response.timeseries_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tcp_resets_timeout = await response.parse()
        assert_matches_type(TCPResetsTimeoutTimeseriesGroupsResponse, tcp_resets_timeout, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.tcp_resets_timeouts.with_streaming_response.timeseries_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tcp_resets_timeout = await response.parse()
            assert_matches_type(TCPResetsTimeoutTimeseriesGroupsResponse, tcp_resets_timeout, path=["response"])

        assert cast(Any, response.is_closed) is True
