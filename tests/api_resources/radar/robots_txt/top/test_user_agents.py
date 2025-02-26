# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date
from cloudflare.types.radar.robots_txt.top import UserAgentDirectiveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_directive(self, client: Cloudflare) -> None:
        user_agent = client.radar.robots_txt.top.user_agents.directive()
        assert_matches_type(UserAgentDirectiveResponse, user_agent, path=["response"])

    @parametrize
    def test_method_directive_with_all_params(self, client: Cloudflare) -> None:
        user_agent = client.radar.robots_txt.top.user_agents.directive(
            date=[parse_date("2019-12-27")],
            directive="ALLOW",
            domain_category=["string"],
            format="JSON",
            limit=5,
            name=["main_series"],
            user_agent_category="AI",
        )
        assert_matches_type(UserAgentDirectiveResponse, user_agent, path=["response"])

    @parametrize
    def test_raw_response_directive(self, client: Cloudflare) -> None:
        response = client.radar.robots_txt.top.user_agents.with_raw_response.directive()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_agent = response.parse()
        assert_matches_type(UserAgentDirectiveResponse, user_agent, path=["response"])

    @parametrize
    def test_streaming_response_directive(self, client: Cloudflare) -> None:
        with client.radar.robots_txt.top.user_agents.with_streaming_response.directive() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_agent = response.parse()
            assert_matches_type(UserAgentDirectiveResponse, user_agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUserAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_directive(self, async_client: AsyncCloudflare) -> None:
        user_agent = await async_client.radar.robots_txt.top.user_agents.directive()
        assert_matches_type(UserAgentDirectiveResponse, user_agent, path=["response"])

    @parametrize
    async def test_method_directive_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_agent = await async_client.radar.robots_txt.top.user_agents.directive(
            date=[parse_date("2019-12-27")],
            directive="ALLOW",
            domain_category=["string"],
            format="JSON",
            limit=5,
            name=["main_series"],
            user_agent_category="AI",
        )
        assert_matches_type(UserAgentDirectiveResponse, user_agent, path=["response"])

    @parametrize
    async def test_raw_response_directive(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.robots_txt.top.user_agents.with_raw_response.directive()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_agent = await response.parse()
        assert_matches_type(UserAgentDirectiveResponse, user_agent, path=["response"])

    @parametrize
    async def test_streaming_response_directive(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.robots_txt.top.user_agents.with_streaming_response.directive() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_agent = await response.parse()
            assert_matches_type(UserAgentDirectiveResponse, user_agent, path=["response"])

        assert cast(Any, response.is_closed) is True
