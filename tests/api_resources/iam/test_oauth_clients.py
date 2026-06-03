# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.iam import (
    OAuthClientGetResponse,
    OAuthClientListResponse,
    OAuthClientCreateResponse,
    OAuthClientDeleteResponse,
    OAuthClientUpdateResponse,
    OAuthClientRotateSecretResponse,
    OAuthClientDeleteRotatedSecretResponse,
)
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuthClients:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        oauth_client = client.iam.oauth_clients.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            client_name="My OAuth App",
            grant_types=["authorization_code", "refresh_token"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
        )
        assert_matches_type(Optional[OAuthClientCreateResponse], oauth_client, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        oauth_client = client.iam.oauth_clients.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            client_name="My OAuth App",
            grant_types=["authorization_code", "refresh_token"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
            allowed_cors_origins=["https://example.com"],
            client_uri="https://example.com",
            logo_uri="https://example.com/logo.png",
            policy_uri="https://example.com/privacy",
            post_logout_redirect_uris=["https://example.com/logout"],
            tos_uri="https://example.com/tos",
        )
        assert_matches_type(Optional[OAuthClientCreateResponse], oauth_client, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.iam.oauth_clients.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            client_name="My OAuth App",
            grant_types=["authorization_code", "refresh_token"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(Optional[OAuthClientCreateResponse], oauth_client, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.iam.oauth_clients.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            client_name="My OAuth App",
            grant_types=["authorization_code", "refresh_token"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(Optional[OAuthClientCreateResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.create(
                account_id="",
                client_name="My OAuth App",
                grant_types=["authorization_code", "refresh_token"],
                redirect_uris=["https://example.com/callback"],
                response_types=["code"],
                scopes=["account.read"],
                token_endpoint_auth_method="client_secret_post",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        oauth_client = client.iam.oauth_clients.update(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientUpdateResponse], oauth_client, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        oauth_client = client.iam.oauth_clients.update(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_cors_origins=["https://example.com"],
            client_name="My OAuth App",
            client_uri="https://example.com",
            grant_types=["authorization_code", "refresh_token"],
            logo_uri="https://example.com/logo.png",
            policy_uri="https://example.com/privacy",
            post_logout_redirect_uris=["https://example.com/logout"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
            tos_uri="https://example.com/tos",
            visibility="public",
        )
        assert_matches_type(Optional[OAuthClientUpdateResponse], oauth_client, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.iam.oauth_clients.with_raw_response.update(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(Optional[OAuthClientUpdateResponse], oauth_client, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.iam.oauth_clients.with_streaming_response.update(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(Optional[OAuthClientUpdateResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.update(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.update(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        oauth_client = client.iam.oauth_clients.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[OAuthClientListResponse], oauth_client, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.iam.oauth_clients.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(SyncSinglePage[OAuthClientListResponse], oauth_client, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.iam.oauth_clients.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(SyncSinglePage[OAuthClientListResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        oauth_client = client.iam.oauth_clients.delete(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientDeleteResponse], oauth_client, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.iam.oauth_clients.with_raw_response.delete(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(Optional[OAuthClientDeleteResponse], oauth_client, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.iam.oauth_clients.with_streaming_response.delete(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(Optional[OAuthClientDeleteResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.delete(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.delete(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete_rotated_secret(self, client: Cloudflare) -> None:
        oauth_client = client.iam.oauth_clients.delete_rotated_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientDeleteRotatedSecretResponse], oauth_client, path=["response"])

    @parametrize
    def test_raw_response_delete_rotated_secret(self, client: Cloudflare) -> None:
        response = client.iam.oauth_clients.with_raw_response.delete_rotated_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(Optional[OAuthClientDeleteRotatedSecretResponse], oauth_client, path=["response"])

    @parametrize
    def test_streaming_response_delete_rotated_secret(self, client: Cloudflare) -> None:
        with client.iam.oauth_clients.with_streaming_response.delete_rotated_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(Optional[OAuthClientDeleteRotatedSecretResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_rotated_secret(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.delete_rotated_secret(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.delete_rotated_secret(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        oauth_client = client.iam.oauth_clients.get(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientGetResponse], oauth_client, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.iam.oauth_clients.with_raw_response.get(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(Optional[OAuthClientGetResponse], oauth_client, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.iam.oauth_clients.with_streaming_response.get(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(Optional[OAuthClientGetResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.get(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.get(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_rotate_secret(self, client: Cloudflare) -> None:
        oauth_client = client.iam.oauth_clients.rotate_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientRotateSecretResponse], oauth_client, path=["response"])

    @parametrize
    def test_raw_response_rotate_secret(self, client: Cloudflare) -> None:
        response = client.iam.oauth_clients.with_raw_response.rotate_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = response.parse()
        assert_matches_type(Optional[OAuthClientRotateSecretResponse], oauth_client, path=["response"])

    @parametrize
    def test_streaming_response_rotate_secret(self, client: Cloudflare) -> None:
        with client.iam.oauth_clients.with_streaming_response.rotate_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = response.parse()
            assert_matches_type(Optional[OAuthClientRotateSecretResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rotate_secret(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.rotate_secret(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            client.iam.oauth_clients.with_raw_response.rotate_secret(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncOAuthClients:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        oauth_client = await async_client.iam.oauth_clients.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            client_name="My OAuth App",
            grant_types=["authorization_code", "refresh_token"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
        )
        assert_matches_type(Optional[OAuthClientCreateResponse], oauth_client, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        oauth_client = await async_client.iam.oauth_clients.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            client_name="My OAuth App",
            grant_types=["authorization_code", "refresh_token"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
            allowed_cors_origins=["https://example.com"],
            client_uri="https://example.com",
            logo_uri="https://example.com/logo.png",
            policy_uri="https://example.com/privacy",
            post_logout_redirect_uris=["https://example.com/logout"],
            tos_uri="https://example.com/tos",
        )
        assert_matches_type(Optional[OAuthClientCreateResponse], oauth_client, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.oauth_clients.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            client_name="My OAuth App",
            grant_types=["authorization_code", "refresh_token"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(Optional[OAuthClientCreateResponse], oauth_client, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.oauth_clients.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            client_name="My OAuth App",
            grant_types=["authorization_code", "refresh_token"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(Optional[OAuthClientCreateResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.create(
                account_id="",
                client_name="My OAuth App",
                grant_types=["authorization_code", "refresh_token"],
                redirect_uris=["https://example.com/callback"],
                response_types=["code"],
                scopes=["account.read"],
                token_endpoint_auth_method="client_secret_post",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        oauth_client = await async_client.iam.oauth_clients.update(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientUpdateResponse], oauth_client, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        oauth_client = await async_client.iam.oauth_clients.update(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_cors_origins=["https://example.com"],
            client_name="My OAuth App",
            client_uri="https://example.com",
            grant_types=["authorization_code", "refresh_token"],
            logo_uri="https://example.com/logo.png",
            policy_uri="https://example.com/privacy",
            post_logout_redirect_uris=["https://example.com/logout"],
            redirect_uris=["https://example.com/callback"],
            response_types=["code"],
            scopes=["account.read"],
            token_endpoint_auth_method="client_secret_post",
            tos_uri="https://example.com/tos",
            visibility="public",
        )
        assert_matches_type(Optional[OAuthClientUpdateResponse], oauth_client, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.oauth_clients.with_raw_response.update(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(Optional[OAuthClientUpdateResponse], oauth_client, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.oauth_clients.with_streaming_response.update(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(Optional[OAuthClientUpdateResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.update(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.update(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        oauth_client = await async_client.iam.oauth_clients.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[OAuthClientListResponse], oauth_client, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.oauth_clients.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(AsyncSinglePage[OAuthClientListResponse], oauth_client, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.oauth_clients.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(AsyncSinglePage[OAuthClientListResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        oauth_client = await async_client.iam.oauth_clients.delete(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientDeleteResponse], oauth_client, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.oauth_clients.with_raw_response.delete(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(Optional[OAuthClientDeleteResponse], oauth_client, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.oauth_clients.with_streaming_response.delete(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(Optional[OAuthClientDeleteResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.delete(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.delete(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete_rotated_secret(self, async_client: AsyncCloudflare) -> None:
        oauth_client = await async_client.iam.oauth_clients.delete_rotated_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientDeleteRotatedSecretResponse], oauth_client, path=["response"])

    @parametrize
    async def test_raw_response_delete_rotated_secret(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.oauth_clients.with_raw_response.delete_rotated_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(Optional[OAuthClientDeleteRotatedSecretResponse], oauth_client, path=["response"])

    @parametrize
    async def test_streaming_response_delete_rotated_secret(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.oauth_clients.with_streaming_response.delete_rotated_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(Optional[OAuthClientDeleteRotatedSecretResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_rotated_secret(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.delete_rotated_secret(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.delete_rotated_secret(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        oauth_client = await async_client.iam.oauth_clients.get(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientGetResponse], oauth_client, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.oauth_clients.with_raw_response.get(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(Optional[OAuthClientGetResponse], oauth_client, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.oauth_clients.with_streaming_response.get(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(Optional[OAuthClientGetResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.get(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.get(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        oauth_client = await async_client.iam.oauth_clients.rotate_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OAuthClientRotateSecretResponse], oauth_client, path=["response"])

    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.oauth_clients.with_raw_response.rotate_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth_client = await response.parse()
        assert_matches_type(Optional[OAuthClientRotateSecretResponse], oauth_client, path=["response"])

    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.oauth_clients.with_streaming_response.rotate_secret(
            oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth_client = await response.parse()
            assert_matches_type(Optional[OAuthClientRotateSecretResponse], oauth_client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.rotate_secret(
                oauth_client_id="a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `oauth_client_id` but received ''"):
            await async_client.iam.oauth_clients.with_raw_response.rotate_secret(
                oauth_client_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
