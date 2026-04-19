# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.api_gateway import LabelListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLabels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        label = client.api_gateway.labels.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[LabelListResponse], label, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        label = client.api_gateway.labels.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            filter="login",
            order="description",
            page=1,
            per_page=5,
            source="user",
            with_mapped_resource_counts=True,
        )
        assert_matches_type(SyncV4PagePaginationArray[LabelListResponse], label, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.api_gateway.labels.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[LabelListResponse], label, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.api_gateway.labels.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[LabelListResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateway.labels.with_raw_response.list(
                zone_id="",
            )


class TestAsyncLabels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.labels.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[LabelListResponse], label, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        label = await async_client.api_gateway.labels.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            filter="login",
            order="description",
            page=1,
            per_page=5,
            source="user",
            with_mapped_resource_counts=True,
        )
        assert_matches_type(AsyncV4PagePaginationArray[LabelListResponse], label, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateway.labels.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        label = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[LabelListResponse], label, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateway.labels.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            label = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[LabelListResponse], label, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateway.labels.with_raw_response.list(
                zone_id="",
            )
