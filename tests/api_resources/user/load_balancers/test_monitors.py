# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.user.load_balancers import (
    LoadBalancingMonitor,
    MonitorDeleteResponse,
    MonitorPreviewResponse,
    MonitorReferencesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.create(
            expected_codes="2xx",
        )
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.create(
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
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.monitors.with_raw_response.create(
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.user.load_balancers.monitors.with_streaming_response.create(
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
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
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.monitors.with_raw_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.user.load_balancers.monitors.with_streaming_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.user.load_balancers.monitors.with_raw_response.update(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.list()
        assert_matches_type(SyncSinglePage[LoadBalancingMonitor], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.monitors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(SyncSinglePage[LoadBalancingMonitor], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.user.load_balancers.monitors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(SyncSinglePage[LoadBalancingMonitor], monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.monitors.with_raw_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.user.load_balancers.monitors.with_streaming_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.user.load_balancers.monitors.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.edit(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.edit(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
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
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.monitors.with_raw_response.edit(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.user.load_balancers.monitors.with_streaming_response.edit(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.user.load_balancers.monitors.with_raw_response.edit(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.monitors.with_raw_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.user.load_balancers.monitors.with_streaming_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.user.load_balancers.monitors.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_preview(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.preview(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(MonitorPreviewResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_preview_with_all_params(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.preview(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
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
        assert_matches_type(MonitorPreviewResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_preview(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.monitors.with_raw_response.preview(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorPreviewResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_preview(self, client: Cloudflare) -> None:
        with client.user.load_balancers.monitors.with_streaming_response.preview(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorPreviewResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_preview(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.user.load_balancers.monitors.with_raw_response.preview(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_references(self, client: Cloudflare) -> None:
        monitor = client.user.load_balancers.monitors.references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(Optional[MonitorReferencesResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_references(self, client: Cloudflare) -> None:
        response = client.user.load_balancers.monitors.with_raw_response.references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(Optional[MonitorReferencesResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_references(self, client: Cloudflare) -> None:
        with client.user.load_balancers.monitors.with_streaming_response.references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(Optional[MonitorReferencesResponse], monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_references(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.user.load_balancers.monitors.with_raw_response.references(
                "",
            )


class TestAsyncMonitors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.create(
            expected_codes="2xx",
        )
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.create(
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
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.monitors.with_raw_response.create(
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.monitors.with_streaming_response.create(
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
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
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.monitors.with_raw_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.monitors.with_streaming_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.user.load_balancers.monitors.with_raw_response.update(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.list()
        assert_matches_type(AsyncSinglePage[LoadBalancingMonitor], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.monitors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(AsyncSinglePage[LoadBalancingMonitor], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.monitors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(AsyncSinglePage[LoadBalancingMonitor], monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.monitors.with_raw_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.monitors.with_streaming_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.user.load_balancers.monitors.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.edit(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.edit(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
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
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.monitors.with_raw_response.edit(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.monitors.with_streaming_response.edit(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.user.load_balancers.monitors.with_raw_response.edit(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.monitors.with_raw_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.monitors.with_streaming_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(LoadBalancingMonitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.user.load_balancers.monitors.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_preview(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.preview(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(MonitorPreviewResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_preview_with_all_params(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.preview(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
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
        assert_matches_type(MonitorPreviewResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_preview(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.monitors.with_raw_response.preview(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorPreviewResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_preview(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.monitors.with_streaming_response.preview(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorPreviewResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_preview(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.user.load_balancers.monitors.with_raw_response.preview(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_references(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.user.load_balancers.monitors.references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(Optional[MonitorReferencesResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_references(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.load_balancers.monitors.with_raw_response.references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(Optional[MonitorReferencesResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_references(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.load_balancers.monitors.with_streaming_response.references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(Optional[MonitorReferencesResponse], monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_references(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.user.load_balancers.monitors.with_raw_response.references(
                "",
            )
