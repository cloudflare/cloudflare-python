# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.secrets_store.stores import (
    SecretGetResponse,
    SecretEditResponse,
    SecretListResponse,
    SecretCreateResponse,
    SecretDeleteResponse,
    SecretDuplicateResponse,
    SecretBulkDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        secret = client.secrets_store.stores.secrets.create(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "name": "MY_API_KEY",
                    "scopes": ["workers"],
                    "value": "api-token-secret-123",
                }
            ],
        )
        assert_matches_type(SyncSinglePage[SecretCreateResponse], secret, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.secrets_store.stores.secrets.with_raw_response.create(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "name": "MY_API_KEY",
                    "scopes": ["workers"],
                    "value": "api-token-secret-123",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SyncSinglePage[SecretCreateResponse], secret, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.secrets_store.stores.secrets.with_streaming_response.create(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "name": "MY_API_KEY",
                    "scopes": ["workers"],
                    "value": "api-token-secret-123",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SyncSinglePage[SecretCreateResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.create(
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body=[
                    {
                        "name": "MY_API_KEY",
                        "scopes": ["workers"],
                        "value": "api-token-secret-123",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.create(
                store_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                body=[
                    {
                        "name": "MY_API_KEY",
                        "scopes": ["workers"],
                        "value": "api-token-secret-123",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        secret = client.secrets_store.stores.secrets.list(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[SecretListResponse], secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        secret = client.secrets_store.stores.secrets.list(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="name",
            page=2,
            per_page=20,
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[SecretListResponse], secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.secrets_store.stores.secrets.with_raw_response.list(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[SecretListResponse], secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.secrets_store.stores.secrets.with_streaming_response.list(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[SecretListResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.list(
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.list(
                store_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        secret = client.secrets_store.stores.secrets.delete(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SecretDeleteResponse], secret, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.secrets_store.stores.secrets.with_raw_response.delete(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Optional[SecretDeleteResponse], secret, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.secrets_store.stores.secrets.with_streaming_response.delete(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Optional[SecretDeleteResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.delete(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.delete(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.delete(
                secret_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        secret = client.secrets_store.stores.secrets.bulk_delete(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[SecretBulkDeleteResponse], secret, path=["response"])

    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = client.secrets_store.stores.secrets.with_raw_response.bulk_delete(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SyncSinglePage[SecretBulkDeleteResponse], secret, path=["response"])

    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.secrets_store.stores.secrets.with_streaming_response.bulk_delete(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SyncSinglePage[SecretBulkDeleteResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.bulk_delete(
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.bulk_delete(
                store_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_duplicate(self, client: Cloudflare) -> None:
        secret = client.secrets_store.stores.secrets.duplicate(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        )
        assert_matches_type(Optional[SecretDuplicateResponse], secret, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_duplicate(self, client: Cloudflare) -> None:
        response = client.secrets_store.stores.secrets.with_raw_response.duplicate(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Optional[SecretDuplicateResponse], secret, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_duplicate(self, client: Cloudflare) -> None:
        with client.secrets_store.stores.secrets.with_streaming_response.duplicate(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Optional[SecretDuplicateResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_duplicate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.duplicate(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="MY_API_KEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.duplicate(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="",
                name="MY_API_KEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.duplicate(
                secret_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="MY_API_KEY",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        secret = client.secrets_store.stores.secrets.edit(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        )
        assert_matches_type(Optional[SecretEditResponse], secret, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        secret = client.secrets_store.stores.secrets.edit(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
            scopes=["workers"],
            value="api-token-secret-123",
        )
        assert_matches_type(Optional[SecretEditResponse], secret, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.secrets_store.stores.secrets.with_raw_response.edit(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Optional[SecretEditResponse], secret, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.secrets_store.stores.secrets.with_streaming_response.edit(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Optional[SecretEditResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.edit(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="MY_API_KEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.edit(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="",
                name="MY_API_KEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.edit(
                secret_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="MY_API_KEY",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        secret = client.secrets_store.stores.secrets.get(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SecretGetResponse], secret, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.secrets_store.stores.secrets.with_raw_response.get(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Optional[SecretGetResponse], secret, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.secrets_store.stores.secrets.with_streaming_response.get(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Optional[SecretGetResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.get(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.get(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.secrets_store.stores.secrets.with_raw_response.get(
                secret_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.secrets_store.stores.secrets.create(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "name": "MY_API_KEY",
                    "scopes": ["workers"],
                    "value": "api-token-secret-123",
                }
            ],
        )
        assert_matches_type(AsyncSinglePage[SecretCreateResponse], secret, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secrets_store.stores.secrets.with_raw_response.create(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "name": "MY_API_KEY",
                    "scopes": ["workers"],
                    "value": "api-token-secret-123",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(AsyncSinglePage[SecretCreateResponse], secret, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secrets_store.stores.secrets.with_streaming_response.create(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "name": "MY_API_KEY",
                    "scopes": ["workers"],
                    "value": "api-token-secret-123",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(AsyncSinglePage[SecretCreateResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.create(
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body=[
                    {
                        "name": "MY_API_KEY",
                        "scopes": ["workers"],
                        "value": "api-token-secret-123",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.create(
                store_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                body=[
                    {
                        "name": "MY_API_KEY",
                        "scopes": ["workers"],
                        "value": "api-token-secret-123",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.secrets_store.stores.secrets.list(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[SecretListResponse], secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.secrets_store.stores.secrets.list(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="name",
            page=2,
            per_page=20,
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[SecretListResponse], secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secrets_store.stores.secrets.with_raw_response.list(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[SecretListResponse], secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secrets_store.stores.secrets.with_streaming_response.list(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[SecretListResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.list(
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.list(
                store_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.secrets_store.stores.secrets.delete(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SecretDeleteResponse], secret, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secrets_store.stores.secrets.with_raw_response.delete(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Optional[SecretDeleteResponse], secret, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secrets_store.stores.secrets.with_streaming_response.delete(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Optional[SecretDeleteResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.delete(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.delete(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.delete(
                secret_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.secrets_store.stores.secrets.bulk_delete(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[SecretBulkDeleteResponse], secret, path=["response"])

    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secrets_store.stores.secrets.with_raw_response.bulk_delete(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(AsyncSinglePage[SecretBulkDeleteResponse], secret, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secrets_store.stores.secrets.with_streaming_response.bulk_delete(
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(AsyncSinglePage[SecretBulkDeleteResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.bulk_delete(
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.bulk_delete(
                store_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_duplicate(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.secrets_store.stores.secrets.duplicate(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        )
        assert_matches_type(Optional[SecretDuplicateResponse], secret, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_duplicate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secrets_store.stores.secrets.with_raw_response.duplicate(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Optional[SecretDuplicateResponse], secret, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_duplicate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secrets_store.stores.secrets.with_streaming_response.duplicate(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Optional[SecretDuplicateResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_duplicate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.duplicate(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="MY_API_KEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.duplicate(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="",
                name="MY_API_KEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.duplicate(
                secret_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="MY_API_KEY",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.secrets_store.stores.secrets.edit(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        )
        assert_matches_type(Optional[SecretEditResponse], secret, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.secrets_store.stores.secrets.edit(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
            scopes=["workers"],
            value="api-token-secret-123",
        )
        assert_matches_type(Optional[SecretEditResponse], secret, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secrets_store.stores.secrets.with_raw_response.edit(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Optional[SecretEditResponse], secret, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secrets_store.stores.secrets.with_streaming_response.edit(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="MY_API_KEY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Optional[SecretEditResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.edit(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="MY_API_KEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.edit(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="",
                name="MY_API_KEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.edit(
                secret_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="MY_API_KEY",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        secret = await async_client.secrets_store.stores.secrets.get(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SecretGetResponse], secret, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secrets_store.stores.secrets.with_raw_response.get(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Optional[SecretGetResponse], secret, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secrets_store.stores.secrets.with_streaming_response.get(
            secret_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="985e105f4ecef8ad9ca31a8372d0c353",
            store_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Optional[SecretGetResponse], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.get(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.get(
                secret_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.secrets_store.stores.secrets.with_raw_response.get(
                secret_id="",
                account_id="985e105f4ecef8ad9ca31a8372d0c353",
                store_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
