# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.images.v1 import (
    V1ImageVariant,
    V1ImageVariants,
    VariantDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVariants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        variant = client.images.v1.variants.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="string",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        variant = client.images.v1.variants.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="string",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
            never_require_signed_urls=True,
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.images.v1.variants.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="string",
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
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.images.v1.variants.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="string",
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
            assert_matches_type(V1ImageVariant, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.variants.with_raw_response.create(
                account_id="",
                id="string",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        variant = client.images.v1.variants.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1ImageVariants, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.images.v1.variants.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(V1ImageVariants, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.images.v1.variants.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(V1ImageVariants, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.variants.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        variant = client.images.v1.variants.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.images.v1.variants.with_raw_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.images.v1.variants.with_streaming_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
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
            client.images.v1.variants.with_raw_response.delete(
                "string",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.images.v1.variants.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        variant = client.images.v1.variants.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        variant = client.images.v1.variants.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
            never_require_signed_urls=True,
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.images.v1.variants.with_raw_response.edit(
            "string",
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
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.images.v1.variants.with_streaming_response.edit(
            "string",
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
            assert_matches_type(V1ImageVariant, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.variants.with_raw_response.edit(
                "string",
                account_id="",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.images.v1.variants.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        variant = client.images.v1.variants.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.images.v1.variants.with_raw_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = response.parse()
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.images.v1.variants.with_streaming_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = response.parse()
            assert_matches_type(V1ImageVariant, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.variants.with_raw_response.get(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            client.images.v1.variants.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncVariants:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1.variants.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="string",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1.variants.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="string",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
            never_require_signed_urls=True,
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.variants.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="string",
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
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.variants.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="string",
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
            assert_matches_type(V1ImageVariant, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.variants.with_raw_response.create(
                account_id="",
                id="string",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1.variants.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1ImageVariants, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.variants.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(V1ImageVariants, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.variants.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(V1ImageVariants, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.variants.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1.variants.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.variants.with_raw_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(VariantDeleteResponse, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.variants.with_streaming_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
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
            await async_client.images.v1.variants.with_raw_response.delete(
                "string",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.images.v1.variants.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1.variants.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1.variants.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            options={
                "fit": "scale-down",
                "height": 768,
                "metadata": "none",
                "width": 1366,
            },
            never_require_signed_urls=True,
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.variants.with_raw_response.edit(
            "string",
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
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.variants.with_streaming_response.edit(
            "string",
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
            assert_matches_type(V1ImageVariant, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.variants.with_raw_response.edit(
                "string",
                account_id="",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.images.v1.variants.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                options={
                    "fit": "scale-down",
                    "height": 768,
                    "metadata": "none",
                    "width": 1366,
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        variant = await async_client.images.v1.variants.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.variants.with_raw_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variant = await response.parse()
        assert_matches_type(V1ImageVariant, variant, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.variants.with_streaming_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variant = await response.parse()
            assert_matches_type(V1ImageVariant, variant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.variants.with_raw_response.get(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variant_id` but received ''"):
            await async_client.images.v1.variants.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
