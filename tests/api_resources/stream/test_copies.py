# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.stream import CopyStreamVideosUploadVideosFromAURLResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import copy_stream_videos_upload_videos_from_a_url_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCopies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_videos_upload_videos_from_a_url(self, client: Cloudflare) -> None:
        copy = client.stream.copies.stream_videos_upload_videos_from_a_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        )
        assert_matches_type(CopyStreamVideosUploadVideosFromAURLResponse, copy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_videos_upload_videos_from_a_url_with_all_params(self, client: Cloudflare) -> None:
        copy = client.stream.copies.stream_videos_upload_videos_from_a_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
        )
        assert_matches_type(CopyStreamVideosUploadVideosFromAURLResponse, copy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_videos_upload_videos_from_a_url(self, client: Cloudflare) -> None:
        response = client.stream.copies.with_raw_response.stream_videos_upload_videos_from_a_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = response.parse()
        assert_matches_type(CopyStreamVideosUploadVideosFromAURLResponse, copy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_videos_upload_videos_from_a_url(self, client: Cloudflare) -> None:
        with client.stream.copies.with_streaming_response.stream_videos_upload_videos_from_a_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = response.parse()
            assert_matches_type(CopyStreamVideosUploadVideosFromAURLResponse, copy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_videos_upload_videos_from_a_url(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.copies.with_raw_response.stream_videos_upload_videos_from_a_url(
                "",
                url="https://example.com/myvideo.mp4",
            )


class TestAsyncCopies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_videos_upload_videos_from_a_url(self, async_client: AsyncCloudflare) -> None:
        copy = await async_client.stream.copies.stream_videos_upload_videos_from_a_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        )
        assert_matches_type(CopyStreamVideosUploadVideosFromAURLResponse, copy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_videos_upload_videos_from_a_url_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        copy = await async_client.stream.copies.stream_videos_upload_videos_from_a_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
        )
        assert_matches_type(CopyStreamVideosUploadVideosFromAURLResponse, copy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_videos_upload_videos_from_a_url(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.copies.with_raw_response.stream_videos_upload_videos_from_a_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = await response.parse()
        assert_matches_type(CopyStreamVideosUploadVideosFromAURLResponse, copy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_videos_upload_videos_from_a_url(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.copies.with_streaming_response.stream_videos_upload_videos_from_a_url(
            "023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/myvideo.mp4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = await response.parse()
            assert_matches_type(CopyStreamVideosUploadVideosFromAURLResponse, copy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_videos_upload_videos_from_a_url(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.copies.with_raw_response.stream_videos_upload_videos_from_a_url(
                "",
                url="https://example.com/myvideo.mp4",
            )
