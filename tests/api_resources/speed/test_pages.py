# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.speed import Trend, PageListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        page = client.speed.pages.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[PageListResponse], page, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.speed.pages.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(SyncSinglePage[PageListResponse], page, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.speed.pages.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(SyncSinglePage[PageListResponse], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.pages.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_trend(self, client: Cloudflare) -> None:
        page = client.speed.pages.trend(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="asia-east1",
            start=parse_datetime("2014-01-01T05:20:00.12345Z"),
            tz="tz",
        )
        assert_matches_type(Optional[Trend], page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_trend_with_all_params(self, client: Cloudflare) -> None:
        page = client.speed.pages.trend(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="asia-east1",
            start=parse_datetime("2014-01-01T05:20:00.12345Z"),
            tz="tz",
            end=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(Optional[Trend], page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_trend(self, client: Cloudflare) -> None:
        response = client.speed.pages.with_raw_response.trend(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="asia-east1",
            start=parse_datetime("2014-01-01T05:20:00.12345Z"),
            tz="tz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = response.parse()
        assert_matches_type(Optional[Trend], page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_trend(self, client: Cloudflare) -> None:
        with client.speed.pages.with_streaming_response.trend(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="asia-east1",
            start=parse_datetime("2014-01-01T05:20:00.12345Z"),
            tz="tz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = response.parse()
            assert_matches_type(Optional[Trend], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_trend(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.pages.with_raw_response.trend(
                url="example.com",
                zone_id="",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="asia-east1",
                start=parse_datetime("2014-01-01T05:20:00.12345Z"),
                tz="tz",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.pages.with_raw_response.trend(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="asia-east1",
                start=parse_datetime("2014-01-01T05:20:00.12345Z"),
                tz="tz",
            )


class TestAsyncPages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        page = await async_client.speed.pages.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[PageListResponse], page, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.pages.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(AsyncSinglePage[PageListResponse], page, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.pages.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(AsyncSinglePage[PageListResponse], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.pages.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_trend(self, async_client: AsyncCloudflare) -> None:
        page = await async_client.speed.pages.trend(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="asia-east1",
            start=parse_datetime("2014-01-01T05:20:00.12345Z"),
            tz="tz",
        )
        assert_matches_type(Optional[Trend], page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_trend_with_all_params(self, async_client: AsyncCloudflare) -> None:
        page = await async_client.speed.pages.trend(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="asia-east1",
            start=parse_datetime("2014-01-01T05:20:00.12345Z"),
            tz="tz",
            end=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(Optional[Trend], page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_trend(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.pages.with_raw_response.trend(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="asia-east1",
            start=parse_datetime("2014-01-01T05:20:00.12345Z"),
            tz="tz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        page = await response.parse()
        assert_matches_type(Optional[Trend], page, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_trend(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.pages.with_streaming_response.trend(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="asia-east1",
            start=parse_datetime("2014-01-01T05:20:00.12345Z"),
            tz="tz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            page = await response.parse()
            assert_matches_type(Optional[Trend], page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_trend(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.pages.with_raw_response.trend(
                url="example.com",
                zone_id="",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="asia-east1",
                start=parse_datetime("2014-01-01T05:20:00.12345Z"),
                tz="tz",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.pages.with_raw_response.trend(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="asia-east1",
                start=parse_datetime("2014-01-01T05:20:00.12345Z"),
                tz="tz",
            )
