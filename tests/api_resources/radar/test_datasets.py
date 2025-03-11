# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_date
from cloudflare.types.radar import (
    DatasetListResponse,
    DatasetDownloadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        dataset = client.radar.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        dataset = client.radar.datasets.list(
            dataset_type="RANKING_BUCKET",
            date=parse_date("2024-09-19"),
            format="JSON",
            limit=5,
            offset=0,
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_download(self, client: Cloudflare) -> None:
        dataset = client.radar.datasets.download(
            dataset_id=3,
        )
        assert_matches_type(DatasetDownloadResponse, dataset, path=["response"])

    @parametrize
    def test_method_download_with_all_params(self, client: Cloudflare) -> None:
        dataset = client.radar.datasets.download(
            dataset_id=3,
            format="JSON",
        )
        assert_matches_type(DatasetDownloadResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_download(self, client: Cloudflare) -> None:
        response = client.radar.datasets.with_raw_response.download(
            dataset_id=3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetDownloadResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_download(self, client: Cloudflare) -> None:
        with client.radar.datasets.with_streaming_response.download(
            dataset_id=3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetDownloadResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dataset = client.radar.datasets.get(
            "ranking_top_1000",
        )
        assert_matches_type(str, dataset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.datasets.with_raw_response.get(
            "ranking_top_1000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(str, dataset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.datasets.with_streaming_response.get(
            "ranking_top_1000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(str, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alias` but received ''"):
            client.radar.datasets.with_raw_response.get(
                "",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.radar.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.radar.datasets.list(
            dataset_type="RANKING_BUCKET",
            date=parse_date("2024-09-19"),
            format="JSON",
            limit=5,
            offset=0,
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_download(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.radar.datasets.download(
            dataset_id=3,
        )
        assert_matches_type(DatasetDownloadResponse, dataset, path=["response"])

    @parametrize
    async def test_method_download_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.radar.datasets.download(
            dataset_id=3,
            format="JSON",
        )
        assert_matches_type(DatasetDownloadResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.datasets.with_raw_response.download(
            dataset_id=3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetDownloadResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.datasets.with_streaming_response.download(
            dataset_id=3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetDownloadResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.radar.datasets.get(
            "ranking_top_1000",
        )
        assert_matches_type(str, dataset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.datasets.with_raw_response.get(
            "ranking_top_1000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(str, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.datasets.with_streaming_response.get(
            "ranking_top_1000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(str, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alias` but received ''"):
            await async_client.radar.datasets.with_raw_response.get(
                "",
            )
