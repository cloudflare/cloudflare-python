# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.analytics import LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.analytics import latency_argo_analytics_for_zone_argo_analytics_for_a_zone_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLatencies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_argo_analytics_for_zone_argo_analytics_for_a_zone(self, client: Cloudflare) -> None:
        latency = client.analytics.latencies.argo_analytics_for_zone_argo_analytics_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse, latency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_argo_analytics_for_zone_argo_analytics_for_a_zone_with_all_params(self, client: Cloudflare) -> None:
        latency = client.analytics.latencies.argo_analytics_for_zone_argo_analytics_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            bins="string",
        )
        assert_matches_type(LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse, latency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_argo_analytics_for_zone_argo_analytics_for_a_zone(self, client: Cloudflare) -> None:
        response = client.analytics.latencies.with_raw_response.argo_analytics_for_zone_argo_analytics_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        latency = response.parse()
        assert_matches_type(LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse, latency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_argo_analytics_for_zone_argo_analytics_for_a_zone(self, client: Cloudflare) -> None:
        with client.analytics.latencies.with_streaming_response.argo_analytics_for_zone_argo_analytics_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            latency = response.parse()
            assert_matches_type(LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse, latency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_argo_analytics_for_zone_argo_analytics_for_a_zone(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.analytics.latencies.with_raw_response.argo_analytics_for_zone_argo_analytics_for_a_zone(
                "",
            )


class TestAsyncLatencies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_argo_analytics_for_zone_argo_analytics_for_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        latency = await async_client.analytics.latencies.argo_analytics_for_zone_argo_analytics_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse, latency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_argo_analytics_for_zone_argo_analytics_for_a_zone_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        latency = await async_client.analytics.latencies.argo_analytics_for_zone_argo_analytics_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
            bins="string",
        )
        assert_matches_type(LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse, latency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_argo_analytics_for_zone_argo_analytics_for_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.analytics.latencies.with_raw_response.argo_analytics_for_zone_argo_analytics_for_a_zone(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        latency = await response.parse()
        assert_matches_type(LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse, latency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_argo_analytics_for_zone_argo_analytics_for_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.analytics.latencies.with_streaming_response.argo_analytics_for_zone_argo_analytics_for_a_zone(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            latency = await response.parse()
            assert_matches_type(LatencyArgoAnalyticsForZoneArgoAnalyticsForAZoneResponse, latency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_argo_analytics_for_zone_argo_analytics_for_a_zone(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.analytics.latencies.with_raw_response.argo_analytics_for_zone_argo_analytics_for_a_zone(
                "",
            )
