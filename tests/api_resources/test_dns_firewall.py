# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.dns_firewall import (
    DNSFirewallGetResponse,
    DNSFirewallEditResponse,
    DNSFirewallListResponse,
    DNSFirewallCreateResponse,
    DNSFirewallDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDNSFirewall:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewall.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )
        assert_matches_type(Optional[DNSFirewallCreateResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewall.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            attack_mitigation={
                "enabled": True,
                "only_when_upstream_unhealthy": False,
            },
            deprecate_any_requests=True,
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            negative_cache_ttl=900,
            ratelimit=600,
            retries=2,
        )
        assert_matches_type(Optional[DNSFirewallCreateResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.dns_firewall.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(Optional[DNSFirewallCreateResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.dns_firewall.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(Optional[DNSFirewallCreateResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewall.with_raw_response.create(
                account_id="",
                name="My Awesome DNS Firewall cluster",
                upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewall.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[DNSFirewallListResponse], dns_firewall, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewall.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[DNSFirewallListResponse], dns_firewall, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dns_firewall.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[DNSFirewallListResponse], dns_firewall, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dns_firewall.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[DNSFirewallListResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewall.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewall.delete(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSFirewallDeleteResponse], dns_firewall, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dns_firewall.with_raw_response.delete(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(Optional[DNSFirewallDeleteResponse], dns_firewall, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dns_firewall.with_streaming_response.delete(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(Optional[DNSFirewallDeleteResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewall.with_raw_response.delete(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            client.dns_firewall.with_raw_response.delete(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewall.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSFirewallEditResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewall.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            attack_mitigation={
                "enabled": True,
                "only_when_upstream_unhealthy": False,
            },
            deprecate_any_requests=True,
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            negative_cache_ttl=900,
            ratelimit=600,
            retries=2,
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )
        assert_matches_type(Optional[DNSFirewallEditResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.dns_firewall.with_raw_response.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(Optional[DNSFirewallEditResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.dns_firewall.with_streaming_response.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(Optional[DNSFirewallEditResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewall.with_raw_response.edit(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            client.dns_firewall.with_raw_response.edit(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewall.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSFirewallGetResponse], dns_firewall, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns_firewall.with_raw_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(Optional[DNSFirewallGetResponse], dns_firewall, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns_firewall.with_streaming_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(Optional[DNSFirewallGetResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewall.with_raw_response.get(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            client.dns_firewall.with_raw_response.get(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDNSFirewall:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewall.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )
        assert_matches_type(Optional[DNSFirewallCreateResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewall.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            attack_mitigation={
                "enabled": True,
                "only_when_upstream_unhealthy": False,
            },
            deprecate_any_requests=True,
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            negative_cache_ttl=900,
            ratelimit=600,
            retries=2,
        )
        assert_matches_type(Optional[DNSFirewallCreateResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewall.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(Optional[DNSFirewallCreateResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewall.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(Optional[DNSFirewallCreateResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewall.with_raw_response.create(
                account_id="",
                name="My Awesome DNS Firewall cluster",
                upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewall.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DNSFirewallListResponse], dns_firewall, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewall.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[DNSFirewallListResponse], dns_firewall, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewall.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[DNSFirewallListResponse], dns_firewall, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewall.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[DNSFirewallListResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewall.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewall.delete(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSFirewallDeleteResponse], dns_firewall, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewall.with_raw_response.delete(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(Optional[DNSFirewallDeleteResponse], dns_firewall, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewall.with_streaming_response.delete(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(Optional[DNSFirewallDeleteResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewall.with_raw_response.delete(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            await async_client.dns_firewall.with_raw_response.delete(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewall.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSFirewallEditResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewall.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            attack_mitigation={
                "enabled": True,
                "only_when_upstream_unhealthy": False,
            },
            deprecate_any_requests=True,
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            negative_cache_ttl=900,
            ratelimit=600,
            retries=2,
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )
        assert_matches_type(Optional[DNSFirewallEditResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewall.with_raw_response.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(Optional[DNSFirewallEditResponse], dns_firewall, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewall.with_streaming_response.edit(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(Optional[DNSFirewallEditResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewall.with_raw_response.edit(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            await async_client.dns_firewall.with_raw_response.edit(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewall.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSFirewallGetResponse], dns_firewall, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewall.with_raw_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(Optional[DNSFirewallGetResponse], dns_firewall, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewall.with_streaming_response.get(
            dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(Optional[DNSFirewallGetResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewall.with_raw_response.get(
                dns_firewall_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            await async_client.dns_firewall.with_raw_response.get(
                dns_firewall_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
