# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.traffic_anomalies import LocationGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        location = client.radar.traffic_anomalies.locations.get()
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        location = client.radar.traffic_anomalies.locations.get(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            limit=5,
            status="VERIFIED",
        )
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.traffic_anomalies.locations.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.traffic_anomalies.locations.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationGetResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLocations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.traffic_anomalies.locations.get()
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.radar.traffic_anomalies.locations.get(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_range="7d",
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            limit=5,
            status="VERIFIED",
        )
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.traffic_anomalies.locations.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationGetResponse, location, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.traffic_anomalies.locations.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationGetResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True
