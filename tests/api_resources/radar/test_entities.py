# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar import EntityGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        entity = client.radar.entities.get(
            ip="8.8.8.8",
        )
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        entity = client.radar.entities.get(
            ip="8.8.8.8",
            format="JSON",
        )
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.entities.with_raw_response.get(
            ip="8.8.8.8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.entities.with_streaming_response.get(
            ip="8.8.8.8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityGetResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        entity = await async_client.radar.entities.get(
            ip="8.8.8.8",
        )
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        entity = await async_client.radar.entities.get(
            ip="8.8.8.8",
            format="JSON",
        )
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.entities.with_raw_response.get(
            ip="8.8.8.8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = await response.parse()
        assert_matches_type(EntityGetResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.entities.with_streaming_response.get(
            ip="8.8.8.8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityGetResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True
