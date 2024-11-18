# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.rate_limits import (
    RateLimit,
    RateLimitDeleteResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRateLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={
                    "mode": "simulate",
                    "response": {
                        "body": "<error>This request has been rate-limited.</error>",
                        "content_type": "text/xml",
                    },
                    "timeout": 86400,
                },
                match={
                    "headers": [
                        {
                            "name": "Cf-Cache-Status",
                            "op": "eq",
                            "value": "HIT",
                        }
                    ],
                    "request": {
                        "methods": ["GET", "POST"],
                        "schemes": ["HTTP", "HTTPS"],
                        "url": "*.example.org/path*",
                    },
                    "response": {"origin_traffic": True},
                },
                period=900,
                threshold=60,
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(RateLimit, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.rate_limits.with_raw_response.create(
                    zone_id="",
                    action={},
                    match={},
                    period=900,
                    threshold=60,
                )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                page=1,
                per_page=1,
            )

        assert_matches_type(SyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(SyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.rate_limits.with_raw_response.list(
                    zone_id="",
                )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.delete(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.delete(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.delete(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.rate_limits.with_raw_response.delete(
                    rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rate_limit_id` but received ''"):
                client.rate_limits.with_raw_response.delete(
                    rate_limit_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.edit(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.edit(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={
                    "mode": "simulate",
                    "response": {
                        "body": "<error>This request has been rate-limited.</error>",
                        "content_type": "text/xml",
                    },
                    "timeout": 86400,
                },
                match={
                    "headers": [
                        {
                            "name": "Cf-Cache-Status",
                            "op": "eq",
                            "value": "HIT",
                        }
                    ],
                    "request": {
                        "methods": ["GET", "POST"],
                        "schemes": ["HTTP", "HTTPS"],
                        "url": "*.example.org/path*",
                    },
                    "response": {"origin_traffic": True},
                },
                period=900,
                threshold=60,
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.edit(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.edit(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(RateLimit, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.rate_limits.with_raw_response.edit(
                    rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_id="",
                    action={},
                    match={},
                    period=900,
                    threshold=60,
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rate_limit_id` but received ''"):
                client.rate_limits.with_raw_response.edit(
                    rate_limit_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                    action={},
                    match={},
                    period=900,
                    threshold=60,
                )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.get(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.get(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.get(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(RateLimit, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.rate_limits.with_raw_response.get(
                    rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rate_limit_id` but received ''"):
                client.rate_limits.with_raw_response.get(
                    rate_limit_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )


class TestAsyncRateLimits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={
                    "mode": "simulate",
                    "response": {
                        "body": "<error>This request has been rate-limited.</error>",
                        "content_type": "text/xml",
                    },
                    "timeout": 86400,
                },
                match={
                    "headers": [
                        {
                            "name": "Cf-Cache-Status",
                            "op": "eq",
                            "value": "HIT",
                        }
                    ],
                    "request": {
                        "methods": ["GET", "POST"],
                        "schemes": ["HTTP", "HTTPS"],
                        "url": "*.example.org/path*",
                    },
                    "response": {"origin_traffic": True},
                },
                period=900,
                threshold=60,
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(RateLimit, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.rate_limits.with_raw_response.create(
                    zone_id="",
                    action={},
                    match={},
                    period=900,
                    threshold=60,
                )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                page=1,
                per_page=1,
            )

        assert_matches_type(AsyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(AsyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.rate_limits.with_raw_response.list(
                    zone_id="",
                )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.delete(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.delete(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.delete(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.rate_limits.with_raw_response.delete(
                    rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rate_limit_id` but received ''"):
                await async_client.rate_limits.with_raw_response.delete(
                    rate_limit_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.edit(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.edit(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={
                    "mode": "simulate",
                    "response": {
                        "body": "<error>This request has been rate-limited.</error>",
                        "content_type": "text/xml",
                    },
                    "timeout": 86400,
                },
                match={
                    "headers": [
                        {
                            "name": "Cf-Cache-Status",
                            "op": "eq",
                            "value": "HIT",
                        }
                    ],
                    "request": {
                        "methods": ["GET", "POST"],
                        "schemes": ["HTTP", "HTTPS"],
                        "url": "*.example.org/path*",
                    },
                    "response": {"origin_traffic": True},
                },
                period=900,
                threshold=60,
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.edit(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.edit(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                match={},
                period=900,
                threshold=60,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(RateLimit, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.rate_limits.with_raw_response.edit(
                    rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_id="",
                    action={},
                    match={},
                    period=900,
                    threshold=60,
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rate_limit_id` but received ''"):
                await async_client.rate_limits.with_raw_response.edit(
                    rate_limit_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                    action={},
                    match={},
                    period=900,
                    threshold=60,
                )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.get(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.get(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(RateLimit, rate_limit, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.get(
                rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(RateLimit, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.rate_limits.with_raw_response.get(
                    rate_limit_id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rate_limit_id` but received ''"):
                await async_client.rate_limits.with_raw_response.get(
                    rate_limit_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )
