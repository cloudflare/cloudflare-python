# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.ai_gateway import (
    ProviderConfigListResponse,
    ProviderConfigCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviderConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        provider_config = client.ai_gateway.provider_configs.create(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            alias="alias",
            default_config=True,
            provider_slug="provider_slug",
            secret="secret",
            secret_id="secret_id",
        )
        assert_matches_type(ProviderConfigCreateResponse, provider_config, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        provider_config = client.ai_gateway.provider_configs.create(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            alias="alias",
            default_config=True,
            provider_slug="provider_slug",
            secret="secret",
            secret_id="secret_id",
            rate_limit=0,
            rate_limit_period=0,
        )
        assert_matches_type(ProviderConfigCreateResponse, provider_config, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ai_gateway.provider_configs.with_raw_response.create(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            alias="alias",
            default_config=True,
            provider_slug="provider_slug",
            secret="secret",
            secret_id="secret_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_config = response.parse()
        assert_matches_type(ProviderConfigCreateResponse, provider_config, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ai_gateway.provider_configs.with_streaming_response.create(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            alias="alias",
            default_config=True,
            provider_slug="provider_slug",
            secret="secret",
            secret_id="secret_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_config = response.parse()
            assert_matches_type(ProviderConfigCreateResponse, provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.provider_configs.with_raw_response.create(
                gateway_id="my-gateway",
                account_id="",
                alias="alias",
                default_config=True,
                provider_slug="provider_slug",
                secret="secret",
                secret_id="secret_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.provider_configs.with_raw_response.create(
                gateway_id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                alias="alias",
                default_config=True,
                provider_slug="provider_slug",
                secret="secret",
                secret_id="secret_id",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        provider_config = client.ai_gateway.provider_configs.list(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        )
        assert_matches_type(SyncV4PagePaginationArray[ProviderConfigListResponse], provider_config, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        provider_config = client.ai_gateway.provider_configs.list(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[ProviderConfigListResponse], provider_config, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.ai_gateway.provider_configs.with_raw_response.list(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_config = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ProviderConfigListResponse], provider_config, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.ai_gateway.provider_configs.with_streaming_response.list(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_config = response.parse()
            assert_matches_type(
                SyncV4PagePaginationArray[ProviderConfigListResponse], provider_config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai_gateway.provider_configs.with_raw_response.list(
                gateway_id="my-gateway",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.ai_gateway.provider_configs.with_raw_response.list(
                gateway_id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            )


class TestAsyncProviderConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        provider_config = await async_client.ai_gateway.provider_configs.create(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            alias="alias",
            default_config=True,
            provider_slug="provider_slug",
            secret="secret",
            secret_id="secret_id",
        )
        assert_matches_type(ProviderConfigCreateResponse, provider_config, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        provider_config = await async_client.ai_gateway.provider_configs.create(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            alias="alias",
            default_config=True,
            provider_slug="provider_slug",
            secret="secret",
            secret_id="secret_id",
            rate_limit=0,
            rate_limit_period=0,
        )
        assert_matches_type(ProviderConfigCreateResponse, provider_config, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.provider_configs.with_raw_response.create(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            alias="alias",
            default_config=True,
            provider_slug="provider_slug",
            secret="secret",
            secret_id="secret_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_config = await response.parse()
        assert_matches_type(ProviderConfigCreateResponse, provider_config, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.provider_configs.with_streaming_response.create(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            alias="alias",
            default_config=True,
            provider_slug="provider_slug",
            secret="secret",
            secret_id="secret_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_config = await response.parse()
            assert_matches_type(ProviderConfigCreateResponse, provider_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.provider_configs.with_raw_response.create(
                gateway_id="my-gateway",
                account_id="",
                alias="alias",
                default_config=True,
                provider_slug="provider_slug",
                secret="secret",
                secret_id="secret_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.provider_configs.with_raw_response.create(
                gateway_id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
                alias="alias",
                default_config=True,
                provider_slug="provider_slug",
                secret="secret",
                secret_id="secret_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        provider_config = await async_client.ai_gateway.provider_configs.list(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ProviderConfigListResponse], provider_config, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        provider_config = await async_client.ai_gateway.provider_configs.list(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[ProviderConfigListResponse], provider_config, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai_gateway.provider_configs.with_raw_response.list(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider_config = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ProviderConfigListResponse], provider_config, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai_gateway.provider_configs.with_streaming_response.list(
            gateway_id="my-gateway",
            account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider_config = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[ProviderConfigListResponse], provider_config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai_gateway.provider_configs.with_raw_response.list(
                gateway_id="my-gateway",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.ai_gateway.provider_configs.with_raw_response.list(
                gateway_id="",
                account_id="3ebbcb006d4d46d7bb6a8c7f14676cb0",
            )
