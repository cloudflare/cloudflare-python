# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users.load_balancers import (
    MonitorLoadBalancerMonitorsListMonitorsResponse,
    MonitorLoadBalancerMonitorsCreateMonitorResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_monitors_create_monitor(self, client: Cloudflare) -> None:
        monitor = client.users.load_balancers.monitors.load_balancer_monitors_create_monitor(
            expected_codes="2xx",
        )
        assert_matches_type(MonitorLoadBalancerMonitorsCreateMonitorResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_monitors_create_monitor_with_all_params(self, client: Cloudflare) -> None:
        monitor = client.users.load_balancers.monitors.load_balancer_monitors_create_monitor(
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
            api_timeout=0,
            type="https",
        )
        assert_matches_type(MonitorLoadBalancerMonitorsCreateMonitorResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_load_balancer_monitors_create_monitor(self, client: Cloudflare) -> None:
        response = client.users.load_balancers.monitors.with_raw_response.load_balancer_monitors_create_monitor(
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorLoadBalancerMonitorsCreateMonitorResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_load_balancer_monitors_create_monitor(self, client: Cloudflare) -> None:
        with client.users.load_balancers.monitors.with_streaming_response.load_balancer_monitors_create_monitor(
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorLoadBalancerMonitorsCreateMonitorResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_monitors_list_monitors(self, client: Cloudflare) -> None:
        monitor = client.users.load_balancers.monitors.load_balancer_monitors_list_monitors()
        assert_matches_type(Optional[MonitorLoadBalancerMonitorsListMonitorsResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_load_balancer_monitors_list_monitors(self, client: Cloudflare) -> None:
        response = client.users.load_balancers.monitors.with_raw_response.load_balancer_monitors_list_monitors()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(Optional[MonitorLoadBalancerMonitorsListMonitorsResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_load_balancer_monitors_list_monitors(self, client: Cloudflare) -> None:
        with client.users.load_balancers.monitors.with_streaming_response.load_balancer_monitors_list_monitors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(Optional[MonitorLoadBalancerMonitorsListMonitorsResponse], monitor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMonitors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_monitors_create_monitor(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.users.load_balancers.monitors.load_balancer_monitors_create_monitor(
            expected_codes="2xx",
        )
        assert_matches_type(MonitorLoadBalancerMonitorsCreateMonitorResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_monitors_create_monitor_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        monitor = await async_client.users.load_balancers.monitors.load_balancer_monitors_create_monitor(
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
            api_timeout=0,
            type="https",
        )
        assert_matches_type(MonitorLoadBalancerMonitorsCreateMonitorResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_load_balancer_monitors_create_monitor(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.users.load_balancers.monitors.with_raw_response.load_balancer_monitors_create_monitor(
                expected_codes="2xx",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorLoadBalancerMonitorsCreateMonitorResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_load_balancer_monitors_create_monitor(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.load_balancers.monitors.with_streaming_response.load_balancer_monitors_create_monitor(
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorLoadBalancerMonitorsCreateMonitorResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_monitors_list_monitors(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.users.load_balancers.monitors.load_balancer_monitors_list_monitors()
        assert_matches_type(Optional[MonitorLoadBalancerMonitorsListMonitorsResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_load_balancer_monitors_list_monitors(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.users.load_balancers.monitors.with_raw_response.load_balancer_monitors_list_monitors()
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(Optional[MonitorLoadBalancerMonitorsListMonitorsResponse], monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_load_balancer_monitors_list_monitors(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.load_balancers.monitors.with_streaming_response.load_balancer_monitors_list_monitors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(Optional[MonitorLoadBalancerMonitorsListMonitorsResponse], monitor, path=["response"])

        assert cast(Any, response.is_closed) is True
