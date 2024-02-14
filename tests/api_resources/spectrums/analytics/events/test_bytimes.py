# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.spectrums.analytics.events import (
    BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBytimes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_analytics_by_time_get_analytics_by_time(self, client: Cloudflare) -> None:
        bytime = client.spectrums.analytics.events.bytimes.spectrum_analytics_by_time_get_analytics_by_time(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse], bytime, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_analytics_by_time_get_analytics_by_time_with_all_params(self, client: Cloudflare) -> None:
        bytime = client.spectrums.analytics.events.bytimes.spectrum_analytics_by_time_get_analytics_by_time(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dimensions=["event", "appID"],
            filters="event==disconnect%20AND%20coloName!=SFO",
            metrics=["count", "bytesIngress"],
            since=parse_datetime("2014-01-02T02:20:00Z"),
            sort=["+count", "-bytesIngress"],
            time_delta="minute",
            until=parse_datetime("2014-01-02T03:20:00Z"),
        )
        assert_matches_type(
            Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse], bytime, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_spectrum_analytics_by_time_get_analytics_by_time(self, client: Cloudflare) -> None:
        response = client.spectrums.analytics.events.bytimes.with_raw_response.spectrum_analytics_by_time_get_analytics_by_time(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bytime = response.parse()
        assert_matches_type(
            Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse], bytime, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_spectrum_analytics_by_time_get_analytics_by_time(self, client: Cloudflare) -> None:
        with client.spectrums.analytics.events.bytimes.with_streaming_response.spectrum_analytics_by_time_get_analytics_by_time(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bytime = response.parse()
            assert_matches_type(
                Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse], bytime, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_spectrum_analytics_by_time_get_analytics_by_time(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrums.analytics.events.bytimes.with_raw_response.spectrum_analytics_by_time_get_analytics_by_time(
                "",
            )


class TestAsyncBytimes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_analytics_by_time_get_analytics_by_time(self, async_client: AsyncCloudflare) -> None:
        bytime = await async_client.spectrums.analytics.events.bytimes.spectrum_analytics_by_time_get_analytics_by_time(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse], bytime, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_analytics_by_time_get_analytics_by_time_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        bytime = await async_client.spectrums.analytics.events.bytimes.spectrum_analytics_by_time_get_analytics_by_time(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dimensions=["event", "appID"],
            filters="event==disconnect%20AND%20coloName!=SFO",
            metrics=["count", "bytesIngress"],
            since=parse_datetime("2014-01-02T02:20:00Z"),
            sort=["+count", "-bytesIngress"],
            time_delta="minute",
            until=parse_datetime("2014-01-02T03:20:00Z"),
        )
        assert_matches_type(
            Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse], bytime, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_spectrum_analytics_by_time_get_analytics_by_time(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.spectrums.analytics.events.bytimes.with_raw_response.spectrum_analytics_by_time_get_analytics_by_time(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bytime = await response.parse()
        assert_matches_type(
            Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse], bytime, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_spectrum_analytics_by_time_get_analytics_by_time(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.spectrums.analytics.events.bytimes.with_streaming_response.spectrum_analytics_by_time_get_analytics_by_time(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bytime = await response.parse()
            assert_matches_type(
                Optional[BytimeSpectrumAnalyticsByTimeGetAnalyticsByTimeResponse], bytime, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_spectrum_analytics_by_time_get_analytics_by_time(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrums.analytics.events.bytimes.with_raw_response.spectrum_analytics_by_time_get_analytics_by_time(
                "",
            )
