# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.containers.registries import CredentialGenerateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate(self, client: Cloudflare) -> None:
        credential = client.containers.registries.credentials.generate(
            domain="registry.cloudflare.com",
            account_id="account-123",
        )
        assert_matches_type(CredentialGenerateResponse, credential, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: Cloudflare) -> None:
        credential = client.containers.registries.credentials.generate(
            domain="registry.cloudflare.com",
            account_id="account-123",
            expiration_minutes=1,
            permissions=["pull"],
        )
        assert_matches_type(CredentialGenerateResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: Cloudflare) -> None:
        response = client.containers.registries.credentials.with_raw_response.generate(
            domain="registry.cloudflare.com",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialGenerateResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: Cloudflare) -> None:
        with client.containers.registries.credentials.with_streaming_response.generate(
            domain="registry.cloudflare.com",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialGenerateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_generate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.registries.credentials.with_raw_response.generate(
                domain="registry.cloudflare.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            client.containers.registries.credentials.with_raw_response.generate(
                domain="",
                account_id="account-123",
            )


class TestAsyncCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_generate(self, async_client: AsyncCloudflare) -> None:
        credential = await async_client.containers.registries.credentials.generate(
            domain="registry.cloudflare.com",
            account_id="account-123",
        )
        assert_matches_type(CredentialGenerateResponse, credential, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncCloudflare) -> None:
        credential = await async_client.containers.registries.credentials.generate(
            domain="registry.cloudflare.com",
            account_id="account-123",
            expiration_minutes=1,
            permissions=["pull"],
        )
        assert_matches_type(CredentialGenerateResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.registries.credentials.with_raw_response.generate(
            domain="registry.cloudflare.com",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialGenerateResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.registries.credentials.with_streaming_response.generate(
            domain="registry.cloudflare.com",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialGenerateResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_generate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.registries.credentials.with_raw_response.generate(
                domain="registry.cloudflare.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            await async_client.containers.registries.credentials.with_raw_response.generate(
                domain="",
                account_id="account-123",
            )
