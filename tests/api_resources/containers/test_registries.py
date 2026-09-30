# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.containers import (
    RegistryListResponse,
    RegistryCreateResponse,
    RegistryDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegistries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        registry = client.containers.registries.create(
            account_id="account-123",
            auth={
                "private_credential": {
                    "secret_name": "API_KEY",
                    "store_id": "14758f1afd44c09b7992073ccf00b43d",
                },
                "public_credential": "example-user",
            },
            domain="docker.io",
            kind="ECR",
        )
        assert_matches_type(RegistryCreateResponse, registry, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        registry = client.containers.registries.create(
            account_id="account-123",
            auth={
                "private_credential": {
                    "secret_name": "API_KEY",
                    "store_id": "14758f1afd44c09b7992073ccf00b43d",
                },
                "public_credential": "example-user",
            },
            domain="docker.io",
            kind="ECR",
            is_public=False,
        )
        assert_matches_type(RegistryCreateResponse, registry, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.containers.registries.with_raw_response.create(
            account_id="account-123",
            auth={
                "private_credential": {
                    "secret_name": "API_KEY",
                    "store_id": "14758f1afd44c09b7992073ccf00b43d",
                },
                "public_credential": "example-user",
            },
            domain="docker.io",
            kind="ECR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = response.parse()
        assert_matches_type(RegistryCreateResponse, registry, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.containers.registries.with_streaming_response.create(
            account_id="account-123",
            auth={
                "private_credential": {
                    "secret_name": "API_KEY",
                    "store_id": "14758f1afd44c09b7992073ccf00b43d",
                },
                "public_credential": "example-user",
            },
            domain="docker.io",
            kind="ECR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = response.parse()
            assert_matches_type(RegistryCreateResponse, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.registries.with_raw_response.create(
                account_id="",
                auth={
                    "private_credential": {
                        "secret_name": "API_KEY",
                        "store_id": "14758f1afd44c09b7992073ccf00b43d",
                    },
                    "public_credential": "example-user",
                },
                domain="docker.io",
                kind="ECR",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        registry = client.containers.registries.list(
            account_id="account-123",
        )
        assert_matches_type(SyncSinglePage[RegistryListResponse], registry, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.containers.registries.with_raw_response.list(
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = response.parse()
        assert_matches_type(SyncSinglePage[RegistryListResponse], registry, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.containers.registries.with_streaming_response.list(
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = response.parse()
            assert_matches_type(SyncSinglePage[RegistryListResponse], registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.registries.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        registry = client.containers.registries.delete(
            domain="domain",
            account_id="account-123",
        )
        assert_matches_type(RegistryDeleteResponse, registry, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.containers.registries.with_raw_response.delete(
            domain="domain",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = response.parse()
        assert_matches_type(RegistryDeleteResponse, registry, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.containers.registries.with_streaming_response.delete(
            domain="domain",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = response.parse()
            assert_matches_type(RegistryDeleteResponse, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.containers.registries.with_raw_response.delete(
                domain="domain",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            client.containers.registries.with_raw_response.delete(
                domain="",
                account_id="account-123",
            )


class TestAsyncRegistries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        registry = await async_client.containers.registries.create(
            account_id="account-123",
            auth={
                "private_credential": {
                    "secret_name": "API_KEY",
                    "store_id": "14758f1afd44c09b7992073ccf00b43d",
                },
                "public_credential": "example-user",
            },
            domain="docker.io",
            kind="ECR",
        )
        assert_matches_type(RegistryCreateResponse, registry, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        registry = await async_client.containers.registries.create(
            account_id="account-123",
            auth={
                "private_credential": {
                    "secret_name": "API_KEY",
                    "store_id": "14758f1afd44c09b7992073ccf00b43d",
                },
                "public_credential": "example-user",
            },
            domain="docker.io",
            kind="ECR",
            is_public=False,
        )
        assert_matches_type(RegistryCreateResponse, registry, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.registries.with_raw_response.create(
            account_id="account-123",
            auth={
                "private_credential": {
                    "secret_name": "API_KEY",
                    "store_id": "14758f1afd44c09b7992073ccf00b43d",
                },
                "public_credential": "example-user",
            },
            domain="docker.io",
            kind="ECR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = await response.parse()
        assert_matches_type(RegistryCreateResponse, registry, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.registries.with_streaming_response.create(
            account_id="account-123",
            auth={
                "private_credential": {
                    "secret_name": "API_KEY",
                    "store_id": "14758f1afd44c09b7992073ccf00b43d",
                },
                "public_credential": "example-user",
            },
            domain="docker.io",
            kind="ECR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = await response.parse()
            assert_matches_type(RegistryCreateResponse, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.registries.with_raw_response.create(
                account_id="",
                auth={
                    "private_credential": {
                        "secret_name": "API_KEY",
                        "store_id": "14758f1afd44c09b7992073ccf00b43d",
                    },
                    "public_credential": "example-user",
                },
                domain="docker.io",
                kind="ECR",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        registry = await async_client.containers.registries.list(
            account_id="account-123",
        )
        assert_matches_type(AsyncSinglePage[RegistryListResponse], registry, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.registries.with_raw_response.list(
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = await response.parse()
        assert_matches_type(AsyncSinglePage[RegistryListResponse], registry, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.registries.with_streaming_response.list(
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = await response.parse()
            assert_matches_type(AsyncSinglePage[RegistryListResponse], registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.registries.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        registry = await async_client.containers.registries.delete(
            domain="domain",
            account_id="account-123",
        )
        assert_matches_type(RegistryDeleteResponse, registry, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.containers.registries.with_raw_response.delete(
            domain="domain",
            account_id="account-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registry = await response.parse()
        assert_matches_type(RegistryDeleteResponse, registry, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.containers.registries.with_streaming_response.delete(
            domain="domain",
            account_id="account-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registry = await response.parse()
            assert_matches_type(RegistryDeleteResponse, registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.containers.registries.with_raw_response.delete(
                domain="domain",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain` but received ''"):
            await async_client.containers.registries.with_raw_response.delete(
                domain="",
                account_id="account-123",
            )
