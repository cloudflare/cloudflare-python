# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.storage.kv import (
    NamespaceListResponse,
    NamespaceCreateResponse,
    NamespaceDeleteResponse,
    NamespaceUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNamespaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        namespace = client.storage.kv.namespaces.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.storage.kv.namespaces.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.storage.kv.namespaces.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.storage.kv.namespaces.with_raw_response.create(
                account_id="",
                title="My Own Namespace",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        namespace = client.storage.kv.namespaces.update(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.storage.kv.namespaces.with_raw_response.update(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.storage.kv.namespaces.with_streaming_response.update(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.storage.kv.namespaces.with_raw_response.update(
                "0f2ac74b498b48028cb68387c421e279",
                account_id="",
                title="My Own Namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.storage.kv.namespaces.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                title="My Own Namespace",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        namespace = client.storage.kv.namespaces.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        namespace = client.storage.kv.namespaces.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.storage.kv.namespaces.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.storage.kv.namespaces.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.storage.kv.namespaces.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        namespace = client.storage.kv.namespaces.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.storage.kv.namespaces.with_raw_response.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = response.parse()
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.storage.kv.namespaces.with_streaming_response.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = response.parse()
            assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.storage.kv.namespaces.with_raw_response.delete(
                "0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.storage.kv.namespaces.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncNamespaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.storage.kv.namespaces.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.storage.kv.namespaces.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.storage.kv.namespaces.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceCreateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.storage.kv.namespaces.with_raw_response.create(
                account_id="",
                title="My Own Namespace",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.storage.kv.namespaces.update(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.storage.kv.namespaces.with_raw_response.update(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.storage.kv.namespaces.with_streaming_response.update(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            title="My Own Namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceUpdateResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.storage.kv.namespaces.with_raw_response.update(
                "0f2ac74b498b48028cb68387c421e279",
                account_id="",
                title="My Own Namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.storage.kv.namespaces.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                title="My Own Namespace",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.storage.kv.namespaces.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.storage.kv.namespaces.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.storage.kv.namespaces.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.storage.kv.namespaces.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[NamespaceListResponse], namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.storage.kv.namespaces.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        namespace = await async_client.storage.kv.namespaces.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.storage.kv.namespaces.with_raw_response.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        namespace = await response.parse()
        assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.storage.kv.namespaces.with_streaming_response.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            namespace = await response.parse()
            assert_matches_type(NamespaceDeleteResponse, namespace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.storage.kv.namespaces.with_raw_response.delete(
                "0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.storage.kv.namespaces.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
