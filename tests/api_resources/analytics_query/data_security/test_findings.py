# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.analytics_query.data_security import (
    FindingSummaryResponse,
    FindingTimeseriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFindings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        finding = client.analytics_query.data_security.findings.summary(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(FindingSummaryResponse, finding, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:
        response = client.analytics_query.data_security.findings.with_raw_response.summary(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = response.parse()
        assert_matches_type(FindingSummaryResponse, finding, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.analytics_query.data_security.findings.with_streaming_response.summary(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = response.parse()
            assert_matches_type(FindingSummaryResponse, finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_summary(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.analytics_query.data_security.findings.with_raw_response.summary(
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

    @parametrize
    def test_method_timeseries(self, client: Cloudflare) -> None:
        finding = client.analytics_query.data_security.findings.timeseries(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(FindingTimeseriesResponse, finding, path=["response"])

    @parametrize
    def test_raw_response_timeseries(self, client: Cloudflare) -> None:
        response = client.analytics_query.data_security.findings.with_raw_response.timeseries(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = response.parse()
        assert_matches_type(FindingTimeseriesResponse, finding, path=["response"])

    @parametrize
    def test_streaming_response_timeseries(self, client: Cloudflare) -> None:
        with client.analytics_query.data_security.findings.with_streaming_response.timeseries(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = response.parse()
            assert_matches_type(FindingTimeseriesResponse, finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_timeseries(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.analytics_query.data_security.findings.with_raw_response.timeseries(
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )


class TestAsyncFindings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.analytics_query.data_security.findings.summary(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(FindingSummaryResponse, finding, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.analytics_query.data_security.findings.with_raw_response.summary(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = await response.parse()
        assert_matches_type(FindingSummaryResponse, finding, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.analytics_query.data_security.findings.with_streaming_response.summary(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = await response.parse()
            assert_matches_type(FindingSummaryResponse, finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_summary(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.analytics_query.data_security.findings.with_raw_response.summary(
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

    @parametrize
    async def test_method_timeseries(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.analytics_query.data_security.findings.timeseries(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(FindingTimeseriesResponse, finding, path=["response"])

    @parametrize
    async def test_raw_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.analytics_query.data_security.findings.with_raw_response.timeseries(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = await response.parse()
        assert_matches_type(FindingTimeseriesResponse, finding, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        async with async_client.analytics_query.data_security.findings.with_streaming_response.timeseries(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = await response.parse()
            assert_matches_type(FindingTimeseriesResponse, finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_timeseries(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.analytics_query.data_security.findings.with_raw_response.timeseries(
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )
