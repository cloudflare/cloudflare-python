# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar import NetflowSummaryResponse, NetflowTimeseriesResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar import netflow_summary_params
from cloudflare.types.radar import netflow_timeseries_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestNetflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        netflow = client.radar.netflows.summary()
        assert_matches_type(NetflowSummaryResponse, netflow, path=['response'])

    @parametrize
    def test_method_summary_with_all_params(self, client: Cloudflare) -> None:
        netflow = client.radar.netflows.summary(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(NetflowSummaryResponse, netflow, path=['response'])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:

        response = client.radar.netflows.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        netflow = response.parse()
        assert_matches_type(NetflowSummaryResponse, netflow, path=['response'])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.radar.netflows.with_streaming_response.summary() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            netflow = response.parse()
            assert_matches_type(NetflowSummaryResponse, netflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries(self, client: Cloudflare) -> None:
        netflow = client.radar.netflows.timeseries()
        assert_matches_type(NetflowTimeseriesResponse, netflow, path=['response'])

    @parametrize
    def test_method_timeseries_with_all_params(self, client: Cloudflare) -> None:
        netflow = client.radar.netflows.timeseries(
            agg_interval="15m",
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            normalization="PERCENTAGE_CHANGE",
            product=["HTTP", "ALL"],
        )
        assert_matches_type(NetflowTimeseriesResponse, netflow, path=['response'])

    @parametrize
    def test_raw_response_timeseries(self, client: Cloudflare) -> None:

        response = client.radar.netflows.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        netflow = response.parse()
        assert_matches_type(NetflowTimeseriesResponse, netflow, path=['response'])

    @parametrize
    def test_streaming_response_timeseries(self, client: Cloudflare) -> None:
        with client.radar.netflows.with_streaming_response.timeseries() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            netflow = response.parse()
            assert_matches_type(NetflowTimeseriesResponse, netflow, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncNetflows:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        netflow = await async_client.radar.netflows.summary()
        assert_matches_type(NetflowSummaryResponse, netflow, path=['response'])

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCloudflare) -> None:
        netflow = await async_client.radar.netflows.summary(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(NetflowSummaryResponse, netflow, path=['response'])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.netflows.with_raw_response.summary()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        netflow = await response.parse()
        assert_matches_type(NetflowSummaryResponse, netflow, path=['response'])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.netflows.with_streaming_response.summary() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            netflow = await response.parse()
            assert_matches_type(NetflowSummaryResponse, netflow, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries(self, async_client: AsyncCloudflare) -> None:
        netflow = await async_client.radar.netflows.timeseries()
        assert_matches_type(NetflowTimeseriesResponse, netflow, path=['response'])

    @parametrize
    async def test_method_timeseries_with_all_params(self, async_client: AsyncCloudflare) -> None:
        netflow = await async_client.radar.netflows.timeseries(
            agg_interval="15m",
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            normalization="PERCENTAGE_CHANGE",
            product=["HTTP", "ALL"],
        )
        assert_matches_type(NetflowTimeseriesResponse, netflow, path=['response'])

    @parametrize
    async def test_raw_response_timeseries(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.netflows.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        netflow = await response.parse()
        assert_matches_type(NetflowTimeseriesResponse, netflow, path=['response'])

    @parametrize
    async def test_streaming_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.netflows.with_streaming_response.timeseries() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            netflow = await response.parse()
            assert_matches_type(NetflowTimeseriesResponse, netflow, path=['response'])

        assert cast(Any, response.is_closed) is True