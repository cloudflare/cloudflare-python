# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_cloud_networking import (
    CatalogSyncGetResponse,
    CatalogSyncEditResponse,
    CatalogSyncListResponse,
    CatalogSyncCreateResponse,
    CatalogSyncDeleteResponse,
    CatalogSyncUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCatalogSyncs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.create(
            account_id="account_id",
            destination_type="NONE",
            name="name",
            update_mode="AUTO",
        )
        assert_matches_type(CatalogSyncCreateResponse, catalog_sync, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.create(
            account_id="account_id",
            destination_type="NONE",
            name="name",
            update_mode="AUTO",
            description="description",
            policy="policy",
            forwarded="forwarded",
        )
        assert_matches_type(CatalogSyncCreateResponse, catalog_sync, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.catalog_syncs.with_raw_response.create(
            account_id="account_id",
            destination_type="NONE",
            name="name",
            update_mode="AUTO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = response.parse()
        assert_matches_type(CatalogSyncCreateResponse, catalog_sync, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.catalog_syncs.with_streaming_response.create(
            account_id="account_id",
            destination_type="NONE",
            name="name",
            update_mode="AUTO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = response.parse()
            assert_matches_type(CatalogSyncCreateResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.create(
                account_id="",
                destination_type="NONE",
                name="name",
                update_mode="AUTO",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.update(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CatalogSyncUpdateResponse, catalog_sync, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.update(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            description="description",
            name="name",
            policy="policy",
            update_mode="AUTO",
        )
        assert_matches_type(CatalogSyncUpdateResponse, catalog_sync, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.catalog_syncs.with_raw_response.update(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = response.parse()
        assert_matches_type(CatalogSyncUpdateResponse, catalog_sync, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.catalog_syncs.with_streaming_response.update(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = response.parse()
            assert_matches_type(CatalogSyncUpdateResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.update(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.update(
                sync_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[CatalogSyncListResponse], catalog_sync, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.catalog_syncs.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = response.parse()
        assert_matches_type(SyncSinglePage[CatalogSyncListResponse], catalog_sync, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.catalog_syncs.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = response.parse()
            assert_matches_type(SyncSinglePage[CatalogSyncListResponse], catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.delete(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CatalogSyncDeleteResponse, catalog_sync, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.delete(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            delete_destination=True,
        )
        assert_matches_type(CatalogSyncDeleteResponse, catalog_sync, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.catalog_syncs.with_raw_response.delete(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = response.parse()
        assert_matches_type(CatalogSyncDeleteResponse, catalog_sync, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.catalog_syncs.with_streaming_response.delete(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = response.parse()
            assert_matches_type(CatalogSyncDeleteResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.delete(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.delete(
                sync_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.edit(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CatalogSyncEditResponse, catalog_sync, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.edit(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            description="description",
            name="name",
            policy="policy",
            update_mode="AUTO",
        )
        assert_matches_type(CatalogSyncEditResponse, catalog_sync, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.catalog_syncs.with_raw_response.edit(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = response.parse()
        assert_matches_type(CatalogSyncEditResponse, catalog_sync, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.catalog_syncs.with_streaming_response.edit(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = response.parse()
            assert_matches_type(CatalogSyncEditResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.edit(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.edit(
                sync_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.get(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CatalogSyncGetResponse, catalog_sync, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.catalog_syncs.with_raw_response.get(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = response.parse()
        assert_matches_type(CatalogSyncGetResponse, catalog_sync, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.catalog_syncs.with_streaming_response.get(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = response.parse()
            assert_matches_type(CatalogSyncGetResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.get(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.get(
                sync_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_refresh(self, client: Cloudflare) -> None:
        catalog_sync = client.magic_cloud_networking.catalog_syncs.refresh(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(str, catalog_sync, path=["response"])

    @parametrize
    def test_raw_response_refresh(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.catalog_syncs.with_raw_response.refresh(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = response.parse()
        assert_matches_type(str, catalog_sync, path=["response"])

    @parametrize
    def test_streaming_response_refresh(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.catalog_syncs.with_streaming_response.refresh(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = response.parse()
            assert_matches_type(str, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_refresh(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.refresh(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.with_raw_response.refresh(
                sync_id="",
                account_id="account_id",
            )


class TestAsyncCatalogSyncs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.create(
            account_id="account_id",
            destination_type="NONE",
            name="name",
            update_mode="AUTO",
        )
        assert_matches_type(CatalogSyncCreateResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.create(
            account_id="account_id",
            destination_type="NONE",
            name="name",
            update_mode="AUTO",
            description="description",
            policy="policy",
            forwarded="forwarded",
        )
        assert_matches_type(CatalogSyncCreateResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.create(
            account_id="account_id",
            destination_type="NONE",
            name="name",
            update_mode="AUTO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = await response.parse()
        assert_matches_type(CatalogSyncCreateResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.catalog_syncs.with_streaming_response.create(
            account_id="account_id",
            destination_type="NONE",
            name="name",
            update_mode="AUTO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = await response.parse()
            assert_matches_type(CatalogSyncCreateResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.create(
                account_id="",
                destination_type="NONE",
                name="name",
                update_mode="AUTO",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.update(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CatalogSyncUpdateResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.update(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            description="description",
            name="name",
            policy="policy",
            update_mode="AUTO",
        )
        assert_matches_type(CatalogSyncUpdateResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.update(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = await response.parse()
        assert_matches_type(CatalogSyncUpdateResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.catalog_syncs.with_streaming_response.update(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = await response.parse()
            assert_matches_type(CatalogSyncUpdateResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.update(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.update(
                sync_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[CatalogSyncListResponse], catalog_sync, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = await response.parse()
        assert_matches_type(AsyncSinglePage[CatalogSyncListResponse], catalog_sync, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.catalog_syncs.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = await response.parse()
            assert_matches_type(AsyncSinglePage[CatalogSyncListResponse], catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.delete(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CatalogSyncDeleteResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.delete(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            delete_destination=True,
        )
        assert_matches_type(CatalogSyncDeleteResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.delete(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = await response.parse()
        assert_matches_type(CatalogSyncDeleteResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.catalog_syncs.with_streaming_response.delete(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = await response.parse()
            assert_matches_type(CatalogSyncDeleteResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.delete(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.delete(
                sync_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.edit(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CatalogSyncEditResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.edit(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            description="description",
            name="name",
            policy="policy",
            update_mode="AUTO",
        )
        assert_matches_type(CatalogSyncEditResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.edit(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = await response.parse()
        assert_matches_type(CatalogSyncEditResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.catalog_syncs.with_streaming_response.edit(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = await response.parse()
            assert_matches_type(CatalogSyncEditResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.edit(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.edit(
                sync_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.get(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(CatalogSyncGetResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.get(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = await response.parse()
        assert_matches_type(CatalogSyncGetResponse, catalog_sync, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.catalog_syncs.with_streaming_response.get(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = await response.parse()
            assert_matches_type(CatalogSyncGetResponse, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.get(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.get(
                sync_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_refresh(self, async_client: AsyncCloudflare) -> None:
        catalog_sync = await async_client.magic_cloud_networking.catalog_syncs.refresh(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(str, catalog_sync, path=["response"])

    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.refresh(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalog_sync = await response.parse()
        assert_matches_type(str, catalog_sync, path=["response"])

    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.catalog_syncs.with_streaming_response.refresh(
            sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalog_sync = await response.parse()
            assert_matches_type(str, catalog_sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_refresh(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.refresh(
                sync_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sync_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.with_raw_response.refresh(
                sync_id="",
                account_id="account_id",
            )
