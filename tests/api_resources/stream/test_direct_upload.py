# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.stream import DirectUploadCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDirectUpload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        direct_upload = client.stream.direct_upload.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        )
        assert_matches_type(Optional[DirectUploadCreateResponse], direct_upload, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        direct_upload = client.stream.direct_upload.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            expiry=parse_datetime("2021-01-02T02:20:00Z"),
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
            upload_creator="creator-id_abcde12345",
        )
        assert_matches_type(Optional[DirectUploadCreateResponse], direct_upload, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.stream.direct_upload.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct_upload = response.parse()
        assert_matches_type(Optional[DirectUploadCreateResponse], direct_upload, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.stream.direct_upload.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct_upload = response.parse()
            assert_matches_type(Optional[DirectUploadCreateResponse], direct_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.direct_upload.with_raw_response.create(
                account_id="",
                max_duration_seconds=1,
            )


class TestAsyncDirectUpload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        direct_upload = await async_client.stream.direct_upload.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        )
        assert_matches_type(Optional[DirectUploadCreateResponse], direct_upload, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        direct_upload = await async_client.stream.direct_upload.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            expiry=parse_datetime("2021-01-02T02:20:00Z"),
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
            upload_creator="creator-id_abcde12345",
        )
        assert_matches_type(Optional[DirectUploadCreateResponse], direct_upload, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.direct_upload.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct_upload = await response.parse()
        assert_matches_type(Optional[DirectUploadCreateResponse], direct_upload, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.direct_upload.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct_upload = await response.parse()
            assert_matches_type(Optional[DirectUploadCreateResponse], direct_upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.direct_upload.with_raw_response.create(
                account_id="",
                max_duration_seconds=1,
            )
