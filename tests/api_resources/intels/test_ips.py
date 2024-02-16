# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.intels import IPIPIntelligenceGetIPOverviewResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_intelligence_get_ip_overview(self, client: Cloudflare) -> None:
        ip = client.intels.ips.ip_intelligence_get_ip_overview(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IPIPIntelligenceGetIPOverviewResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_intelligence_get_ip_overview_with_all_params(self, client: Cloudflare) -> None:
        ip = client.intels.ips.ip_intelligence_get_ip_overview(
            "023e105f4ecef8ad9ca31a8372d0c353",
            ipv4="string",
            ipv6="string",
        )
        assert_matches_type(Optional[IPIPIntelligenceGetIPOverviewResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_intelligence_get_ip_overview(self, client: Cloudflare) -> None:
        response = client.intels.ips.with_raw_response.ip_intelligence_get_ip_overview(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = response.parse()
        assert_matches_type(Optional[IPIPIntelligenceGetIPOverviewResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_intelligence_get_ip_overview(self, client: Cloudflare) -> None:
        with client.intels.ips.with_streaming_response.ip_intelligence_get_ip_overview(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = response.parse()
            assert_matches_type(Optional[IPIPIntelligenceGetIPOverviewResponse], ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_ip_intelligence_get_ip_overview(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intels.ips.with_raw_response.ip_intelligence_get_ip_overview(
                "",
            )


class TestAsyncIPs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_intelligence_get_ip_overview(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.intels.ips.ip_intelligence_get_ip_overview(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IPIPIntelligenceGetIPOverviewResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_intelligence_get_ip_overview_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.intels.ips.ip_intelligence_get_ip_overview(
            "023e105f4ecef8ad9ca31a8372d0c353",
            ipv4="string",
            ipv6="string",
        )
        assert_matches_type(Optional[IPIPIntelligenceGetIPOverviewResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_intelligence_get_ip_overview(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intels.ips.with_raw_response.ip_intelligence_get_ip_overview(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = await response.parse()
        assert_matches_type(Optional[IPIPIntelligenceGetIPOverviewResponse], ip, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_intelligence_get_ip_overview(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intels.ips.with_streaming_response.ip_intelligence_get_ip_overview(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = await response.parse()
            assert_matches_type(Optional[IPIPIntelligenceGetIPOverviewResponse], ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_ip_intelligence_get_ip_overview(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intels.ips.with_raw_response.ip_intelligence_get_ip_overview(
                "",
            )
