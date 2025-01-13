# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.firewall import (
    Lockdown,
    LockdownDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLockdowns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        lockdown = client.firewall.lockdowns.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.firewall.lockdowns.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.firewall.lockdowns.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.lockdowns.with_raw_response.create(
                zone_id="",
                configurations=[{}],
                urls=["shop.example.com/*"],
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        lockdown = client.firewall.lockdowns.update(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.firewall.lockdowns.with_raw_response.update(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.firewall.lockdowns.with_streaming_response.update(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.lockdowns.with_raw_response.update(
                lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
                configurations=[{}],
                urls=["shop.example.com/*"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lock_downs_id` but received ''"):
            client.firewall.lockdowns.with_raw_response.update(
                lock_downs_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                configurations=[{}],
                urls=["shop.example.com/*"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        lockdown = client.firewall.lockdowns.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        lockdown = client.firewall.lockdowns.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            created_on=parse_datetime("2014-01-01T05:20:00.12345Z"),
            description="endpoints",
            description_search="endpoints",
            ip="1.2.3.4",
            ip_range_search="1.2.3.0/16",
            ip_search="1.2.3.4",
            modified_on=parse_datetime("2014-01-01T05:20:00.12345Z"),
            page=1,
            per_page=1,
            priority=5,
            uri_search="/some/path",
        )
        assert_matches_type(SyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.firewall.lockdowns.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.firewall.lockdowns.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.lockdowns.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        lockdown = client.firewall.lockdowns.delete(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.firewall.lockdowns.with_raw_response.delete(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.firewall.lockdowns.with_streaming_response.delete(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.lockdowns.with_raw_response.delete(
                lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lock_downs_id` but received ''"):
            client.firewall.lockdowns.with_raw_response.delete(
                lock_downs_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        lockdown = client.firewall.lockdowns.get(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewall.lockdowns.with_raw_response.get(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewall.lockdowns.with_streaming_response.get(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.lockdowns.with_raw_response.get(
                lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lock_downs_id` but received ''"):
            client.firewall.lockdowns.with_raw_response.get(
                lock_downs_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncLockdowns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewall.lockdowns.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.create(
                zone_id="",
                configurations=[{}],
                urls=["shop.example.com/*"],
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewall.lockdowns.update(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.update(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.update(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configurations=[{}],
            urls=["shop.example.com/*"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.update(
                lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
                configurations=[{}],
                urls=["shop.example.com/*"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lock_downs_id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.update(
                lock_downs_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                configurations=[{}],
                urls=["shop.example.com/*"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewall.lockdowns.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewall.lockdowns.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            created_on=parse_datetime("2014-01-01T05:20:00.12345Z"),
            description="endpoints",
            description_search="endpoints",
            ip="1.2.3.4",
            ip_range_search="1.2.3.0/16",
            ip_search="1.2.3.4",
            modified_on=parse_datetime("2014-01-01T05:20:00.12345Z"),
            page=1,
            per_page=1,
            priority=5,
            uri_search="/some/path",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Lockdown], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewall.lockdowns.delete(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.delete(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.delete(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.delete(
                lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lock_downs_id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.delete(
                lock_downs_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewall.lockdowns.get(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.lockdowns.with_raw_response.get(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Lockdown, lockdown, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.lockdowns.with_streaming_response.get(
            lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Lockdown, lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.get(
                lock_downs_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `lock_downs_id` but received ''"):
            await async_client.firewall.lockdowns.with_raw_response.get(
                lock_downs_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
