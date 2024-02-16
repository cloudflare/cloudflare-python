# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.access import (
    ServiceTokenUpdateResponse,
    ServiceTokenDeleteResponse,
    ServiceTokenAccessServiceTokensCreateAServiceTokenResponse,
    ServiceTokenAccessServiceTokensListServiceTokensResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import service_token_update_params
from cloudflare.types.access import service_token_access_service_tokens_create_a_service_token_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        service_token = client.access.service_tokens.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ServiceTokenUpdateResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        service_token = client.access.service_tokens.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            duration="60m",
            name="CI/CD token",
        )
        assert_matches_type(ServiceTokenUpdateResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.service_tokens.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(ServiceTokenUpdateResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.service_tokens.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(ServiceTokenUpdateResponse, service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.service_tokens.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.service_tokens.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.service_tokens.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        service_token = client.access.service_tokens.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ServiceTokenDeleteResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.access.service_tokens.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(ServiceTokenDeleteResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.access.service_tokens.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(ServiceTokenDeleteResponse, service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.service_tokens.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.service_tokens.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.service_tokens.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_service_tokens_create_a_service_token(self, client: Cloudflare) -> None:
        service_token = client.access.service_tokens.access_service_tokens_create_a_service_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            name="CI/CD token",
        )
        assert_matches_type(
            ServiceTokenAccessServiceTokensCreateAServiceTokenResponse, service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_service_tokens_create_a_service_token_with_all_params(self, client: Cloudflare) -> None:
        service_token = client.access.service_tokens.access_service_tokens_create_a_service_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            name="CI/CD token",
            duration="60m",
        )
        assert_matches_type(
            ServiceTokenAccessServiceTokensCreateAServiceTokenResponse, service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_service_tokens_create_a_service_token(self, client: Cloudflare) -> None:
        response = client.access.service_tokens.with_raw_response.access_service_tokens_create_a_service_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            name="CI/CD token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(
            ServiceTokenAccessServiceTokensCreateAServiceTokenResponse, service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_service_tokens_create_a_service_token(self, client: Cloudflare) -> None:
        with client.access.service_tokens.with_streaming_response.access_service_tokens_create_a_service_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            name="CI/CD token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(
                ServiceTokenAccessServiceTokensCreateAServiceTokenResponse, service_token, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_service_tokens_create_a_service_token(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.service_tokens.with_raw_response.access_service_tokens_create_a_service_token(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                name="CI/CD token",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.service_tokens.with_raw_response.access_service_tokens_create_a_service_token(
                "",
                account_or_zone="string",
                name="CI/CD token",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_service_tokens_list_service_tokens(self, client: Cloudflare) -> None:
        service_token = client.access.service_tokens.access_service_tokens_list_service_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(
            Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse], service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_service_tokens_list_service_tokens(self, client: Cloudflare) -> None:
        response = client.access.service_tokens.with_raw_response.access_service_tokens_list_service_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = response.parse()
        assert_matches_type(
            Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse], service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_service_tokens_list_service_tokens(self, client: Cloudflare) -> None:
        with client.access.service_tokens.with_streaming_response.access_service_tokens_list_service_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = response.parse()
            assert_matches_type(
                Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse], service_token, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_service_tokens_list_service_tokens(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.service_tokens.with_raw_response.access_service_tokens_list_service_tokens(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.service_tokens.with_raw_response.access_service_tokens_list_service_tokens(
                "",
                account_or_zone="string",
            )


class TestAsyncServiceTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.access.service_tokens.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ServiceTokenUpdateResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.access.service_tokens.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            duration="60m",
            name="CI/CD token",
        )
        assert_matches_type(ServiceTokenUpdateResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.service_tokens.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(ServiceTokenUpdateResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.service_tokens.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(ServiceTokenUpdateResponse, service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.service_tokens.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.service_tokens.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.service_tokens.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.access.service_tokens.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ServiceTokenDeleteResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.service_tokens.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(ServiceTokenDeleteResponse, service_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.service_tokens.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(ServiceTokenDeleteResponse, service_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.service_tokens.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.service_tokens.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.service_tokens.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_service_tokens_create_a_service_token(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.access.service_tokens.access_service_tokens_create_a_service_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            name="CI/CD token",
        )
        assert_matches_type(
            ServiceTokenAccessServiceTokensCreateAServiceTokenResponse, service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_service_tokens_create_a_service_token_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        service_token = await async_client.access.service_tokens.access_service_tokens_create_a_service_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            name="CI/CD token",
            duration="60m",
        )
        assert_matches_type(
            ServiceTokenAccessServiceTokensCreateAServiceTokenResponse, service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_service_tokens_create_a_service_token(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.access.service_tokens.with_raw_response.access_service_tokens_create_a_service_token(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                name="CI/CD token",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(
            ServiceTokenAccessServiceTokensCreateAServiceTokenResponse, service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_service_tokens_create_a_service_token(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.service_tokens.with_streaming_response.access_service_tokens_create_a_service_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            name="CI/CD token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(
                ServiceTokenAccessServiceTokensCreateAServiceTokenResponse, service_token, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_service_tokens_create_a_service_token(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.service_tokens.with_raw_response.access_service_tokens_create_a_service_token(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                name="CI/CD token",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.service_tokens.with_raw_response.access_service_tokens_create_a_service_token(
                "",
                account_or_zone="string",
                name="CI/CD token",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_service_tokens_list_service_tokens(self, async_client: AsyncCloudflare) -> None:
        service_token = await async_client.access.service_tokens.access_service_tokens_list_service_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(
            Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse], service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_service_tokens_list_service_tokens(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.service_tokens.with_raw_response.access_service_tokens_list_service_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_token = await response.parse()
        assert_matches_type(
            Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse], service_token, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_service_tokens_list_service_tokens(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.service_tokens.with_streaming_response.access_service_tokens_list_service_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_token = await response.parse()
            assert_matches_type(
                Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse], service_token, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_service_tokens_list_service_tokens(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.service_tokens.with_raw_response.access_service_tokens_list_service_tokens(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.service_tokens.with_raw_response.access_service_tokens_list_service_tokens(
                "",
                account_or_zone="string",
            )
