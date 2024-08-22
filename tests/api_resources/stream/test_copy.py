# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.stream import Video

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCopy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        copy = client.stream.copy.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        )
        assert_matches_type(Optional[Video], copy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        copy = client.stream.copy.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
            upload_creator="creator-id_abcde12345",
            upload_metadata="name aGVsbG8gd29ybGQ=, requiresignedurls, allowedorigins ZXhhbXBsZS5jb20sdGVzdC5jb20=",
        )
        assert_matches_type(Optional[Video], copy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.stream.copy.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = response.parse()
        assert_matches_type(Optional[Video], copy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.stream.copy.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = response.parse()
            assert_matches_type(Optional[Video], copy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.copy.with_raw_response.create(
                account_id="",
                url="https://example.com/myvideo.mp4",
            )


class TestAsyncCopy:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        copy = await async_client.stream.copy.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        )
        assert_matches_type(Optional[Video], copy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        copy = await async_client.stream.copy.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
            upload_creator="creator-id_abcde12345",
            upload_metadata="name aGVsbG8gd29ybGQ=, requiresignedurls, allowedorigins ZXhhbXBsZS5jb20sdGVzdC5jb20=",
        )
        assert_matches_type(Optional[Video], copy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.copy.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = await response.parse()
        assert_matches_type(Optional[Video], copy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.copy.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = await response.parse()
            assert_matches_type(Optional[Video], copy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.copy.with_raw_response.create(
                account_id="",
                url="https://example.com/myvideo.mp4",
            )
