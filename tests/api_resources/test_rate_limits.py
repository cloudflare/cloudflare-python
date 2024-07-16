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
    RateLimitGetResponse,
    RateLimitEditResponse,
    RateLimitCreateResponse,
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
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(RateLimitCreateResponse, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(RateLimitCreateResponse, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(RateLimitCreateResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.rate_limits.with_raw_response.create(
                    zone_identifier="",
                    body={},
                )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                page=1,
                per_page=1,
            )

        assert_matches_type(SyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(SyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.rate_limits.with_raw_response.list(
                    zone_identifier="",
                )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.delete(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.rate_limits.with_raw_response.delete(
                    id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_identifier="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                client.rate_limits.with_raw_response.delete(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.edit(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(RateLimitEditResponse, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.edit(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(RateLimitEditResponse, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.edit(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(RateLimitEditResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.rate_limits.with_raw_response.edit(
                    id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_identifier="",
                    body={},
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                client.rate_limits.with_raw_response.edit(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                    body={},
                )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = client.rate_limits.get(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(RateLimitGetResponse, rate_limit, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.rate_limits.with_raw_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(RateLimitGetResponse, rate_limit, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.rate_limits.with_streaming_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = response.parse()
                assert_matches_type(RateLimitGetResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                client.rate_limits.with_raw_response.get(
                    id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_identifier="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                client.rate_limits.with_raw_response.get(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                )


class TestAsyncRateLimits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(RateLimitCreateResponse, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(RateLimitCreateResponse, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(RateLimitCreateResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.rate_limits.with_raw_response.create(
                    zone_identifier="",
                    body={},
                )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                page=1,
                per_page=1,
            )

        assert_matches_type(AsyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(AsyncV4PagePaginationArray[RateLimit], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.rate_limits.with_raw_response.list(
                    zone_identifier="",
                )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.delete(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(RateLimitDeleteResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.rate_limits.with_raw_response.delete(
                    id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_identifier="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                await async_client.rate_limits.with_raw_response.delete(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.edit(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(RateLimitEditResponse, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.edit(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(RateLimitEditResponse, rate_limit, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.edit(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(RateLimitEditResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.rate_limits.with_raw_response.edit(
                    id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_identifier="",
                    body={},
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                await async_client.rate_limits.with_raw_response.edit(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                    body={},
                )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rate_limit = await async_client.rate_limits.get(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(RateLimitGetResponse, rate_limit, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.rate_limits.with_raw_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(RateLimitGetResponse, rate_limit, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.rate_limits.with_streaming_response.get(
                id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rate_limit = await response.parse()
                assert_matches_type(RateLimitGetResponse, rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
                await async_client.rate_limits.with_raw_response.get(
                    id="372e67954025e0ba6aaa6d586b9e0b59",
                    zone_identifier="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
                await async_client.rate_limits.with_raw_response.get(
                    id="",
                    zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                )
