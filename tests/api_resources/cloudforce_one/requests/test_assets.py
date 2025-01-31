# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.cloudforce_one.requests import (
    AssetGetResponse,
    AssetCreateResponse,
    AssetDeleteResponse,
    AssetUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        asset = client.cloudforce_one.requests.assets.create(
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )
        assert_matches_type(SyncSinglePage[AssetCreateResponse], asset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.assets.with_raw_response.create(
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(SyncSinglePage[AssetCreateResponse], asset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.assets.with_streaming_response.create(
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(SyncSinglePage[AssetCreateResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.create(
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                page=0,
                per_page=10,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.create(
                request_identifier="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                page=0,
                per_page=10,
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        asset = client.cloudforce_one.requests.assets.update(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        asset = client.cloudforce_one.requests.assets.update(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            source="@/Users/me/example.docx",
        )
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.assets.with_raw_response.update(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.assets.with_streaming_response.update(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.update(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.update(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_identifer` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.update(
                asset_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        asset = client.cloudforce_one.requests.assets.delete(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(AssetDeleteResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.assets.with_raw_response.delete(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetDeleteResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.assets.with_streaming_response.delete(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetDeleteResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.delete(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.delete(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_identifer` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.delete(
                asset_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        asset = client.cloudforce_one.requests.assets.get(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(SyncSinglePage[AssetGetResponse], asset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.requests.assets.with_raw_response.get(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(SyncSinglePage[AssetGetResponse], asset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.requests.assets.with_streaming_response.get(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(SyncSinglePage[AssetGetResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.get(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.get(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_identifer` but received ''"):
            client.cloudforce_one.requests.assets.with_raw_response.get(
                asset_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.cloudforce_one.requests.assets.create(
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )
        assert_matches_type(AsyncSinglePage[AssetCreateResponse], asset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.assets.with_raw_response.create(
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AsyncSinglePage[AssetCreateResponse], asset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.assets.with_streaming_response.create(
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=10,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AsyncSinglePage[AssetCreateResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.create(
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                page=0,
                per_page=10,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.create(
                request_identifier="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                page=0,
                per_page=10,
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.cloudforce_one.requests.assets.update(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.cloudforce_one.requests.assets.update(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            source="@/Users/me/example.docx",
        )
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.assets.with_raw_response.update(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.assets.with_streaming_response.update(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.update(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.update(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_identifer` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.update(
                asset_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.cloudforce_one.requests.assets.delete(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(AssetDeleteResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.assets.with_raw_response.delete(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetDeleteResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.assets.with_streaming_response.delete(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetDeleteResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.delete(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.delete(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_identifer` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.delete(
                asset_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.cloudforce_one.requests.assets.get(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(AsyncSinglePage[AssetGetResponse], asset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.requests.assets.with_raw_response.get(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AsyncSinglePage[AssetGetResponse], asset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.requests.assets.with_streaming_response.get(
            asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AsyncSinglePage[AssetGetResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.get(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_identifier` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.get(
                asset_identifer="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_identifer` but received ''"):
            await async_client.cloudforce_one.requests.assets.with_raw_response.get(
                asset_identifer="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                request_identifier="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )
