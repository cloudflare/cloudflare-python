# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import (
    IdentityProviderGetResponse,
    IdentityProviderListResponse,
    IdentityProviderCreateResponse,
    IdentityProviderDeleteResponse,
    IdentityProviderUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdentityProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        identity_provider = client.access.identity_providers.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        )
        assert_matches_type(IdentityProviderCreateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        identity_provider = client.access.identity_providers.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "email_claim_name": "custom_claim_name",
                "conditional_access_enabled": True,
                "directory_id": "<your azure directory uuid>",
                "support_groups": True,
                "centrify_account": "https://abc123.my.centrify.com/",
                "centrify_app_id": "exampleapp",
                "apps_domain": "mycompany.com",
                "auth_url": "https://accounts.google.com/o/oauth2/auth",
                "certs_url": "https://www.googleapis.com/oauth2/v3/certs",
                "scopes": ["openid", "email", "profile"],
                "token_url": "https://accounts.google.com/o/oauth2/token",
                "authorization_server_id": "aus9o8wzkhckw9TLa0h7z",
                "okta_account": "https://dev-abc123.oktapreview.com",
                "onelogin_account": "https://mycompany.onelogin.com",
                "ping_env_id": "342b5660-0c32-4936-a5a4-ce21fae57b0a",
                "attributes": ["group", "department_code", "divison"],
                "email_attribute_name": "Email",
                "header_attributes": [
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                ],
                "idp_public_certs": ["string", "string", "string"],
                "issuer_url": "https://whoami.com",
                "sign_request": True,
                "sso_target_url": "https://edgeaccess.org/idp/saml/login",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            scim_config={
                "enabled": True,
                "group_member_deprovision": True,
                "seat_deprovision": True,
                "secret": "string",
                "user_deprovision": True,
            },
        )
        assert_matches_type(IdentityProviderCreateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.access.identity_providers.with_raw_response.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(IdentityProviderCreateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.access.identity_providers.with_streaming_response.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(IdentityProviderCreateResponse, identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.identity_providers.with_raw_response.create(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.identity_providers.with_raw_response.create(
                account_id="string",
                zone_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        identity_provider = client.access.identity_providers.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        )
        assert_matches_type(IdentityProviderUpdateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        identity_provider = client.access.identity_providers.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "email_claim_name": "custom_claim_name",
                "conditional_access_enabled": True,
                "directory_id": "<your azure directory uuid>",
                "support_groups": True,
                "centrify_account": "https://abc123.my.centrify.com/",
                "centrify_app_id": "exampleapp",
                "apps_domain": "mycompany.com",
                "auth_url": "https://accounts.google.com/o/oauth2/auth",
                "certs_url": "https://www.googleapis.com/oauth2/v3/certs",
                "scopes": ["openid", "email", "profile"],
                "token_url": "https://accounts.google.com/o/oauth2/token",
                "authorization_server_id": "aus9o8wzkhckw9TLa0h7z",
                "okta_account": "https://dev-abc123.oktapreview.com",
                "onelogin_account": "https://mycompany.onelogin.com",
                "ping_env_id": "342b5660-0c32-4936-a5a4-ce21fae57b0a",
                "attributes": ["group", "department_code", "divison"],
                "email_attribute_name": "Email",
                "header_attributes": [
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                ],
                "idp_public_certs": ["string", "string", "string"],
                "issuer_url": "https://whoami.com",
                "sign_request": True,
                "sso_target_url": "https://edgeaccess.org/idp/saml/login",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            scim_config={
                "enabled": True,
                "group_member_deprovision": True,
                "seat_deprovision": True,
                "secret": "string",
                "user_deprovision": True,
            },
        )
        assert_matches_type(IdentityProviderUpdateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.identity_providers.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(IdentityProviderUpdateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.identity_providers.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(IdentityProviderUpdateResponse, identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.identity_providers.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.identity_providers.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.identity_providers.with_raw_response.update(
                "",
                account_id="string",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        identity_provider = client.access.identity_providers.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.access.identity_providers.with_raw_response.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.access.identity_providers.with_streaming_response.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProviderListResponse], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.identity_providers.with_raw_response.list(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.identity_providers.with_raw_response.list(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        identity_provider = client.access.identity_providers.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IdentityProviderDeleteResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.access.identity_providers.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(IdentityProviderDeleteResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.access.identity_providers.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(IdentityProviderDeleteResponse, identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.identity_providers.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.identity_providers.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.identity_providers.with_raw_response.delete(
                "",
                account_id="string",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        identity_provider = client.access.identity_providers.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IdentityProviderGetResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.access.identity_providers.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(IdentityProviderGetResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.access.identity_providers.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(IdentityProviderGetResponse, identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.identity_providers.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.identity_providers.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.identity_providers.with_raw_response.get(
                "",
                account_id="string",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncIdentityProviders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.access.identity_providers.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        )
        assert_matches_type(IdentityProviderCreateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.access.identity_providers.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "email_claim_name": "custom_claim_name",
                "conditional_access_enabled": True,
                "directory_id": "<your azure directory uuid>",
                "support_groups": True,
                "centrify_account": "https://abc123.my.centrify.com/",
                "centrify_app_id": "exampleapp",
                "apps_domain": "mycompany.com",
                "auth_url": "https://accounts.google.com/o/oauth2/auth",
                "certs_url": "https://www.googleapis.com/oauth2/v3/certs",
                "scopes": ["openid", "email", "profile"],
                "token_url": "https://accounts.google.com/o/oauth2/token",
                "authorization_server_id": "aus9o8wzkhckw9TLa0h7z",
                "okta_account": "https://dev-abc123.oktapreview.com",
                "onelogin_account": "https://mycompany.onelogin.com",
                "ping_env_id": "342b5660-0c32-4936-a5a4-ce21fae57b0a",
                "attributes": ["group", "department_code", "divison"],
                "email_attribute_name": "Email",
                "header_attributes": [
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                ],
                "idp_public_certs": ["string", "string", "string"],
                "issuer_url": "https://whoami.com",
                "sign_request": True,
                "sso_target_url": "https://edgeaccess.org/idp/saml/login",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            scim_config={
                "enabled": True,
                "group_member_deprovision": True,
                "seat_deprovision": True,
                "secret": "string",
                "user_deprovision": True,
            },
        )
        assert_matches_type(IdentityProviderCreateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.identity_providers.with_raw_response.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(IdentityProviderCreateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.identity_providers.with_streaming_response.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(IdentityProviderCreateResponse, identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.create(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.create(
                account_id="string",
                zone_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.access.identity_providers.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        )
        assert_matches_type(IdentityProviderUpdateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.access.identity_providers.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "email_claim_name": "custom_claim_name",
                "conditional_access_enabled": True,
                "directory_id": "<your azure directory uuid>",
                "support_groups": True,
                "centrify_account": "https://abc123.my.centrify.com/",
                "centrify_app_id": "exampleapp",
                "apps_domain": "mycompany.com",
                "auth_url": "https://accounts.google.com/o/oauth2/auth",
                "certs_url": "https://www.googleapis.com/oauth2/v3/certs",
                "scopes": ["openid", "email", "profile"],
                "token_url": "https://accounts.google.com/o/oauth2/token",
                "authorization_server_id": "aus9o8wzkhckw9TLa0h7z",
                "okta_account": "https://dev-abc123.oktapreview.com",
                "onelogin_account": "https://mycompany.onelogin.com",
                "ping_env_id": "342b5660-0c32-4936-a5a4-ce21fae57b0a",
                "attributes": ["group", "department_code", "divison"],
                "email_attribute_name": "Email",
                "header_attributes": [
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                    {
                        "attribute_name": "string",
                        "header_name": "string",
                    },
                ],
                "idp_public_certs": ["string", "string", "string"],
                "issuer_url": "https://whoami.com",
                "sign_request": True,
                "sso_target_url": "https://edgeaccess.org/idp/saml/login",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            scim_config={
                "enabled": True,
                "group_member_deprovision": True,
                "seat_deprovision": True,
                "secret": "string",
                "user_deprovision": True,
            },
        )
        assert_matches_type(IdentityProviderUpdateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.identity_providers.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(IdentityProviderUpdateResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.identity_providers.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(IdentityProviderUpdateResponse, identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.identity_providers.with_raw_response.update(
                "",
                account_id="string",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.access.identity_providers.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.identity_providers.with_raw_response.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.identity_providers.with_streaming_response.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProviderListResponse], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.list(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.list(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.access.identity_providers.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IdentityProviderDeleteResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.identity_providers.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(IdentityProviderDeleteResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.identity_providers.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(IdentityProviderDeleteResponse, identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.identity_providers.with_raw_response.delete(
                "",
                account_id="string",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.access.identity_providers.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IdentityProviderGetResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.identity_providers.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(IdentityProviderGetResponse, identity_provider, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.identity_providers.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(IdentityProviderGetResponse, identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.identity_providers.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.identity_providers.with_raw_response.get(
                "",
                account_id="string",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
