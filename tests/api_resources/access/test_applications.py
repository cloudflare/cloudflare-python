# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import (
    ApplicationGetResponse,
    ApplicationListResponse,
    ApplicationCreateResponse,
    ApplicationDeleteResponse,
    ApplicationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        application = client.access.applications.create(
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        application = client.access.applications.create(
            account_id="string",
            zone_id="string",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible={},
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": [{}, {}, {}],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="string",
            custom_deny_url="string",
            custom_non_identity_deny_url="string",
            custom_pages=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            domain="https://mybookmark.com",
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            saas_app={
                "auth_type": "saml",
                "consumer_service_url": "https://example.com",
                "custom_attributes": {
                    "name": "family_name",
                    "name_format": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "source": {"name": "last_name"},
                },
                "default_relay_state": "https://example.com",
                "idp_entity_id": "https://example.cloudflareaccess.com",
                "name_id_format": "id",
                "name_id_transform_jsonata": "$substringBefore(email, '@') & '+sandbox@' & $substringAfter(email, '@')",
                "public_key": "example unique name",
                "sp_entity_id": "example unique name",
                "sso_endpoint": "https://example.cloudflareaccess.com/cdn-cgi/access/sso/saml/b3f58a2b414e0b51d45c8c2af26fccca0e27c63763c426fa52f98dcf0b3b3bfd",
            },
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
            type="bookmark",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.access.applications.with_raw_response.create(
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.access.applications.with_streaming_response.create(
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationCreateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.applications.with_raw_response.create(
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.applications.with_raw_response.create(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        application = client.access.applications.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ApplicationUpdateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        application = client.access.applications.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible={},
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": [{}, {}, {}],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="string",
            custom_deny_url="string",
            custom_non_identity_deny_url="string",
            custom_pages=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            domain="https://mybookmark.com",
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            saas_app={
                "auth_type": "saml",
                "consumer_service_url": "https://example.com",
                "custom_attributes": {
                    "name": "family_name",
                    "name_format": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "source": {"name": "last_name"},
                },
                "default_relay_state": "https://example.com",
                "idp_entity_id": "https://example.cloudflareaccess.com",
                "name_id_format": "id",
                "name_id_transform_jsonata": "$substringBefore(email, '@') & '+sandbox@' & $substringAfter(email, '@')",
                "public_key": "example unique name",
                "sp_entity_id": "example unique name",
                "sso_endpoint": "https://example.cloudflareaccess.com/cdn-cgi/access/sso/saml/b3f58a2b414e0b51d45c8c2af26fccca0e27c63763c426fa52f98dcf0b3b3bfd",
            },
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
            type="bookmark",
        )
        assert_matches_type(ApplicationUpdateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.applications.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationUpdateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.applications.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationUpdateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.applications.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.applications.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        application = client.access.applications.list(
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Optional[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.access.applications.with_raw_response.list(
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.access.applications.with_streaming_response.list(
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.applications.with_raw_response.list(
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.applications.with_raw_response.list(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        application = client.access.applications.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.access.applications.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.access.applications.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.applications.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.applications.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        application = client.access.applications.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ApplicationGetResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.access.applications.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationGetResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.access.applications.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationGetResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.applications.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.applications.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_revoke_tokens(self, client: Cloudflare) -> None:
        application = client.access.applications.revoke_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_revoke_tokens(self, client: Cloudflare) -> None:
        response = client.access.applications.with_raw_response.revoke_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_revoke_tokens(self, client: Cloudflare) -> None:
        with client.access.applications.with_streaming_response.revoke_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_revoke_tokens(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.applications.with_raw_response.revoke_tokens(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.applications.with_raw_response.revoke_tokens(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="string",
                zone_id="",
            )


class TestAsyncApplications:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.access.applications.create(
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.access.applications.create(
            account_id="string",
            zone_id="string",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible={},
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": [{}, {}, {}],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="string",
            custom_deny_url="string",
            custom_non_identity_deny_url="string",
            custom_pages=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            domain="https://mybookmark.com",
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            saas_app={
                "auth_type": "saml",
                "consumer_service_url": "https://example.com",
                "custom_attributes": {
                    "name": "family_name",
                    "name_format": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "source": {"name": "last_name"},
                },
                "default_relay_state": "https://example.com",
                "idp_entity_id": "https://example.cloudflareaccess.com",
                "name_id_format": "id",
                "name_id_transform_jsonata": "$substringBefore(email, '@') & '+sandbox@' & $substringAfter(email, '@')",
                "public_key": "example unique name",
                "sp_entity_id": "example unique name",
                "sso_endpoint": "https://example.cloudflareaccess.com/cdn-cgi/access/sso/saml/b3f58a2b414e0b51d45c8c2af26fccca0e27c63763c426fa52f98dcf0b3b3bfd",
            },
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
            type="bookmark",
        )
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.applications.with_raw_response.create(
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationCreateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.applications.with_streaming_response.create(
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationCreateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.applications.with_raw_response.create(
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.applications.with_raw_response.create(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.access.applications.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ApplicationUpdateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.access.applications.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible={},
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": [{}, {}, {}],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="string",
            custom_deny_url="string",
            custom_non_identity_deny_url="string",
            custom_pages=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            domain="https://mybookmark.com",
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            saas_app={
                "auth_type": "saml",
                "consumer_service_url": "https://example.com",
                "custom_attributes": {
                    "name": "family_name",
                    "name_format": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "source": {"name": "last_name"},
                },
                "default_relay_state": "https://example.com",
                "idp_entity_id": "https://example.cloudflareaccess.com",
                "name_id_format": "id",
                "name_id_transform_jsonata": "$substringBefore(email, '@') & '+sandbox@' & $substringAfter(email, '@')",
                "public_key": "example unique name",
                "sp_entity_id": "example unique name",
                "sso_endpoint": "https://example.cloudflareaccess.com/cdn-cgi/access/sso/saml/b3f58a2b414e0b51d45c8c2af26fccca0e27c63763c426fa52f98dcf0b3b3bfd",
            },
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
            type="bookmark",
        )
        assert_matches_type(ApplicationUpdateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.applications.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationUpdateResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.applications.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationUpdateResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.applications.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.applications.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.access.applications.list(
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Optional[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.applications.with_raw_response.list(
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.applications.with_streaming_response.list(
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.applications.with_raw_response.list(
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.applications.with_raw_response.list(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.access.applications.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.applications.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.applications.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationDeleteResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.applications.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.applications.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.access.applications.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ApplicationGetResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.applications.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationGetResponse, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.applications.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationGetResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.applications.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.applications.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_revoke_tokens(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.access.applications.revoke_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_revoke_tokens(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.applications.with_raw_response.revoke_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_revoke_tokens(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.applications.with_streaming_response.revoke_tokens(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_revoke_tokens(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.applications.with_raw_response.revoke_tokens(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.applications.with_raw_response.revoke_tokens(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="string",
                zone_id="",
            )
