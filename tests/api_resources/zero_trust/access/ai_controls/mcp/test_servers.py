# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.access.ai_controls.mcp import (
    ServerListResponse,
    ServerReadResponse,
    ServerCreateResponse,
    ServerDeleteResponse,
    ServerUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        server = client.zero_trust.access.ai_controls.mcp.servers.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-server",
            auth_type="unauthenticated",
            hostname="https://exmaple.com/mcp",
            name="My MCP Server",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        server = client.zero_trust.access.ai_controls.mcp.servers.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-server",
            auth_type="unauthenticated",
            hostname="https://exmaple.com/mcp",
            name="My MCP Server",
            auth_credentials="auth_credentials",
            description="This is one remote mcp server",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-server",
            auth_type="unauthenticated",
            hostname="https://exmaple.com/mcp",
            name="My MCP Server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-server",
            auth_type="unauthenticated",
            hostname="https://exmaple.com/mcp",
            name="My MCP Server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerCreateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.create(
                account_id="",
                id="my-mcp-server",
                auth_type="unauthenticated",
                hostname="https://exmaple.com/mcp",
                name="My MCP Server",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        server = client.zero_trust.access.ai_controls.mcp.servers.update(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        server = client.zero_trust.access.ai_controls.mcp.servers.update(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            auth_credentials="auth_credentials",
            description="This is one remote mcp server",
            name="My MCP Server",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.update(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.update(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.update(
                id="my-mcp-server",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.update(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        server = client.zero_trust.access.ai_controls.mcp.servers.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(SyncV4PagePaginationArray[ServerListResponse], server, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        server = client.zero_trust.access.ai_controls.mcp.servers.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[ServerListResponse], server, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ServerListResponse], server, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[ServerListResponse], server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        server = client.zero_trust.access.ai_controls.mcp.servers.delete(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.delete(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.delete(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerDeleteResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.delete(
                id="my-mcp-server",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.delete(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    def test_method_read(self, client: Cloudflare) -> None:
        server = client.zero_trust.access.ai_controls.mcp.servers.read(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(ServerReadResponse, server, path=["response"])

    @parametrize
    def test_raw_response_read(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.read(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(ServerReadResponse, server, path=["response"])

    @parametrize
    def test_streaming_response_read(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.read(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(ServerReadResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_read(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.read(
                id="my-mcp-server",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.read(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    def test_method_sync(self, client: Cloudflare) -> None:
        server = client.zero_trust.access.ai_controls.mcp.servers.sync(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(object, server, path=["response"])

    @parametrize
    def test_raw_response_sync(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.sync(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = response.parse()
        assert_matches_type(object, server, path=["response"])

    @parametrize
    def test_streaming_response_sync(self, client: Cloudflare) -> None:
        with client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.sync(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sync(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.sync(
                id="my-mcp-portal",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.sync(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )


class TestAsyncServers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        server = await async_client.zero_trust.access.ai_controls.mcp.servers.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-server",
            auth_type="unauthenticated",
            hostname="https://exmaple.com/mcp",
            name="My MCP Server",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        server = await async_client.zero_trust.access.ai_controls.mcp.servers.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-server",
            auth_type="unauthenticated",
            hostname="https://exmaple.com/mcp",
            name="My MCP Server",
            auth_credentials="auth_credentials",
            description="This is one remote mcp server",
        )
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-server",
            auth_type="unauthenticated",
            hostname="https://exmaple.com/mcp",
            name="My MCP Server",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerCreateResponse, server, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.create(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            id="my-mcp-server",
            auth_type="unauthenticated",
            hostname="https://exmaple.com/mcp",
            name="My MCP Server",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerCreateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.create(
                account_id="",
                id="my-mcp-server",
                auth_type="unauthenticated",
                hostname="https://exmaple.com/mcp",
                name="My MCP Server",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        server = await async_client.zero_trust.access.ai_controls.mcp.servers.update(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        server = await async_client.zero_trust.access.ai_controls.mcp.servers.update(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            auth_credentials="auth_credentials",
            description="This is one remote mcp server",
            name="My MCP Server",
        )
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.update(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerUpdateResponse, server, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.update(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerUpdateResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.update(
                id="my-mcp-server",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.update(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        server = await async_client.zero_trust.access.ai_controls.mcp.servers.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ServerListResponse], server, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        server = await async_client.zero_trust.access.ai_controls.mcp.servers.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ServerListResponse], server, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ServerListResponse], server, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.list(
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[ServerListResponse], server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        server = await async_client.zero_trust.access.ai_controls.mcp.servers.delete(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.delete(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerDeleteResponse, server, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.delete(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerDeleteResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.delete(
                id="my-mcp-server",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.delete(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    async def test_method_read(self, async_client: AsyncCloudflare) -> None:
        server = await async_client.zero_trust.access.ai_controls.mcp.servers.read(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(ServerReadResponse, server, path=["response"])

    @parametrize
    async def test_raw_response_read(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.read(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(ServerReadResponse, server, path=["response"])

    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.read(
            id="my-mcp-server",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(ServerReadResponse, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_read(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.read(
                id="my-mcp-server",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.read(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )

    @parametrize
    async def test_method_sync(self, async_client: AsyncCloudflare) -> None:
        server = await async_client.zero_trust.access.ai_controls.mcp.servers.sync(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )
        assert_matches_type(object, server, path=["response"])

    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.sync(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        server = await response.parse()
        assert_matches_type(object, server, path=["response"])

    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.ai_controls.mcp.servers.with_streaming_response.sync(
            id="my-mcp-portal",
            account_id="a86a8f5c339544d7bdc89926de14fb8c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            server = await response.parse()
            assert_matches_type(object, server, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sync(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.sync(
                id="my-mcp-portal",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.zero_trust.access.ai_controls.mcp.servers.with_raw_response.sync(
                id="",
                account_id="a86a8f5c339544d7bdc89926de14fb8c",
            )
