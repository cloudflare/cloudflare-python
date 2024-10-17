# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.spectrum.analytics.events import BytimeGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBytimes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bytime = client.spectrum.analytics.events.bytimes.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            time_delta="year",
        )
        assert_matches_type(Optional[BytimeGetResponse], bytime, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        bytime = client.spectrum.analytics.events.bytimes.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            time_delta="year",
            dimensions=["event", "appID"],
            filters="event==disconnect%20AND%20coloName!=SFO",
            metrics=["count", "bytesIngress"],
            since=parse_datetime("2014-01-01T05:20:00.12345Z"),
            sort=["+count", "-bytesIngress"],
            until=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(Optional[BytimeGetResponse], bytime, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.spectrum.analytics.events.bytimes.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            time_delta="year",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bytime = response.parse()
        assert_matches_type(Optional[BytimeGetResponse], bytime, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.spectrum.analytics.events.bytimes.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            time_delta="year",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bytime = response.parse()
            assert_matches_type(Optional[BytimeGetResponse], bytime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.spectrum.analytics.events.bytimes.with_raw_response.get(
                zone_id="",
                time_delta="year",
            )


class TestAsyncBytimes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bytime = await async_client.spectrum.analytics.events.bytimes.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            time_delta="year",
        )
        assert_matches_type(Optional[BytimeGetResponse], bytime, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bytime = await async_client.spectrum.analytics.events.bytimes.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            time_delta="year",
            dimensions=["event", "appID"],
            filters="event==disconnect%20AND%20coloName!=SFO",
            metrics=["count", "bytesIngress"],
            since=parse_datetime("2014-01-01T05:20:00.12345Z"),
            sort=["+count", "-bytesIngress"],
            until=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(Optional[BytimeGetResponse], bytime, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.analytics.events.bytimes.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            time_delta="year",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bytime = await response.parse()
        assert_matches_type(Optional[BytimeGetResponse], bytime, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.analytics.events.bytimes.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            time_delta="year",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bytime = await response.parse()
            assert_matches_type(Optional[BytimeGetResponse], bytime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.spectrum.analytics.events.bytimes.with_raw_response.get(
                zone_id="",
                time_delta="year",
            )
