# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.load_balancers.monitors import PreviewCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        preview = client.load_balancers.monitors.previews.create(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        preview = client.load_balancers.monitors.previews.create(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            expected_codes="2xx",
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
            type="http",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.load_balancers.monitors.previews.with_raw_response.create(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.load_balancers.monitors.previews.with_streaming_response.create(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(PreviewCreateResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.load_balancers.monitors.previews.with_raw_response.create(
                monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.load_balancers.monitors.previews.with_raw_response.create(
                monitor_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPreviews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.load_balancers.monitors.previews.create(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.load_balancers.monitors.previews.create(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            expected_codes="2xx",
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
            type="http",
        )
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.monitors.previews.with_raw_response.create(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(PreviewCreateResponse, preview, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitors.previews.with_streaming_response.create(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(PreviewCreateResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.load_balancers.monitors.previews.with_raw_response.create(
                monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.load_balancers.monitors.previews.with_raw_response.create(
                monitor_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
