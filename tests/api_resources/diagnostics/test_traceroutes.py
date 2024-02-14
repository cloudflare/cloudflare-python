# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.diagnostics import TracerouteDiagnosticsTracerouteResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.diagnostics import traceroute_diagnostics_traceroute_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraceroutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_diagnostics_traceroute(self, client: Cloudflare) -> None:
        traceroute = client.diagnostics.traceroutes.diagnostics_traceroute(
            "023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        )
        assert_matches_type(Optional[TracerouteDiagnosticsTracerouteResponse], traceroute, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_diagnostics_traceroute_with_all_params(self, client: Cloudflare) -> None:
        traceroute = client.diagnostics.traceroutes.diagnostics_traceroute(
            "023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
            colos=["den", "sin"],
            options={
                "max_ttl": 15,
                "packet_type": "icmp",
                "packets_per_ttl": 0,
                "port": 0,
                "wait_time": 1,
            },
        )
        assert_matches_type(Optional[TracerouteDiagnosticsTracerouteResponse], traceroute, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_diagnostics_traceroute(self, client: Cloudflare) -> None:
        response = client.diagnostics.traceroutes.with_raw_response.diagnostics_traceroute(
            "023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute = response.parse()
        assert_matches_type(Optional[TracerouteDiagnosticsTracerouteResponse], traceroute, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_diagnostics_traceroute(self, client: Cloudflare) -> None:
        with client.diagnostics.traceroutes.with_streaming_response.diagnostics_traceroute(
            "023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute = response.parse()
            assert_matches_type(Optional[TracerouteDiagnosticsTracerouteResponse], traceroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_diagnostics_traceroute(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.diagnostics.traceroutes.with_raw_response.diagnostics_traceroute(
                "",
                targets=["203.0.113.1", "cloudflare.com"],
            )


class TestAsyncTraceroutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_diagnostics_traceroute(self, async_client: AsyncCloudflare) -> None:
        traceroute = await async_client.diagnostics.traceroutes.diagnostics_traceroute(
            "023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        )
        assert_matches_type(Optional[TracerouteDiagnosticsTracerouteResponse], traceroute, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_diagnostics_traceroute_with_all_params(self, async_client: AsyncCloudflare) -> None:
        traceroute = await async_client.diagnostics.traceroutes.diagnostics_traceroute(
            "023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
            colos=["den", "sin"],
            options={
                "max_ttl": 15,
                "packet_type": "icmp",
                "packets_per_ttl": 0,
                "port": 0,
                "wait_time": 1,
            },
        )
        assert_matches_type(Optional[TracerouteDiagnosticsTracerouteResponse], traceroute, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_diagnostics_traceroute(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.diagnostics.traceroutes.with_raw_response.diagnostics_traceroute(
            "023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute = await response.parse()
        assert_matches_type(Optional[TracerouteDiagnosticsTracerouteResponse], traceroute, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_diagnostics_traceroute(self, async_client: AsyncCloudflare) -> None:
        async with async_client.diagnostics.traceroutes.with_streaming_response.diagnostics_traceroute(
            "023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute = await response.parse()
            assert_matches_type(Optional[TracerouteDiagnosticsTracerouteResponse], traceroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_diagnostics_traceroute(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.diagnostics.traceroutes.with_raw_response.diagnostics_traceroute(
                "",
                targets=["203.0.113.1", "cloudflare.com"],
            )
