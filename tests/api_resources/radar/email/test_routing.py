# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.email import (
    RoutingSummaryV2Response,
    RoutingTimeseriesGroupsV2Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRouting:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary_v2(self, client: Cloudflare) -> None:
        routing = client.radar.email.routing.summary_v2(
            dimension="IP_VERSION",
        )
        assert_matches_type(RoutingSummaryV2Response, routing, path=["response"])

    @parametrize
    def test_method_summary_v2_with_all_params(self, client: Cloudflare) -> None:
        routing = client.radar.email.routing.summary_v2(
            dimension="IP_VERSION",
            arc=["PASS"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS"],
            dmarc=["PASS"],
            encrypted=["ENCRYPTED"],
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            name=["main_series"],
            spf=["PASS"],
        )
        assert_matches_type(RoutingSummaryV2Response, routing, path=["response"])

    @parametrize
    def test_raw_response_summary_v2(self, client: Cloudflare) -> None:
        response = client.radar.email.routing.with_raw_response.summary_v2(
            dimension="IP_VERSION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(RoutingSummaryV2Response, routing, path=["response"])

    @parametrize
    def test_streaming_response_summary_v2(self, client: Cloudflare) -> None:
        with client.radar.email.routing.with_streaming_response.summary_v2(
            dimension="IP_VERSION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(RoutingSummaryV2Response, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries_groups_v2(self, client: Cloudflare) -> None:
        routing = client.radar.email.routing.timeseries_groups_v2(
            dimension="IP_VERSION",
        )
        assert_matches_type(RoutingTimeseriesGroupsV2Response, routing, path=["response"])

    @parametrize
    def test_method_timeseries_groups_v2_with_all_params(self, client: Cloudflare) -> None:
        routing = client.radar.email.routing.timeseries_groups_v2(
            dimension="IP_VERSION",
            agg_interval="1h",
            arc=["PASS"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS"],
            dmarc=["PASS"],
            encrypted=["ENCRYPTED"],
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            name=["main_series"],
            spf=["PASS"],
        )
        assert_matches_type(RoutingTimeseriesGroupsV2Response, routing, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups_v2(self, client: Cloudflare) -> None:
        response = client.radar.email.routing.with_raw_response.timeseries_groups_v2(
            dimension="IP_VERSION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = response.parse()
        assert_matches_type(RoutingTimeseriesGroupsV2Response, routing, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups_v2(self, client: Cloudflare) -> None:
        with client.radar.email.routing.with_streaming_response.timeseries_groups_v2(
            dimension="IP_VERSION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = response.parse()
            assert_matches_type(RoutingTimeseriesGroupsV2Response, routing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRouting:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_summary_v2(self, async_client: AsyncCloudflare) -> None:
        routing = await async_client.radar.email.routing.summary_v2(
            dimension="IP_VERSION",
        )
        assert_matches_type(RoutingSummaryV2Response, routing, path=["response"])

    @parametrize
    async def test_method_summary_v2_with_all_params(self, async_client: AsyncCloudflare) -> None:
        routing = await async_client.radar.email.routing.summary_v2(
            dimension="IP_VERSION",
            arc=["PASS"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS"],
            dmarc=["PASS"],
            encrypted=["ENCRYPTED"],
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            name=["main_series"],
            spf=["PASS"],
        )
        assert_matches_type(RoutingSummaryV2Response, routing, path=["response"])

    @parametrize
    async def test_raw_response_summary_v2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.email.routing.with_raw_response.summary_v2(
            dimension="IP_VERSION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(RoutingSummaryV2Response, routing, path=["response"])

    @parametrize
    async def test_streaming_response_summary_v2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.routing.with_streaming_response.summary_v2(
            dimension="IP_VERSION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(RoutingSummaryV2Response, routing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries_groups_v2(self, async_client: AsyncCloudflare) -> None:
        routing = await async_client.radar.email.routing.timeseries_groups_v2(
            dimension="IP_VERSION",
        )
        assert_matches_type(RoutingTimeseriesGroupsV2Response, routing, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_v2_with_all_params(self, async_client: AsyncCloudflare) -> None:
        routing = await async_client.radar.email.routing.timeseries_groups_v2(
            dimension="IP_VERSION",
            agg_interval="1h",
            arc=["PASS"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS"],
            dmarc=["PASS"],
            encrypted=["ENCRYPTED"],
            format="JSON",
            ip_version=["IPv4"],
            limit_per_group=10,
            name=["main_series"],
            spf=["PASS"],
        )
        assert_matches_type(RoutingTimeseriesGroupsV2Response, routing, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups_v2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.email.routing.with_raw_response.timeseries_groups_v2(
            dimension="IP_VERSION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing = await response.parse()
        assert_matches_type(RoutingTimeseriesGroupsV2Response, routing, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups_v2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.routing.with_streaming_response.timeseries_groups_v2(
            dimension="IP_VERSION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing = await response.parse()
            assert_matches_type(RoutingTimeseriesGroupsV2Response, routing, path=["response"])

        assert cast(Any, response.is_closed) is True
