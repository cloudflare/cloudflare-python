# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date
from cloudflare.types.radar.robots_txt import TopDomainCategoriesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_domain_categories(self, client: Cloudflare) -> None:
        top = client.radar.robots_txt.top.domain_categories()
        assert_matches_type(TopDomainCategoriesResponse, top, path=["response"])

    @parametrize
    def test_method_domain_categories_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.robots_txt.top.domain_categories(
            date=[parse_date("2019-12-27")],
            format="JSON",
            limit=5,
            name=["main_series"],
            user_agent_category="AI",
        )
        assert_matches_type(TopDomainCategoriesResponse, top, path=["response"])

    @parametrize
    def test_raw_response_domain_categories(self, client: Cloudflare) -> None:
        response = client.radar.robots_txt.top.with_raw_response.domain_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopDomainCategoriesResponse, top, path=["response"])

    @parametrize
    def test_streaming_response_domain_categories(self, client: Cloudflare) -> None:
        with client.radar.robots_txt.top.with_streaming_response.domain_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopDomainCategoriesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_domain_categories(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.robots_txt.top.domain_categories()
        assert_matches_type(TopDomainCategoriesResponse, top, path=["response"])

    @parametrize
    async def test_method_domain_categories_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.robots_txt.top.domain_categories(
            date=[parse_date("2019-12-27")],
            format="JSON",
            limit=5,
            name=["main_series"],
            user_agent_category="AI",
        )
        assert_matches_type(TopDomainCategoriesResponse, top, path=["response"])

    @parametrize
    async def test_raw_response_domain_categories(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.robots_txt.top.with_raw_response.domain_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopDomainCategoriesResponse, top, path=["response"])

    @parametrize
    async def test_streaming_response_domain_categories(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.robots_txt.top.with_streaming_response.domain_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopDomainCategoriesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True
