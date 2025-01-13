# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.assets import UploadCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        upload = client.workers.assets.upload.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            base64=True,
        )
        assert_matches_type(Optional[UploadCreateResponse], upload, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        upload = client.workers.assets.upload.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            base64=True,
            any_file_hash=["string"],
        )
        assert_matches_type(Optional[UploadCreateResponse], upload, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.assets.upload.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            base64=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Optional[UploadCreateResponse], upload, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.assets.upload.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            base64=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Optional[UploadCreateResponse], upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.assets.upload.with_raw_response.create(
                account_id="",
                base64=True,
            )


class TestAsyncUpload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        upload = await async_client.workers.assets.upload.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            base64=True,
        )
        assert_matches_type(Optional[UploadCreateResponse], upload, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        upload = await async_client.workers.assets.upload.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            base64=True,
            any_file_hash=["string"],
        )
        assert_matches_type(Optional[UploadCreateResponse], upload, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.assets.upload.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            base64=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Optional[UploadCreateResponse], upload, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.assets.upload.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            base64=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Optional[UploadCreateResponse], upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.assets.upload.with_raw_response.create(
                account_id="",
                base64=True,
            )
