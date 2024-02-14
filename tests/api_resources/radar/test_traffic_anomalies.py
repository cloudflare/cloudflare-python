# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar import TrafficAnomalyListResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar import traffic_anomaly_list_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrafficAnomalies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        traffic_anomaly = client.radar.traffic_anomalies.list()
        assert_matches_type(TrafficAnomalyListResponse, traffic_anomaly, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        traffic_anomaly = client.radar.traffic_anomalies.list(
            asn=174,
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            limit=5,
            location="US",
            offset=0,
            status="VERIFIED",
        )
        assert_matches_type(TrafficAnomalyListResponse, traffic_anomaly, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.traffic_anomalies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_anomaly = response.parse()
        assert_matches_type(TrafficAnomalyListResponse, traffic_anomaly, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.traffic_anomalies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_anomaly = response.parse()
            assert_matches_type(TrafficAnomalyListResponse, traffic_anomaly, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrafficAnomalies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        traffic_anomaly = await async_client.radar.traffic_anomalies.list()
        assert_matches_type(TrafficAnomalyListResponse, traffic_anomaly, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        traffic_anomaly = await async_client.radar.traffic_anomalies.list(
            asn=174,
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            limit=5,
            location="US",
            offset=0,
            status="VERIFIED",
        )
        assert_matches_type(TrafficAnomalyListResponse, traffic_anomaly, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.traffic_anomalies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traffic_anomaly = await response.parse()
        assert_matches_type(TrafficAnomalyListResponse, traffic_anomaly, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.traffic_anomalies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traffic_anomaly = await response.parse()
            assert_matches_type(TrafficAnomalyListResponse, traffic_anomaly, path=["response"])

        assert cast(Any, response.is_closed) is True
