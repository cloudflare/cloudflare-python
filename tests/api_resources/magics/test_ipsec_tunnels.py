# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.magics import (
    IpsecTunnelUpdateResponse,
    IpsecTunnelDeleteResponse,
    IpsecTunnelGetResponse,
    IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse,
    IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse,
    IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magics import ipsec_tunnel_update_params
from cloudflare.types.magics import ipsec_tunnel_magic_i_psec_tunnels_create_i_psec_tunnels_params
from cloudflare.types.magics import ipsec_tunnel_magic_i_psec_tunnels_update_multiple_i_psec_tunnels_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIpsecTunnels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magics.ipsec_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IpsecTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magics.ipsec_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
        )
        assert_matches_type(IpsecTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magics.ipsec_tunnels.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IpsecTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magics.ipsec_tunnels.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IpsecTunnelUpdateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.ipsec_tunnels.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magics.ipsec_tunnels.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magics.ipsec_tunnels.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IpsecTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magics.ipsec_tunnels.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IpsecTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magics.ipsec_tunnels.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IpsecTunnelDeleteResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.ipsec_tunnels.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magics.ipsec_tunnels.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magics.ipsec_tunnels.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IpsecTunnelGetResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magics.ipsec_tunnels.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IpsecTunnelGetResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magics.ipsec_tunnels.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IpsecTunnelGetResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.ipsec_tunnels.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magics.ipsec_tunnels.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_i_psec_tunnels_create_i_psec_tunnels(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magics.ipsec_tunnels.magic_i_psec_tunnels_create_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_i_psec_tunnels_create_i_psec_tunnels_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magics.ipsec_tunnels.magic_i_psec_tunnels_create_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
        )
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_i_psec_tunnels_create_i_psec_tunnels(self, client: Cloudflare) -> None:
        response = client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_create_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_i_psec_tunnels_create_i_psec_tunnels(self, client: Cloudflare) -> None:
        with client.magics.ipsec_tunnels.with_streaming_response.magic_i_psec_tunnels_create_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_i_psec_tunnels_create_i_psec_tunnels(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_create_i_psec_tunnels(
                "",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_i_psec_tunnels_list_i_psec_tunnels(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magics.ipsec_tunnels.magic_i_psec_tunnels_list_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_i_psec_tunnels_list_i_psec_tunnels(self, client: Cloudflare) -> None:
        response = client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_list_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_i_psec_tunnels_list_i_psec_tunnels(self, client: Cloudflare) -> None:
        with client.magics.ipsec_tunnels.with_streaming_response.magic_i_psec_tunnels_list_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_i_psec_tunnels_list_i_psec_tunnels(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_list_i_psec_tunnels(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_i_psec_tunnels_update_multiple_i_psec_tunnels(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magics.ipsec_tunnels.magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(
            IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse, ipsec_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_i_psec_tunnels_update_multiple_i_psec_tunnels(self, client: Cloudflare) -> None:
        response = client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(
            IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse, ipsec_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_i_psec_tunnels_update_multiple_i_psec_tunnels(self, client: Cloudflare) -> None:
        with client.magics.ipsec_tunnels.with_streaming_response.magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(
                IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse, ipsec_tunnel, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_i_psec_tunnels_update_multiple_i_psec_tunnels(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
                "",
                body={},
            )


class TestAsyncIpsecTunnels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magics.ipsec_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IpsecTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magics.ipsec_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
        )
        assert_matches_type(IpsecTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.ipsec_tunnels.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IpsecTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.ipsec_tunnels.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IpsecTunnelUpdateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magics.ipsec_tunnels.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IpsecTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.ipsec_tunnels.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IpsecTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.ipsec_tunnels.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IpsecTunnelDeleteResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magics.ipsec_tunnels.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IpsecTunnelGetResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.ipsec_tunnels.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IpsecTunnelGetResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magics.ipsec_tunnels.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IpsecTunnelGetResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_i_psec_tunnels_create_i_psec_tunnels(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magics.ipsec_tunnels.magic_i_psec_tunnels_create_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_i_psec_tunnels_create_i_psec_tunnels_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        ipsec_tunnel = await async_client.magics.ipsec_tunnels.magic_i_psec_tunnels_create_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
        )
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_i_psec_tunnels_create_i_psec_tunnels(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_create_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_i_psec_tunnels_create_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.magics.ipsec_tunnels.with_streaming_response.magic_i_psec_tunnels_create_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IpsecTunnelMagicIPsecTunnelsCreateIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_i_psec_tunnels_create_i_psec_tunnels(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_create_i_psec_tunnels(
                "",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_i_psec_tunnels_list_i_psec_tunnels(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magics.ipsec_tunnels.magic_i_psec_tunnels_list_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_i_psec_tunnels_list_i_psec_tunnels(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_list_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_i_psec_tunnels_list_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.magics.ipsec_tunnels.with_streaming_response.magic_i_psec_tunnels_list_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IpsecTunnelMagicIPsecTunnelsListIPsecTunnelsResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_i_psec_tunnels_list_i_psec_tunnels(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_list_i_psec_tunnels(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        ipsec_tunnel = await async_client.magics.ipsec_tunnels.magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(
            IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse, ipsec_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(
            IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse, ipsec_tunnel, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.magics.ipsec_tunnels.with_streaming_response.magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(
                IpsecTunnelMagicIPsecTunnelsUpdateMultipleIPsecTunnelsResponse, ipsec_tunnel, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await (
                async_client.magics.ipsec_tunnels.with_raw_response.magic_i_psec_tunnels_update_multiple_i_psec_tunnels(
                    "",
                    body={},
                )
            )
