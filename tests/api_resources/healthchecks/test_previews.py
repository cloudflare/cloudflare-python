# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.healthchecks import (
    Healthcheck,
    PreviewDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        preview = client.healthchecks.previews.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        preview = client.healthchecks.previews.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
            check_regions=["WNAM", "ENAM"],
            consecutive_fails=0,
            consecutive_successes=0,
            description="Health check for www.example.com",
            http_config={
                "allow_insecure": True,
                "expected_body": "success",
                "expected_codes": ["2xx", "302"],
                "follow_redirects": True,
                "header": {
                    "Host": ["example.com"],
                    "X-App-ID": ["abc123"],
                },
                "method": "GET",
                "path": "/health",
                "port": 0,
            },
            interval=0,
            retries=0,
            suspended=True,
            tcp_config={
                "method": "connection_established",
                "port": 0,
            },
            healthcheck_timeout=0,
            type="HTTPS",
        )
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.healthchecks.previews.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.healthchecks.previews.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(Healthcheck, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.healthchecks.previews.with_raw_response.create(
                zone_id="",
                address="www.example.com",
                name="server-1",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        preview = client.healthchecks.previews.delete(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PreviewDeleteResponse, preview, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.healthchecks.previews.with_raw_response.delete(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(PreviewDeleteResponse, preview, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.healthchecks.previews.with_streaming_response.delete(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(PreviewDeleteResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.healthchecks.previews.with_raw_response.delete(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            client.healthchecks.previews.with_raw_response.delete(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        preview = client.healthchecks.previews.get(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.healthchecks.previews.with_raw_response.get(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.healthchecks.previews.with_streaming_response.get(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(Healthcheck, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.healthchecks.previews.with_raw_response.get(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            client.healthchecks.previews.with_raw_response.get(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPreviews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.healthchecks.previews.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.healthchecks.previews.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
            check_regions=["WNAM", "ENAM"],
            consecutive_fails=0,
            consecutive_successes=0,
            description="Health check for www.example.com",
            http_config={
                "allow_insecure": True,
                "expected_body": "success",
                "expected_codes": ["2xx", "302"],
                "follow_redirects": True,
                "header": {
                    "Host": ["example.com"],
                    "X-App-ID": ["abc123"],
                },
                "method": "GET",
                "path": "/health",
                "port": 0,
            },
            interval=0,
            retries=0,
            suspended=True,
            tcp_config={
                "method": "connection_established",
                "port": 0,
            },
            healthcheck_timeout=0,
            type="HTTPS",
        )
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.healthchecks.previews.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.healthchecks.previews.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            address="www.example.com",
            name="server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(Healthcheck, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.healthchecks.previews.with_raw_response.create(
                zone_id="",
                address="www.example.com",
                name="server-1",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.healthchecks.previews.delete(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PreviewDeleteResponse, preview, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.healthchecks.previews.with_raw_response.delete(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(PreviewDeleteResponse, preview, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.healthchecks.previews.with_streaming_response.delete(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(PreviewDeleteResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.healthchecks.previews.with_raw_response.delete(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            await async_client.healthchecks.previews.with_raw_response.delete(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.healthchecks.previews.get(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.healthchecks.previews.with_raw_response.get(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(Healthcheck, preview, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.healthchecks.previews.with_streaming_response.get(
            healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(Healthcheck, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.healthchecks.previews.with_raw_response.get(
                healthcheck_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `healthcheck_id` but received ''"):
            await async_client.healthchecks.previews.with_raw_response.get(
                healthcheck_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
