# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_transit import (
    IPSECTunnelGetResponse,
    IPSECTunnelListResponse,
    IPSECTunnelCreateResponse,
    IPSECTunnelDeleteResponse,
    IPSECTunnelUpdateResponse,
    IPSECTunnelBulkUpdateResponse,
    IPSECTunnelPSKGenerateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPSECTunnels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "unidirectional",
                "enabled": True,
                "rate": "low",
                "target": {"saved": "203.0.113.1"},
                "type": "reply",
            },
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.create(
                account_id="",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.update(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.update(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "unidirectional",
                "enabled": True,
                "rate": "low",
                "target": {"saved": "203.0.113.1"},
                "type": "reply",
            },
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.update(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.update(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.update(
                ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ipsec_tunnel_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.update(
                ipsec_tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.delete(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.delete(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.delete(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.delete(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.delete(
                ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ipsec_tunnel_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.delete(
                ipsec_tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_bulk_update(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(IPSECTunnelBulkUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_bulk_update_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelBulkUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_bulk_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelBulkUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_bulk_update(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelBulkUpdateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_bulk_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.bulk_update(
                account_id="",
                body={},
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.get(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.get(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.get(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.get(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.get(
                ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ipsec_tunnel_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.get(
                ipsec_tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_psk_generate(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.psk_generate(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_raw_response_psk_generate(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    def test_streaming_response_psk_generate(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.psk_generate(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_psk_generate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
                ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ipsec_tunnel_id` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
                ipsec_tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )


class TestAsyncIPSECTunnels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "unidirectional",
                "enabled": True,
                "rate": "low",
                "target": {"saved": "203.0.113.1"},
                "type": "reply",
            },
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.create(
                account_id="",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.update(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.update(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "unidirectional",
                "enabled": True,
                "rate": "low",
                "target": {"saved": "203.0.113.1"},
                "type": "reply",
            },
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.update(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.update(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.update(
                ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ipsec_tunnel_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.update(
                ipsec_tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.delete(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.delete(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.delete(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.delete(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.delete(
                ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ipsec_tunnel_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.delete(
                ipsec_tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(IPSECTunnelBulkUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_bulk_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelBulkUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelBulkUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelBulkUpdateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.bulk_update(
                account_id="",
                body={},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.get(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.get(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            x_magic_new_hc_target=True,
        )
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.get(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.get(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.get(
                ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ipsec_tunnel_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.get(
                ipsec_tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_psk_generate(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.psk_generate(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_raw_response_psk_generate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

    @parametrize
    async def test_streaming_response_psk_generate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.psk_generate(
            ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_psk_generate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
                ipsec_tunnel_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ipsec_tunnel_id` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
                ipsec_tunnel_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )
