# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import Clip

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClip:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        clip = client.stream.clip.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
            end_time_seconds=0,
            start_time_seconds=0,
        )
        assert_matches_type(Optional[Clip], clip, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        clip = client.stream.clip.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
            end_time_seconds=0,
            start_time_seconds=0,
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            max_duration_seconds=1,
            require_signed_urls=True,
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
        )
        assert_matches_type(Optional[Clip], clip, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.stream.clip.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
            end_time_seconds=0,
            start_time_seconds=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clip = response.parse()
        assert_matches_type(Optional[Clip], clip, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.stream.clip.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
            end_time_seconds=0,
            start_time_seconds=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clip = response.parse()
            assert_matches_type(Optional[Clip], clip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.clip.with_raw_response.create(
                account_id="",
                clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
                end_time_seconds=0,
                start_time_seconds=0,
            )


class TestAsyncClip:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        clip = await async_client.stream.clip.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
            end_time_seconds=0,
            start_time_seconds=0,
        )
        assert_matches_type(Optional[Clip], clip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        clip = await async_client.stream.clip.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
            end_time_seconds=0,
            start_time_seconds=0,
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            max_duration_seconds=1,
            require_signed_urls=True,
            thumbnail_timestamp_pct=0.529241,
            watermark={"uid": "ea95132c15732412d22c1476fa83f27a"},
        )
        assert_matches_type(Optional[Clip], clip, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.clip.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
            end_time_seconds=0,
            start_time_seconds=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        clip = await response.parse()
        assert_matches_type(Optional[Clip], clip, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.clip.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
            end_time_seconds=0,
            start_time_seconds=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            clip = await response.parse()
            assert_matches_type(Optional[Clip], clip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.clip.with_raw_response.create(
                account_id="",
                clipped_from_video_uid="023e105f4ecef8ad9ca31a8372d0c353",
                end_time_seconds=0,
                start_time_seconds=0,
            )
