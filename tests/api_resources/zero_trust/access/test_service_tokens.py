# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access import ServiceToken, ServiceTokenCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.create(
            name="CI/CD token",
            account_id="string",
        )
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.create(
            name="CI/CD token",
            account_id="string",
            duration="60m",
        )
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.service_tokens.with_raw_response.create(
            name="CI/CD token",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.service_tokens.with_streaming_response.create(
            name="CI/CD token",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.create(
                name="CI/CD token",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.create(
                name="CI/CD token",
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.list(
            account_id="string",
        )
        assert_matches_type(SyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        service_token = client.zero_trust.access.service_tokens.list(
            account_id="string",
        )
        assert_matches_type(SyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.service_tokens.with_raw_response.list(
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(SyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.service_tokens.with_streaming_response.list(
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(SyncSinglePage[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zero_trust.access.service_tokens.with_raw_response.list(
                account_id="string",
            )


class TestAsyncServiceTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.create(
            name="CI/CD token",
            account_id="string",
        )
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.create(
            name="CI/CD token",
            account_id="string",
            duration="60m",
        )
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.service_tokens.with_raw_response.create(
            name="CI/CD token",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.service_tokens.with_streaming_response.create(
            name="CI/CD token",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(Optional[ServiceTokenCreateResponse], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.create(
                name="CI/CD token",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.create(
                name="CI/CD token",
                account_id="string",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.list(
            account_id="string",
        )
        assert_matches_type(AsyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.zero_trust.access.service_tokens.list(
            account_id="string",
        )
        assert_matches_type(AsyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.service_tokens.with_raw_response.list(
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(AsyncSinglePage[ServiceToken], service_token, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.service_tokens.with_streaming_response.list(
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(AsyncSinglePage[ServiceToken], service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zero_trust.access.service_tokens.with_raw_response.list(
                account_id="string",
            )
