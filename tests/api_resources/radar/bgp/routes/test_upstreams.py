# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.bgp.routes import UpstreamTimeseriesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpstreams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_timeseries(self, client: Cloudflare) -> None:
        upstream = client.radar.bgp.routes.upstreams.timeseries(
            asn=174,
        )
        assert_matches_type(UpstreamTimeseriesResponse, upstream, path=["response"])

    @parametrize
    def test_method_timeseries_with_all_params(self, client: Cloudflare) -> None:
        upstream = client.radar.bgp.routes.upstreams.timeseries(
            asn=174,
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            ip_version="IPv4",
            limit=5,
        )
        assert_matches_type(UpstreamTimeseriesResponse, upstream, path=["response"])

    @parametrize
    def test_raw_response_timeseries(self, client: Cloudflare) -> None:
        response = client.radar.bgp.routes.upstreams.with_raw_response.timeseries(
            asn=174,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upstream = response.parse()
        assert_matches_type(UpstreamTimeseriesResponse, upstream, path=["response"])

    @parametrize
    def test_streaming_response_timeseries(self, client: Cloudflare) -> None:
        with client.radar.bgp.routes.upstreams.with_streaming_response.timeseries(
            asn=174,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upstream = response.parse()
            assert_matches_type(UpstreamTimeseriesResponse, upstream, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUpstreams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_timeseries(self, async_client: AsyncCloudflare) -> None:
        upstream = await async_client.radar.bgp.routes.upstreams.timeseries(
            asn=174,
        )
        assert_matches_type(UpstreamTimeseriesResponse, upstream, path=["response"])

    @parametrize
    async def test_method_timeseries_with_all_params(self, async_client: AsyncCloudflare) -> None:
        upstream = await async_client.radar.bgp.routes.upstreams.timeseries(
            asn=174,
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            ip_version="IPv4",
            limit=5,
        )
        assert_matches_type(UpstreamTimeseriesResponse, upstream, path=["response"])

    @parametrize
    async def test_raw_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.routes.upstreams.with_raw_response.timeseries(
            asn=174,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upstream = await response.parse()
        assert_matches_type(UpstreamTimeseriesResponse, upstream, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.routes.upstreams.with_streaming_response.timeseries(
            asn=174,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upstream = await response.parse()
            assert_matches_type(UpstreamTimeseriesResponse, upstream, path=["response"])

        assert cast(Any, response.is_closed) is True
