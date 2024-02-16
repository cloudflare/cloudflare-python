# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.analytics import (
    DashboardZoneAnalyticsDeprecatedGetDashboardResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDashboards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_analytics_deprecated_get_dashboard(self, client: Cloudflare) -> None:
        dashboard = client.analytics.dashboards.zone_analytics_deprecated_get_dashboard(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DashboardZoneAnalyticsDeprecatedGetDashboardResponse, dashboard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_analytics_deprecated_get_dashboard_with_all_params(self, client: Cloudflare) -> None:
        dashboard = client.analytics.dashboards.zone_analytics_deprecated_get_dashboard(
            "023e105f4ecef8ad9ca31a8372d0c353",
            continuous=True,
            since="2015-01-01T12:23:00Z",
            until="2015-01-02T12:23:00Z",
        )
        assert_matches_type(DashboardZoneAnalyticsDeprecatedGetDashboardResponse, dashboard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_analytics_deprecated_get_dashboard(self, client: Cloudflare) -> None:
        response = client.analytics.dashboards.with_raw_response.zone_analytics_deprecated_get_dashboard(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = response.parse()
        assert_matches_type(DashboardZoneAnalyticsDeprecatedGetDashboardResponse, dashboard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_analytics_deprecated_get_dashboard(self, client: Cloudflare) -> None:
        with client.analytics.dashboards.with_streaming_response.zone_analytics_deprecated_get_dashboard(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = response.parse()
            assert_matches_type(DashboardZoneAnalyticsDeprecatedGetDashboardResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_analytics_deprecated_get_dashboard(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.analytics.dashboards.with_raw_response.zone_analytics_deprecated_get_dashboard(
                "",
            )


class TestAsyncDashboards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_analytics_deprecated_get_dashboard(self, async_client: AsyncCloudflare) -> None:
        dashboard = await async_client.analytics.dashboards.zone_analytics_deprecated_get_dashboard(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DashboardZoneAnalyticsDeprecatedGetDashboardResponse, dashboard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_analytics_deprecated_get_dashboard_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        dashboard = await async_client.analytics.dashboards.zone_analytics_deprecated_get_dashboard(
            "023e105f4ecef8ad9ca31a8372d0c353",
            continuous=True,
            since="2015-01-01T12:23:00Z",
            until="2015-01-02T12:23:00Z",
        )
        assert_matches_type(DashboardZoneAnalyticsDeprecatedGetDashboardResponse, dashboard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_analytics_deprecated_get_dashboard(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.analytics.dashboards.with_raw_response.zone_analytics_deprecated_get_dashboard(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dashboard = await response.parse()
        assert_matches_type(DashboardZoneAnalyticsDeprecatedGetDashboardResponse, dashboard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_analytics_deprecated_get_dashboard(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.analytics.dashboards.with_streaming_response.zone_analytics_deprecated_get_dashboard(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dashboard = await response.parse()
            assert_matches_type(DashboardZoneAnalyticsDeprecatedGetDashboardResponse, dashboard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_analytics_deprecated_get_dashboard(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.analytics.dashboards.with_raw_response.zone_analytics_deprecated_get_dashboard(
                "",
            )
