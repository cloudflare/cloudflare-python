# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date
from cloudflare.types.radar import AgentReadinessSummaryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgentReadiness:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary(self, client: Cloudflare) -> None:
        agent_readiness = client.radar.agent_readiness.summary(
            dimension="CHECK",
        )
        assert_matches_type(AgentReadinessSummaryResponse, agent_readiness, path=["response"])

    @parametrize
    def test_method_summary_with_all_params(self, client: Cloudflare) -> None:
        agent_readiness = client.radar.agent_readiness.summary(
            dimension="CHECK",
            date=parse_date("2024-09-19"),
            domain_category=["string"],
            format="JSON",
            name=["main_series"],
        )
        assert_matches_type(AgentReadinessSummaryResponse, agent_readiness, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Cloudflare) -> None:
        response = client.radar.agent_readiness.with_raw_response.summary(
            dimension="CHECK",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_readiness = response.parse()
        assert_matches_type(AgentReadinessSummaryResponse, agent_readiness, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Cloudflare) -> None:
        with client.radar.agent_readiness.with_streaming_response.summary(
            dimension="CHECK",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_readiness = response.parse()
            assert_matches_type(AgentReadinessSummaryResponse, agent_readiness, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgentReadiness:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_summary(self, async_client: AsyncCloudflare) -> None:
        agent_readiness = await async_client.radar.agent_readiness.summary(
            dimension="CHECK",
        )
        assert_matches_type(AgentReadinessSummaryResponse, agent_readiness, path=["response"])

    @parametrize
    async def test_method_summary_with_all_params(self, async_client: AsyncCloudflare) -> None:
        agent_readiness = await async_client.radar.agent_readiness.summary(
            dimension="CHECK",
            date=parse_date("2024-09-19"),
            domain_category=["string"],
            format="JSON",
            name=["main_series"],
        )
        assert_matches_type(AgentReadinessSummaryResponse, agent_readiness, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.agent_readiness.with_raw_response.summary(
            dimension="CHECK",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_readiness = await response.parse()
        assert_matches_type(AgentReadinessSummaryResponse, agent_readiness, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.agent_readiness.with_streaming_response.summary(
            dimension="CHECK",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_readiness = await response.parse()
            assert_matches_type(AgentReadinessSummaryResponse, agent_readiness, path=["response"])

        assert cast(Any, response.is_closed) is True
