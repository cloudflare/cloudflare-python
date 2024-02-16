# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import PurgeCachZonePurgeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurgeCaches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_purge_overload_1(self, client: Cloudflare) -> None:
        purge_cach = client.purge_caches.zone_purge(
            "string",
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_purge_with_all_params_overload_1(self, client: Cloudflare) -> None:
        purge_cach = client.purge_caches.zone_purge(
            "string",
            hosts=["www.example.com", "images.example.com"],
            prefixes=["www.example.com/foo", "images.example.com/bar/baz"],
            tags=["some-tag", "another-tag"],
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_purge_overload_1(self, client: Cloudflare) -> None:
        response = client.purge_caches.with_raw_response.zone_purge(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge_cach = response.parse()
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_purge_overload_1(self, client: Cloudflare) -> None:
        with client.purge_caches.with_streaming_response.zone_purge(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge_cach = response.parse()
            assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_purge_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.purge_caches.with_raw_response.zone_purge(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_purge_overload_2(self, client: Cloudflare) -> None:
        purge_cach = client.purge_caches.zone_purge(
            "string",
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_purge_with_all_params_overload_2(self, client: Cloudflare) -> None:
        purge_cach = client.purge_caches.zone_purge(
            "string",
            purge_everything=True,
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_purge_overload_2(self, client: Cloudflare) -> None:
        response = client.purge_caches.with_raw_response.zone_purge(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge_cach = response.parse()
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_purge_overload_2(self, client: Cloudflare) -> None:
        with client.purge_caches.with_streaming_response.zone_purge(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge_cach = response.parse()
            assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_purge_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.purge_caches.with_raw_response.zone_purge(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_purge_overload_3(self, client: Cloudflare) -> None:
        purge_cach = client.purge_caches.zone_purge(
            "string",
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_purge_with_all_params_overload_3(self, client: Cloudflare) -> None:
        purge_cach = client.purge_caches.zone_purge(
            "string",
            files=[
                "http://www.example.com/css/styles.css",
                "http://www.example.com/css/styles.css",
                "http://www.example.com/css/styles.css",
            ],
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_purge_overload_3(self, client: Cloudflare) -> None:
        response = client.purge_caches.with_raw_response.zone_purge(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge_cach = response.parse()
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_purge_overload_3(self, client: Cloudflare) -> None:
        with client.purge_caches.with_streaming_response.zone_purge(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge_cach = response.parse()
            assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_purge_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.purge_caches.with_raw_response.zone_purge(
                "",
            )


class TestAsyncPurgeCaches:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        purge_cach = await async_client.purge_caches.zone_purge(
            "string",
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_purge_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        purge_cach = await async_client.purge_caches.zone_purge(
            "string",
            hosts=["www.example.com", "images.example.com"],
            prefixes=["www.example.com/foo", "images.example.com/bar/baz"],
            tags=["some-tag", "another-tag"],
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.purge_caches.with_raw_response.zone_purge(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge_cach = await response.parse()
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.purge_caches.with_streaming_response.zone_purge(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge_cach = await response.parse()
            assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_purge_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.purge_caches.with_raw_response.zone_purge(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        purge_cach = await async_client.purge_caches.zone_purge(
            "string",
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_purge_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        purge_cach = await async_client.purge_caches.zone_purge(
            "string",
            purge_everything=True,
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.purge_caches.with_raw_response.zone_purge(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge_cach = await response.parse()
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.purge_caches.with_streaming_response.zone_purge(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge_cach = await response.parse()
            assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_purge_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.purge_caches.with_raw_response.zone_purge(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        purge_cach = await async_client.purge_caches.zone_purge(
            "string",
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_purge_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        purge_cach = await async_client.purge_caches.zone_purge(
            "string",
            files=[
                "http://www.example.com/css/styles.css",
                "http://www.example.com/css/styles.css",
                "http://www.example.com/css/styles.css",
            ],
        )
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.purge_caches.with_raw_response.zone_purge(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge_cach = await response.parse()
        assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.purge_caches.with_streaming_response.zone_purge(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge_cach = await response.parse()
            assert_matches_type(Optional[PurgeCachZonePurgeResponse], purge_cach, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_purge_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.purge_caches.with_raw_response.zone_purge(
                "",
            )
