# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.users.load_balancers.monitors import PreviewLoadBalancerMonitorsPreviewMonitorResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users.load_balancers.monitors import preview_load_balancer_monitors_preview_monitor_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_monitors_preview_monitor(self, client: Cloudflare) -> None:
        preview = client.users.load_balancers.monitors.previews.load_balancer_monitors_preview_monitor(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(PreviewLoadBalancerMonitorsPreviewMonitorResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_monitors_preview_monitor_with_all_params(self, client: Cloudflare) -> None:
        preview = client.users.load_balancers.monitors.previews.load_balancer_monitors_preview_monitor(
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
        assert_matches_type(PreviewLoadBalancerMonitorsPreviewMonitorResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_load_balancer_monitors_preview_monitor(self, client: Cloudflare) -> None:
        response = (
            client.users.load_balancers.monitors.previews.with_raw_response.load_balancer_monitors_preview_monitor(
                "f1aba936b94213e5b8dca0c0dbf1f9cc",
                expected_codes="2xx",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(PreviewLoadBalancerMonitorsPreviewMonitorResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_load_balancer_monitors_preview_monitor(self, client: Cloudflare) -> None:
        with client.users.load_balancers.monitors.previews.with_streaming_response.load_balancer_monitors_preview_monitor(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(PreviewLoadBalancerMonitorsPreviewMonitorResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_load_balancer_monitors_preview_monitor(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.load_balancers.monitors.previews.with_raw_response.load_balancer_monitors_preview_monitor(
                "",
                expected_codes="2xx",
            )


class TestAsyncPreviews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_monitors_preview_monitor(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.users.load_balancers.monitors.previews.load_balancer_monitors_preview_monitor(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )
        assert_matches_type(PreviewLoadBalancerMonitorsPreviewMonitorResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_monitors_preview_monitor_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        preview = await async_client.users.load_balancers.monitors.previews.load_balancer_monitors_preview_monitor(
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
        assert_matches_type(PreviewLoadBalancerMonitorsPreviewMonitorResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_load_balancer_monitors_preview_monitor(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.load_balancers.monitors.previews.with_raw_response.load_balancer_monitors_preview_monitor(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(PreviewLoadBalancerMonitorsPreviewMonitorResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_load_balancer_monitors_preview_monitor(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.load_balancers.monitors.previews.with_streaming_response.load_balancer_monitors_preview_monitor(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(PreviewLoadBalancerMonitorsPreviewMonitorResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_load_balancer_monitors_preview_monitor(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.load_balancers.monitors.previews.with_raw_response.load_balancer_monitors_preview_monitor(
                "",
                expected_codes="2xx",
            )
