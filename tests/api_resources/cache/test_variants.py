# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cache import VariantGetResponse, VariantEditResponse, VariantDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVariants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        variant = client.cache.variants.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VariantDeleteResponse], variant, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cache.variants.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(Optional[VariantDeleteResponse], variant, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cache.variants.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(Optional[VariantDeleteResponse], variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.variants.with_raw_response.delete(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        variant = client.cache.variants.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        )
        assert_matches_type(Optional[VariantEditResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        variant = client.cache.variants.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "avif": ["image/webp", "image/jpeg"],
                "bmp": ["image/webp", "image/jpeg"],
                "gif": ["image/webp", "image/jpeg"],
                "jp2": ["image/webp", "image/avif"],
                "jpeg": ["image/webp", "image/avif"],
                "jpg": ["image/webp", "image/avif"],
                "jpg2": ["image/webp", "image/avif"],
                "png": ["image/webp", "image/avif"],
                "tif": ["image/webp", "image/avif"],
                "tiff": ["image/webp", "image/avif"],
                "webp": ["image/jpeg", "image/avif"],
            },
        )
        assert_matches_type(Optional[VariantEditResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cache.variants.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(Optional[VariantEditResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cache.variants.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(Optional[VariantEditResponse], variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.variants.with_raw_response.edit(
                zone_id="",
                value={},
            )

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        variant = client.cache.variants.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VariantGetResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cache.variants.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(Optional[VariantGetResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cache.variants.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(Optional[VariantGetResponse], variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.variants.with_raw_response.get(
                zone_id="",
            )


class TestAsyncVariants:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.cache.variants.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VariantDeleteResponse], variant, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.variants.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(Optional[VariantDeleteResponse], variant, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.variants.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(Optional[VariantDeleteResponse], variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.variants.with_raw_response.delete(
                zone_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.cache.variants.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        )
        assert_matches_type(Optional[VariantEditResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.cache.variants.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "avif": ["image/webp", "image/jpeg"],
                "bmp": ["image/webp", "image/jpeg"],
                "gif": ["image/webp", "image/jpeg"],
                "jp2": ["image/webp", "image/avif"],
                "jpeg": ["image/webp", "image/avif"],
                "jpg": ["image/webp", "image/avif"],
                "jpg2": ["image/webp", "image/avif"],
                "png": ["image/webp", "image/avif"],
                "tif": ["image/webp", "image/avif"],
                "tiff": ["image/webp", "image/avif"],
                "webp": ["image/jpeg", "image/avif"],
            },
        )
        assert_matches_type(Optional[VariantEditResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.variants.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(Optional[VariantEditResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.variants.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(Optional[VariantEditResponse], variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.variants.with_raw_response.edit(
                zone_id="",
                value={},
            )

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.cache.variants.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[VariantGetResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.variants.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(Optional[VariantGetResponse], variant, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.variants.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(Optional[VariantGetResponse], variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.variants.with_raw_response.get(
                zone_id="",
            )
