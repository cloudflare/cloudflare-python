# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import (
    DNSFirewallCreateResponse,
    DNSFirewallUpdateResponse,
    DNSFirewallListResponse,
    DNSFirewallDeleteResponse,
    DNSFirewallGetResponse,
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
from cloudflare.types import dns_firewall_create_params
from cloudflare.types import dns_firewall_update_params
from cloudflare.types import dns_firewall_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDNSFirewalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewalls.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )
        assert_matches_type(DNSFirewallCreateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewalls.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            attack_mitigation={
                "enabled": True,
                "only_when_origin_unhealthy": {},
                "only_when_upstream_unhealthy": False,
            },
            deprecate_any_requests=True,
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            negative_cache_ttl=900,
            origin_ips={},
            ratelimit=600,
            retries=2,
        )
        assert_matches_type(DNSFirewallCreateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.dns_firewalls.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(DNSFirewallCreateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.dns_firewalls.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(DNSFirewallCreateResponse, dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewalls.with_raw_response.create(
                "",
                name="My Awesome DNS Firewall cluster",
                upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewalls.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deprecate_any_requests=True,
            dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )
        assert_matches_type(DNSFirewallUpdateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewalls.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deprecate_any_requests=True,
            dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            attack_mitigation={
                "enabled": True,
                "only_when_origin_unhealthy": {},
                "only_when_upstream_unhealthy": False,
            },
            negative_cache_ttl=900,
            origin_ips={},
            ratelimit=600,
            retries=2,
        )
        assert_matches_type(DNSFirewallUpdateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.dns_firewalls.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deprecate_any_requests=True,
            dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(DNSFirewallUpdateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.dns_firewalls.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deprecate_any_requests=True,
            dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(DNSFirewallUpdateResponse, dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewalls.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                deprecate_any_requests=True,
                dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
                ecs_fallback=False,
                maximum_cache_ttl=900,
                minimum_cache_ttl=60,
                name="My Awesome DNS Firewall cluster",
                upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            client.dns_firewalls.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                deprecate_any_requests=True,
                dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
                ecs_fallback=False,
                maximum_cache_ttl=900,
                minimum_cache_ttl=60,
                name="My Awesome DNS Firewall cluster",
                upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewalls.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSFirewallListResponse], dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewalls.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(Optional[DNSFirewallListResponse], dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dns_firewalls.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(Optional[DNSFirewallListResponse], dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dns_firewalls.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(Optional[DNSFirewallListResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewalls.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewalls.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSFirewallDeleteResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dns_firewalls.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(DNSFirewallDeleteResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dns_firewalls.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(DNSFirewallDeleteResponse, dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewalls.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            client.dns_firewalls.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dns_firewall = client.dns_firewalls.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSFirewallGetResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns_firewalls.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = response.parse()
        assert_matches_type(DNSFirewallGetResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns_firewalls.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = response.parse()
            assert_matches_type(DNSFirewallGetResponse, dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dns_firewalls.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            client.dns_firewalls.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDNSFirewalls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewalls.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )
        assert_matches_type(DNSFirewallCreateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewalls.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            attack_mitigation={
                "enabled": True,
                "only_when_origin_unhealthy": {},
                "only_when_upstream_unhealthy": False,
            },
            deprecate_any_requests=True,
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            negative_cache_ttl=900,
            origin_ips={},
            ratelimit=600,
            retries=2,
        )
        assert_matches_type(DNSFirewallCreateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewalls.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(DNSFirewallCreateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewalls.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(DNSFirewallCreateResponse, dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewalls.with_raw_response.create(
                "",
                name="My Awesome DNS Firewall cluster",
                upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewalls.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deprecate_any_requests=True,
            dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )
        assert_matches_type(DNSFirewallUpdateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewalls.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deprecate_any_requests=True,
            dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            attack_mitigation={
                "enabled": True,
                "only_when_origin_unhealthy": {},
                "only_when_upstream_unhealthy": False,
            },
            negative_cache_ttl=900,
            origin_ips={},
            ratelimit=600,
            retries=2,
        )
        assert_matches_type(DNSFirewallUpdateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewalls.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deprecate_any_requests=True,
            dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(DNSFirewallUpdateResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewalls.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deprecate_any_requests=True,
            dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
            ecs_fallback=False,
            maximum_cache_ttl=900,
            minimum_cache_ttl=60,
            name="My Awesome DNS Firewall cluster",
            upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(DNSFirewallUpdateResponse, dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewalls.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                deprecate_any_requests=True,
                dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
                ecs_fallback=False,
                maximum_cache_ttl=900,
                minimum_cache_ttl=60,
                name="My Awesome DNS Firewall cluster",
                upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            await async_client.dns_firewalls.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                deprecate_any_requests=True,
                dns_firewall_ips=["203.0.113.1", "203.0.113.254", "2001:DB8:AB::CF", "2001:DB8:CD::CF"],
                ecs_fallback=False,
                maximum_cache_ttl=900,
                minimum_cache_ttl=60,
                name="My Awesome DNS Firewall cluster",
                upstream_ips=["192.0.2.1", "198.51.100.1", "2001:DB8:100::CF"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewalls.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSFirewallListResponse], dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewalls.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(Optional[DNSFirewallListResponse], dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewalls.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(Optional[DNSFirewallListResponse], dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewalls.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(Optional[DNSFirewallListResponse], dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewalls.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewalls.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSFirewallDeleteResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewalls.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(DNSFirewallDeleteResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewalls.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(DNSFirewallDeleteResponse, dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewalls.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            await async_client.dns_firewalls.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dns_firewall = await async_client.dns_firewalls.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSFirewallGetResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_firewalls.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_firewall = await response.parse()
        assert_matches_type(DNSFirewallGetResponse, dns_firewall, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_firewalls.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_firewall = await response.parse()
            assert_matches_type(DNSFirewallGetResponse, dns_firewall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dns_firewalls.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_firewall_id` but received ''"):
            await async_client.dns_firewalls.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
