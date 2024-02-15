# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.spectrums.analytics.aggregates import (
    CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_aggregate_analytics_get_current_aggregated_analytics(self, client: Cloudflare) -> None:
        current = client.spectrums.analytics.aggregates.currents.spectrum_aggregate_analytics_get_current_aggregated_analytics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse, current, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_aggregate_analytics_get_current_aggregated_analytics_with_all_params(
        self, client: Cloudflare
    ) -> None:
        current = client.spectrums.analytics.aggregates.currents.spectrum_aggregate_analytics_get_current_aggregated_analytics(
            "023e105f4ecef8ad9ca31a8372d0c353",
            app_id_param="ea95132c15732412d22c1476fa83f27a,d122c5f4bb71e25cc9e86ab43b142e2f",
            app_id="ea95132c15732412d22c1476fa83f27a,d122c5f4bb71e25cc9e86ab43b142e2f",
            colo_name="PDX",
        )
        assert_matches_type(
            CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse, current, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_spectrum_aggregate_analytics_get_current_aggregated_analytics(
        self, client: Cloudflare
    ) -> None:
        response = client.spectrums.analytics.aggregates.currents.with_raw_response.spectrum_aggregate_analytics_get_current_aggregated_analytics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current = response.parse()
        assert_matches_type(
            CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse, current, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_spectrum_aggregate_analytics_get_current_aggregated_analytics(
        self, client: Cloudflare
    ) -> None:
        with client.spectrums.analytics.aggregates.currents.with_streaming_response.spectrum_aggregate_analytics_get_current_aggregated_analytics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current = response.parse()
            assert_matches_type(
                CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse, current, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_spectrum_aggregate_analytics_get_current_aggregated_analytics(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrums.analytics.aggregates.currents.with_raw_response.spectrum_aggregate_analytics_get_current_aggregated_analytics(
                "",
            )


class TestAsyncCurrents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_aggregate_analytics_get_current_aggregated_analytics(
        self, async_client: AsyncCloudflare
    ) -> None:
        current = await async_client.spectrums.analytics.aggregates.currents.spectrum_aggregate_analytics_get_current_aggregated_analytics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse, current, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_aggregate_analytics_get_current_aggregated_analytics_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        current = await async_client.spectrums.analytics.aggregates.currents.spectrum_aggregate_analytics_get_current_aggregated_analytics(
            "023e105f4ecef8ad9ca31a8372d0c353",
            app_id_param="ea95132c15732412d22c1476fa83f27a,d122c5f4bb71e25cc9e86ab43b142e2f",
            app_id="ea95132c15732412d22c1476fa83f27a,d122c5f4bb71e25cc9e86ab43b142e2f",
            colo_name="PDX",
        )
        assert_matches_type(
            CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse, current, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_spectrum_aggregate_analytics_get_current_aggregated_analytics(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.spectrums.analytics.aggregates.currents.with_raw_response.spectrum_aggregate_analytics_get_current_aggregated_analytics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current = await response.parse()
        assert_matches_type(
            CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse, current, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_spectrum_aggregate_analytics_get_current_aggregated_analytics(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.spectrums.analytics.aggregates.currents.with_streaming_response.spectrum_aggregate_analytics_get_current_aggregated_analytics(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current = await response.parse()
            assert_matches_type(
                CurrentSpectrumAggregateAnalyticsGetCurrentAggregatedAnalyticsResponse, current, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_spectrum_aggregate_analytics_get_current_aggregated_analytics(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrums.analytics.aggregates.currents.with_raw_response.spectrum_aggregate_analytics_get_current_aggregated_analytics(
                "",
            )
