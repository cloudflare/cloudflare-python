# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magics import (
    GreTunnelGetResponse,
    GreTunnelDeleteResponse,
    GreTunnelUpdateResponse,
    GreTunnelMagicGreTunnelsListGreTunnelsResponse,
    GreTunnelMagicGreTunnelsCreateGreTunnelsResponse,
    GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGreTunnels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        gre_tunnel = client.magics.gre_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        )
        assert_matches_type(GreTunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        gre_tunnel = client.magics.gre_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "bidirectional",
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            mtu=0,
            ttl=0,
        )
        assert_matches_type(GreTunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magics.gre_tunnels.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GreTunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magics.gre_tunnels.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GreTunnelUpdateResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.gre_tunnels.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                cloudflare_gre_endpoint="203.0.113.1",
                customer_gre_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="GRE_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magics.gre_tunnels.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_gre_endpoint="203.0.113.1",
                customer_gre_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="GRE_1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        gre_tunnel = client.magics.gre_tunnels.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GreTunnelDeleteResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magics.gre_tunnels.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GreTunnelDeleteResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magics.gre_tunnels.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GreTunnelDeleteResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.gre_tunnels.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magics.gre_tunnels.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        gre_tunnel = client.magics.gre_tunnels.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GreTunnelGetResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magics.gre_tunnels.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GreTunnelGetResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magics.gre_tunnels.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GreTunnelGetResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.gre_tunnels.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magics.gre_tunnels.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_gre_tunnels_create_gre_tunnels(self, client: Cloudflare) -> None:
        gre_tunnel = client.magics.gre_tunnels.magic_gre_tunnels_create_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(GreTunnelMagicGreTunnelsCreateGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_gre_tunnels_create_gre_tunnels(self, client: Cloudflare) -> None:
        response = client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_create_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GreTunnelMagicGreTunnelsCreateGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_gre_tunnels_create_gre_tunnels(self, client: Cloudflare) -> None:
        with client.magics.gre_tunnels.with_streaming_response.magic_gre_tunnels_create_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GreTunnelMagicGreTunnelsCreateGreTunnelsResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_gre_tunnels_create_gre_tunnels(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_create_gre_tunnels(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_gre_tunnels_list_gre_tunnels(self, client: Cloudflare) -> None:
        gre_tunnel = client.magics.gre_tunnels.magic_gre_tunnels_list_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GreTunnelMagicGreTunnelsListGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_gre_tunnels_list_gre_tunnels(self, client: Cloudflare) -> None:
        response = client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_list_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GreTunnelMagicGreTunnelsListGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_gre_tunnels_list_gre_tunnels(self, client: Cloudflare) -> None:
        with client.magics.gre_tunnels.with_streaming_response.magic_gre_tunnels_list_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GreTunnelMagicGreTunnelsListGreTunnelsResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_gre_tunnels_list_gre_tunnels(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_list_gre_tunnels(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_gre_tunnels_update_multiple_gre_tunnels(self, client: Cloudflare) -> None:
        gre_tunnel = client.magics.gre_tunnels.magic_gre_tunnels_update_multiple_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_gre_tunnels_update_multiple_gre_tunnels(self, client: Cloudflare) -> None:
        response = client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_update_multiple_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_gre_tunnels_update_multiple_gre_tunnels(self, client: Cloudflare) -> None:
        with client.magics.gre_tunnels.with_streaming_response.magic_gre_tunnels_update_multiple_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_gre_tunnels_update_multiple_gre_tunnels(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_update_multiple_gre_tunnels(
                "",
                body={},
            )


class TestAsyncGreTunnels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magics.gre_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        )
        assert_matches_type(GreTunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magics.gre_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "bidirectional",
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            mtu=0,
            ttl=0,
        )
        assert_matches_type(GreTunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.gre_tunnels.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GreTunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.gre_tunnels.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GreTunnelUpdateResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.gre_tunnels.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                cloudflare_gre_endpoint="203.0.113.1",
                customer_gre_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="GRE_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magics.gre_tunnels.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_gre_endpoint="203.0.113.1",
                customer_gre_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="GRE_1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magics.gre_tunnels.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GreTunnelDeleteResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.gre_tunnels.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GreTunnelDeleteResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.gre_tunnels.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GreTunnelDeleteResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.gre_tunnels.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magics.gre_tunnels.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magics.gre_tunnels.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GreTunnelGetResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.gre_tunnels.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GreTunnelGetResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.gre_tunnels.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GreTunnelGetResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.gre_tunnels.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magics.gre_tunnels.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_gre_tunnels_create_gre_tunnels(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magics.gre_tunnels.magic_gre_tunnels_create_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(GreTunnelMagicGreTunnelsCreateGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_gre_tunnels_create_gre_tunnels(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_create_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GreTunnelMagicGreTunnelsCreateGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_gre_tunnels_create_gre_tunnels(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.gre_tunnels.with_streaming_response.magic_gre_tunnels_create_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GreTunnelMagicGreTunnelsCreateGreTunnelsResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_gre_tunnels_create_gre_tunnels(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_create_gre_tunnels(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_gre_tunnels_list_gre_tunnels(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magics.gre_tunnels.magic_gre_tunnels_list_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GreTunnelMagicGreTunnelsListGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_gre_tunnels_list_gre_tunnels(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_list_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GreTunnelMagicGreTunnelsListGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_gre_tunnels_list_gre_tunnels(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.gre_tunnels.with_streaming_response.magic_gre_tunnels_list_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GreTunnelMagicGreTunnelsListGreTunnelsResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_gre_tunnels_list_gre_tunnels(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_list_gre_tunnels(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_gre_tunnels_update_multiple_gre_tunnels(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magics.gre_tunnels.magic_gre_tunnels_update_multiple_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_gre_tunnels_update_multiple_gre_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_update_multiple_gre_tunnels(
                "023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_gre_tunnels_update_multiple_gre_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.magics.gre_tunnels.with_streaming_response.magic_gre_tunnels_update_multiple_gre_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_gre_tunnels_update_multiple_gre_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.gre_tunnels.with_raw_response.magic_gre_tunnels_update_multiple_gre_tunnels(
                "",
                body={},
            )
