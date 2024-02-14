# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.images.v2s import (
    DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDirectUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_create_authenticated_direct_upload_url_v_2(self, client: Cloudflare) -> None:
        direct_upload = client.images.v2s.direct_uploads.cloudflare_images_create_authenticated_direct_upload_url_v_2(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_images_create_authenticated_direct_upload_url_v_2_with_all_params(
        self, client: Cloudflare
    ) -> None:
        direct_upload = client.images.v2s.direct_uploads.cloudflare_images_create_authenticated_direct_upload_url_v_2(
            "023e105f4ecef8ad9ca31a8372d0c353",
            expiry=parse_datetime("2021-01-02T02:20:00Z"),
            metadata={},
            require_signed_urls=True,
        )
        assert_matches_type(
            DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_images_create_authenticated_direct_upload_url_v_2(
        self, client: Cloudflare
    ) -> None:
        response = client.images.v2s.direct_uploads.with_raw_response.cloudflare_images_create_authenticated_direct_upload_url_v_2(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct_upload = response.parse()
        assert_matches_type(
            DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_images_create_authenticated_direct_upload_url_v_2(
        self, client: Cloudflare
    ) -> None:
        with client.images.v2s.direct_uploads.with_streaming_response.cloudflare_images_create_authenticated_direct_upload_url_v_2(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct_upload = response.parse()
            assert_matches_type(
                DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response,
                direct_upload,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_images_create_authenticated_direct_upload_url_v_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v2s.direct_uploads.with_raw_response.cloudflare_images_create_authenticated_direct_upload_url_v_2(
                "",
            )


class TestAsyncDirectUploads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_create_authenticated_direct_upload_url_v_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        direct_upload = (
            await async_client.images.v2s.direct_uploads.cloudflare_images_create_authenticated_direct_upload_url_v_2(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )
        assert_matches_type(
            DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_images_create_authenticated_direct_upload_url_v_2_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        direct_upload = (
            await async_client.images.v2s.direct_uploads.cloudflare_images_create_authenticated_direct_upload_url_v_2(
                "023e105f4ecef8ad9ca31a8372d0c353",
                expiry=parse_datetime("2021-01-02T02:20:00Z"),
                metadata={},
                require_signed_urls=True,
            )
        )
        assert_matches_type(
            DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_images_create_authenticated_direct_upload_url_v_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.images.v2s.direct_uploads.with_raw_response.cloudflare_images_create_authenticated_direct_upload_url_v_2(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct_upload = await response.parse()
        assert_matches_type(
            DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_images_create_authenticated_direct_upload_url_v_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.images.v2s.direct_uploads.with_streaming_response.cloudflare_images_create_authenticated_direct_upload_url_v_2(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct_upload = await response.parse()
            assert_matches_type(
                DirectUploadCloudflareImagesCreateAuthenticatedDirectUploadURLV2Response,
                direct_upload,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_images_create_authenticated_direct_upload_url_v_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v2s.direct_uploads.with_raw_response.cloudflare_images_create_authenticated_direct_upload_url_v_2(
                "",
            )
