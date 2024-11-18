# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.load_balancers import (
    LoadBalancer,
    LoadBalancerDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoadBalancers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        load_balancer = client.load_balancers.create(
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        load_balancer = client.load_balancers.create(
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
            adaptive_routing={"failover_across_pools": True},
            country_pools={
                "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
            },
            description="Load Balancer for www.example.com",
            location_strategy={
                "mode": "pop",
                "prefer_ecs": "always",
            },
            networks=["string"],
            pop_pools={
                "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
            },
            proxied=True,
            random_steering={
                "default_weight": 0.2,
                "pool_weights": {
                    "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                    "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                },
            },
            region_pools={
                "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
            },
            rules=[
                {
                    "condition": 'http.request.uri.path contains "/testing"',
                    "disabled": True,
                    "fixed_response": {
                        "content_type": "application/json",
                        "location": "www.example.com",
                        "message_body": "Testing Hello",
                        "status_code": 0,
                    },
                    "name": "route the path /testing to testing datacenter.",
                    "overrides": {
                        "adaptive_routing": {"failover_across_pools": True},
                        "country_pools": {
                            "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                            "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "default_pools": [
                            "17b5962d775c646f3f9725cbc7a53df4",
                            "9290f38c5d07c2e2f4df57b1f61d4196",
                            "00920f38ce07c2e2f4df50b1f61d4194",
                        ],
                        "fallback_pool": "fallback_pool",
                        "location_strategy": {
                            "mode": "pop",
                            "prefer_ecs": "always",
                        },
                        "pop_pools": {
                            "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                            "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                            "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "random_steering": {
                            "default_weight": 0.2,
                            "pool_weights": {
                                "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                                "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                            },
                        },
                        "region_pools": {
                            "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                            "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                        },
                        "session_affinity": "none",
                        "session_affinity_attributes": {
                            "drain_duration": 100,
                            "headers": ["x"],
                            "require_all_headers": True,
                            "samesite": "Auto",
                            "secure": "Auto",
                            "zero_downtime_failover": "none",
                        },
                        "session_affinity_ttl": 1800,
                        "steering_policy": "off",
                        "ttl": 30,
                    },
                    "priority": 0,
                    "terminates": True,
                }
            ],
            session_affinity="none",
            session_affinity_attributes={
                "drain_duration": 100,
                "headers": ["x"],
                "require_all_headers": True,
                "samesite": "Auto",
                "secure": "Auto",
                "zero_downtime_failover": "none",
            },
            session_affinity_ttl=1800,
            steering_policy="off",
            ttl=30,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.load_balancers.with_raw_response.create(
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.load_balancers.with_streaming_response.create(
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.load_balancers.with_raw_response.create(
                zone_id="",
                default_pools=[
                    "17b5962d775c646f3f9725cbc7a53df4",
                    "9290f38c5d07c2e2f4df57b1f61d4196",
                    "00920f38ce07c2e2f4df50b1f61d4194",
                ],
                fallback_pool="fallback_pool",
                name="www.example.com",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        load_balancer = client.load_balancers.update(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        load_balancer = client.load_balancers.update(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
            adaptive_routing={"failover_across_pools": True},
            country_pools={
                "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
            },
            description="Load Balancer for www.example.com",
            enabled=True,
            location_strategy={
                "mode": "pop",
                "prefer_ecs": "always",
            },
            networks=["string"],
            pop_pools={
                "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
            },
            proxied=True,
            random_steering={
                "default_weight": 0.2,
                "pool_weights": {
                    "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                    "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                },
            },
            region_pools={
                "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
            },
            rules=[
                {
                    "condition": 'http.request.uri.path contains "/testing"',
                    "disabled": True,
                    "fixed_response": {
                        "content_type": "application/json",
                        "location": "www.example.com",
                        "message_body": "Testing Hello",
                        "status_code": 0,
                    },
                    "name": "route the path /testing to testing datacenter.",
                    "overrides": {
                        "adaptive_routing": {"failover_across_pools": True},
                        "country_pools": {
                            "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                            "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "default_pools": [
                            "17b5962d775c646f3f9725cbc7a53df4",
                            "9290f38c5d07c2e2f4df57b1f61d4196",
                            "00920f38ce07c2e2f4df50b1f61d4194",
                        ],
                        "fallback_pool": "fallback_pool",
                        "location_strategy": {
                            "mode": "pop",
                            "prefer_ecs": "always",
                        },
                        "pop_pools": {
                            "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                            "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                            "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "random_steering": {
                            "default_weight": 0.2,
                            "pool_weights": {
                                "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                                "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                            },
                        },
                        "region_pools": {
                            "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                            "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                        },
                        "session_affinity": "none",
                        "session_affinity_attributes": {
                            "drain_duration": 100,
                            "headers": ["x"],
                            "require_all_headers": True,
                            "samesite": "Auto",
                            "secure": "Auto",
                            "zero_downtime_failover": "none",
                        },
                        "session_affinity_ttl": 1800,
                        "steering_policy": "off",
                        "ttl": 30,
                    },
                    "priority": 0,
                    "terminates": True,
                }
            ],
            session_affinity="none",
            session_affinity_attributes={
                "drain_duration": 100,
                "headers": ["x"],
                "require_all_headers": True,
                "samesite": "Auto",
                "secure": "Auto",
                "zero_downtime_failover": "none",
            },
            session_affinity_ttl=1800,
            steering_policy="off",
            ttl=30,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.load_balancers.with_raw_response.update(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.load_balancers.with_streaming_response.update(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.load_balancers.with_raw_response.update(
                load_balancer_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                default_pools=[
                    "17b5962d775c646f3f9725cbc7a53df4",
                    "9290f38c5d07c2e2f4df57b1f61d4196",
                    "00920f38ce07c2e2f4df50b1f61d4194",
                ],
                fallback_pool="fallback_pool",
                name="www.example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `load_balancer_id` but received ''"):
            client.load_balancers.with_raw_response.update(
                load_balancer_id="",
                zone_id="699d98642c564d2e855e9661899b7252",
                default_pools=[
                    "17b5962d775c646f3f9725cbc7a53df4",
                    "9290f38c5d07c2e2f4df57b1f61d4196",
                    "00920f38ce07c2e2f4df50b1f61d4194",
                ],
                fallback_pool="fallback_pool",
                name="www.example.com",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        load_balancer = client.load_balancers.list(
            zone_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.load_balancers.with_raw_response.list(
            zone_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(SyncSinglePage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.load_balancers.with_streaming_response.list(
            zone_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(SyncSinglePage[LoadBalancer], load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.load_balancers.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        load_balancer = client.load_balancers.delete(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoadBalancerDeleteResponse, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.load_balancers.with_raw_response.delete(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(LoadBalancerDeleteResponse, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.load_balancers.with_streaming_response.delete(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(LoadBalancerDeleteResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.load_balancers.with_raw_response.delete(
                load_balancer_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `load_balancer_id` but received ''"):
            client.load_balancers.with_raw_response.delete(
                load_balancer_id="",
                zone_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        load_balancer = client.load_balancers.edit(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        load_balancer = client.load_balancers.edit(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            adaptive_routing={"failover_across_pools": True},
            country_pools={
                "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
            },
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            description="Load Balancer for www.example.com",
            enabled=True,
            fallback_pool="fallback_pool",
            location_strategy={
                "mode": "pop",
                "prefer_ecs": "always",
            },
            name="www.example.com",
            pop_pools={
                "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
            },
            proxied=True,
            random_steering={
                "default_weight": 0.2,
                "pool_weights": {
                    "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                    "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                },
            },
            region_pools={
                "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
            },
            rules=[
                {
                    "condition": 'http.request.uri.path contains "/testing"',
                    "disabled": True,
                    "fixed_response": {
                        "content_type": "application/json",
                        "location": "www.example.com",
                        "message_body": "Testing Hello",
                        "status_code": 0,
                    },
                    "name": "route the path /testing to testing datacenter.",
                    "overrides": {
                        "adaptive_routing": {"failover_across_pools": True},
                        "country_pools": {
                            "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                            "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "default_pools": [
                            "17b5962d775c646f3f9725cbc7a53df4",
                            "9290f38c5d07c2e2f4df57b1f61d4196",
                            "00920f38ce07c2e2f4df50b1f61d4194",
                        ],
                        "fallback_pool": "fallback_pool",
                        "location_strategy": {
                            "mode": "pop",
                            "prefer_ecs": "always",
                        },
                        "pop_pools": {
                            "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                            "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                            "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "random_steering": {
                            "default_weight": 0.2,
                            "pool_weights": {
                                "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                                "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                            },
                        },
                        "region_pools": {
                            "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                            "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                        },
                        "session_affinity": "none",
                        "session_affinity_attributes": {
                            "drain_duration": 100,
                            "headers": ["x"],
                            "require_all_headers": True,
                            "samesite": "Auto",
                            "secure": "Auto",
                            "zero_downtime_failover": "none",
                        },
                        "session_affinity_ttl": 1800,
                        "steering_policy": "off",
                        "ttl": 30,
                    },
                    "priority": 0,
                    "terminates": True,
                }
            ],
            session_affinity="none",
            session_affinity_attributes={
                "drain_duration": 100,
                "headers": ["x"],
                "require_all_headers": True,
                "samesite": "Auto",
                "secure": "Auto",
                "zero_downtime_failover": "none",
            },
            session_affinity_ttl=1800,
            steering_policy="off",
            ttl=30,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.load_balancers.with_raw_response.edit(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.load_balancers.with_streaming_response.edit(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.load_balancers.with_raw_response.edit(
                load_balancer_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `load_balancer_id` but received ''"):
            client.load_balancers.with_raw_response.edit(
                load_balancer_id="",
                zone_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        load_balancer = client.load_balancers.get(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.load_balancers.with_raw_response.get(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.load_balancers.with_streaming_response.get(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.load_balancers.with_raw_response.get(
                load_balancer_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `load_balancer_id` but received ''"):
            client.load_balancers.with_raw_response.get(
                load_balancer_id="",
                zone_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncLoadBalancers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        load_balancer = await async_client.load_balancers.create(
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        load_balancer = await async_client.load_balancers.create(
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
            adaptive_routing={"failover_across_pools": True},
            country_pools={
                "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
            },
            description="Load Balancer for www.example.com",
            location_strategy={
                "mode": "pop",
                "prefer_ecs": "always",
            },
            networks=["string"],
            pop_pools={
                "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
            },
            proxied=True,
            random_steering={
                "default_weight": 0.2,
                "pool_weights": {
                    "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                    "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                },
            },
            region_pools={
                "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
            },
            rules=[
                {
                    "condition": 'http.request.uri.path contains "/testing"',
                    "disabled": True,
                    "fixed_response": {
                        "content_type": "application/json",
                        "location": "www.example.com",
                        "message_body": "Testing Hello",
                        "status_code": 0,
                    },
                    "name": "route the path /testing to testing datacenter.",
                    "overrides": {
                        "adaptive_routing": {"failover_across_pools": True},
                        "country_pools": {
                            "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                            "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "default_pools": [
                            "17b5962d775c646f3f9725cbc7a53df4",
                            "9290f38c5d07c2e2f4df57b1f61d4196",
                            "00920f38ce07c2e2f4df50b1f61d4194",
                        ],
                        "fallback_pool": "fallback_pool",
                        "location_strategy": {
                            "mode": "pop",
                            "prefer_ecs": "always",
                        },
                        "pop_pools": {
                            "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                            "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                            "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "random_steering": {
                            "default_weight": 0.2,
                            "pool_weights": {
                                "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                                "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                            },
                        },
                        "region_pools": {
                            "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                            "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                        },
                        "session_affinity": "none",
                        "session_affinity_attributes": {
                            "drain_duration": 100,
                            "headers": ["x"],
                            "require_all_headers": True,
                            "samesite": "Auto",
                            "secure": "Auto",
                            "zero_downtime_failover": "none",
                        },
                        "session_affinity_ttl": 1800,
                        "steering_policy": "off",
                        "ttl": 30,
                    },
                    "priority": 0,
                    "terminates": True,
                }
            ],
            session_affinity="none",
            session_affinity_attributes={
                "drain_duration": 100,
                "headers": ["x"],
                "require_all_headers": True,
                "samesite": "Auto",
                "secure": "Auto",
                "zero_downtime_failover": "none",
            },
            session_affinity_ttl=1800,
            steering_policy="off",
            ttl=30,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.with_raw_response.create(
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.with_streaming_response.create(
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.load_balancers.with_raw_response.create(
                zone_id="",
                default_pools=[
                    "17b5962d775c646f3f9725cbc7a53df4",
                    "9290f38c5d07c2e2f4df57b1f61d4196",
                    "00920f38ce07c2e2f4df50b1f61d4194",
                ],
                fallback_pool="fallback_pool",
                name="www.example.com",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        load_balancer = await async_client.load_balancers.update(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        load_balancer = await async_client.load_balancers.update(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
            adaptive_routing={"failover_across_pools": True},
            country_pools={
                "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
            },
            description="Load Balancer for www.example.com",
            enabled=True,
            location_strategy={
                "mode": "pop",
                "prefer_ecs": "always",
            },
            networks=["string"],
            pop_pools={
                "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
            },
            proxied=True,
            random_steering={
                "default_weight": 0.2,
                "pool_weights": {
                    "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                    "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                },
            },
            region_pools={
                "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
            },
            rules=[
                {
                    "condition": 'http.request.uri.path contains "/testing"',
                    "disabled": True,
                    "fixed_response": {
                        "content_type": "application/json",
                        "location": "www.example.com",
                        "message_body": "Testing Hello",
                        "status_code": 0,
                    },
                    "name": "route the path /testing to testing datacenter.",
                    "overrides": {
                        "adaptive_routing": {"failover_across_pools": True},
                        "country_pools": {
                            "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                            "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "default_pools": [
                            "17b5962d775c646f3f9725cbc7a53df4",
                            "9290f38c5d07c2e2f4df57b1f61d4196",
                            "00920f38ce07c2e2f4df50b1f61d4194",
                        ],
                        "fallback_pool": "fallback_pool",
                        "location_strategy": {
                            "mode": "pop",
                            "prefer_ecs": "always",
                        },
                        "pop_pools": {
                            "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                            "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                            "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "random_steering": {
                            "default_weight": 0.2,
                            "pool_weights": {
                                "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                                "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                            },
                        },
                        "region_pools": {
                            "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                            "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                        },
                        "session_affinity": "none",
                        "session_affinity_attributes": {
                            "drain_duration": 100,
                            "headers": ["x"],
                            "require_all_headers": True,
                            "samesite": "Auto",
                            "secure": "Auto",
                            "zero_downtime_failover": "none",
                        },
                        "session_affinity_ttl": 1800,
                        "steering_policy": "off",
                        "ttl": 30,
                    },
                    "priority": 0,
                    "terminates": True,
                }
            ],
            session_affinity="none",
            session_affinity_attributes={
                "drain_duration": 100,
                "headers": ["x"],
                "require_all_headers": True,
                "samesite": "Auto",
                "secure": "Auto",
                "zero_downtime_failover": "none",
            },
            session_affinity_ttl=1800,
            steering_policy="off",
            ttl=30,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.with_raw_response.update(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.with_streaming_response.update(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            fallback_pool="fallback_pool",
            name="www.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.load_balancers.with_raw_response.update(
                load_balancer_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
                default_pools=[
                    "17b5962d775c646f3f9725cbc7a53df4",
                    "9290f38c5d07c2e2f4df57b1f61d4196",
                    "00920f38ce07c2e2f4df50b1f61d4194",
                ],
                fallback_pool="fallback_pool",
                name="www.example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `load_balancer_id` but received ''"):
            await async_client.load_balancers.with_raw_response.update(
                load_balancer_id="",
                zone_id="699d98642c564d2e855e9661899b7252",
                default_pools=[
                    "17b5962d775c646f3f9725cbc7a53df4",
                    "9290f38c5d07c2e2f4df57b1f61d4196",
                    "00920f38ce07c2e2f4df50b1f61d4194",
                ],
                fallback_pool="fallback_pool",
                name="www.example.com",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        load_balancer = await async_client.load_balancers.list(
            zone_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.with_raw_response.list(
            zone_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(AsyncSinglePage[LoadBalancer], load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.with_streaming_response.list(
            zone_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(AsyncSinglePage[LoadBalancer], load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.load_balancers.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        load_balancer = await async_client.load_balancers.delete(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoadBalancerDeleteResponse, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.with_raw_response.delete(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancerDeleteResponse, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.with_streaming_response.delete(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancerDeleteResponse, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.load_balancers.with_raw_response.delete(
                load_balancer_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `load_balancer_id` but received ''"):
            await async_client.load_balancers.with_raw_response.delete(
                load_balancer_id="",
                zone_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        load_balancer = await async_client.load_balancers.edit(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        load_balancer = await async_client.load_balancers.edit(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
            adaptive_routing={"failover_across_pools": True},
            country_pools={
                "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
            },
            default_pools=[
                "17b5962d775c646f3f9725cbc7a53df4",
                "9290f38c5d07c2e2f4df57b1f61d4196",
                "00920f38ce07c2e2f4df50b1f61d4194",
            ],
            description="Load Balancer for www.example.com",
            enabled=True,
            fallback_pool="fallback_pool",
            location_strategy={
                "mode": "pop",
                "prefer_ecs": "always",
            },
            name="www.example.com",
            pop_pools={
                "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
            },
            proxied=True,
            random_steering={
                "default_weight": 0.2,
                "pool_weights": {
                    "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                    "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                },
            },
            region_pools={
                "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
            },
            rules=[
                {
                    "condition": 'http.request.uri.path contains "/testing"',
                    "disabled": True,
                    "fixed_response": {
                        "content_type": "application/json",
                        "location": "www.example.com",
                        "message_body": "Testing Hello",
                        "status_code": 0,
                    },
                    "name": "route the path /testing to testing datacenter.",
                    "overrides": {
                        "adaptive_routing": {"failover_across_pools": True},
                        "country_pools": {
                            "GB": ["abd90f38ced07c2e2f4df50b1f61d4194"],
                            "US": ["de90f38ced07c2e2f4df50b1f61d4194", "00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "default_pools": [
                            "17b5962d775c646f3f9725cbc7a53df4",
                            "9290f38c5d07c2e2f4df57b1f61d4196",
                            "00920f38ce07c2e2f4df50b1f61d4194",
                        ],
                        "fallback_pool": "fallback_pool",
                        "location_strategy": {
                            "mode": "pop",
                            "prefer_ecs": "always",
                        },
                        "pop_pools": {
                            "LAX": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                            "LHR": ["abd90f38ced07c2e2f4df50b1f61d4194", "f9138c5d07c2e2f4df57b1f61d4196"],
                            "SJC": ["00920f38ce07c2e2f4df50b1f61d4194"],
                        },
                        "random_steering": {
                            "default_weight": 0.2,
                            "pool_weights": {
                                "9290f38c5d07c2e2f4df57b1f61d4196": 0.5,
                                "de90f38ced07c2e2f4df50b1f61d4194": 0.3,
                            },
                        },
                        "region_pools": {
                            "ENAM": ["00920f38ce07c2e2f4df50b1f61d4194"],
                            "WNAM": ["de90f38ced07c2e2f4df50b1f61d4194", "9290f38c5d07c2e2f4df57b1f61d4196"],
                        },
                        "session_affinity": "none",
                        "session_affinity_attributes": {
                            "drain_duration": 100,
                            "headers": ["x"],
                            "require_all_headers": True,
                            "samesite": "Auto",
                            "secure": "Auto",
                            "zero_downtime_failover": "none",
                        },
                        "session_affinity_ttl": 1800,
                        "steering_policy": "off",
                        "ttl": 30,
                    },
                    "priority": 0,
                    "terminates": True,
                }
            ],
            session_affinity="none",
            session_affinity_attributes={
                "drain_duration": 100,
                "headers": ["x"],
                "require_all_headers": True,
                "samesite": "Auto",
                "secure": "Auto",
                "zero_downtime_failover": "none",
            },
            session_affinity_ttl=1800,
            steering_policy="off",
            ttl=30,
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.with_raw_response.edit(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.with_streaming_response.edit(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.load_balancers.with_raw_response.edit(
                load_balancer_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `load_balancer_id` but received ''"):
            await async_client.load_balancers.with_raw_response.edit(
                load_balancer_id="",
                zone_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        load_balancer = await async_client.load_balancers.get(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.with_raw_response.get(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        load_balancer = await response.parse()
        assert_matches_type(LoadBalancer, load_balancer, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.with_streaming_response.get(
            load_balancer_id="699d98642c564d2e855e9661899b7252",
            zone_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            load_balancer = await response.parse()
            assert_matches_type(LoadBalancer, load_balancer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.load_balancers.with_raw_response.get(
                load_balancer_id="699d98642c564d2e855e9661899b7252",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `load_balancer_id` but received ''"):
            await async_client.load_balancers.with_raw_response.get(
                load_balancer_id="",
                zone_id="699d98642c564d2e855e9661899b7252",
            )
