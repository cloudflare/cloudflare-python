# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.images import (
    V1GetResponse,
    V1DeleteResponse,
    V1UpdateResponse,
    V1CloudflareImagesListImagesResponse,
    V1CloudflareImagesUploadAnImageViaURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1s:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        v1 = client.images.v1s.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1UpdateResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        v1 = client.images.v1s.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={},
            require_signed_urls=True,
        )
        assert_matches_type(V1UpdateResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.images.v1s.with_raw_response.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1UpdateResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.images.v1s.with_streaming_response.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1UpdateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.with_raw_response.update(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.images.v1s.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        v1 = client.images.v1s.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.images.v1s.with_raw_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.images.v1s.with_streaming_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DeleteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.with_raw_response.delete(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.images.v1s.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_list_images(self, client: Cloudflare) -> None:
        v1 = client.images.v1s.cloudflare_images_list_images(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1CloudflareImagesListImagesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_list_images_with_all_params(self, client: Cloudflare) -> None:
        v1 = client.images.v1s.cloudflare_images_list_images(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=10,
        )
        assert_matches_type(V1CloudflareImagesListImagesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_images_list_images(self, client: Cloudflare) -> None:
        response = client.images.v1s.with_raw_response.cloudflare_images_list_images(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CloudflareImagesListImagesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_images_list_images(self, client: Cloudflare) -> None:
        with client.images.v1s.with_streaming_response.cloudflare_images_list_images(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CloudflareImagesListImagesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_images_list_images(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.with_raw_response.cloudflare_images_list_images(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_upload_an_image_via_url_overload_1(self, client: Cloudflare) -> None:
        v1 = client.images.v1s.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        )
        assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_images_upload_an_image_via_url_overload_1(self, client: Cloudflare) -> None:
        response = client.images.v1s.with_raw_response.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_images_upload_an_image_via_url_overload_1(self, client: Cloudflare) -> None:
        with client.images.v1s.with_streaming_response.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_images_upload_an_image_via_url_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.with_raw_response.cloudflare_images_upload_an_image_via_url(
                "",
                file={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_upload_an_image_via_url_overload_2(self, client: Cloudflare) -> None:
        v1 = client.images.v1s.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        )
        assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_images_upload_an_image_via_url_overload_2(self, client: Cloudflare) -> None:
        response = client.images.v1s.with_raw_response.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_images_upload_an_image_via_url_overload_2(self, client: Cloudflare) -> None:
        with client.images.v1s.with_streaming_response.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_images_upload_an_image_via_url_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.with_raw_response.cloudflare_images_upload_an_image_via_url(
                "",
                url="https://example.com/path/to/logo.png",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        v1 = client.images.v1s.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1GetResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.images.v1s.with_raw_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1GetResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.images.v1s.with_streaming_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1GetResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.with_raw_response.get(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.images.v1s.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncV1s:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1s.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1UpdateResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1s.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={},
            require_signed_urls=True,
        )
        assert_matches_type(V1UpdateResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1s.with_raw_response.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1UpdateResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1s.with_streaming_response.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1UpdateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.with_raw_response.update(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.images.v1s.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1s.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1s.with_raw_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1s.with_streaming_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DeleteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.with_raw_response.delete(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.images.v1s.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_list_images(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1s.cloudflare_images_list_images(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1CloudflareImagesListImagesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_list_images_with_all_params(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1s.cloudflare_images_list_images(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=10,
        )
        assert_matches_type(V1CloudflareImagesListImagesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_images_list_images(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1s.with_raw_response.cloudflare_images_list_images(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CloudflareImagesListImagesResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_images_list_images(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1s.with_streaming_response.cloudflare_images_list_images(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CloudflareImagesListImagesResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_images_list_images(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.with_raw_response.cloudflare_images_list_images(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_upload_an_image_via_url_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        v1 = await async_client.images.v1s.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        )
        assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_images_upload_an_image_via_url_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.images.v1s.with_raw_response.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_images_upload_an_image_via_url_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.images.v1s.with_streaming_response.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_images_upload_an_image_via_url_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.with_raw_response.cloudflare_images_upload_an_image_via_url(
                "",
                file={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_upload_an_image_via_url_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        v1 = await async_client.images.v1s.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        )
        assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_images_upload_an_image_via_url_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.images.v1s.with_raw_response.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_images_upload_an_image_via_url_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.images.v1s.with_streaming_response.cloudflare_images_upload_an_image_via_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CloudflareImagesUploadAnImageViaURLResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_images_upload_an_image_via_url_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.with_raw_response.cloudflare_images_upload_an_image_via_url(
                "",
                url="https://example.com/path/to/logo.png",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1s.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1GetResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1s.with_raw_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1GetResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1s.with_streaming_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1GetResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.with_raw_response.get(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.images.v1s.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
