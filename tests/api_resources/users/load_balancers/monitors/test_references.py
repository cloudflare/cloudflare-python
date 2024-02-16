# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.users.load_balancers.monitors import ReferenceLoadBalancerMonitorsListMonitorReferencesResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_monitors_list_monitor_references(self, client: Cloudflare) -> None:
        reference = client.users.load_balancers.monitors.references.load_balancer_monitors_list_monitor_references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )
        assert_matches_type(
            Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse], reference, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_load_balancer_monitors_list_monitor_references(self, client: Cloudflare) -> None:
        response = client.users.load_balancers.monitors.references.with_raw_response.load_balancer_monitors_list_monitor_references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = response.parse()
        assert_matches_type(
            Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse], reference, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_load_balancer_monitors_list_monitor_references(self, client: Cloudflare) -> None:
        with client.users.load_balancers.monitors.references.with_streaming_response.load_balancer_monitors_list_monitor_references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = response.parse()
            assert_matches_type(
                Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse], reference, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_load_balancer_monitors_list_monitor_references(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.users.load_balancers.monitors.references.with_raw_response.load_balancer_monitors_list_monitor_references(
                "",
            )


class TestAsyncReferences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_monitors_list_monitor_references(self, async_client: AsyncCloudflare) -> None:
        reference = (
            await async_client.users.load_balancers.monitors.references.load_balancer_monitors_list_monitor_references(
                "f1aba936b94213e5b8dca0c0dbf1f9cc",
            )
        )
        assert_matches_type(
            Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse], reference, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_load_balancer_monitors_list_monitor_references(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.users.load_balancers.monitors.references.with_raw_response.load_balancer_monitors_list_monitor_references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = await response.parse()
        assert_matches_type(
            Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse], reference, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_load_balancer_monitors_list_monitor_references(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.load_balancers.monitors.references.with_streaming_response.load_balancer_monitors_list_monitor_references(
            "f1aba936b94213e5b8dca0c0dbf1f9cc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = await response.parse()
            assert_matches_type(
                Optional[ReferenceLoadBalancerMonitorsListMonitorReferencesResponse], reference, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_load_balancer_monitors_list_monitor_references(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.users.load_balancers.monitors.references.with_raw_response.load_balancer_monitors_list_monitor_references(
                "",
            )
