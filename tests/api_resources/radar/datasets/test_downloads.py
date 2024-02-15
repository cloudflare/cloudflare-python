# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.datasets import (
    DownloadRadarPostDatasetDownloadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDownloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_radar_post_dataset_download(self, client: Cloudflare) -> None:
        download = client.radar.datasets.downloads.radar_post_dataset_download(
            dataset_id=3,
        )
        assert_matches_type(DownloadRadarPostDatasetDownloadResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_radar_post_dataset_download_with_all_params(self, client: Cloudflare) -> None:
        download = client.radar.datasets.downloads.radar_post_dataset_download(
            dataset_id=3,
            format="JSON",
        )
        assert_matches_type(DownloadRadarPostDatasetDownloadResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_radar_post_dataset_download(self, client: Cloudflare) -> None:
        response = client.radar.datasets.downloads.with_raw_response.radar_post_dataset_download(
            dataset_id=3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert_matches_type(DownloadRadarPostDatasetDownloadResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_radar_post_dataset_download(self, client: Cloudflare) -> None:
        with client.radar.datasets.downloads.with_streaming_response.radar_post_dataset_download(
            dataset_id=3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert_matches_type(DownloadRadarPostDatasetDownloadResponse, download, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDownloads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_radar_post_dataset_download(self, async_client: AsyncCloudflare) -> None:
        download = await async_client.radar.datasets.downloads.radar_post_dataset_download(
            dataset_id=3,
        )
        assert_matches_type(DownloadRadarPostDatasetDownloadResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_radar_post_dataset_download_with_all_params(self, async_client: AsyncCloudflare) -> None:
        download = await async_client.radar.datasets.downloads.radar_post_dataset_download(
            dataset_id=3,
            format="JSON",
        )
        assert_matches_type(DownloadRadarPostDatasetDownloadResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_radar_post_dataset_download(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.datasets.downloads.with_raw_response.radar_post_dataset_download(
            dataset_id=3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert_matches_type(DownloadRadarPostDatasetDownloadResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_radar_post_dataset_download(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.datasets.downloads.with_streaming_response.radar_post_dataset_download(
            dataset_id=3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert_matches_type(DownloadRadarPostDatasetDownloadResponse, download, path=["response"])

        assert cast(Any, response.is_closed) is True
