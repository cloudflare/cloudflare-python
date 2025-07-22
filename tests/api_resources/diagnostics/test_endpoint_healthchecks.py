# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.diagnostics import (
    EndpointHealthcheckListResponse,
    EndpointHealthcheckCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEndpointHealthchecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        endpoint_healthcheck = client.diagnostics.endpoint_healthchecks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            check_type="icmp",
            endpoint="203.0.113.1",
        )
        assert_matches_type(Optional[EndpointHealthcheckCreateResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        endpoint_healthcheck = client.diagnostics.endpoint_healthchecks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            check_type="icmp",
            endpoint="203.0.113.1",
            name="My Endpoint",
        )
        assert_matches_type(Optional[EndpointHealthcheckCreateResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.diagnostics.endpoint_healthchecks.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            check_type="icmp",
            endpoint="203.0.113.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint_healthcheck = response.parse()
        assert_matches_type(Optional[EndpointHealthcheckCreateResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.diagnostics.endpoint_healthchecks.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            check_type="icmp",
            endpoint="203.0.113.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint_healthcheck = response.parse()
            assert_matches_type(Optional[EndpointHealthcheckCreateResponse], endpoint_healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.diagnostics.endpoint_healthchecks.with_raw_response.create(
                account_id="",
                check_type="icmp",
                endpoint="203.0.113.1",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        endpoint_healthcheck = client.diagnostics.endpoint_healthchecks.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EndpointHealthcheckListResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.diagnostics.endpoint_healthchecks.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint_healthcheck = response.parse()
        assert_matches_type(Optional[EndpointHealthcheckListResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.diagnostics.endpoint_healthchecks.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint_healthcheck = response.parse()
            assert_matches_type(Optional[EndpointHealthcheckListResponse], endpoint_healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.diagnostics.endpoint_healthchecks.with_raw_response.list(
                account_id="",
            )


class TestAsyncEndpointHealthchecks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        endpoint_healthcheck = await async_client.diagnostics.endpoint_healthchecks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            check_type="icmp",
            endpoint="203.0.113.1",
        )
        assert_matches_type(Optional[EndpointHealthcheckCreateResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        endpoint_healthcheck = await async_client.diagnostics.endpoint_healthchecks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            check_type="icmp",
            endpoint="203.0.113.1",
            name="My Endpoint",
        )
        assert_matches_type(Optional[EndpointHealthcheckCreateResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.diagnostics.endpoint_healthchecks.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            check_type="icmp",
            endpoint="203.0.113.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint_healthcheck = await response.parse()
        assert_matches_type(Optional[EndpointHealthcheckCreateResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.diagnostics.endpoint_healthchecks.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            check_type="icmp",
            endpoint="203.0.113.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint_healthcheck = await response.parse()
            assert_matches_type(Optional[EndpointHealthcheckCreateResponse], endpoint_healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.diagnostics.endpoint_healthchecks.with_raw_response.create(
                account_id="",
                check_type="icmp",
                endpoint="203.0.113.1",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        endpoint_healthcheck = await async_client.diagnostics.endpoint_healthchecks.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EndpointHealthcheckListResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.diagnostics.endpoint_healthchecks.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint_healthcheck = await response.parse()
        assert_matches_type(Optional[EndpointHealthcheckListResponse], endpoint_healthcheck, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.diagnostics.endpoint_healthchecks.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint_healthcheck = await response.parse()
            assert_matches_type(Optional[EndpointHealthcheckListResponse], endpoint_healthcheck, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.diagnostics.endpoint_healthchecks.with_raw_response.list(
                account_id="",
            )
