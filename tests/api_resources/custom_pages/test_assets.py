# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.custom_pages import (
    AssetGetResponse,
    AssetListResponse,
    AssetCreateResponse,
    AssetUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.create(
            description="Custom 500 error page",
            name="my_custom_error_page",
            url="https://example.com/error.html",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetCreateResponse], asset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.create(
            description="Custom 500 error page",
            name="my_custom_error_page",
            url="https://example.com/error.html",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetCreateResponse], asset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.custom_pages.assets.with_raw_response.create(
            description="Custom 500 error page",
            name="my_custom_error_page",
            url="https://example.com/error.html",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(Optional[AssetCreateResponse], asset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.custom_pages.assets.with_streaming_response.create(
            description="Custom 500 error page",
            name="my_custom_error_page",
            url="https://example.com/error.html",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(Optional[AssetCreateResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.create(
                description="Custom 500 error page",
                name="my_custom_error_page",
                url="https://example.com/error.html",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.create(
                description="Custom 500 error page",
                name="my_custom_error_page",
                url="https://example.com/error.html",
                account_id="account_id",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.update(
            asset_name="my_custom_error_page",
            description="Custom 500 error page",
            url="https://example.com/error.html",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.update(
            asset_name="my_custom_error_page",
            description="Custom 500 error page",
            url="https://example.com/error.html",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.custom_pages.assets.with_raw_response.update(
            asset_name="my_custom_error_page",
            description="Custom 500 error page",
            url="https://example.com/error.html",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.custom_pages.assets.with_streaming_response.update(
            asset_name="my_custom_error_page",
            description="Custom 500 error page",
            url="https://example.com/error.html",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_name` but received ''"):
            client.custom_pages.assets.with_raw_response.update(
                asset_name="",
                description="Custom 500 error page",
                url="https://example.com/error.html",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.update(
                asset_name="my_custom_error_page",
                description="Custom 500 error page",
                url="https://example.com/error.html",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.update(
                asset_name="my_custom_error_page",
                description="Custom 500 error page",
                url="https://example.com/error.html",
                account_id="account_id",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[AssetListResponse], asset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.list(
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[AssetListResponse], asset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.custom_pages.assets.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[AssetListResponse], asset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.custom_pages.assets.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[AssetListResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.list(
                account_id="account_id",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.delete(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )
        assert asset is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.delete(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )
        assert asset is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.custom_pages.assets.with_raw_response.delete(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.custom_pages.assets.with_streaming_response.delete(
            asset_name="my_custom_error_page",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_name` but received ''"):
            client.custom_pages.assets.with_raw_response.delete(
                asset_name="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.delete(
                asset_name="my_custom_error_page",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.delete(
                asset_name="my_custom_error_page",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.get(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetGetResponse], asset, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        asset = client.custom_pages.assets.get(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetGetResponse], asset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.custom_pages.assets.with_raw_response.get(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(Optional[AssetGetResponse], asset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.custom_pages.assets.with_streaming_response.get(
            asset_name="my_custom_error_page",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(Optional[AssetGetResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_name` but received ''"):
            client.custom_pages.assets.with_raw_response.get(
                asset_name="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.get(
                asset_name="my_custom_error_page",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.custom_pages.assets.with_raw_response.get(
                asset_name="my_custom_error_page",
                account_id="account_id",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.create(
            description="Custom 500 error page",
            name="my_custom_error_page",
            url="https://example.com/error.html",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetCreateResponse], asset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.create(
            description="Custom 500 error page",
            name="my_custom_error_page",
            url="https://example.com/error.html",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetCreateResponse], asset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_pages.assets.with_raw_response.create(
            description="Custom 500 error page",
            name="my_custom_error_page",
            url="https://example.com/error.html",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(Optional[AssetCreateResponse], asset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_pages.assets.with_streaming_response.create(
            description="Custom 500 error page",
            name="my_custom_error_page",
            url="https://example.com/error.html",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(Optional[AssetCreateResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.create(
                description="Custom 500 error page",
                name="my_custom_error_page",
                url="https://example.com/error.html",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.create(
                description="Custom 500 error page",
                name="my_custom_error_page",
                url="https://example.com/error.html",
                account_id="account_id",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.update(
            asset_name="my_custom_error_page",
            description="Custom 500 error page",
            url="https://example.com/error.html",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.update(
            asset_name="my_custom_error_page",
            description="Custom 500 error page",
            url="https://example.com/error.html",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_pages.assets.with_raw_response.update(
            asset_name="my_custom_error_page",
            description="Custom 500 error page",
            url="https://example.com/error.html",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_pages.assets.with_streaming_response.update(
            asset_name="my_custom_error_page",
            description="Custom 500 error page",
            url="https://example.com/error.html",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(Optional[AssetUpdateResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_name` but received ''"):
            await async_client.custom_pages.assets.with_raw_response.update(
                asset_name="",
                description="Custom 500 error page",
                url="https://example.com/error.html",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.update(
                asset_name="my_custom_error_page",
                description="Custom 500 error page",
                url="https://example.com/error.html",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.update(
                asset_name="my_custom_error_page",
                description="Custom 500 error page",
                url="https://example.com/error.html",
                account_id="account_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[AssetListResponse], asset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.list(
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[AssetListResponse], asset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_pages.assets.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[AssetListResponse], asset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_pages.assets.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[AssetListResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.list(
                account_id="account_id",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.delete(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )
        assert asset is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.delete(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )
        assert asset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_pages.assets.with_raw_response.delete(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_pages.assets.with_streaming_response.delete(
            asset_name="my_custom_error_page",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_name` but received ''"):
            await async_client.custom_pages.assets.with_raw_response.delete(
                asset_name="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.delete(
                asset_name="my_custom_error_page",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.delete(
                asset_name="my_custom_error_page",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.get(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetGetResponse], asset, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        asset = await async_client.custom_pages.assets.get(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )
        assert_matches_type(Optional[AssetGetResponse], asset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_pages.assets.with_raw_response.get(
            asset_name="my_custom_error_page",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(Optional[AssetGetResponse], asset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_pages.assets.with_streaming_response.get(
            asset_name="my_custom_error_page",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(Optional[AssetGetResponse], asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_name` but received ''"):
            await async_client.custom_pages.assets.with_raw_response.get(
                asset_name="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.get(
                asset_name="my_custom_error_page",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.custom_pages.assets.with_raw_response.get(
                asset_name="my_custom_error_page",
                account_id="account_id",
            )
