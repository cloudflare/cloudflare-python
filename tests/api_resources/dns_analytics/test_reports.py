# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.dns_analytics import ReportListResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dns_analytics import report_list_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        report = client.dns_analytics.reports.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        report = client.dns_analytics.reports.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dimensions="queryType",
            filters="responseCode==NOERROR,queryType==A",
            limit=100,
            metrics="queryCount,uncachedCount",
            since=parse_datetime("2023-11-11T12:00:00Z"),
            sort="+responseCode,-queryName",
            until=parse_datetime("2023-11-11T13:00:00Z"),
        )
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dns_analytics.reports.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dns_analytics.reports.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportListResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.dns_analytics.reports.with_raw_response.list(
                "",
            )


class TestAsyncReports:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        report = await async_client.dns_analytics.reports.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        report = await async_client.dns_analytics.reports.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dimensions="queryType",
            filters="responseCode==NOERROR,queryType==A",
            limit=100,
            metrics="queryCount,uncachedCount",
            since=parse_datetime("2023-11-11T12:00:00Z"),
            sort="+responseCode,-queryName",
            until=parse_datetime("2023-11-11T13:00:00Z"),
        )
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_analytics.reports.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_analytics.reports.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportListResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.dns_analytics.reports.with_raw_response.list(
                "",
            )
