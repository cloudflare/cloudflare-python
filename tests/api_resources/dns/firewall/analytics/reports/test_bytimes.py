# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.dns.analytics.reports import ByTime

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dns.firewall.analytics.reports import bytime_get_params
from cloudflare.types.dns.firewall import Delta
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBytimes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bytime = client.dns.firewall.analytics.reports.bytimes.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ByTime], bytime, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        bytime = client.dns.firewall.analytics.reports.bytimes.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dimensions="queryType",
            filters="responseCode==NOERROR,queryType==A",
            limit=100,
            metrics="queryCount,uncachedCount",
            since=parse_datetime("2023-11-11T12:00:00Z"),
            sort="+responseCode,-queryName",
            time_delta="all",
            until=parse_datetime("2023-11-11T13:00:00Z"),
        )
        assert_matches_type(Optional[ByTime], bytime, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns.firewall.analytics.reports.bytimes.with_raw_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bytime = response.parse()
        assert_matches_type(Optional[ByTime], bytime, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns.firewall.analytics.reports.bytimes.with_streaming_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bytime = response.parse()
            assert_matches_type(Optional[ByTime], bytime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns.firewall.analytics.reports.bytimes.with_raw_response.get(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            client.dns.firewall.analytics.reports.bytimes.with_raw_response.get(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncBytimes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bytime = await async_client.dns.firewall.analytics.reports.bytimes.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ByTime], bytime, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bytime = await async_client.dns.firewall.analytics.reports.bytimes.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dimensions="queryType",
            filters="responseCode==NOERROR,queryType==A",
            limit=100,
            metrics="queryCount,uncachedCount",
            since=parse_datetime("2023-11-11T12:00:00Z"),
            sort="+responseCode,-queryName",
            time_delta="all",
            until=parse_datetime("2023-11-11T13:00:00Z"),
        )
        assert_matches_type(Optional[ByTime], bytime, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.firewall.analytics.reports.bytimes.with_raw_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bytime = await response.parse()
        assert_matches_type(Optional[ByTime], bytime, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.firewall.analytics.reports.bytimes.with_streaming_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bytime = await response.parse()
            assert_matches_type(Optional[ByTime], bytime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns.firewall.analytics.reports.bytimes.with_raw_response.get(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            await async_client.dns.firewall.analytics.reports.bytimes.with_raw_response.get(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
