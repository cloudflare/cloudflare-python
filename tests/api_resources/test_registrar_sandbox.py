# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.registrar_sandbox import (
    RegistrarSandboxCheckResponse,
    RegistrarSandboxSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegistrarSandbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_check(self, client: Cloudflare) -> None:
        registrar_sandbox = client.registrar_sandbox.check(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=[
                "myawesomebrand.com",
                "myawesomebrand.net",
                "myawesomebrand.org",
                "myawesomebrand.app",
                "myawesomebrand.dev",
            ],
        )
        assert_matches_type(RegistrarSandboxCheckResponse, registrar_sandbox, path=["response"])

    @parametrize
    def test_raw_response_check(self, client: Cloudflare) -> None:
        response = client.registrar_sandbox.with_raw_response.check(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=[
                "myawesomebrand.com",
                "myawesomebrand.net",
                "myawesomebrand.org",
                "myawesomebrand.app",
                "myawesomebrand.dev",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registrar_sandbox = response.parse()
        assert_matches_type(RegistrarSandboxCheckResponse, registrar_sandbox, path=["response"])

    @parametrize
    def test_streaming_response_check(self, client: Cloudflare) -> None:
        with client.registrar_sandbox.with_streaming_response.check(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=[
                "myawesomebrand.com",
                "myawesomebrand.net",
                "myawesomebrand.org",
                "myawesomebrand.app",
                "myawesomebrand.dev",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registrar_sandbox = response.parse()
            assert_matches_type(RegistrarSandboxCheckResponse, registrar_sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_check(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.registrar_sandbox.with_raw_response.check(
                account_id="",
                domains=[
                    "myawesomebrand.com",
                    "myawesomebrand.net",
                    "myawesomebrand.org",
                    "myawesomebrand.app",
                    "myawesomebrand.dev",
                ],
            )

    @parametrize
    def test_method_search(self, client: Cloudflare) -> None:
        registrar_sandbox = client.registrar_sandbox.search(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            q="x",
        )
        assert_matches_type(RegistrarSandboxSearchResponse, registrar_sandbox, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Cloudflare) -> None:
        registrar_sandbox = client.registrar_sandbox.search(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            q="x",
            extensions=["string"],
            limit=1,
        )
        assert_matches_type(RegistrarSandboxSearchResponse, registrar_sandbox, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Cloudflare) -> None:
        response = client.registrar_sandbox.with_raw_response.search(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registrar_sandbox = response.parse()
        assert_matches_type(RegistrarSandboxSearchResponse, registrar_sandbox, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Cloudflare) -> None:
        with client.registrar_sandbox.with_streaming_response.search(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registrar_sandbox = response.parse()
            assert_matches_type(RegistrarSandboxSearchResponse, registrar_sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.registrar_sandbox.with_raw_response.search(
                account_id="",
                q="x",
            )


class TestAsyncRegistrarSandbox:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_check(self, async_client: AsyncCloudflare) -> None:
        registrar_sandbox = await async_client.registrar_sandbox.check(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=[
                "myawesomebrand.com",
                "myawesomebrand.net",
                "myawesomebrand.org",
                "myawesomebrand.app",
                "myawesomebrand.dev",
            ],
        )
        assert_matches_type(RegistrarSandboxCheckResponse, registrar_sandbox, path=["response"])

    @parametrize
    async def test_raw_response_check(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.registrar_sandbox.with_raw_response.check(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=[
                "myawesomebrand.com",
                "myawesomebrand.net",
                "myawesomebrand.org",
                "myawesomebrand.app",
                "myawesomebrand.dev",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registrar_sandbox = await response.parse()
        assert_matches_type(RegistrarSandboxCheckResponse, registrar_sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncCloudflare) -> None:
        async with async_client.registrar_sandbox.with_streaming_response.check(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domains=[
                "myawesomebrand.com",
                "myawesomebrand.net",
                "myawesomebrand.org",
                "myawesomebrand.app",
                "myawesomebrand.dev",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registrar_sandbox = await response.parse()
            assert_matches_type(RegistrarSandboxCheckResponse, registrar_sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_check(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.registrar_sandbox.with_raw_response.check(
                account_id="",
                domains=[
                    "myawesomebrand.com",
                    "myawesomebrand.net",
                    "myawesomebrand.org",
                    "myawesomebrand.app",
                    "myawesomebrand.dev",
                ],
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncCloudflare) -> None:
        registrar_sandbox = await async_client.registrar_sandbox.search(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            q="x",
        )
        assert_matches_type(RegistrarSandboxSearchResponse, registrar_sandbox, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncCloudflare) -> None:
        registrar_sandbox = await async_client.registrar_sandbox.search(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            q="x",
            extensions=["string"],
            limit=1,
        )
        assert_matches_type(RegistrarSandboxSearchResponse, registrar_sandbox, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.registrar_sandbox.with_raw_response.search(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            q="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registrar_sandbox = await response.parse()
        assert_matches_type(RegistrarSandboxSearchResponse, registrar_sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncCloudflare) -> None:
        async with async_client.registrar_sandbox.with_streaming_response.search(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            q="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registrar_sandbox = await response.parse()
            assert_matches_type(RegistrarSandboxSearchResponse, registrar_sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.registrar_sandbox.with_raw_response.search(
                account_id="",
                q="x",
            )
