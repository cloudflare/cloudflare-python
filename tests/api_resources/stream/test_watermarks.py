# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.shared import (
    UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0,
    UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a,
)
from cloudflare.types.stream import Watermaks

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatermarks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        watermark = client.stream.watermarks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        )
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        watermark = client.stream.watermarks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
            name="Marketing Videos",
            opacity=0.75,
            padding=0.1,
            position="center",
            scale=0.1,
        )
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.stream.watermarks.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = response.parse()
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.stream.watermarks.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = response.parse()
            assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.watermarks.with_raw_response.create(
                account_id="",
                file="@/Users/rchen/Downloads/watermark.png",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        watermark = client.stream.watermarks.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Watermaks], watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.stream.watermarks.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = response.parse()
        assert_matches_type(SyncSinglePage[Watermaks], watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.stream.watermarks.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = response.parse()
            assert_matches_type(SyncSinglePage[Watermaks], watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.watermarks.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        watermark = client.stream.watermarks.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.watermarks.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = response.parse()
        assert_matches_type(UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.watermarks.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = response.parse()
            assert_matches_type(UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.watermarks.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.watermarks.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        watermark = client.stream.watermarks.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.stream.watermarks.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = response.parse()
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.stream.watermarks.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = response.parse()
            assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.watermarks.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.watermarks.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncWatermarks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        watermark = await async_client.stream.watermarks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        )
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        watermark = await async_client.stream.watermarks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
            name="Marketing Videos",
            opacity=0.75,
            padding=0.1,
            position="center",
            scale=0.1,
        )
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.watermarks.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = await response.parse()
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.watermarks.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = await response.parse()
            assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.watermarks.with_raw_response.create(
                account_id="",
                file="@/Users/rchen/Downloads/watermark.png",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        watermark = await async_client.stream.watermarks.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Watermaks], watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.watermarks.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = await response.parse()
        assert_matches_type(AsyncSinglePage[Watermaks], watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.watermarks.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = await response.parse()
            assert_matches_type(AsyncSinglePage[Watermaks], watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.watermarks.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        watermark = await async_client.stream.watermarks.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.watermarks.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = await response.parse()
        assert_matches_type(UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.watermarks.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = await response.parse()
            assert_matches_type(UnnamedSchemaRef602dd5f63eab958d53da61434dec08f0, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.watermarks.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.watermarks.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        watermark = await async_client.stream.watermarks.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.watermarks.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = await response.parse()
        assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.watermarks.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = await response.parse()
            assert_matches_type(UnnamedSchemaRef9444735ca60712dbcf8afd832eb5716a, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.watermarks.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.watermarks.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
