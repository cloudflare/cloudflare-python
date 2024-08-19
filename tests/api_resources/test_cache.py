# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cache import CachePurgeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCache:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_purge_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_1(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
            tags=["a-cache-tag", "another-cache-tag"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_1(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_1(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_2(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_2(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_2(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_3(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
            prefixes=["www.example.com/foo", "images.example.com/bar/baz"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_3(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_3(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_4(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
            purge_everything=True,
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_4(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_4(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_5(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
            files=["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_5(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_5(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    def test_method_purge_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_method_purge_with_all_params_overload_6(self, client: Cloudflare) -> None:
        cache = client.cache.purge(
            zone_id="zone_id",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "http://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "EU",
                    },
                    "url": "http://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_raw_response_purge_overload_6(self, client: Cloudflare) -> None:
        response = client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    def test_streaming_response_purge_overload_6(self, client: Cloudflare) -> None:
        with client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.with_raw_response.purge(
                zone_id="",
            )


class TestAsyncCache:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
            tags=["a-cache-tag", "another-cache-tag"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
            hosts=["www.example.com", "images.example.com"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
            prefixes=["www.example.com/foo", "images.example.com/bar/baz"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_4(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
            purge_everything=True,
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_5(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
            files=["http://www.example.com/css/styles.css", "http://www.example.com/js/index.js"],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )

    @parametrize
    async def test_method_purge_overload_6(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_method_purge_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        cache = await async_client.cache.purge(
            zone_id="zone_id",
            files=[
                {
                    "headers": {
                        "Accept-Language": "zh-CN",
                        "CF-Device-Type": "desktop",
                        "CF-IPCountry": "US",
                    },
                    "url": "http://www.example.com/cat_picture.jpg",
                },
                {
                    "headers": {
                        "Accept-Language": "en-US",
                        "CF-Device-Type": "mobile",
                        "CF-IPCountry": "EU",
                    },
                    "url": "http://www.example.com/dog_picture.jpg",
                },
            ],
        )
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_raw_response_purge_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.with_raw_response.purge(
            zone_id="zone_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

    @parametrize
    async def test_streaming_response_purge_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.with_streaming_response.purge(
            zone_id="zone_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(Optional[CachePurgeResponse], cache, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.with_raw_response.purge(
                zone_id="",
            )
