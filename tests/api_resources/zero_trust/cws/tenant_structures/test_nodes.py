# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.zero_trust.cws.tenant_structures import (
    NodeBatchResponse,
    NodeDeleteResponse,
    TenantStructureNode,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        node = client.zero_trust.cws.tenant_structures.nodes.create(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            native_id="x",
            node_kind="x",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        node = client.zero_trust.cws.tenant_structures.nodes.create(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            native_id="x",
            node_kind="x",
            name="name",
            parent="parent",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.tenant_structures.nodes.with_raw_response.create(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            native_id="x",
            node_kind="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.create(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            native_id="x",
            node_kind="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(TenantStructureNode, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.create(
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                native_id="x",
                node_kind="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.create(
                structure_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                native_id="x",
                node_kind="x",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        node = client.zero_trust.cws.tenant_structures.nodes.update(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            native_id="x",
            node_kind="x",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        node = client.zero_trust.cws.tenant_structures.nodes.update(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            native_id="x",
            node_kind="x",
            name="name",
            parent="parent",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.tenant_structures.nodes.with_raw_response.update(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            native_id="x",
            node_kind="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.update(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            native_id="x",
            node_kind="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(TenantStructureNode, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.update(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                native_id="x",
                node_kind="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.update(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="",
                native_id="x",
                node_kind="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.update(
                node_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                native_id="x",
                node_kind="x",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        node = client.zero_trust.cws.tenant_structures.nodes.list(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(SyncCursorPagination[TenantStructureNode], node, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        node = client.zero_trust.cws.tenant_structures.nodes.list(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            direction="asc",
            name="name",
            native_id="native_id",
            node_kind="node_kind",
            order="name",
            parent="parent",
            per_page=1,
        )
        assert_matches_type(SyncCursorPagination[TenantStructureNode], node, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.tenant_structures.nodes.with_raw_response.list(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(SyncCursorPagination[TenantStructureNode], node, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.list(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(SyncCursorPagination[TenantStructureNode], node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.list(
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.list(
                structure_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        node = client.zero_trust.cws.tenant_structures.nodes.delete(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.tenant_structures.nodes.with_raw_response.delete(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.delete(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(NodeDeleteResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.delete(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.delete(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.delete(
                node_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_batch(self, client: Cloudflare) -> None:
        node = client.zero_trust.cws.tenant_structures.nodes.batch(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            creates=[
                {
                    "native_id": "x",
                    "node_kind": "x",
                }
            ],
            deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(NodeBatchResponse, node, path=["response"])

    @parametrize
    def test_raw_response_batch(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.tenant_structures.nodes.with_raw_response.batch(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            creates=[
                {
                    "native_id": "x",
                    "node_kind": "x",
                }
            ],
            deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(NodeBatchResponse, node, path=["response"])

    @parametrize
    def test_streaming_response_batch(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.batch(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            creates=[
                {
                    "native_id": "x",
                    "node_kind": "x",
                }
            ],
            deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(NodeBatchResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_batch(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.batch(
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                creates=[
                    {
                        "native_id": "x",
                        "node_kind": "x",
                    }
                ],
                deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.batch(
                structure_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                creates=[
                    {
                        "native_id": "x",
                        "node_kind": "x",
                    }
                ],
                deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        node = client.zero_trust.cws.tenant_structures.nodes.get(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.cws.tenant_structures.nodes.with_raw_response.get(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = response.parse()
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.get(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = response.parse()
            assert_matches_type(TenantStructureNode, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.get(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.get(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            client.zero_trust.cws.tenant_structures.nodes.with_raw_response.get(
                node_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncNodes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        node = await async_client.zero_trust.cws.tenant_structures.nodes.create(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            native_id="x",
            node_kind="x",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        node = await async_client.zero_trust.cws.tenant_structures.nodes.create(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            native_id="x",
            node_kind="x",
            name="name",
            parent="parent",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.create(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            native_id="x",
            node_kind="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.create(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            native_id="x",
            node_kind="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(TenantStructureNode, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.create(
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                native_id="x",
                node_kind="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.create(
                structure_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                native_id="x",
                node_kind="x",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        node = await async_client.zero_trust.cws.tenant_structures.nodes.update(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            native_id="x",
            node_kind="x",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        node = await async_client.zero_trust.cws.tenant_structures.nodes.update(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            native_id="x",
            node_kind="x",
            name="name",
            parent="parent",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.update(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            native_id="x",
            node_kind="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.update(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            native_id="x",
            node_kind="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(TenantStructureNode, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.update(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                native_id="x",
                node_kind="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.update(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="",
                native_id="x",
                node_kind="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.update(
                node_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                native_id="x",
                node_kind="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        node = await async_client.zero_trust.cws.tenant_structures.nodes.list(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(AsyncCursorPagination[TenantStructureNode], node, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        node = await async_client.zero_trust.cws.tenant_structures.nodes.list(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            cursor="cursor",
            direction="asc",
            name="name",
            native_id="native_id",
            node_kind="node_kind",
            order="name",
            parent="parent",
            per_page=1,
        )
        assert_matches_type(AsyncCursorPagination[TenantStructureNode], node, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.list(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(AsyncCursorPagination[TenantStructureNode], node, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.list(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(AsyncCursorPagination[TenantStructureNode], node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.list(
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.list(
                structure_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        node = await async_client.zero_trust.cws.tenant_structures.nodes.delete(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.delete(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(NodeDeleteResponse, node, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.delete(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(NodeDeleteResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.delete(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.delete(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.delete(
                node_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_batch(self, async_client: AsyncCloudflare) -> None:
        node = await async_client.zero_trust.cws.tenant_structures.nodes.batch(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            creates=[
                {
                    "native_id": "x",
                    "node_kind": "x",
                }
            ],
            deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )
        assert_matches_type(NodeBatchResponse, node, path=["response"])

    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.batch(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            creates=[
                {
                    "native_id": "x",
                    "node_kind": "x",
                }
            ],
            deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(NodeBatchResponse, node, path=["response"])

    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.batch(
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            creates=[
                {
                    "native_id": "x",
                    "node_kind": "x",
                }
            ],
            deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(NodeBatchResponse, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_batch(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.batch(
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                creates=[
                    {
                        "native_id": "x",
                        "node_kind": "x",
                    }
                ],
                deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.batch(
                structure_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                creates=[
                    {
                        "native_id": "x",
                        "node_kind": "x",
                    }
                ],
                deletes=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
                updates=[{"id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        node = await async_client.zero_trust.cws.tenant_structures.nodes.get(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.get(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        node = await response.parse()
        assert_matches_type(TenantStructureNode, node, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.cws.tenant_structures.nodes.with_streaming_response.get(
            node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            node = await response.parse()
            assert_matches_type(TenantStructureNode, node, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.get(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `structure_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.get(
                node_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `node_id` but received ''"):
            await async_client.zero_trust.cws.tenant_structures.nodes.with_raw_response.get(
                node_id="",
                account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                structure_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
