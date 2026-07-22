# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.casb.applications import AuthMethodListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthMethods:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        auth_method = client.zero_trust.casb.applications.auth_methods.list(
            application_id="ANTHROPIC",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.applications.auth_methods.with_raw_response.list(
            application_id="ANTHROPIC",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_method = response.parse()
        assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.applications.auth_methods.with_streaming_response.list(
            application_id="ANTHROPIC",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_method = response.parse()
            assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.applications.auth_methods.with_raw_response.list(
                application_id="ANTHROPIC",
                account_id="",
            )


class TestAsyncAuthMethods:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        auth_method = await async_client.zero_trust.casb.applications.auth_methods.list(
            application_id="ANTHROPIC",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.applications.auth_methods.with_raw_response.list(
            application_id="ANTHROPIC",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_method = await response.parse()
        assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.applications.auth_methods.with_streaming_response.list(
            application_id="ANTHROPIC",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_method = await response.parse()
            assert_matches_type(AuthMethodListResponse, auth_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.applications.auth_methods.with_raw_response.list(
                application_id="ANTHROPIC",
                account_id="",
            )
