# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.teamnets import (
    VirtualNetworkDeleteResponse,
    VirtualNetworkUpdateResponse,
    VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse,
    VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVirtualNetworks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        virtual_network = client.teamnets.virtual_networks.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(VirtualNetworkUpdateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        virtual_network = client.teamnets.virtual_networks.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="Staging VPC for data science",
            is_default_network=True,
            name="us-east-1-vpc",
        )
        assert_matches_type(VirtualNetworkUpdateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.teamnets.virtual_networks.with_raw_response.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = response.parse()
        assert_matches_type(VirtualNetworkUpdateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.teamnets.virtual_networks.with_streaming_response.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = response.parse()
            assert_matches_type(VirtualNetworkUpdateResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.teamnets.virtual_networks.with_raw_response.update(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `virtual_network_id` but received ''"):
            client.teamnets.virtual_networks.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        virtual_network = client.teamnets.virtual_networks.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.teamnets.virtual_networks.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = response.parse()
        assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.teamnets.virtual_networks.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = response.parse()
            assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.teamnets.virtual_networks.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `virtual_network_id` but received ''"):
            client.teamnets.virtual_networks.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_tunnel_virtual_network_create_a_virtual_network(self, client: Cloudflare) -> None:
        virtual_network = client.teamnets.virtual_networks.tunnel_virtual_network_create_a_virtual_network(
            "699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        )
        assert_matches_type(
            VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse, virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_tunnel_virtual_network_create_a_virtual_network_with_all_params(self, client: Cloudflare) -> None:
        virtual_network = client.teamnets.virtual_networks.tunnel_virtual_network_create_a_virtual_network(
            "699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
            comment="Staging VPC for data science",
            is_default=True,
        )
        assert_matches_type(
            VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse, virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tunnel_virtual_network_create_a_virtual_network(self, client: Cloudflare) -> None:
        response = client.teamnets.virtual_networks.with_raw_response.tunnel_virtual_network_create_a_virtual_network(
            "699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = response.parse()
        assert_matches_type(
            VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse, virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tunnel_virtual_network_create_a_virtual_network(self, client: Cloudflare) -> None:
        with client.teamnets.virtual_networks.with_streaming_response.tunnel_virtual_network_create_a_virtual_network(
            "699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = response.parse()
            assert_matches_type(
                VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse, virtual_network, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_tunnel_virtual_network_create_a_virtual_network(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.teamnets.virtual_networks.with_raw_response.tunnel_virtual_network_create_a_virtual_network(
                "",
                name="us-east-1-vpc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_tunnel_virtual_network_list_virtual_networks(self, client: Cloudflare) -> None:
        virtual_network = client.teamnets.virtual_networks.tunnel_virtual_network_list_virtual_networks(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse], virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_tunnel_virtual_network_list_virtual_networks_with_all_params(self, client: Cloudflare) -> None:
        virtual_network = client.teamnets.virtual_networks.tunnel_virtual_network_list_virtual_networks(
            "699d98642c564d2e855e9661899b7252",
            is_default={},
            is_deleted={},
            name="us-east-1-vpc",
            vnet_name="us-east-1-vpc",
        )
        assert_matches_type(
            Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse], virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tunnel_virtual_network_list_virtual_networks(self, client: Cloudflare) -> None:
        response = client.teamnets.virtual_networks.with_raw_response.tunnel_virtual_network_list_virtual_networks(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = response.parse()
        assert_matches_type(
            Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse], virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tunnel_virtual_network_list_virtual_networks(self, client: Cloudflare) -> None:
        with client.teamnets.virtual_networks.with_streaming_response.tunnel_virtual_network_list_virtual_networks(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = response.parse()
            assert_matches_type(
                Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse],
                virtual_network,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_tunnel_virtual_network_list_virtual_networks(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.teamnets.virtual_networks.with_raw_response.tunnel_virtual_network_list_virtual_networks(
                "",
            )


class TestAsyncVirtualNetworks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.teamnets.virtual_networks.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(VirtualNetworkUpdateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.teamnets.virtual_networks.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            comment="Staging VPC for data science",
            is_default_network=True,
            name="us-east-1-vpc",
        )
        assert_matches_type(VirtualNetworkUpdateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.teamnets.virtual_networks.with_raw_response.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = await response.parse()
        assert_matches_type(VirtualNetworkUpdateResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.teamnets.virtual_networks.with_streaming_response.update(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = await response.parse()
            assert_matches_type(VirtualNetworkUpdateResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.teamnets.virtual_networks.with_raw_response.update(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `virtual_network_id` but received ''"):
            await async_client.teamnets.virtual_networks.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.teamnets.virtual_networks.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.teamnets.virtual_networks.with_raw_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = await response.parse()
        assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.teamnets.virtual_networks.with_streaming_response.delete(
            "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = await response.parse()
            assert_matches_type(VirtualNetworkDeleteResponse, virtual_network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.teamnets.virtual_networks.with_raw_response.delete(
                "f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `virtual_network_id` but received ''"):
            await async_client.teamnets.virtual_networks.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_tunnel_virtual_network_create_a_virtual_network(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.teamnets.virtual_networks.tunnel_virtual_network_create_a_virtual_network(
            "699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        )
        assert_matches_type(
            VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse, virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_tunnel_virtual_network_create_a_virtual_network_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        virtual_network = await async_client.teamnets.virtual_networks.tunnel_virtual_network_create_a_virtual_network(
            "699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
            comment="Staging VPC for data science",
            is_default=True,
        )
        assert_matches_type(
            VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse, virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tunnel_virtual_network_create_a_virtual_network(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.teamnets.virtual_networks.with_raw_response.tunnel_virtual_network_create_a_virtual_network(
            "699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = await response.parse()
        assert_matches_type(
            VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse, virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tunnel_virtual_network_create_a_virtual_network(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.teamnets.virtual_networks.with_streaming_response.tunnel_virtual_network_create_a_virtual_network(
            "699d98642c564d2e855e9661899b7252",
            name="us-east-1-vpc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = await response.parse()
            assert_matches_type(
                VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkResponse, virtual_network, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_tunnel_virtual_network_create_a_virtual_network(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.teamnets.virtual_networks.with_raw_response.tunnel_virtual_network_create_a_virtual_network(
                "",
                name="us-east-1-vpc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_tunnel_virtual_network_list_virtual_networks(self, async_client: AsyncCloudflare) -> None:
        virtual_network = await async_client.teamnets.virtual_networks.tunnel_virtual_network_list_virtual_networks(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse], virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_tunnel_virtual_network_list_virtual_networks_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        virtual_network = await async_client.teamnets.virtual_networks.tunnel_virtual_network_list_virtual_networks(
            "699d98642c564d2e855e9661899b7252",
            is_default={},
            is_deleted={},
            name="us-east-1-vpc",
            vnet_name="us-east-1-vpc",
        )
        assert_matches_type(
            Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse], virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tunnel_virtual_network_list_virtual_networks(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.teamnets.virtual_networks.with_raw_response.tunnel_virtual_network_list_virtual_networks(
                "699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        virtual_network = await response.parse()
        assert_matches_type(
            Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse], virtual_network, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tunnel_virtual_network_list_virtual_networks(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.teamnets.virtual_networks.with_streaming_response.tunnel_virtual_network_list_virtual_networks(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            virtual_network = await response.parse()
            assert_matches_type(
                Optional[VirtualNetworkTunnelVirtualNetworkListVirtualNetworksResponse],
                virtual_network,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_tunnel_virtual_network_list_virtual_networks(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.teamnets.virtual_networks.with_raw_response.tunnel_virtual_network_list_virtual_networks(
                "",
            )
