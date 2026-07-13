# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    AnalyticsQueryTopNResponse,
    AnalyticsQuerySummaryResponse,
    AnalyticsQueryTimeseriesResponse,
)
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalyticsQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        analytics_query = client.analytics_query.summary(
            dataset="access-logins",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["string"],
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(AnalyticsQuerySummaryResponse, analytics_query, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:
        response = client.analytics_query.with_raw_response.summary(
            dataset="access-logins",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["string"],
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_query = response.parse()
        assert_matches_type(AnalyticsQuerySummaryResponse, analytics_query, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.analytics_query.with_streaming_response.summary(
            dataset="access-logins",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["string"],
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_query = response.parse()
            assert_matches_type(AnalyticsQuerySummaryResponse, analytics_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_summary(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.analytics_query.with_raw_response.summary(
                dataset="access-logins",
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                group_by=["string"],
                stats=["attemptsTotal"],
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset` but received ''"):
            client.analytics_query.with_raw_response.summary(
                dataset="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                group_by=["string"],
                stats=["attemptsTotal"],
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

    @parametrize
    def test_method_timeseries(self, client: Cloudflare) -> None:
        analytics_query = client.analytics_query.timeseries(
            dataset="shadow_it",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "allowed",
                    "op": "eq",
                    "values": [True],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["country", "allowed"],
            resolution="day",
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(AnalyticsQueryTimeseriesResponse, analytics_query, path=["response"])

    @parametrize
    def test_raw_response_timeseries(self, client: Cloudflare) -> None:
        response = client.analytics_query.with_raw_response.timeseries(
            dataset="shadow_it",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "allowed",
                    "op": "eq",
                    "values": [True],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["country", "allowed"],
            resolution="day",
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_query = response.parse()
        assert_matches_type(AnalyticsQueryTimeseriesResponse, analytics_query, path=["response"])

    @parametrize
    def test_streaming_response_timeseries(self, client: Cloudflare) -> None:
        with client.analytics_query.with_streaming_response.timeseries(
            dataset="shadow_it",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "allowed",
                    "op": "eq",
                    "values": [True],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["country", "allowed"],
            resolution="day",
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_query = response.parse()
            assert_matches_type(AnalyticsQueryTimeseriesResponse, analytics_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_timeseries(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.analytics_query.with_raw_response.timeseries(
                dataset="shadow_it",
                account_id="",
                filters=[
                    {
                        "name": "allowed",
                        "op": "eq",
                        "values": [True],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                group_by=["country", "allowed"],
                resolution="day",
                stats=["attemptsTotal"],
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset` but received ''"):
            client.analytics_query.with_raw_response.timeseries(
                dataset="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                filters=[
                    {
                        "name": "allowed",
                        "op": "eq",
                        "values": [True],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                group_by=["country", "allowed"],
                resolution="day",
                stats=["attemptsTotal"],
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

    @parametrize
    def test_method_top_n(self, client: Cloudflare) -> None:
        analytics_query = client.analytics_query.top_n(
            dataset="gateway-http",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-05T00:00:00Z"),
            group_by=["appName", "appCategory"],
            n=10,
            order_by="bytesTotal",
            stats=["bytesTotal", "requestsTotal"],
            to=parse_datetime("2024-11-06T00:00:00Z"),
        )
        assert_matches_type(SyncSinglePage[AnalyticsQueryTopNResponse], analytics_query, path=["response"])

    @parametrize
    def test_raw_response_top_n(self, client: Cloudflare) -> None:
        response = client.analytics_query.with_raw_response.top_n(
            dataset="gateway-http",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-05T00:00:00Z"),
            group_by=["appName", "appCategory"],
            n=10,
            order_by="bytesTotal",
            stats=["bytesTotal", "requestsTotal"],
            to=parse_datetime("2024-11-06T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_query = response.parse()
        assert_matches_type(SyncSinglePage[AnalyticsQueryTopNResponse], analytics_query, path=["response"])

    @parametrize
    def test_streaming_response_top_n(self, client: Cloudflare) -> None:
        with client.analytics_query.with_streaming_response.top_n(
            dataset="gateway-http",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-05T00:00:00Z"),
            group_by=["appName", "appCategory"],
            n=10,
            order_by="bytesTotal",
            stats=["bytesTotal", "requestsTotal"],
            to=parse_datetime("2024-11-06T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_query = response.parse()
            assert_matches_type(SyncSinglePage[AnalyticsQueryTopNResponse], analytics_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_top_n(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.analytics_query.with_raw_response.top_n(
                dataset="gateway-http",
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-05T00:00:00Z"),
                group_by=["appName", "appCategory"],
                n=10,
                order_by="bytesTotal",
                stats=["bytesTotal", "requestsTotal"],
                to=parse_datetime("2024-11-06T00:00:00Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset` but received ''"):
            client.analytics_query.with_raw_response.top_n(
                dataset="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-05T00:00:00Z"),
                group_by=["appName", "appCategory"],
                n=10,
                order_by="bytesTotal",
                stats=["bytesTotal", "requestsTotal"],
                to=parse_datetime("2024-11-06T00:00:00Z"),
            )


class TestAsyncAnalyticsQuery:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        analytics_query = await async_client.analytics_query.summary(
            dataset="access-logins",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["string"],
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(AnalyticsQuerySummaryResponse, analytics_query, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.analytics_query.with_raw_response.summary(
            dataset="access-logins",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["string"],
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_query = await response.parse()
        assert_matches_type(AnalyticsQuerySummaryResponse, analytics_query, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.analytics_query.with_streaming_response.summary(
            dataset="access-logins",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["string"],
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_query = await response.parse()
            assert_matches_type(AnalyticsQuerySummaryResponse, analytics_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_summary(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.analytics_query.with_raw_response.summary(
                dataset="access-logins",
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                group_by=["string"],
                stats=["attemptsTotal"],
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset` but received ''"):
            await async_client.analytics_query.with_raw_response.summary(
                dataset="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                group_by=["string"],
                stats=["attemptsTotal"],
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

    @parametrize
    async def test_method_timeseries(self, async_client: AsyncCloudflare) -> None:
        analytics_query = await async_client.analytics_query.timeseries(
            dataset="shadow_it",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "allowed",
                    "op": "eq",
                    "values": [True],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["country", "allowed"],
            resolution="day",
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )
        assert_matches_type(AnalyticsQueryTimeseriesResponse, analytics_query, path=["response"])

    @parametrize
    async def test_raw_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.analytics_query.with_raw_response.timeseries(
            dataset="shadow_it",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "allowed",
                    "op": "eq",
                    "values": [True],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["country", "allowed"],
            resolution="day",
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_query = await response.parse()
        assert_matches_type(AnalyticsQueryTimeseriesResponse, analytics_query, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries(self, async_client: AsyncCloudflare) -> None:
        async with async_client.analytics_query.with_streaming_response.timeseries(
            dataset="shadow_it",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "allowed",
                    "op": "eq",
                    "values": [True],
                }
            ],
            from_=parse_datetime("2024-11-01T00:00:00Z"),
            group_by=["country", "allowed"],
            resolution="day",
            stats=["attemptsTotal"],
            to=parse_datetime("2024-11-08T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_query = await response.parse()
            assert_matches_type(AnalyticsQueryTimeseriesResponse, analytics_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_timeseries(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.analytics_query.with_raw_response.timeseries(
                dataset="shadow_it",
                account_id="",
                filters=[
                    {
                        "name": "allowed",
                        "op": "eq",
                        "values": [True],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                group_by=["country", "allowed"],
                resolution="day",
                stats=["attemptsTotal"],
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset` but received ''"):
            await async_client.analytics_query.with_raw_response.timeseries(
                dataset="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                filters=[
                    {
                        "name": "allowed",
                        "op": "eq",
                        "values": [True],
                    }
                ],
                from_=parse_datetime("2024-11-01T00:00:00Z"),
                group_by=["country", "allowed"],
                resolution="day",
                stats=["attemptsTotal"],
                to=parse_datetime("2024-11-08T00:00:00Z"),
            )

    @parametrize
    async def test_method_top_n(self, async_client: AsyncCloudflare) -> None:
        analytics_query = await async_client.analytics_query.top_n(
            dataset="gateway-http",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-05T00:00:00Z"),
            group_by=["appName", "appCategory"],
            n=10,
            order_by="bytesTotal",
            stats=["bytesTotal", "requestsTotal"],
            to=parse_datetime("2024-11-06T00:00:00Z"),
        )
        assert_matches_type(AsyncSinglePage[AnalyticsQueryTopNResponse], analytics_query, path=["response"])

    @parametrize
    async def test_raw_response_top_n(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.analytics_query.with_raw_response.top_n(
            dataset="gateway-http",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-05T00:00:00Z"),
            group_by=["appName", "appCategory"],
            n=10,
            order_by="bytesTotal",
            stats=["bytesTotal", "requestsTotal"],
            to=parse_datetime("2024-11-06T00:00:00Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_query = await response.parse()
        assert_matches_type(AsyncSinglePage[AnalyticsQueryTopNResponse], analytics_query, path=["response"])

    @parametrize
    async def test_streaming_response_top_n(self, async_client: AsyncCloudflare) -> None:
        async with async_client.analytics_query.with_streaming_response.top_n(
            dataset="gateway-http",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            filters=[
                {
                    "name": "country",
                    "op": "in",
                    "values": ["US", "CA", "GB"],
                }
            ],
            from_=parse_datetime("2024-11-05T00:00:00Z"),
            group_by=["appName", "appCategory"],
            n=10,
            order_by="bytesTotal",
            stats=["bytesTotal", "requestsTotal"],
            to=parse_datetime("2024-11-06T00:00:00Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_query = await response.parse()
            assert_matches_type(AsyncSinglePage[AnalyticsQueryTopNResponse], analytics_query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_top_n(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.analytics_query.with_raw_response.top_n(
                dataset="gateway-http",
                account_id="",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-05T00:00:00Z"),
                group_by=["appName", "appCategory"],
                n=10,
                order_by="bytesTotal",
                stats=["bytesTotal", "requestsTotal"],
                to=parse_datetime("2024-11-06T00:00:00Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset` but received ''"):
            await async_client.analytics_query.with_raw_response.top_n(
                dataset="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                filters=[
                    {
                        "name": "country",
                        "op": "in",
                        "values": ["US", "CA", "GB"],
                    }
                ],
                from_=parse_datetime("2024-11-05T00:00:00Z"),
                group_by=["appName", "appCategory"],
                n=10,
                order_by="bytesTotal",
                stats=["bytesTotal", "requestsTotal"],
                to=parse_datetime("2024-11-06T00:00:00Z"),
            )
