# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.cfd_tunnels import (
    ConnectionDeleteResponse,
    ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cfd_tunnels import connection_delete_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        connection = client.cfd_tunnels.connections.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        connection = client.cfd_tunnels.connections.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
            client_id="string",
        )
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cfd_tunnels.connections.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cfd_tunnels.connections.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cfd_tunnels.connections.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.cfd_tunnels.connections.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_cloudflare_tunnel_list_cloudflare_tunnel_connections(self, client: Cloudflare) -> None:
        connection = client.cfd_tunnels.connections.cloudflare_tunnel_list_cloudflare_tunnel_connections(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cloudflare_tunnel_list_cloudflare_tunnel_connections(self, client: Cloudflare) -> None:
        response = (
            client.cfd_tunnels.connections.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnel_connections(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(
            Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cloudflare_tunnel_list_cloudflare_tunnel_connections(self, client: Cloudflare) -> None:
        with client.cfd_tunnels.connections.with_streaming_response.cloudflare_tunnel_list_cloudflare_tunnel_connections(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(
                Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse],
                connection,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cloudflare_tunnel_list_cloudflare_tunnel_connections(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cfd_tunnels.connections.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnel_connections(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.cfd_tunnels.connections.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnel_connections(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        connection = await async_client.cfd_tunnels.connections.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        connection = await async_client.cfd_tunnels.connections.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
            client_id="string",
        )
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cfd_tunnels.connections.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cfd_tunnels.connections.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cfd_tunnels.connections.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.cfd_tunnels.connections.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_cloudflare_tunnel_list_cloudflare_tunnel_connections(
        self, async_client: AsyncCloudflare
    ) -> None:
        connection = await async_client.cfd_tunnels.connections.cloudflare_tunnel_list_cloudflare_tunnel_connections(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cloudflare_tunnel_list_cloudflare_tunnel_connections(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.cfd_tunnels.connections.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnel_connections(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(
            Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse], connection, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cloudflare_tunnel_list_cloudflare_tunnel_connections(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.cfd_tunnels.connections.with_streaming_response.cloudflare_tunnel_list_cloudflare_tunnel_connections(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(
                Optional[ConnectionCloudflareTunnelListCloudflareTunnelConnectionsResponse],
                connection,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cloudflare_tunnel_list_cloudflare_tunnel_connections(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cfd_tunnels.connections.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnel_connections(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.cfd_tunnels.connections.with_raw_response.cloudflare_tunnel_list_cloudflare_tunnel_connections(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )
