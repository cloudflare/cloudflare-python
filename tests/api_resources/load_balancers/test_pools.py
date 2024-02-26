# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.load_balancers import (
    PoolGetResponse,
    PoolEditResponse,
    PoolListResponse,
    PoolCreateResponse,
    PoolDeleteResponse,
    PoolUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(PoolCreateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(PoolCreateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolCreateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolCreateResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.pools.with_raw_response.create(
                account_id="",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolUpdateResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.pools.with_raw_response.update(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.load_balancers.pools.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PoolListResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            monitor={},
        )
        assert_matches_type(Optional[PoolListResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(Optional[PoolListResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(Optional[PoolListResponse], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.pools.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolDeleteResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.pools.with_raw_response.delete(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.load_balancers.pools.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolEditResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(PoolEditResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolEditResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolEditResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.pools.with_raw_response.edit(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.load_balancers.pools.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolGetResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.pools.with_raw_response.get(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            client.load_balancers.pools.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(PoolCreateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(PoolCreateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolCreateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolCreateResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.create(
                account_id="",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolUpdateResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.update(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PoolListResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            monitor={},
        )
        assert_matches_type(Optional[PoolListResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(Optional[PoolListResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(Optional[PoolListResponse], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolDeleteResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.delete(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolEditResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(PoolEditResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolEditResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.edit(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolEditResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.edit(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolGetResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.get(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pool_id` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
