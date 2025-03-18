# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.http import (
    TopBrowserResponse,
    TopBrowserFamilyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_browser(self, client: Cloudflare) -> None:
        top = client.radar.http.top.browser()
        assert_matches_type(TopBrowserResponse, top, path=["response"])

    @parametrize
    def test_method_browser_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.http.top.browser(
            asn=["string"],
            bot_class=["LIKELY_AUTOMATED"],
            browser_family=["CHROME"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP"],
            format="JSON",
            http_protocol=["HTTP"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            os=["WINDOWS"],
            tls_version=["TLSv1_0"],
        )
        assert_matches_type(TopBrowserResponse, top, path=["response"])

    @parametrize
    def test_raw_response_browser(self, client: Cloudflare) -> None:
        response = client.radar.http.top.with_raw_response.browser()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopBrowserResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_browser(self, client: Cloudflare) -> None:
        with client.radar.http.top.with_streaming_response.browser() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopBrowserResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_browser_family(self, client: Cloudflare) -> None:
        top = client.radar.http.top.browser_family()
        assert_matches_type(TopBrowserFamilyResponse, top, path=["response"])

    @parametrize
    def test_method_browser_family_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.http.top.browser_family(
            asn=["string"],
            bot_class=["LIKELY_AUTOMATED"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP"],
            format="JSON",
            http_protocol=["HTTP"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            os=["WINDOWS"],
            tls_version=["TLSv1_0"],
        )
        assert_matches_type(TopBrowserFamilyResponse, top, path=["response"])

    @parametrize
    def test_raw_response_browser_family(self, client: Cloudflare) -> None:
        response = client.radar.http.top.with_raw_response.browser_family()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopBrowserFamilyResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_browser_family(self, client: Cloudflare) -> None:
        with client.radar.http.top.with_streaming_response.browser_family() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopBrowserFamilyResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_browser(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.http.top.browser()
        assert_matches_type(TopBrowserResponse, top, path=["response"])

    @parametrize
    async def test_method_browser_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.http.top.browser(
            asn=["string"],
            bot_class=["LIKELY_AUTOMATED"],
            browser_family=["CHROME"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP"],
            format="JSON",
            http_protocol=["HTTP"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            os=["WINDOWS"],
            tls_version=["TLSv1_0"],
        )
        assert_matches_type(TopBrowserResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_browser(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.top.with_raw_response.browser()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopBrowserResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_browser(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.top.with_streaming_response.browser() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopBrowserResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_browser_family(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.http.top.browser_family()
        assert_matches_type(TopBrowserFamilyResponse, top, path=["response"])

    @parametrize
    async def test_method_browser_family_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.http.top.browser_family(
            asn=["string"],
            bot_class=["LIKELY_AUTOMATED"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP"],
            format="JSON",
            http_protocol=["HTTP"],
            http_version=["HTTPv1"],
            ip_version=["IPv4"],
            limit=5,
            location=["string"],
            name=["main_series"],
            os=["WINDOWS"],
            tls_version=["TLSv1_0"],
        )
        assert_matches_type(TopBrowserFamilyResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_browser_family(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.top.with_raw_response.browser_family()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopBrowserFamilyResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_browser_family(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.top.with_streaming_response.browser_family() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopBrowserFamilyResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True
