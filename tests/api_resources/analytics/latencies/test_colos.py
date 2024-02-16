# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.analytics.latencies import (
    ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestColos:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self, client: Cloudflare
    ) -> None:
        colo = client.analytics.latencies.colos.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse, colo, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self, client: Cloudflare
    ) -> None:
        response = client.analytics.latencies.colos.with_raw_response.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colo = response.parse()
        assert_matches_type(
            ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse, colo, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self, client: Cloudflare
    ) -> None:
        with client.analytics.latencies.colos.with_streaming_response.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colo = response.parse()
            assert_matches_type(
                ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse, colo, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.analytics.latencies.colos.with_raw_response.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
                "",
            )


class TestAsyncColos:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self, async_client: AsyncCloudflare
    ) -> None:
        colo = await async_client.analytics.latencies.colos.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse, colo, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.analytics.latencies.colos.with_raw_response.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colo = await response.parse()
        assert_matches_type(
            ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse, colo, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.analytics.latencies.colos.with_streaming_response.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colo = await response.parse()
            assert_matches_type(
                ColoArgoAnalyticsForGeolocationArgoAnalyticsForAZoneAtDifferentPoPsResponse, colo, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.analytics.latencies.colos.with_raw_response.argo_analytics_for_geolocation_argo_analytics_for_a_zone_at_different_po_ps(
                "",
            )
