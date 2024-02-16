# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    StreamGetResponse,
    StreamUpdateResponse,
    StreamStreamVideosListVideosResponse,
)
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStream:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        stream = client.stream.update(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        stream = client.stream.update(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            max_duration_seconds=1,
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            upload_expiry=parse_datetime("2014-01-02T02:20:00Z"),
        )
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.stream.with_raw_response.update(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.stream.with_streaming_response.update(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamUpdateResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.with_raw_response.update(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        stream = client.stream.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert stream is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert stream is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        stream = client.stream.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamGetResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.stream.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamGetResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.stream.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamGetResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_videos_initiate_video_uploads_using_tus(self, client: Cloudflare) -> None:
        stream = client.stream.stream_videos_initiate_video_uploads_using_tus(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert stream is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_videos_initiate_video_uploads_using_tus(self, client: Cloudflare) -> None:
        response = client.stream.with_raw_response.stream_videos_initiate_video_uploads_using_tus(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert stream is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_videos_initiate_video_uploads_using_tus(self, client: Cloudflare) -> None:
        with client.stream.with_streaming_response.stream_videos_initiate_video_uploads_using_tus(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_videos_initiate_video_uploads_using_tus(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.with_raw_response.stream_videos_initiate_video_uploads_using_tus(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_videos_list_videos(self, client: Cloudflare) -> None:
        stream = client.stream.stream_videos_list_videos(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamStreamVideosListVideosResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_videos_list_videos_with_all_params(self, client: Cloudflare) -> None:
        stream = client.stream.stream_videos_list_videos(
            "023e105f4ecef8ad9ca31a8372d0c353",
            asc=True,
            creator="creator-id_abcde12345",
            end=parse_datetime("2014-01-02T02:20:00Z"),
            include_counts=True,
            search="puppy.mp4",
            start=parse_datetime("2014-01-02T02:20:00Z"),
            status="inprogress",
            type="live",
        )
        assert_matches_type(StreamStreamVideosListVideosResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_videos_list_videos(self, client: Cloudflare) -> None:
        response = client.stream.with_raw_response.stream_videos_list_videos(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        assert_matches_type(StreamStreamVideosListVideosResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_videos_list_videos(self, client: Cloudflare) -> None:
        with client.stream.with_streaming_response.stream_videos_list_videos(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            assert_matches_type(StreamStreamVideosListVideosResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_videos_list_videos(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.with_raw_response.stream_videos_list_videos(
                "",
            )


class TestAsyncStream:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.stream.update(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.stream.update(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_origins=["example.com"],
            creator="creator-id_abcde12345",
            max_duration_seconds=1,
            meta={"name": "video12345.mp4"},
            require_signed_urls=True,
            scheduled_deletion=parse_datetime("2014-01-02T02:20:00Z"),
            thumbnail_timestamp_pct=0.529241,
            upload_expiry=parse_datetime("2014-01-02T02:20:00Z"),
        )
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.with_raw_response.update(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamUpdateResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.with_streaming_response.update(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamUpdateResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.with_raw_response.update(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.stream.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert stream is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert stream is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.stream.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamGetResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamGetResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamGetResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_videos_initiate_video_uploads_using_tus(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.stream.stream_videos_initiate_video_uploads_using_tus(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert stream is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_videos_initiate_video_uploads_using_tus(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.stream.with_raw_response.stream_videos_initiate_video_uploads_using_tus(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert stream is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_videos_initiate_video_uploads_using_tus(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.with_streaming_response.stream_videos_initiate_video_uploads_using_tus(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert stream is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_videos_initiate_video_uploads_using_tus(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.with_raw_response.stream_videos_initiate_video_uploads_using_tus(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_videos_list_videos(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.stream.stream_videos_list_videos(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(StreamStreamVideosListVideosResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_videos_list_videos_with_all_params(self, async_client: AsyncCloudflare) -> None:
        stream = await async_client.stream.stream_videos_list_videos(
            "023e105f4ecef8ad9ca31a8372d0c353",
            asc=True,
            creator="creator-id_abcde12345",
            end=parse_datetime("2014-01-02T02:20:00Z"),
            include_counts=True,
            search="puppy.mp4",
            start=parse_datetime("2014-01-02T02:20:00Z"),
            status="inprogress",
            type="live",
        )
        assert_matches_type(StreamStreamVideosListVideosResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_videos_list_videos(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.with_raw_response.stream_videos_list_videos(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        assert_matches_type(StreamStreamVideosListVideosResponse, stream, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_videos_list_videos(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.with_streaming_response.stream_videos_list_videos(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            assert_matches_type(StreamStreamVideosListVideosResponse, stream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_videos_list_videos(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.with_raw_response.stream_videos_list_videos(
                "",
            )
