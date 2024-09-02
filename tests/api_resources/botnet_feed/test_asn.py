# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.botnet_feed import ASNDayReportResponse, ASNFullReportResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.botnet_feed import asn_day_report_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestASN:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_day_report(self, client: Cloudflare) -> None:
        asn = client.botnet_feed.asn.day_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ASNDayReportResponse], asn, path=["response"])

    @parametrize
    def test_method_day_report_with_all_params(self, client: Cloudflare) -> None:
        asn = client.botnet_feed.asn.day_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            date=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(Optional[ASNDayReportResponse], asn, path=["response"])

    @parametrize
    def test_raw_response_day_report(self, client: Cloudflare) -> None:
        response = client.botnet_feed.asn.with_raw_response.day_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = response.parse()
        assert_matches_type(Optional[ASNDayReportResponse], asn, path=["response"])

    @parametrize
    def test_streaming_response_day_report(self, client: Cloudflare) -> None:
        with client.botnet_feed.asn.with_streaming_response.day_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = response.parse()
            assert_matches_type(Optional[ASNDayReportResponse], asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_day_report(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.botnet_feed.asn.with_raw_response.day_report(
                asn_id=0,
                account_id="",
            )

    @parametrize
    def test_method_full_report(self, client: Cloudflare) -> None:
        asn = client.botnet_feed.asn.full_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ASNFullReportResponse], asn, path=["response"])

    @parametrize
    def test_raw_response_full_report(self, client: Cloudflare) -> None:
        response = client.botnet_feed.asn.with_raw_response.full_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = response.parse()
        assert_matches_type(Optional[ASNFullReportResponse], asn, path=["response"])

    @parametrize
    def test_streaming_response_full_report(self, client: Cloudflare) -> None:
        with client.botnet_feed.asn.with_streaming_response.full_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = response.parse()
            assert_matches_type(Optional[ASNFullReportResponse], asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_full_report(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.botnet_feed.asn.with_raw_response.full_report(
                asn_id=0,
                account_id="",
            )


class TestAsyncASN:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_day_report(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.botnet_feed.asn.day_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ASNDayReportResponse], asn, path=["response"])

    @parametrize
    async def test_method_day_report_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.botnet_feed.asn.day_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            date=parse_datetime("2014-01-01T05:20:00.12345Z"),
        )
        assert_matches_type(Optional[ASNDayReportResponse], asn, path=["response"])

    @parametrize
    async def test_raw_response_day_report(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.botnet_feed.asn.with_raw_response.day_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = await response.parse()
        assert_matches_type(Optional[ASNDayReportResponse], asn, path=["response"])

    @parametrize
    async def test_streaming_response_day_report(self, async_client: AsyncCloudflare) -> None:
        async with async_client.botnet_feed.asn.with_streaming_response.day_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = await response.parse()
            assert_matches_type(Optional[ASNDayReportResponse], asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_day_report(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.botnet_feed.asn.with_raw_response.day_report(
                asn_id=0,
                account_id="",
            )

    @parametrize
    async def test_method_full_report(self, async_client: AsyncCloudflare) -> None:
        asn = await async_client.botnet_feed.asn.full_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ASNFullReportResponse], asn, path=["response"])

    @parametrize
    async def test_raw_response_full_report(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.botnet_feed.asn.with_raw_response.full_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asn = await response.parse()
        assert_matches_type(Optional[ASNFullReportResponse], asn, path=["response"])

    @parametrize
    async def test_streaming_response_full_report(self, async_client: AsyncCloudflare) -> None:
        async with async_client.botnet_feed.asn.with_streaming_response.full_report(
            asn_id=0,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asn = await response.parse()
            assert_matches_type(Optional[ASNFullReportResponse], asn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_full_report(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.botnet_feed.asn.with_raw_response.full_report(
                asn_id=0,
                account_id="",
            )
