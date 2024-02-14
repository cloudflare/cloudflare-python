# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.users.load_balancers import (
    MonitorUpdateResponse,
    MonitorDeleteResponse,
    MonitorGetResponse,
    MonitorLoadBalancerMonitorsCreateMonitorResponse,
    MonitorLoadBalancerMonitorsListMonitorsResponse,
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
from cloudflare.types.users.load_balancers import monitor_update_params
from cloudflare.types.users.load_balancers import monitor_load_balancer_monitors_create_monitor_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        monitor = client.users.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        monitor = client.users.load_balancers.monitors.update(
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
            api_timeout=0,
            type="https",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.users.load_balancers.monitors.with_raw_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.users.load_balancers.monitors.with_streaming_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.load_balancers.monitors.with_raw_response.update(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        monitor = client.users.load_balancers.monitors.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.users.load_balancers.monitors.with_raw_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.users.load_balancers.monitors.with_streaming_response.delete(
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.load_balancers.monitors.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        monitor = client.users.load_balancers.monitors.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(MonitorGetResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.users.load_balancers.monitors.with_raw_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorGetResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.users.load_balancers.monitors.with_streaming_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorGetResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.load_balancers.monitors.with_raw_response.get(
                "",
            )

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
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.users.load_balancers.monitors.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.users.load_balancers.monitors.update(
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
            api_timeout=0,
            type="https",
        )
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.load_balancers.monitors.with_raw_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.load_balancers.monitors.with_streaming_response.update(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorUpdateResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.load_balancers.monitors.with_raw_response.update(
                "",
                expected_codes="2xx",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.users.load_balancers.monitors.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.load_balancers.monitors.with_raw_response.delete(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorDeleteResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.load_balancers.monitors.with_streaming_response.delete(
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.load_balancers.monitors.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        monitor = await async_client.users.load_balancers.monitors.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(MonitorGetResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.load_balancers.monitors.with_raw_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorGetResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.load_balancers.monitors.with_streaming_response.get(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorGetResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.load_balancers.monitors.with_raw_response.get(
                "",
            )

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
