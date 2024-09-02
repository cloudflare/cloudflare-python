# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar import RobotsTXTDomainsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar import robots_txt_domains_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRobotsTXT:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_domains(self, client: Cloudflare) -> None:
        robots_txt = client.radar.robots_txt.domains()
        assert_matches_type(RobotsTXTDomainsResponse, robots_txt, path=["response"])

    @parametrize
    def test_method_domains_with_all_params(self, client: Cloudflare) -> None:
        robots_txt = client.radar.robots_txt.domains(
            domain_category="domainCategory",
            domain_name="domainName",
            format="JSON",
            limit=5,
            offset=0,
        )
        assert_matches_type(RobotsTXTDomainsResponse, robots_txt, path=["response"])

    @parametrize
    def test_raw_response_domains(self, client: Cloudflare) -> None:
        response = client.radar.robots_txt.with_raw_response.domains()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        robots_txt = response.parse()
        assert_matches_type(RobotsTXTDomainsResponse, robots_txt, path=["response"])

    @parametrize
    def test_streaming_response_domains(self, client: Cloudflare) -> None:
        with client.radar.robots_txt.with_streaming_response.domains() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            robots_txt = response.parse()
            assert_matches_type(RobotsTXTDomainsResponse, robots_txt, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRobotsTXT:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_domains(self, async_client: AsyncCloudflare) -> None:
        robots_txt = await async_client.radar.robots_txt.domains()
        assert_matches_type(RobotsTXTDomainsResponse, robots_txt, path=["response"])

    @parametrize
    async def test_method_domains_with_all_params(self, async_client: AsyncCloudflare) -> None:
        robots_txt = await async_client.radar.robots_txt.domains(
            domain_category="domainCategory",
            domain_name="domainName",
            format="JSON",
            limit=5,
            offset=0,
        )
        assert_matches_type(RobotsTXTDomainsResponse, robots_txt, path=["response"])

    @parametrize
    async def test_raw_response_domains(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.robots_txt.with_raw_response.domains()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        robots_txt = await response.parse()
        assert_matches_type(RobotsTXTDomainsResponse, robots_txt, path=["response"])

    @parametrize
    async def test_streaming_response_domains(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.robots_txt.with_streaming_response.domains() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            robots_txt = await response.parse()
            assert_matches_type(RobotsTXTDomainsResponse, robots_txt, path=["response"])

        assert cast(Any, response.is_closed) is True
