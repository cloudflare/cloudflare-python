# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.dns.analytics import DNSDNSAnalyticsAPIReport

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        report = client.dns.analytics.reports.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSDNSAnalyticsAPIReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        report = client.dns.analytics.reports.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dimensions="queryType",
            filters="responseCode==NOERROR,queryType==A",
            limit=100,
            metrics="queryCount,uncachedCount",
            since=parse_datetime("2023-11-11T12:00:00Z"),
            sort="+responseCode,-queryName",
            until=parse_datetime("2023-11-11T13:00:00Z"),
        )
        assert_matches_type(DNSDNSAnalyticsAPIReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns.analytics.reports.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(DNSDNSAnalyticsAPIReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns.analytics.reports.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(DNSDNSAnalyticsAPIReport, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.dns.analytics.reports.with_raw_response.get(
                "",
            )


class TestAsyncReports:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        report = await async_client.dns.analytics.reports.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSDNSAnalyticsAPIReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        report = await async_client.dns.analytics.reports.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dimensions="queryType",
            filters="responseCode==NOERROR,queryType==A",
            limit=100,
            metrics="queryCount,uncachedCount",
            since=parse_datetime("2023-11-11T12:00:00Z"),
            sort="+responseCode,-queryName",
            until=parse_datetime("2023-11-11T13:00:00Z"),
        )
        assert_matches_type(DNSDNSAnalyticsAPIReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.analytics.reports.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(DNSDNSAnalyticsAPIReport, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.analytics.reports.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(DNSDNSAnalyticsAPIReport, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.dns.analytics.reports.with_raw_response.get(
                "",
            )
