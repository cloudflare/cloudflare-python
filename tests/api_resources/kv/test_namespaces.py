# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.kv import (
    Namespace,
    NamespaceDeleteResponse,
    NamespaceUpdateResponse,
    NamespaceBulkDeleteResponse,
    NamespaceBulkUpdateResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNamespaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        namespace = client.kv.namespaces.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )
        assert_matches_type(Optional[Namespace], namespace, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(Optional[Namespace], namespace, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.kv.namespaces.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(Optional[Namespace], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.with_raw_response.create(
                account_id="",
                title="My Own Namespace",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        namespace = client.kv.namespaces.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )
        assert_matches_type(Optional[NamespaceUpdateResponse], namespace, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.with_raw_response.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(Optional[NamespaceUpdateResponse], namespace, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.kv.namespaces.with_streaming_response.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(Optional[NamespaceUpdateResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.with_raw_response.update(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
                title="My Own Namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.with_raw_response.update(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                title="My Own Namespace",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        namespace = client.kv.namespaces.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[Namespace], namespace, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        namespace = client.kv.namespaces.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[Namespace], namespace, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Namespace], namespace, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.kv.namespaces.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Namespace], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        namespace = client.kv.namespaces.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[NamespaceDeleteResponse], namespace, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.with_raw_response.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(Optional[NamespaceDeleteResponse], namespace, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.kv.namespaces.with_streaming_response.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(Optional[NamespaceDeleteResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.with_raw_response.delete(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.with_raw_response.delete(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        namespace = client.kv.namespaces.bulk_delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key"],
        )
        assert_matches_type(Optional[NamespaceBulkDeleteResponse], namespace, path=["response"])

    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.with_raw_response.bulk_delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(Optional[NamespaceBulkDeleteResponse], namespace, path=["response"])

    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.kv.namespaces.with_streaming_response.bulk_delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(Optional[NamespaceBulkDeleteResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.with_raw_response.bulk_delete(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=["My-Key"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.with_raw_response.bulk_delete(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=["My-Key"],
            )

    @parametrize
    def test_method_bulk_update(self, client: Cloudflare) -> None:
        namespace = client.kv.namespaces.bulk_update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}],
        )
        assert_matches_type(Optional[NamespaceBulkUpdateResponse], namespace, path=["response"])

    @parametrize
    def test_raw_response_bulk_update(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.with_raw_response.bulk_update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(Optional[NamespaceBulkUpdateResponse], namespace, path=["response"])

    @parametrize
    def test_streaming_response_bulk_update(self, client: Cloudflare) -> None:
        with client.kv.namespaces.with_streaming_response.bulk_update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(Optional[NamespaceBulkUpdateResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.with_raw_response.bulk_update(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.with_raw_response.bulk_update(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        namespace = client.kv.namespaces.get(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Namespace], namespace, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.with_raw_response.get(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(Optional[Namespace], namespace, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.kv.namespaces.with_streaming_response.get(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(Optional[Namespace], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.with_raw_response.get(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.with_raw_response.get(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncNamespaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.kv.namespaces.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )
        assert_matches_type(Optional[Namespace], namespace, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(Optional[Namespace], namespace, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(Optional[Namespace], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.create(
                account_id="",
                title="My Own Namespace",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.kv.namespaces.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )
        assert_matches_type(Optional[NamespaceUpdateResponse], namespace, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.with_raw_response.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(Optional[NamespaceUpdateResponse], namespace, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.with_streaming_response.update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(Optional[NamespaceUpdateResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.update(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
                title="My Own Namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.update(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                title="My Own Namespace",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.kv.namespaces.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Namespace], namespace, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.kv.namespaces.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[Namespace], namespace, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Namespace], namespace, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Namespace], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.kv.namespaces.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[NamespaceDeleteResponse], namespace, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.with_raw_response.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(Optional[NamespaceDeleteResponse], namespace, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.with_streaming_response.delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(Optional[NamespaceDeleteResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.delete(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.delete(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.kv.namespaces.bulk_delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key"],
        )
        assert_matches_type(Optional[NamespaceBulkDeleteResponse], namespace, path=["response"])

    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.with_raw_response.bulk_delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(Optional[NamespaceBulkDeleteResponse], namespace, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.with_streaming_response.bulk_delete(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(Optional[NamespaceBulkDeleteResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.bulk_delete(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=["My-Key"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.bulk_delete(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=["My-Key"],
            )

    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.kv.namespaces.bulk_update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}],
        )
        assert_matches_type(Optional[NamespaceBulkUpdateResponse], namespace, path=["response"])

    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.with_raw_response.bulk_update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(Optional[NamespaceBulkUpdateResponse], namespace, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.with_streaming_response.bulk_update(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(Optional[NamespaceBulkUpdateResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.bulk_update(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.bulk_update(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.kv.namespaces.get(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Namespace], namespace, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.with_raw_response.get(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(Optional[Namespace], namespace, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.with_streaming_response.get(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(Optional[Namespace], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.get(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.with_raw_response.get(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
