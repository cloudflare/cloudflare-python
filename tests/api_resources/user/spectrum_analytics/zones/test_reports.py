# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.user.spectrum_analytics.zones import ReportGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        report = client.user.spectrum_analytics.zones.reports.get()
        assert_matches_type(ReportGetResponse, report, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        report = client.user.spectrum_analytics.zones.reports.get(
            cdn_traffic=True,
            since=parse_datetime("2014-01-01T05:20:00.12345Z"),
            until=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(ReportGetResponse, report, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.user.spectrum_analytics.zones.reports.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportGetResponse, report, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.user.spectrum_analytics.zones.reports.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportGetResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        report = await async_client.user.spectrum_analytics.zones.reports.get()
        assert_matches_type(ReportGetResponse, report, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        report = await async_client.user.spectrum_analytics.zones.reports.get(
            cdn_traffic=True,
            since=parse_datetime("2014-01-01T05:20:00.12345Z"),
            until=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(ReportGetResponse, report, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.spectrum_analytics.zones.reports.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportGetResponse, report, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.spectrum_analytics.zones.reports.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportGetResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True
