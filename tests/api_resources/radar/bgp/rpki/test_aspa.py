# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.bgp.rpki import (
    ASPAChangesResponse,
    ASPASnapshotResponse,
    ASPATimeseriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestASPA:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_changes(self, client: Cloudflare) -> None:
        aspa = client.radar.bgp.rpki.aspa.changes()
        assert_matches_type(ASPAChangesResponse, aspa, path=["response"])

    @parametrize
    def test_method_changes_with_all_params(self, client: Cloudflare) -> None:
        aspa = client.radar.bgp.rpki.aspa.changes(
            asn=13335,
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            include_asn_info=True,
        )
        assert_matches_type(ASPAChangesResponse, aspa, path=["response"])

    @parametrize
    def test_raw_response_changes(self, client: Cloudflare) -> None:
        response = client.radar.bgp.rpki.aspa.with_raw_response.changes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aspa = response.parse()
        assert_matches_type(ASPAChangesResponse, aspa, path=["response"])

    @parametrize
    def test_streaming_response_changes(self, client: Cloudflare) -> None:
        with client.radar.bgp.rpki.aspa.with_streaming_response.changes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aspa = response.parse()
            assert_matches_type(ASPAChangesResponse, aspa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_snapshot(self, client: Cloudflare) -> None:
        aspa = client.radar.bgp.rpki.aspa.snapshot()
        assert_matches_type(ASPASnapshotResponse, aspa, path=["response"])

    @parametrize
    def test_method_snapshot_with_all_params(self, client: Cloudflare) -> None:
        aspa = client.radar.bgp.rpki.aspa.snapshot(
            customer_asn=13335,
            date=parse_datetime("2024-09-19T00:00:00Z"),
            format="JSON",
            include_asn_info=True,
            provider_asn=174,
        )
        assert_matches_type(ASPASnapshotResponse, aspa, path=["response"])

    @parametrize
    def test_raw_response_snapshot(self, client: Cloudflare) -> None:
        response = client.radar.bgp.rpki.aspa.with_raw_response.snapshot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aspa = response.parse()
        assert_matches_type(ASPASnapshotResponse, aspa, path=["response"])

    @parametrize
    def test_streaming_response_snapshot(self, client: Cloudflare) -> None:
        with client.radar.bgp.rpki.aspa.with_streaming_response.snapshot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aspa = response.parse()
            assert_matches_type(ASPASnapshotResponse, aspa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries(self, client: Cloudflare) -> None:
        aspa = client.radar.bgp.rpki.aspa.timeseries()
        assert_matches_type(ASPATimeseriesResponse, aspa, path=["response"])

    @parametrize
    def test_method_timeseries_with_all_params(self, client: Cloudflare) -> None:
        aspa = client.radar.bgp.rpki.aspa.timeseries(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            location=["string"],
            name=["main_series"],
            rir=["RIPE_NCC"],
        )
        assert_matches_type(ASPATimeseriesResponse, aspa, path=["response"])

    @parametrize
    def test_raw_response_timeseries(self, client: Cloudflare) -> None:
        response = client.radar.bgp.rpki.aspa.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aspa = response.parse()
        assert_matches_type(ASPATimeseriesResponse, aspa, path=["response"])

    @parametrize
    def test_streaming_response_timeseries(self, client: Cloudflare) -> None:
        with client.radar.bgp.rpki.aspa.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aspa = response.parse()
            assert_matches_type(ASPATimeseriesResponse, aspa, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncASPA:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_changes(self, async_client: AsyncCloudflare) -> None:
        aspa = await async_client.radar.bgp.rpki.aspa.changes()
        assert_matches_type(ASPAChangesResponse, aspa, path=["response"])

    @parametrize
    async def test_method_changes_with_all_params(self, async_client: AsyncCloudflare) -> None:
        aspa = await async_client.radar.bgp.rpki.aspa.changes(
            asn=13335,
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            include_asn_info=True,
        )
        assert_matches_type(ASPAChangesResponse, aspa, path=["response"])

    @parametrize
    async def test_raw_response_changes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.rpki.aspa.with_raw_response.changes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aspa = await response.parse()
        assert_matches_type(ASPAChangesResponse, aspa, path=["response"])

    @parametrize
    async def test_streaming_response_changes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.rpki.aspa.with_streaming_response.changes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aspa = await response.parse()
            assert_matches_type(ASPAChangesResponse, aspa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_snapshot(self, async_client: AsyncCloudflare) -> None:
        aspa = await async_client.radar.bgp.rpki.aspa.snapshot()
        assert_matches_type(ASPASnapshotResponse, aspa, path=["response"])

    @parametrize
    async def test_method_snapshot_with_all_params(self, async_client: AsyncCloudflare) -> None:
        aspa = await async_client.radar.bgp.rpki.aspa.snapshot(
            customer_asn=13335,
            date=parse_datetime("2024-09-19T00:00:00Z"),
            format="JSON",
            include_asn_info=True,
            provider_asn=174,
        )
        assert_matches_type(ASPASnapshotResponse, aspa, path=["response"])

    @parametrize
    async def test_raw_response_snapshot(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.rpki.aspa.with_raw_response.snapshot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aspa = await response.parse()
        assert_matches_type(ASPASnapshotResponse, aspa, path=["response"])

    @parametrize
    async def test_streaming_response_snapshot(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.rpki.aspa.with_streaming_response.snapshot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aspa = await response.parse()
            assert_matches_type(ASPASnapshotResponse, aspa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries(self, async_client: AsyncCloudflare) -> None:
        aspa = await async_client.radar.bgp.rpki.aspa.timeseries()
        assert_matches_type(ASPATimeseriesResponse, aspa, path=["response"])

    @parametrize
    async def test_method_timeseries_with_all_params(self, async_client: AsyncCloudflare) -> None:
        aspa = await async_client.radar.bgp.rpki.aspa.timeseries(
            date_end=parse_datetime("2023-09-01T11:41:33.782Z"),
            date_start=parse_datetime("2023-09-01T11:41:33.782Z"),
            format="JSON",
            location=["string"],
            name=["main_series"],
            rir=["RIPE_NCC"],
        )
        assert_matches_type(ASPATimeseriesResponse, aspa, path=["response"])

    @parametrize
    async def test_raw_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.rpki.aspa.with_raw_response.timeseries()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aspa = await response.parse()
        assert_matches_type(ASPATimeseriesResponse, aspa, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.rpki.aspa.with_streaming_response.timeseries() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aspa = await response.parse()
            assert_matches_type(ASPATimeseriesResponse, aspa, path=["response"])

        assert cast(Any, response.is_closed) is True
