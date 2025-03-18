# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date, parse_datetime
from cloudflare.types.radar.ranking import (
    InternetServiceTopResponse,
    InternetServiceCategoriesResponse,
    InternetServiceTimeseriesGroupsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInternetServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_categories(self, client: Cloudflare) -> None:
        internet_service = client.radar.ranking.internet_services.categories()
        assert_matches_type(InternetServiceCategoriesResponse, internet_service, path=["response"])

    @parametrize
    def test_method_categories_with_all_params(self, client: Cloudflare) -> None:
        internet_service = client.radar.ranking.internet_services.categories(
            date=[parse_date("2019-12-27")],
            format="JSON",
            limit=5,
            name=["main_series"],
        )
        assert_matches_type(InternetServiceCategoriesResponse, internet_service, path=["response"])

    @parametrize
    def test_raw_response_categories(self, client: Cloudflare) -> None:
        response = client.radar.ranking.internet_services.with_raw_response.categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internet_service = response.parse()
        assert_matches_type(InternetServiceCategoriesResponse, internet_service, path=["response"])

    @parametrize
    def test_streaming_response_categories(self, client: Cloudflare) -> None:
        with client.radar.ranking.internet_services.with_streaming_response.categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internet_service = response.parse()
            assert_matches_type(InternetServiceCategoriesResponse, internet_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries_groups(self, client: Cloudflare) -> None:
        internet_service = client.radar.ranking.internet_services.timeseries_groups()
        assert_matches_type(InternetServiceTimeseriesGroupsResponse, internet_service, path=["response"])

    @parametrize
    def test_method_timeseries_groups_with_all_params(self, client: Cloudflare) -> None:
        internet_service = client.radar.ranking.internet_services.timeseries_groups(
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            name=["main_series"],
            service_category=["string"],
        )
        assert_matches_type(InternetServiceTimeseriesGroupsResponse, internet_service, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups(self, client: Cloudflare) -> None:
        response = client.radar.ranking.internet_services.with_raw_response.timeseries_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internet_service = response.parse()
        assert_matches_type(InternetServiceTimeseriesGroupsResponse, internet_service, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups(self, client: Cloudflare) -> None:
        with client.radar.ranking.internet_services.with_streaming_response.timeseries_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internet_service = response.parse()
            assert_matches_type(InternetServiceTimeseriesGroupsResponse, internet_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_top(self, client: Cloudflare) -> None:
        internet_service = client.radar.ranking.internet_services.top()
        assert_matches_type(InternetServiceTopResponse, internet_service, path=["response"])

    @parametrize
    def test_method_top_with_all_params(self, client: Cloudflare) -> None:
        internet_service = client.radar.ranking.internet_services.top(
            date=[parse_date("2019-12-27")],
            format="JSON",
            limit=5,
            name=["main_series"],
            service_category=["string"],
        )
        assert_matches_type(InternetServiceTopResponse, internet_service, path=["response"])

    @parametrize
    def test_raw_response_top(self, client: Cloudflare) -> None:
        response = client.radar.ranking.internet_services.with_raw_response.top()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internet_service = response.parse()
        assert_matches_type(InternetServiceTopResponse, internet_service, path=["response"])

    @parametrize
    def test_streaming_response_top(self, client: Cloudflare) -> None:
        with client.radar.ranking.internet_services.with_streaming_response.top() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internet_service = response.parse()
            assert_matches_type(InternetServiceTopResponse, internet_service, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInternetServices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_categories(self, async_client: AsyncCloudflare) -> None:
        internet_service = await async_client.radar.ranking.internet_services.categories()
        assert_matches_type(InternetServiceCategoriesResponse, internet_service, path=["response"])

    @parametrize
    async def test_method_categories_with_all_params(self, async_client: AsyncCloudflare) -> None:
        internet_service = await async_client.radar.ranking.internet_services.categories(
            date=[parse_date("2019-12-27")],
            format="JSON",
            limit=5,
            name=["main_series"],
        )
        assert_matches_type(InternetServiceCategoriesResponse, internet_service, path=["response"])

    @parametrize
    async def test_raw_response_categories(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ranking.internet_services.with_raw_response.categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internet_service = await response.parse()
        assert_matches_type(InternetServiceCategoriesResponse, internet_service, path=["response"])

    @parametrize
    async def test_streaming_response_categories(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ranking.internet_services.with_streaming_response.categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internet_service = await response.parse()
            assert_matches_type(InternetServiceCategoriesResponse, internet_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        internet_service = await async_client.radar.ranking.internet_services.timeseries_groups()
        assert_matches_type(InternetServiceTimeseriesGroupsResponse, internet_service, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_with_all_params(self, async_client: AsyncCloudflare) -> None:
        internet_service = await async_client.radar.ranking.internet_services.timeseries_groups(
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit=5,
            name=["main_series"],
            service_category=["string"],
        )
        assert_matches_type(InternetServiceTimeseriesGroupsResponse, internet_service, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ranking.internet_services.with_raw_response.timeseries_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internet_service = await response.parse()
        assert_matches_type(InternetServiceTimeseriesGroupsResponse, internet_service, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ranking.internet_services.with_streaming_response.timeseries_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internet_service = await response.parse()
            assert_matches_type(InternetServiceTimeseriesGroupsResponse, internet_service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_top(self, async_client: AsyncCloudflare) -> None:
        internet_service = await async_client.radar.ranking.internet_services.top()
        assert_matches_type(InternetServiceTopResponse, internet_service, path=["response"])

    @parametrize
    async def test_method_top_with_all_params(self, async_client: AsyncCloudflare) -> None:
        internet_service = await async_client.radar.ranking.internet_services.top(
            date=[parse_date("2019-12-27")],
            format="JSON",
            limit=5,
            name=["main_series"],
            service_category=["string"],
        )
        assert_matches_type(InternetServiceTopResponse, internet_service, path=["response"])

    @parametrize
    async def test_raw_response_top(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.ranking.internet_services.with_raw_response.top()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        internet_service = await response.parse()
        assert_matches_type(InternetServiceTopResponse, internet_service, path=["response"])

    @parametrize
    async def test_streaming_response_top(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.ranking.internet_services.with_streaming_response.top() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            internet_service = await response.parse()
            assert_matches_type(InternetServiceTopResponse, internet_service, path=["response"])

        assert cast(Any, response.is_closed) is True
