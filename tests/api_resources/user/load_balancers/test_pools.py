# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.user.load_balancers import (
    LoadBalancingPool,
    PoolDeleteResponse,
    PoolHealthResponse,
    PoolPreviewResponse,
    PoolReferencesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.create(
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.create(
            name="primary-dc-1",
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
            check_regions=["WEU", "ENAM"],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.pools.with_raw_response.create(
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.user.load_balancers.pools.with_streaming_response.create(
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(LoadBalancingPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            name="primary-dc-1",
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
            check_regions=["WEU", "ENAM"],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.pools.with_raw_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.user.load_balancers.pools.with_streaming_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(LoadBalancingPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.user.load_balancers.pools.with_raw_response.update(
                "",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.list()
        assert_matches_type(SyncSinglePage[LoadBalancingPool], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.list(
            monitor={},
        )
        assert_matches_type(SyncSinglePage[LoadBalancingPool], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.pools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(SyncSinglePage[LoadBalancingPool], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.user.load_balancers.pools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(SyncSinglePage[LoadBalancingPool], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.pools.with_raw_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.user.load_balancers.pools.with_streaming_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolDeleteResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.user.load_balancers.pools.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            check_regions=["WEU", "ENAM"],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            name="primary-dc-1",
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.pools.with_raw_response.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.user.load_balancers.pools.with_streaming_response.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(LoadBalancingPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.user.load_balancers.pools.with_raw_response.edit(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.get(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.pools.with_raw_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.user.load_balancers.pools.with_streaming_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(LoadBalancingPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.user.load_balancers.pools.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_health(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.health(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(PoolHealthResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_health(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.pools.with_raw_response.health(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolHealthResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_health(self, client: Cloudflare) -> None:
        with client.user.load_balancers.pools.with_streaming_response.health(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolHealthResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_health(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.user.load_balancers.pools.with_raw_response.health(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_preview(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.preview(
            "17b5962d775c646f3f9725cbc7a53df4",
            expected_codes="2xx",
        )
        assert_matches_type(PoolPreviewResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_preview_with_all_params(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.preview(
            "17b5962d775c646f3f9725cbc7a53df4",
            expected_codes="2xx",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            follow_redirects=True,
            header={
                "Host": ["example.com"],
                "X-App-ID": ["abc123"],
            },
            interval=0,
            method="GET",
            path="/health",
            port=0,
            probe_zone="example.com",
            retries=0,
            load_balancer_monitor_timeout=0,
            type="https",
        )
        assert_matches_type(PoolPreviewResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_preview(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.pools.with_raw_response.preview(
            "17b5962d775c646f3f9725cbc7a53df4",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolPreviewResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_preview(self, client: Cloudflare) -> None:
        with client.user.load_balancers.pools.with_streaming_response.preview(
            "17b5962d775c646f3f9725cbc7a53df4",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolPreviewResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_preview(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.user.load_balancers.pools.with_raw_response.preview(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_references(self, client: Cloudflare) -> None:
        pool = client.user.load_balancers.pools.references(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(Optional[PoolReferencesResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_references(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.pools.with_raw_response.references(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(Optional[PoolReferencesResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_references(self, client: Cloudflare) -> None:
        with client.user.load_balancers.pools.with_streaming_response.references(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(Optional[PoolReferencesResponse], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_references(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.user.load_balancers.pools.with_raw_response.references(
                "",
            )


class TestAsyncPools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.create(
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.create(
            name="primary-dc-1",
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
            check_regions=["WEU", "ENAM"],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.pools.with_raw_response.create(
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.pools.with_streaming_response.create(
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(LoadBalancingPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            name="primary-dc-1",
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
            check_regions=["WEU", "ENAM"],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.pools.with_raw_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.pools.with_streaming_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(LoadBalancingPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.user.load_balancers.pools.with_raw_response.update(
                "",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.list()
        assert_matches_type(AsyncSinglePage[LoadBalancingPool], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.list(
            monitor={},
        )
        assert_matches_type(AsyncSinglePage[LoadBalancingPool], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.pools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(AsyncSinglePage[LoadBalancingPool], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.pools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(AsyncSinglePage[LoadBalancingPool], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.pools.with_raw_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.pools.with_streaming_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolDeleteResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.user.load_balancers.pools.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            check_regions=["WEU", "ENAM"],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            name="primary-dc-1",
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.pools.with_raw_response.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.pools.with_streaming_response.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(LoadBalancingPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.user.load_balancers.pools.with_raw_response.edit(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.get(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.pools.with_raw_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(LoadBalancingPool, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.pools.with_streaming_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(LoadBalancingPool, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.user.load_balancers.pools.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_health(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.health(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(PoolHealthResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_health(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.pools.with_raw_response.health(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolHealthResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_health(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.pools.with_streaming_response.health(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolHealthResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_health(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.user.load_balancers.pools.with_raw_response.health(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_preview(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.preview(
            "17b5962d775c646f3f9725cbc7a53df4",
            expected_codes="2xx",
        )
        assert_matches_type(PoolPreviewResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_preview_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.preview(
            "17b5962d775c646f3f9725cbc7a53df4",
            expected_codes="2xx",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            follow_redirects=True,
            header={
                "Host": ["example.com"],
                "X-App-ID": ["abc123"],
            },
            interval=0,
            method="GET",
            path="/health",
            port=0,
            probe_zone="example.com",
            retries=0,
            load_balancer_monitor_timeout=0,
            type="https",
        )
        assert_matches_type(PoolPreviewResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.pools.with_raw_response.preview(
            "17b5962d775c646f3f9725cbc7a53df4",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolPreviewResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.pools.with_streaming_response.preview(
            "17b5962d775c646f3f9725cbc7a53df4",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolPreviewResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_preview(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.user.load_balancers.pools.with_raw_response.preview(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_references(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.user.load_balancers.pools.references(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(Optional[PoolReferencesResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_references(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.pools.with_raw_response.references(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(Optional[PoolReferencesResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_references(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.pools.with_streaming_response.references(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(Optional[PoolReferencesResponse], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_references(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.user.load_balancers.pools.with_raw_response.references(
                "",
            )
