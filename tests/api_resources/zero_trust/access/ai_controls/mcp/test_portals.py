# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.access.ai_controls.mcp.portals import (
    PortalListResponse,
    PortalReadResponse,
    PortalCreateResponse,
    PortalDeleteResponse,
    PortalUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        portal = client.zero_trust.access.ai_controls.mcp.portals.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-portal",
            hostname="exmaple.com",
            name="My MCP Portal",
        )
        assert_matches_type(PortalCreateResponse, portal, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        portal = client.zero_trust.access.ai_controls.mcp.portals.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-portal",
            hostname="exmaple.com",
            name="My MCP Portal",
            description="This is my custom MCP Portal",
            servers=[
                {
                    "server_id": "my-mcp-server",
                    "default_disabled": True,
                    "on_behalf": True,
                    "updated_prompts": [
                        {
                            "name": "name",
                            "description": "description",
                            "enabled": True,
                        }
                    ],
                    "updated_tools": [
                        {
                            "name": "name",
                            "description": "description",
                            "enabled": True,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(PortalCreateResponse, portal, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-portal",
            hostname="exmaple.com",
            name="My MCP Portal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(PortalCreateResponse, portal, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-portal",
            hostname="exmaple.com",
            name="My MCP Portal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(PortalCreateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.create(
                account_id="",
                id="my-mcp-portal",
                hostname="exmaple.com",
                name="My MCP Portal",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        portal = client.zero_trust.access.ai_controls.mcp.portals.update(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(PortalUpdateResponse, portal, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        portal = client.zero_trust.access.ai_controls.mcp.portals.update(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            description="This is my custom MCP Portal",
            hostname="exmaple.com",
            name="My MCP Portal",
            servers=[
                {
                    "server_id": "my-mcp-server",
                    "default_disabled": True,
                    "on_behalf": True,
                    "updated_prompts": [
                        {
                            "name": "name",
                            "description": "description",
                            "enabled": True,
                        }
                    ],
                    "updated_tools": [
                        {
                            "name": "name",
                            "description": "description",
                            "enabled": True,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(PortalUpdateResponse, portal, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.update(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(PortalUpdateResponse, portal, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.update(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(PortalUpdateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.update(
                id="my-mcp-portal",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.update(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        portal = client.zero_trust.access.ai_controls.mcp.portals.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(SyncV4PagePaginationArray[PortalListResponse], portal, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        portal = client.zero_trust.access.ai_controls.mcp.portals.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[PortalListResponse], portal, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[PortalListResponse], portal, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[PortalListResponse], portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        portal = client.zero_trust.access.ai_controls.mcp.portals.delete(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(PortalDeleteResponse, portal, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.delete(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(PortalDeleteResponse, portal, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.delete(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(PortalDeleteResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.delete(
                id="my-mcp-portal",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.delete(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    def test_method_read(self, client: Cloudflare) -> None:
        portal = client.zero_trust.access.ai_controls.mcp.portals.read(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(PortalReadResponse, portal, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.read(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = response.parse()
        assert_matches_type(PortalReadResponse, portal, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.read(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = response.parse()
            assert_matches_type(PortalReadResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.read(
                id="my-mcp-portal",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.read(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )


class TestAsyncPortals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        portal = await async_client.zero_trust.access.ai_controls.mcp.portals.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-portal",
            hostname="exmaple.com",
            name="My MCP Portal",
        )
        assert_matches_type(PortalCreateResponse, portal, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        portal = await async_client.zero_trust.access.ai_controls.mcp.portals.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-portal",
            hostname="exmaple.com",
            name="My MCP Portal",
            description="This is my custom MCP Portal",
            servers=[
                {
                    "server_id": "my-mcp-server",
                    "default_disabled": True,
                    "on_behalf": True,
                    "updated_prompts": [
                        {
                            "name": "name",
                            "description": "description",
                            "enabled": True,
                        }
                    ],
                    "updated_tools": [
                        {
                            "name": "name",
                            "description": "description",
                            "enabled": True,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(PortalCreateResponse, portal, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-portal",
            hostname="exmaple.com",
            name="My MCP Portal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(PortalCreateResponse, portal, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-portal",
            hostname="exmaple.com",
            name="My MCP Portal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(PortalCreateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.create(
                account_id="",
                id="my-mcp-portal",
                hostname="exmaple.com",
                name="My MCP Portal",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        portal = await async_client.zero_trust.access.ai_controls.mcp.portals.update(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(PortalUpdateResponse, portal, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        portal = await async_client.zero_trust.access.ai_controls.mcp.portals.update(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            description="This is my custom MCP Portal",
            hostname="exmaple.com",
            name="My MCP Portal",
            servers=[
                {
                    "server_id": "my-mcp-server",
                    "default_disabled": True,
                    "on_behalf": True,
                    "updated_prompts": [
                        {
                            "name": "name",
                            "description": "description",
                            "enabled": True,
                        }
                    ],
                    "updated_tools": [
                        {
                            "name": "name",
                            "description": "description",
                            "enabled": True,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(PortalUpdateResponse, portal, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.update(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(PortalUpdateResponse, portal, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.update(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(PortalUpdateResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.update(
                id="my-mcp-portal",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.update(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        portal = await async_client.zero_trust.access.ai_controls.mcp.portals.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(AsyncV4PagePaginationArray[PortalListResponse], portal, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        portal = await async_client.zero_trust.access.ai_controls.mcp.portals.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[PortalListResponse], portal, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[PortalListResponse], portal, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[PortalListResponse], portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        portal = await async_client.zero_trust.access.ai_controls.mcp.portals.delete(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(PortalDeleteResponse, portal, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.delete(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(PortalDeleteResponse, portal, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.delete(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(PortalDeleteResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.delete(
                id="my-mcp-portal",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.delete(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    async def test_method_read(self, async_client: AsyncCloudflare) -> None:
        portal = await async_client.zero_trust.access.ai_controls.mcp.portals.read(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(PortalReadResponse, portal, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.read(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portal = await response.parse()
        assert_matches_type(PortalReadResponse, portal, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.portals.with_streaming_response.read(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portal = await response.parse()
            assert_matches_type(PortalReadResponse, portal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.read(
                id="my-mcp-portal",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.portals.with_raw_response.read(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )
