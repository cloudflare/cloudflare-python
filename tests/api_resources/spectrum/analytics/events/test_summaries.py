# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.spectrum.analytics.events import SummaryGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummaries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        summary = client.spectrum.analytics.events.summaries.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SummaryGetResponse], summary, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        summary = client.spectrum.analytics.events.summaries.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dimensions=["event", "appID"],
            filters="event==disconnect%20AND%20coloName!=SFO",
            metrics=["count", "bytesIngress"],
            since=parse_datetime("2014-01-01T05:20:00.12345Z"),
            sort=["+count", "-bytesIngress"],
            until=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(Optional[SummaryGetResponse], summary, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.spectrum.analytics.events.summaries.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(Optional[SummaryGetResponse], summary, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.spectrum.analytics.events.summaries.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(Optional[SummaryGetResponse], summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.spectrum.analytics.events.summaries.with_raw_response.get(
                zone_id="",
            )


class TestAsyncSummaries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.spectrum.analytics.events.summaries.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SummaryGetResponse], summary, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.spectrum.analytics.events.summaries.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dimensions=["event", "appID"],
            filters="event==disconnect%20AND%20coloName!=SFO",
            metrics=["count", "bytesIngress"],
            since=parse_datetime("2014-01-01T05:20:00.12345Z"),
            sort=["+count", "-bytesIngress"],
            until=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(Optional[SummaryGetResponse], summary, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.analytics.events.summaries.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(Optional[SummaryGetResponse], summary, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.analytics.events.summaries.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(Optional[SummaryGetResponse], summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.spectrum.analytics.events.summaries.with_raw_response.get(
                zone_id="",
            )
