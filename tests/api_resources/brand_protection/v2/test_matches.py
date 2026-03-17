# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.brand_protection.v2 import MatchGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        match = client.brand_protection.v2.matches.get(
            account_id="x",
            query_id="x",
        )
        assert_matches_type(MatchGetResponse, match, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        match = client.brand_protection.v2.matches.get(
            account_id="x",
            query_id="x",
            include_dismissed="include_dismissed",
            include_domain_id="include_domain_id",
            limit="limit",
            offset="offset",
            order="asc",
            order_by="domain",
        )
        assert_matches_type(MatchGetResponse, match, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.brand_protection.v2.matches.with_raw_response.get(
            account_id="x",
            query_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = response.parse()
        assert_matches_type(MatchGetResponse, match, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.brand_protection.v2.matches.with_streaming_response.get(
            account_id="x",
            query_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = response.parse()
            assert_matches_type(MatchGetResponse, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.brand_protection.v2.matches.with_raw_response.get(
                account_id="",
                query_id="x",
            )


class TestAsyncMatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        match = await async_client.brand_protection.v2.matches.get(
            account_id="x",
            query_id="x",
        )
        assert_matches_type(MatchGetResponse, match, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        match = await async_client.brand_protection.v2.matches.get(
            account_id="x",
            query_id="x",
            include_dismissed="include_dismissed",
            include_domain_id="include_domain_id",
            limit="limit",
            offset="offset",
            order="asc",
            order_by="domain",
        )
        assert_matches_type(MatchGetResponse, match, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.brand_protection.v2.matches.with_raw_response.get(
            account_id="x",
            query_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        match = await response.parse()
        assert_matches_type(MatchGetResponse, match, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.brand_protection.v2.matches.with_streaming_response.get(
            account_id="x",
            query_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            match = await response.parse()
            assert_matches_type(MatchGetResponse, match, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.brand_protection.v2.matches.with_raw_response.get(
                account_id="",
                query_id="x",
            )
