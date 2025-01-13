# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar import SearchGlobalResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_global(self, client: Cloudflare) -> None:
        search = client.radar.search.global_(
            query="United",
        )
        assert_matches_type(SearchGlobalResponse, search, path=["response"])

    @parametrize
    def test_method_global_with_all_params(self, client: Cloudflare) -> None:
        search = client.radar.search.global_(
            query="United",
            exclude=["SPECIAL_EVENTS"],
            format="JSON",
            include=["SPECIAL_EVENTS"],
            limit=5,
            limit_per_group=0,
        )
        assert_matches_type(SearchGlobalResponse, search, path=["response"])

    @parametrize
    def test_raw_response_global(self, client: Cloudflare) -> None:
        response = client.radar.search.with_raw_response.global_(
            query="United",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchGlobalResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_global(self, client: Cloudflare) -> None:
        with client.radar.search.with_streaming_response.global_(
            query="United",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchGlobalResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_global(self, async_client: AsyncCloudflare) -> None:
        search = await async_client.radar.search.global_(
            query="United",
        )
        assert_matches_type(SearchGlobalResponse, search, path=["response"])

    @parametrize
    async def test_method_global_with_all_params(self, async_client: AsyncCloudflare) -> None:
        search = await async_client.radar.search.global_(
            query="United",
            exclude=["SPECIAL_EVENTS"],
            format="JSON",
            include=["SPECIAL_EVENTS"],
            limit=5,
            limit_per_group=0,
        )
        assert_matches_type(SearchGlobalResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_global(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.search.with_raw_response.global_(
            query="United",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchGlobalResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_global(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.search.with_streaming_response.global_(
            query="United",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchGlobalResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
