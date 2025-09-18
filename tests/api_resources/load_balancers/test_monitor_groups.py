# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.load_balancers import (
    MonitorGroup,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitorGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        monitor_group = client.load_balancers.monitor_groups.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitor_groups.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.load_balancers.monitor_groups.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.create(
                account_id="",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        monitor_group = client.load_balancers.monitor_groups.update(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitor_groups.with_raw_response.update(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.load_balancers.monitor_groups.with_streaming_response.update(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.update(
                monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_group_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.update(
                monitor_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        monitor_group = client.load_balancers.monitor_groups.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[MonitorGroup], monitor_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitor_groups.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = response.parse()
        assert_matches_type(SyncSinglePage[MonitorGroup], monitor_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.load_balancers.monitor_groups.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = response.parse()
            assert_matches_type(SyncSinglePage[MonitorGroup], monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        monitor_group = client.load_balancers.monitor_groups.delete(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitor_groups.with_raw_response.delete(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.load_balancers.monitor_groups.with_streaming_response.delete(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.delete(
                monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_group_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.delete(
                monitor_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        monitor_group = client.load_balancers.monitor_groups.edit(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitor_groups.with_raw_response.edit(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.load_balancers.monitor_groups.with_streaming_response.edit(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.edit(
                monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_group_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.edit(
                monitor_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        monitor_group = client.load_balancers.monitor_groups.get(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitor_groups.with_raw_response.get(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.load_balancers.monitor_groups.with_streaming_response.get(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.get(
                monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_group_id` but received ''"):
            client.load_balancers.monitor_groups.with_raw_response.get(
                monitor_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncMonitorGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        monitor_group = await async_client.load_balancers.monitor_groups.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitor_groups.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = await response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitor_groups.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = await response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.create(
                account_id="",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        monitor_group = await async_client.load_balancers.monitor_groups.update(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitor_groups.with_raw_response.update(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = await response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitor_groups.with_streaming_response.update(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = await response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.update(
                monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_group_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.update(
                monitor_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        monitor_group = await async_client.load_balancers.monitor_groups.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[MonitorGroup], monitor_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitor_groups.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = await response.parse()
        assert_matches_type(AsyncSinglePage[MonitorGroup], monitor_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitor_groups.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = await response.parse()
            assert_matches_type(AsyncSinglePage[MonitorGroup], monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        monitor_group = await async_client.load_balancers.monitor_groups.delete(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitor_groups.with_raw_response.delete(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = await response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitor_groups.with_streaming_response.delete(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = await response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.delete(
                monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_group_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.delete(
                monitor_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        monitor_group = await async_client.load_balancers.monitor_groups.edit(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitor_groups.with_raw_response.edit(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = await response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitor_groups.with_streaming_response.edit(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="id",
            description="Primary datacenter monitors",
            members=[
                {
                    "enabled": True,
                    "monitor_id": "monitor_id",
                    "monitoring_only": False,
                    "must_be_healthy": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = await response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.edit(
                monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_group_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.edit(
                monitor_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="id",
                description="Primary datacenter monitors",
                members=[
                    {
                        "enabled": True,
                        "monitor_id": "monitor_id",
                        "monitoring_only": False,
                        "must_be_healthy": True,
                    }
                ],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        monitor_group = await async_client.load_balancers.monitor_groups.get(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitor_groups.with_raw_response.get(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor_group = await response.parse()
        assert_matches_type(MonitorGroup, monitor_group, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitor_groups.with_streaming_response.get(
            monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor_group = await response.parse()
            assert_matches_type(MonitorGroup, monitor_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.get(
                monitor_group_id="17b5962d775c646f3f9725cbc7a53df4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_group_id` but received ''"):
            await async_client.load_balancers.monitor_groups.with_raw_response.get(
                monitor_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
