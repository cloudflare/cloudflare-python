# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.aisearch.namespaces.instances import (
    ItemGetResponse,
    ItemListResponse,
    ItemLogsResponse,
    ItemSyncResponse,
    ItemChunksResponse,
    ItemDeleteResponse,
    ItemUploadResponse,
    ItemCreateOrUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
        )
        assert_matches_type(SyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            item_id="item_id",
            metadata_filter="metadata_filter",
            page=1,
            per_page=0,
            search="search",
            sort_by="status",
            source="source",
            status="queued",
        )
        assert_matches_type(SyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.instances.items.with_raw_response.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.instances.items.with_streaming_response.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.list(
                id="my-ai-search",
                account_id="",
                name="my-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.list(
                id="my-ai-search",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.list(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.delete(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.instances.items.with_raw_response.delete(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.instances.items.with_streaming_response.delete(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemDeleteResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.delete(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.delete(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.delete(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.delete(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    def test_method_chunks(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.chunks(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert_matches_type(ItemChunksResponse, item, path=["response"])

    @parametrize
    def test_method_chunks_with_all_params(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.chunks(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            limit=1,
            offset=0,
        )
        assert_matches_type(ItemChunksResponse, item, path=["response"])

    @parametrize
    def test_raw_response_chunks(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.instances.items.with_raw_response.chunks(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemChunksResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_chunks(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.instances.items.with_streaming_response.chunks(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemChunksResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_chunks(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.chunks(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.chunks(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.chunks(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.chunks(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    def test_method_create_or_update(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.create_or_update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            key="key",
            next_action="INDEX",
        )
        assert_matches_type(ItemCreateOrUpdateResponse, item, path=["response"])

    @parametrize
    def test_raw_response_create_or_update(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.instances.items.with_raw_response.create_or_update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            key="key",
            next_action="INDEX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemCreateOrUpdateResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.instances.items.with_streaming_response.create_or_update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            key="key",
            next_action="INDEX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemCreateOrUpdateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_or_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.create_or_update(
                id="my-ai-search",
                account_id="",
                name="my-namespace",
                key="key",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.create_or_update(
                id="my-ai-search",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                key="key",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.create_or_update(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                key="key",
                next_action="INDEX",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/c3dc5f0b34a14ff8e1b3ec04895e1b22/ai-search/namespaces/my-namespace/instances/my-ai-search/items/item_id/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        item = client.aisearch.namespaces.instances.items.download(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert item.is_closed
        assert item.json() == {"foo": "bar"}
        assert cast(Any, item.is_closed) is True
        assert isinstance(item, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/c3dc5f0b34a14ff8e1b3ec04895e1b22/ai-search/namespaces/my-namespace/instances/my-ai-search/items/item_id/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        item = client.aisearch.namespaces.instances.items.with_raw_response.download(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert item.is_closed is True
        assert item.http_request.headers.get("X-Stainless-Lang") == "python"
        assert item.json() == {"foo": "bar"}
        assert isinstance(item, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/c3dc5f0b34a14ff8e1b3ec04895e1b22/ai-search/namespaces/my-namespace/instances/my-ai-search/items/item_id/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.aisearch.namespaces.instances.items.with_streaming_response.download(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as item:
            assert not item.is_closed
            assert item.http_request.headers.get("X-Stainless-Lang") == "python"

            assert item.json() == {"foo": "bar"}
            assert cast(Any, item.is_closed) is True
            assert isinstance(item, StreamedBinaryAPIResponse)

        assert cast(Any, item.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.download(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.download(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.download(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.download(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.instances.items.with_raw_response.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.instances.items.with_streaming_response.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemGetResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.get(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    def test_method_logs(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.logs(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert_matches_type(ItemLogsResponse, item, path=["response"])

    @parametrize
    def test_method_logs_with_all_params(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.logs(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ItemLogsResponse, item, path=["response"])

    @parametrize
    def test_raw_response_logs(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.instances.items.with_raw_response.logs(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemLogsResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_logs(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.instances.items.with_streaming_response.logs(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemLogsResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_logs(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.logs(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.logs(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.logs(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.logs(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    def test_method_sync(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.sync(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            next_action="INDEX",
        )
        assert_matches_type(ItemSyncResponse, item, path=["response"])

    @parametrize
    def test_raw_response_sync(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.instances.items.with_raw_response.sync(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            next_action="INDEX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemSyncResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_sync(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.instances.items.with_streaming_response.sync(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            next_action="INDEX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemSyncResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sync(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.sync(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.sync(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.sync(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.sync(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
                next_action="INDEX",
            )

    @parametrize
    def test_method_upload(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.upload(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            file={"file": b"Example data"},
        )
        assert_matches_type(ItemUploadResponse, item, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: Cloudflare) -> None:
        item = client.aisearch.namespaces.instances.items.upload(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            file={
                "file": b"Example data",
                "metadata": "metadata",
                "wait_for_completion": True,
            },
        )
        assert_matches_type(ItemUploadResponse, item, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Cloudflare) -> None:
        response = client.aisearch.namespaces.instances.items.with_raw_response.upload(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            file={"file": b"Example data"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemUploadResponse, item, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Cloudflare) -> None:
        with client.aisearch.namespaces.instances.items.with_streaming_response.upload(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            file={"file": b"Example data"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemUploadResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.upload(
                id="my-ai-search",
                account_id="",
                name="my-namespace",
                file={"file": b"Example data"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.upload(
                id="my-ai-search",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                file={"file": b"Example data"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aisearch.namespaces.instances.items.with_raw_response.upload(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                file={"file": b"Example data"},
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            item_id="item_id",
            metadata_filter="metadata_filter",
            page=1,
            per_page=0,
            search="search",
            sort_by="status",
            source="source",
            status="queued",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.instances.items.with_raw_response.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.instances.items.with_streaming_response.list(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[ItemListResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.list(
                id="my-ai-search",
                account_id="",
                name="my-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.list(
                id="my-ai-search",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.list(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.delete(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.instances.items.with_raw_response.delete(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemDeleteResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.instances.items.with_streaming_response.delete(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemDeleteResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.delete(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.delete(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.delete(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.delete(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    async def test_method_chunks(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.chunks(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert_matches_type(ItemChunksResponse, item, path=["response"])

    @parametrize
    async def test_method_chunks_with_all_params(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.chunks(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            limit=1,
            offset=0,
        )
        assert_matches_type(ItemChunksResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_chunks(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.instances.items.with_raw_response.chunks(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemChunksResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_chunks(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.instances.items.with_streaming_response.chunks(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemChunksResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_chunks(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.chunks(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.chunks(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.chunks(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.chunks(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.create_or_update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            key="key",
            next_action="INDEX",
        )
        assert_matches_type(ItemCreateOrUpdateResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.instances.items.with_raw_response.create_or_update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            key="key",
            next_action="INDEX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemCreateOrUpdateResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.instances.items.with_streaming_response.create_or_update(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            key="key",
            next_action="INDEX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemCreateOrUpdateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_or_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.create_or_update(
                id="my-ai-search",
                account_id="",
                name="my-namespace",
                key="key",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.create_or_update(
                id="my-ai-search",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                key="key",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.create_or_update(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                key="key",
                next_action="INDEX",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/c3dc5f0b34a14ff8e1b3ec04895e1b22/ai-search/namespaces/my-namespace/instances/my-ai-search/items/item_id/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        item = await async_client.aisearch.namespaces.instances.items.download(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert item.is_closed
        assert await item.json() == {"foo": "bar"}
        assert cast(Any, item.is_closed) is True
        assert isinstance(item, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/c3dc5f0b34a14ff8e1b3ec04895e1b22/ai-search/namespaces/my-namespace/instances/my-ai-search/items/item_id/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        item = await async_client.aisearch.namespaces.instances.items.with_raw_response.download(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert item.is_closed is True
        assert item.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await item.json() == {"foo": "bar"}
        assert isinstance(item, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/c3dc5f0b34a14ff8e1b3ec04895e1b22/ai-search/namespaces/my-namespace/instances/my-ai-search/items/item_id/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.aisearch.namespaces.instances.items.with_streaming_response.download(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as item:
            assert not item.is_closed
            assert item.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await item.json() == {"foo": "bar"}
            assert cast(Any, item.is_closed) is True
            assert isinstance(item, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, item.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.download(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.download(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.download(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.download(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.instances.items.with_raw_response.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemGetResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.instances.items.with_streaming_response.get(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemGetResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.get(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.get(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    async def test_method_logs(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.logs(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )
        assert_matches_type(ItemLogsResponse, item, path=["response"])

    @parametrize
    async def test_method_logs_with_all_params(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.logs(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(ItemLogsResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_logs(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.instances.items.with_raw_response.logs(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemLogsResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_logs(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.instances.items.with_streaming_response.logs(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemLogsResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_logs(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.logs(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.logs(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.logs(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.logs(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
            )

    @parametrize
    async def test_method_sync(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.sync(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            next_action="INDEX",
        )
        assert_matches_type(ItemSyncResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.instances.items.with_raw_response.sync(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            next_action="INDEX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemSyncResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.instances.items.with_streaming_response.sync(
            item_id="item_id",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            id="my-ai-search",
            next_action="INDEX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemSyncResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sync(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.sync(
                item_id="item_id",
                account_id="",
                name="my-namespace",
                id="my-ai-search",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.sync(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                id="my-ai-search",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.sync(
                item_id="item_id",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="",
                next_action="INDEX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.sync(
                item_id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                id="my-ai-search",
                next_action="INDEX",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.upload(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            file={"file": b"Example data"},
        )
        assert_matches_type(ItemUploadResponse, item, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.aisearch.namespaces.instances.items.upload(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            file={
                "file": b"Example data",
                "metadata": "metadata",
                "wait_for_completion": True,
            },
        )
        assert_matches_type(ItemUploadResponse, item, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.aisearch.namespaces.instances.items.with_raw_response.upload(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            file={"file": b"Example data"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemUploadResponse, item, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncCloudflare) -> None:
        async with async_client.aisearch.namespaces.instances.items.with_streaming_response.upload(
            id="my-ai-search",
            account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
            name="my-namespace",
            file={"file": b"Example data"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemUploadResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.upload(
                id="my-ai-search",
                account_id="",
                name="my-namespace",
                file={"file": b"Example data"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.upload(
                id="my-ai-search",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="",
                file={"file": b"Example data"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aisearch.namespaces.instances.items.with_raw_response.upload(
                id="",
                account_id="c3dc5f0b34a14ff8e1b3ec04895e1b22",
                name="my-namespace",
                file={"file": b"Example data"},
            )
