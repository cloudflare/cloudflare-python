# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.realtime_kit import AnalyticsGetOrgAnalyticsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalytics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_org_analytics(self, client: Cloudflare) -> None:
        analytics = client.realtime_kit.analytics.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AnalyticsGetOrgAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_org_analytics_with_all_params(self, client: Cloudflare) -> None:
        analytics = client.realtime_kit.analytics.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_date="2022-09-22",
            start_date="2022-09-01",
        )
        assert_matches_type(AnalyticsGetOrgAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_org_analytics(self, client: Cloudflare) -> None:
        response = client.realtime_kit.analytics.with_raw_response.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = response.parse()
        assert_matches_type(AnalyticsGetOrgAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_org_analytics(self, client: Cloudflare) -> None:
        with client.realtime_kit.analytics.with_streaming_response.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = response.parse()
            assert_matches_type(AnalyticsGetOrgAnalyticsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_org_analytics(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.analytics.with_raw_response.get_org_analytics(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.analytics.with_raw_response.get_org_analytics(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAnalytics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_org_analytics(self, async_client: AsyncCloudflare) -> None:
        analytics = await async_client.realtime_kit.analytics.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AnalyticsGetOrgAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_org_analytics_with_all_params(self, async_client: AsyncCloudflare) -> None:
        analytics = await async_client.realtime_kit.analytics.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_date="2022-09-22",
            start_date="2022-09-01",
        )
        assert_matches_type(AnalyticsGetOrgAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_org_analytics(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.analytics.with_raw_response.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics = await response.parse()
        assert_matches_type(AnalyticsGetOrgAnalyticsResponse, analytics, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_org_analytics(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.analytics.with_streaming_response.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics = await response.parse()
            assert_matches_type(AnalyticsGetOrgAnalyticsResponse, analytics, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_org_analytics(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.analytics.with_raw_response.get_org_analytics(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.analytics.with_raw_response.get_org_analytics(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
