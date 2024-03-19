# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_transit.sites import (
    LanGetResponse,
    LanListResponse,
    LanCreateResponse,
    LanDeleteResponse,
    LanUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanCreateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            lan={
                "description": "string",
                "ha_link": True,
                "nat": {"static_prefix": "192.0.2.0/24"},
                "physport": 1,
                "routed_subnets": [
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                ],
                "static_addressing": {
                    "address": "192.0.2.0/24",
                    "dhcp_relay": {"server_addresses": ["192.0.2.1", "192.0.2.1", "192.0.2.1"]},
                    "dhcp_server": {
                        "dhcp_pool_end": "192.0.2.1",
                        "dhcp_pool_start": "192.0.2.1",
                        "dns_server": "192.0.2.1",
                        "reservations": {
                            "00:11:22:33:44:55": "192.0.2.100",
                            "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                        },
                    },
                    "secondary_address": "192.0.2.0/24",
                    "virtual_address": "192.0.2.0/24",
                },
                "vlan_tag": 0,
            },
        )
        assert_matches_type(LanCreateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(LanCreateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(LanCreateResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.create(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanUpdateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            lan={
                "description": "string",
                "nat": {"static_prefix": "192.0.2.0/24"},
                "physport": 1,
                "routed_subnets": [
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                ],
                "static_addressing": {
                    "address": "192.0.2.0/24",
                    "dhcp_relay": {"server_addresses": ["192.0.2.1", "192.0.2.1", "192.0.2.1"]},
                    "dhcp_server": {
                        "dhcp_pool_end": "192.0.2.1",
                        "dhcp_pool_start": "192.0.2.1",
                        "dns_server": "192.0.2.1",
                        "reservations": {
                            "00:11:22:33:44:55": "192.0.2.100",
                            "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                        },
                    },
                    "secondary_address": "192.0.2.0/24",
                    "virtual_address": "192.0.2.0/24",
                },
                "vlan_tag": 0,
            },
        )
        assert_matches_type(LanUpdateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(LanUpdateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(LanUpdateResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanListResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(LanListResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(LanListResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.list(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanDeleteResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(LanDeleteResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(LanDeleteResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        lan = client.magic_transit.sites.lans.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanGetResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.sites.lans.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = response.parse()
        assert_matches_type(LanGetResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.sites.lans.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = response.parse()
            assert_matches_type(LanGetResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_identifier` but received ''"):
            client.magic_transit.sites.lans.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncLans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanCreateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            lan={
                "description": "string",
                "ha_link": True,
                "nat": {"static_prefix": "192.0.2.0/24"},
                "physport": 1,
                "routed_subnets": [
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                ],
                "static_addressing": {
                    "address": "192.0.2.0/24",
                    "dhcp_relay": {"server_addresses": ["192.0.2.1", "192.0.2.1", "192.0.2.1"]},
                    "dhcp_server": {
                        "dhcp_pool_end": "192.0.2.1",
                        "dhcp_pool_start": "192.0.2.1",
                        "dns_server": "192.0.2.1",
                        "reservations": {
                            "00:11:22:33:44:55": "192.0.2.100",
                            "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                        },
                    },
                    "secondary_address": "192.0.2.0/24",
                    "virtual_address": "192.0.2.0/24",
                },
                "vlan_tag": 0,
            },
        )
        assert_matches_type(LanCreateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(LanCreateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(LanCreateResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.create(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanUpdateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            lan={
                "description": "string",
                "nat": {"static_prefix": "192.0.2.0/24"},
                "physport": 1,
                "routed_subnets": [
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                    {
                        "nat": {"static_prefix": "192.0.2.0/24"},
                        "next_hop": "192.0.2.1",
                        "prefix": "192.0.2.0/24",
                    },
                ],
                "static_addressing": {
                    "address": "192.0.2.0/24",
                    "dhcp_relay": {"server_addresses": ["192.0.2.1", "192.0.2.1", "192.0.2.1"]},
                    "dhcp_server": {
                        "dhcp_pool_end": "192.0.2.1",
                        "dhcp_pool_start": "192.0.2.1",
                        "dns_server": "192.0.2.1",
                        "reservations": {
                            "00:11:22:33:44:55": "192.0.2.100",
                            "AA:BB:CC:DD:EE:FF": "192.168.1.101",
                        },
                    },
                    "secondary_address": "192.0.2.0/24",
                    "virtual_address": "192.0.2.0/24",
                },
                "vlan_tag": 0,
            },
        )
        assert_matches_type(LanUpdateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(LanUpdateResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(LanUpdateResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanListResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(LanListResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(LanListResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.list(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanDeleteResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(LanDeleteResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(LanDeleteResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        lan = await async_client.magic_transit.sites.lans.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LanGetResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.sites.lans.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lan = await response.parse()
        assert_matches_type(LanGetResponse, lan, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.sites.lans.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lan = await response.parse()
            assert_matches_type(LanGetResponse, lan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lan_identifier` but received ''"):
            await async_client.magic_transit.sites.lans.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                site_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
