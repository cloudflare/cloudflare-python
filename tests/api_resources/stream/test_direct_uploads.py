# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.stream import DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import direct_upload_stream_videos_upload_videos_via_direct_upload_urls_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDirectUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_videos_upload_videos_via_direct_upload_urls(self, client: Cloudflare) -> None:
        direct_upload = client.stream.direct_uploads.stream_videos_upload_videos_via_direct_upload_urls(
            "023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        )
        assert_matches_type(
            DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_videos_upload_videos_via_direct_upload_urls_with_all_params(
        self, client: Cloudflare
    ) -> None:
        direct_upload = client.stream.direct_uploads.stream_videos_upload_videos_via_direct_upload_urls(
            "023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            expiry=parse_datetime("2021-01-02T02:20:00Z"),
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
        )
        assert_matches_type(
            DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_videos_upload_videos_via_direct_upload_urls(self, client: Cloudflare) -> None:
        response = client.stream.direct_uploads.with_raw_response.stream_videos_upload_videos_via_direct_upload_urls(
            "023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct_upload = response.parse()
        assert_matches_type(
            DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_videos_upload_videos_via_direct_upload_urls(self, client: Cloudflare) -> None:
        with client.stream.direct_uploads.with_streaming_response.stream_videos_upload_videos_via_direct_upload_urls(
            "023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct_upload = response.parse()
            assert_matches_type(
                DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse, direct_upload, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_videos_upload_videos_via_direct_upload_urls(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.direct_uploads.with_raw_response.stream_videos_upload_videos_via_direct_upload_urls(
                "",
                max_duration_seconds=1,
            )


class TestAsyncDirectUploads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_videos_upload_videos_via_direct_upload_urls(
        self, async_client: AsyncCloudflare
    ) -> None:
        direct_upload = await async_client.stream.direct_uploads.stream_videos_upload_videos_via_direct_upload_urls(
            "023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        )
        assert_matches_type(
            DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_videos_upload_videos_via_direct_upload_urls_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        direct_upload = await async_client.stream.direct_uploads.stream_videos_upload_videos_via_direct_upload_urls(
            "023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            expiry=parse_datetime("2021-01-02T02:20:00Z"),
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
        )
        assert_matches_type(
            DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_videos_upload_videos_via_direct_upload_urls(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.stream.direct_uploads.with_raw_response.stream_videos_upload_videos_via_direct_upload_urls(
            "023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        direct_upload = await response.parse()
        assert_matches_type(
            DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse, direct_upload, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_videos_upload_videos_via_direct_upload_urls(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.direct_uploads.with_streaming_response.stream_videos_upload_videos_via_direct_upload_urls(
            "023e105f4ecef8ad9ca31a8372d0c353",
            max_duration_seconds=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            direct_upload = await response.parse()
            assert_matches_type(
                DirectUploadStreamVideosUploadVideosViaDirectUploadURLsResponse, direct_upload, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_videos_upload_videos_via_direct_upload_urls(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await (
                async_client.stream.direct_uploads.with_raw_response.stream_videos_upload_videos_via_direct_upload_urls(
                    "",
                    max_duration_seconds=1,
                )
            )
