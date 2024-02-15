# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.images.v1s import (
    VariantGetResponse,
    VariantDeleteResponse,
    VariantUpdateResponse,
    VariantCloudflareImagesVariantsListVariantsResponse,
    VariantCloudflareImagesVariantsCreateAVariantResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVariants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        variant = client.images.v1s.variants.update(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )
        assert_matches_type(VariantUpdateResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        variant = client.images.v1s.variants.update(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
            never_require_signed_urls=True,
        )
        assert_matches_type(VariantUpdateResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.images.v1s.variants.with_raw_response.update(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(VariantUpdateResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.images.v1s.variants.with_streaming_response.update(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(VariantUpdateResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.variants.with_raw_response.update(
                "hero",
                account_id="",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        variant = client.images.v1s.variants.delete(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.images.v1s.variants.with_raw_response.delete(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.images.v1s.variants.with_streaming_response.delete(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(VariantDeleteResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.variants.with_raw_response.delete(
                "hero",
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_variants_create_a_variant(self, client: Cloudflare) -> None:
        variant = client.images.v1s.variants.cloudflare_images_variants_create_a_variant(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="hero",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )
        assert_matches_type(VariantCloudflareImagesVariantsCreateAVariantResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_variants_create_a_variant_with_all_params(self, client: Cloudflare) -> None:
        variant = client.images.v1s.variants.cloudflare_images_variants_create_a_variant(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="hero",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
            never_require_signed_urls=True,
        )
        assert_matches_type(VariantCloudflareImagesVariantsCreateAVariantResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_images_variants_create_a_variant(self, client: Cloudflare) -> None:
        response = client.images.v1s.variants.with_raw_response.cloudflare_images_variants_create_a_variant(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="hero",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(VariantCloudflareImagesVariantsCreateAVariantResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_images_variants_create_a_variant(self, client: Cloudflare) -> None:
        with client.images.v1s.variants.with_streaming_response.cloudflare_images_variants_create_a_variant(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="hero",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(VariantCloudflareImagesVariantsCreateAVariantResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_images_variants_create_a_variant(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.variants.with_raw_response.cloudflare_images_variants_create_a_variant(
                "",
                id="hero",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_variants_list_variants(self, client: Cloudflare) -> None:
        variant = client.images.v1s.variants.cloudflare_images_variants_list_variants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantCloudflareImagesVariantsListVariantsResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_images_variants_list_variants(self, client: Cloudflare) -> None:
        response = client.images.v1s.variants.with_raw_response.cloudflare_images_variants_list_variants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(VariantCloudflareImagesVariantsListVariantsResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_images_variants_list_variants(self, client: Cloudflare) -> None:
        with client.images.v1s.variants.with_streaming_response.cloudflare_images_variants_list_variants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(VariantCloudflareImagesVariantsListVariantsResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_images_variants_list_variants(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.variants.with_raw_response.cloudflare_images_variants_list_variants(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        variant = client.images.v1s.variants.get(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantGetResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.images.v1s.variants.with_raw_response.get(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(VariantGetResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.images.v1s.variants.with_streaming_response.get(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(VariantGetResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.variants.with_raw_response.get(
                "hero",
                account_id="",
            )


class TestAsyncVariants:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1s.variants.update(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )
        assert_matches_type(VariantUpdateResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1s.variants.update(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
            never_require_signed_urls=True,
        )
        assert_matches_type(VariantUpdateResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1s.variants.with_raw_response.update(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(VariantUpdateResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1s.variants.with_streaming_response.update(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(VariantUpdateResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.variants.with_raw_response.update(
                "hero",
                account_id="",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1s.variants.delete(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1s.variants.with_raw_response.delete(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1s.variants.with_streaming_response.delete(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(VariantDeleteResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.variants.with_raw_response.delete(
                "hero",
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_variants_create_a_variant(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1s.variants.cloudflare_images_variants_create_a_variant(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="hero",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )
        assert_matches_type(VariantCloudflareImagesVariantsCreateAVariantResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_variants_create_a_variant_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        variant = await async_client.images.v1s.variants.cloudflare_images_variants_create_a_variant(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="hero",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
            never_require_signed_urls=True,
        )
        assert_matches_type(VariantCloudflareImagesVariantsCreateAVariantResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_images_variants_create_a_variant(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.images.v1s.variants.with_raw_response.cloudflare_images_variants_create_a_variant(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="hero",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(VariantCloudflareImagesVariantsCreateAVariantResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_images_variants_create_a_variant(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.images.v1s.variants.with_streaming_response.cloudflare_images_variants_create_a_variant(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="hero",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(VariantCloudflareImagesVariantsCreateAVariantResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_images_variants_create_a_variant(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.variants.with_raw_response.cloudflare_images_variants_create_a_variant(
                "",
                id="hero",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_variants_list_variants(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1s.variants.cloudflare_images_variants_list_variants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantCloudflareImagesVariantsListVariantsResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_images_variants_list_variants(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1s.variants.with_raw_response.cloudflare_images_variants_list_variants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(VariantCloudflareImagesVariantsListVariantsResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_images_variants_list_variants(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.images.v1s.variants.with_streaming_response.cloudflare_images_variants_list_variants(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(VariantCloudflareImagesVariantsListVariantsResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_images_variants_list_variants(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.variants.with_raw_response.cloudflare_images_variants_list_variants(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1s.variants.get(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(VariantGetResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1s.variants.with_raw_response.get(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(VariantGetResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1s.variants.with_streaming_response.get(
            "hero",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(VariantGetResponse, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.variants.with_raw_response.get(
                "hero",
                account_id="",
            )
