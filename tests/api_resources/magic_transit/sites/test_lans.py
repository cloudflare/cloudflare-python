# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_transit.sites import (
    LAN,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLANs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            physport=1,
            vlan_tag=0,
        )
        assert_matches_type(SyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            physport=1,
            vlan_tag=0,
            ha_link=True,
            name="name",
            nat={"static_prefix": "192.0.2.0/24"},
            routed_subnets=[
                {
                    "next_hop": "192.0.2.1",
                    "prefix": "192.0.2.0/24",
                    "nat": {"static_prefix": "192.0.2.0/24"},
                }
            ],
            static_addressing={
                "address": "192.0.2.0/24",
                "dhcp_relay": {"server_addresses": ["192.0.2.1"]},
                "dhcp_server": {
                    "dhcp_pool_end": "192.0.2.1",
                    "dhcp_pool_start": "192.0.2.1",
                    "dns_server": "192.0.2.1",
                    "dns_servers": ["192.0.2.1"],
                    "reservations": {
                        "00:11:22:33:44:55": "192.0.2.100",
                        "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                    },
                },
                "secondary_address": "192.0.2.0/24",
                "virtual_address": "192.0.2.0/24",
            },
        )
        assert_matches_type(SyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            physport=1,
            vlan_tag=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(SyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            physport=1,
            vlan_tag=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(SyncSinglePage[LAN], lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.create(
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                physport=1,
                vlan_tag=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.create(
                site_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                physport=1,
                vlan_tag=0,
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.update(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.update(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            nat={"static_prefix": "192.0.2.0/24"},
            physport=1,
            routed_subnets=[
                {
                    "next_hop": "192.0.2.1",
                    "prefix": "192.0.2.0/24",
                    "nat": {"static_prefix": "192.0.2.0/24"},
                }
            ],
            static_addressing={
                "address": "192.0.2.0/24",
                "dhcp_relay": {"server_addresses": ["192.0.2.1"]},
                "dhcp_server": {
                    "dhcp_pool_end": "192.0.2.1",
                    "dhcp_pool_start": "192.0.2.1",
                    "dns_server": "192.0.2.1",
                    "dns_servers": ["192.0.2.1"],
                    "reservations": {
                        "00:11:22:33:44:55": "192.0.2.100",
                        "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                    },
                },
                "secondary_address": "192.0.2.0/24",
                "virtual_address": "192.0.2.0/24",
            },
            vlan_tag=0,
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.update(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.update(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(LAN, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.update(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.update(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.update(
                lan_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(SyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(SyncSinglePage[LAN], lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.list(
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.list(
                site_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.delete(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.delete(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.delete(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(LAN, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.delete(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.delete(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.delete(
                lan_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.edit(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.edit(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            nat={"static_prefix": "192.0.2.0/24"},
            physport=1,
            routed_subnets=[
                {
                    "next_hop": "192.0.2.1",
                    "prefix": "192.0.2.0/24",
                    "nat": {"static_prefix": "192.0.2.0/24"},
                }
            ],
            static_addressing={
                "address": "192.0.2.0/24",
                "dhcp_relay": {"server_addresses": ["192.0.2.1"]},
                "dhcp_server": {
                    "dhcp_pool_end": "192.0.2.1",
                    "dhcp_pool_start": "192.0.2.1",
                    "dns_server": "192.0.2.1",
                    "dns_servers": ["192.0.2.1"],
                    "reservations": {
                        "00:11:22:33:44:55": "192.0.2.100",
                        "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                    },
                },
                "secondary_address": "192.0.2.0/24",
                "virtual_address": "192.0.2.0/24",
            },
            vlan_tag=0,
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.edit(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.edit(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(LAN, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.edit(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.edit(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.edit(
                lan_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.get(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.get(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.get(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(LAN, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.get(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.get(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_id` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.get(
                lan_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncLANs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            physport=1,
            vlan_tag=0,
        )
        assert_matches_type(AsyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            physport=1,
            vlan_tag=0,
            ha_link=True,
            name="name",
            nat={"static_prefix": "192.0.2.0/24"},
            routed_subnets=[
                {
                    "next_hop": "192.0.2.1",
                    "prefix": "192.0.2.0/24",
                    "nat": {"static_prefix": "192.0.2.0/24"},
                }
            ],
            static_addressing={
                "address": "192.0.2.0/24",
                "dhcp_relay": {"server_addresses": ["192.0.2.1"]},
                "dhcp_server": {
                    "dhcp_pool_end": "192.0.2.1",
                    "dhcp_pool_start": "192.0.2.1",
                    "dns_server": "192.0.2.1",
                    "dns_servers": ["192.0.2.1"],
                    "reservations": {
                        "00:11:22:33:44:55": "192.0.2.100",
                        "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                    },
                },
                "secondary_address": "192.0.2.0/24",
                "virtual_address": "192.0.2.0/24",
            },
        )
        assert_matches_type(AsyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            physport=1,
            vlan_tag=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(AsyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.create(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            physport=1,
            vlan_tag=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(AsyncSinglePage[LAN], lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.create(
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                physport=1,
                vlan_tag=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.create(
                site_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                physport=1,
                vlan_tag=0,
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.update(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.update(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            nat={"static_prefix": "192.0.2.0/24"},
            physport=1,
            routed_subnets=[
                {
                    "next_hop": "192.0.2.1",
                    "prefix": "192.0.2.0/24",
                    "nat": {"static_prefix": "192.0.2.0/24"},
                }
            ],
            static_addressing={
                "address": "192.0.2.0/24",
                "dhcp_relay": {"server_addresses": ["192.0.2.1"]},
                "dhcp_server": {
                    "dhcp_pool_end": "192.0.2.1",
                    "dhcp_pool_start": "192.0.2.1",
                    "dns_server": "192.0.2.1",
                    "dns_servers": ["192.0.2.1"],
                    "reservations": {
                        "00:11:22:33:44:55": "192.0.2.100",
                        "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                    },
                },
                "secondary_address": "192.0.2.0/24",
                "virtual_address": "192.0.2.0/24",
            },
            vlan_tag=0,
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.update(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.update(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(LAN, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.update(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.update(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.update(
                lan_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(AsyncSinglePage[LAN], lan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.list(
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(AsyncSinglePage[LAN], lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.list(
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.list(
                site_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.delete(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.delete(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.delete(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(LAN, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.delete(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.delete(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.delete(
                lan_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.edit(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.edit(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="name",
            nat={"static_prefix": "192.0.2.0/24"},
            physport=1,
            routed_subnets=[
                {
                    "next_hop": "192.0.2.1",
                    "prefix": "192.0.2.0/24",
                    "nat": {"static_prefix": "192.0.2.0/24"},
                }
            ],
            static_addressing={
                "address": "192.0.2.0/24",
                "dhcp_relay": {"server_addresses": ["192.0.2.1"]},
                "dhcp_server": {
                    "dhcp_pool_end": "192.0.2.1",
                    "dhcp_pool_start": "192.0.2.1",
                    "dns_server": "192.0.2.1",
                    "dns_servers": ["192.0.2.1"],
                    "reservations": {
                        "00:11:22:33:44:55": "192.0.2.100",
                        "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                    },
                },
                "secondary_address": "192.0.2.0/24",
                "virtual_address": "192.0.2.0/24",
            },
            vlan_tag=0,
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.edit(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.edit(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(LAN, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.edit(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.edit(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.edit(
                lan_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.get(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.get(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(LAN, lan, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.get(
            lan_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            site_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(LAN, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.get(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.get(
                lan_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_id` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.get(
                lan_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                site_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
