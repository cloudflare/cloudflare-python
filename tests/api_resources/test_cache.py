# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import CachePurgeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCache:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_purge(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="string",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_purge_with_all_params(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="string",
            files=[
                "http://www.example.com/css/styles.css",
                "http://www.example.com/css/styles.css",
                "http://www.example.com/css/styles.css",
            ],
            hosts=["www.example.com", "images.example.com"],
            prefixes=["www.example.com/foo", "images.example.com/bar/baz"],
            purge_everything=True,
            tags=["some-tag", "another-tag"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_purge(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_purge(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_purge(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )


class TestAsyncCache:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_purge(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="string",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_purge_with_all_params(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="string",
            files=[
                "http://www.example.com/css/styles.css",
                "http://www.example.com/css/styles.css",
                "http://www.example.com/css/styles.css",
            ],
            hosts=["www.example.com", "images.example.com"],
            prefixes=["www.example.com/foo", "images.example.com/bar/baz"],
            purge_everything=True,
            tags=["some-tag", "another-tag"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_purge(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_purge(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_purge(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )
