# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.diagnostics import Traceroute

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTraceroutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        traceroute = client.diagnostics.traceroutes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        )
        assert_matches_type(SyncSinglePage[Traceroute], traceroute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        traceroute = client.diagnostics.traceroutes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(SyncSinglePage[Traceroute], traceroute, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.diagnostics.traceroutes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute = response.parse()
        assert_matches_type(SyncSinglePage[Traceroute], traceroute, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.diagnostics.traceroutes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute = response.parse()
            assert_matches_type(SyncSinglePage[Traceroute], traceroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.diagnostics.traceroutes.with_raw_response.create(
                account_id="",
                targets=["203.0.113.1", "cloudflare.com"],
            )


class TestAsyncTraceroutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        traceroute = await async_client.diagnostics.traceroutes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        )
        assert_matches_type(AsyncSinglePage[Traceroute], traceroute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        traceroute = await async_client.diagnostics.traceroutes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(AsyncSinglePage[Traceroute], traceroute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.diagnostics.traceroutes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        traceroute = await response.parse()
        assert_matches_type(AsyncSinglePage[Traceroute], traceroute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.diagnostics.traceroutes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            targets=["203.0.113.1", "cloudflare.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            traceroute = await response.parse()
            assert_matches_type(AsyncSinglePage[Traceroute], traceroute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.diagnostics.traceroutes.with_raw_response.create(
                account_id="",
                targets=["203.0.113.1", "cloudflare.com"],
            )
