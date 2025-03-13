# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access import (
    ApplicationGetResponse,
    ApplicationListResponse,
    ApplicationCreateResponse,
    ApplicationDeleteResponse,
    ApplicationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            saas_app={
                "auth_type": "saml",
                "consumer_service_url": "https://example.com",
                "custom_attributes": [
                    {
                        "friendly_name": "Last Name",
                        "name": "family_name",
                        "name_format": "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
                        "required": True,
                        "source": {
                            "name": "last_name",
                            "name_by_idp": [
                                {
                                    "idp_id": "exampleIdPID1",
                                    "source_name": "AttributeName1",
                                }
                            ],
                        },
                    }
                ],
                "default_relay_state": "https://example.com",
                "idp_entity_id": "https://example.cloudflareaccess.com",
                "name_id_format": "id",
                "name_id_transform_jsonata": "$substringBefore(email, '@') & '+sandbox@' & $substringAfter(email, '@')",
                "public_key": "example unique name",
                "saml_attribute_transform_jsonata": "$ ~>| groups | {'group_name': name} |",
                "sp_entity_id": "example unique name",
                "sso_endpoint": "https://example.cloudflareaccess.com/cdn-cgi/access/sso/saml/b3f58a2b414e0b51d45c8c2af26fccca0e27c63763c426fa52f98dcf0b3b3bfd",
            },
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            tags=["engineers"],
            type="saas",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_3(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="ssh",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="ssh",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_4(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="vnc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="vnc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_5(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_6(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_6(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_7(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_7(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_8(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            account_id="account_id",
            app_launcher_visible=True,
            domain="https://mybookmark.com",
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            tags=["engineers"],
            type="bookmark",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_8(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_9(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
            name="Admin Site",
            policies=[
                {
                    "decision": "allow",
                    "include": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "name": "Allow devs",
                    "connection_rules": {
                        "ssh": {
                            "usernames": ["root", "ubuntu"],
                            "allow_email_alias": True,
                        }
                    },
                    "exclude": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "require": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                }
            ],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_9(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_9(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_10(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_10(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.create(
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_10(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.create(
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            saas_app={
                "auth_type": "saml",
                "consumer_service_url": "https://example.com",
                "custom_attributes": [
                    {
                        "friendly_name": "Last Name",
                        "name": "family_name",
                        "name_format": "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
                        "required": True,
                        "source": {
                            "name": "last_name",
                            "name_by_idp": [
                                {
                                    "idp_id": "exampleIdPID1",
                                    "source_name": "AttributeName1",
                                }
                            ],
                        },
                    }
                ],
                "default_relay_state": "https://example.com",
                "idp_entity_id": "https://example.cloudflareaccess.com",
                "name_id_format": "id",
                "name_id_transform_jsonata": "$substringBefore(email, '@') & '+sandbox@' & $substringAfter(email, '@')",
                "public_key": "example unique name",
                "saml_attribute_transform_jsonata": "$ ~>| groups | {'group_name': name} |",
                "sp_entity_id": "example unique name",
                "sso_endpoint": "https://example.cloudflareaccess.com/cdn-cgi/access/sso/saml/b3f58a2b414e0b51d45c8c2af26fccca0e27c63763c426fa52f98dcf0b3b3bfd",
            },
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            tags=["engineers"],
            type="saas",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                domain="test.example.com/admin",
                type="ssh",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="ssh",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="ssh",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_4(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_4(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                domain="test.example.com/admin",
                type="vnc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="vnc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="vnc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_5(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_5(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_5(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_6(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_6(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_6(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_7(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_7(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_7(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_8(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
            app_launcher_visible=True,
            domain="https://mybookmark.com",
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            tags=["engineers"],
            type="bookmark",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_8(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_8(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_9(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_9(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
            name="Admin Site",
            policies=[
                {
                    "decision": "allow",
                    "include": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "name": "Allow devs",
                    "connection_rules": {
                        "ssh": {
                            "usernames": ["root", "ubuntu"],
                            "allow_email_alias": True,
                        }
                    },
                    "exclude": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "require": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                }
            ],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_9(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_9(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_10(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_10(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_10(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_10(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.list(
            account_id="account_id",
            aud="aud",
            domain="domain",
            name="name",
            search="search",
        )
        assert_matches_type(SyncSinglePage[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(SyncSinglePage[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(SyncSinglePage[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationDeleteResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationDeleteResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationDeleteResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationDeleteResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.delete(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.delete(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.delete(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.get(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.get(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.get(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_revoke_tokens(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.revoke_tokens(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_revoke_tokens_with_all_params(self, client: Cloudflare) -> None:
        application = client.zero_trust.access.applications.revoke_tokens(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_revoke_tokens(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.with_raw_response.revoke_tokens(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_revoke_tokens(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.with_streaming_response.revoke_tokens(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_revoke_tokens(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.zero_trust.access.applications.with_raw_response.revoke_tokens(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.revoke_tokens(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.applications.with_raw_response.revoke_tokens(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )


class TestAsyncApplications:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            saas_app={
                "auth_type": "saml",
                "consumer_service_url": "https://example.com",
                "custom_attributes": [
                    {
                        "friendly_name": "Last Name",
                        "name": "family_name",
                        "name_format": "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
                        "required": True,
                        "source": {
                            "name": "last_name",
                            "name_by_idp": [
                                {
                                    "idp_id": "exampleIdPID1",
                                    "source_name": "AttributeName1",
                                }
                            ],
                        },
                    }
                ],
                "default_relay_state": "https://example.com",
                "idp_entity_id": "https://example.cloudflareaccess.com",
                "name_id_format": "id",
                "name_id_transform_jsonata": "$substringBefore(email, '@') & '+sandbox@' & $substringAfter(email, '@')",
                "public_key": "example unique name",
                "saml_attribute_transform_jsonata": "$ ~>| groups | {'group_name': name} |",
                "sp_entity_id": "example unique name",
                "sso_endpoint": "https://example.cloudflareaccess.com/cdn-cgi/access/sso/saml/b3f58a2b414e0b51d45c8c2af26fccca0e27c63763c426fa52f98dcf0b3b3bfd",
            },
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            tags=["engineers"],
            type="saas",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="ssh",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="ssh",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="vnc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                type="vnc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            account_id="account_id",
            app_launcher_visible=True,
            domain="https://mybookmark.com",
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            tags=["engineers"],
            type="bookmark",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
            name="Admin Site",
            policies=[
                {
                    "decision": "allow",
                    "include": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "name": "Allow devs",
                    "connection_rules": {
                        "ssh": {
                            "usernames": ["root", "ubuntu"],
                            "allow_email_alias": True,
                        }
                    },
                    "exclude": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "require": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                }
            ],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.create(
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.create(
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.create(
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.create(
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            saas_app={
                "auth_type": "saml",
                "consumer_service_url": "https://example.com",
                "custom_attributes": [
                    {
                        "friendly_name": "Last Name",
                        "name": "family_name",
                        "name_format": "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
                        "required": True,
                        "source": {
                            "name": "last_name",
                            "name_by_idp": [
                                {
                                    "idp_id": "exampleIdPID1",
                                    "source_name": "AttributeName1",
                                }
                            ],
                        },
                    }
                ],
                "default_relay_state": "https://example.com",
                "idp_entity_id": "https://example.cloudflareaccess.com",
                "name_id_format": "id",
                "name_id_transform_jsonata": "$substringBefore(email, '@') & '+sandbox@' & $substringAfter(email, '@')",
                "public_key": "example unique name",
                "saml_attribute_transform_jsonata": "$ ~>| groups | {'group_name': name} |",
                "sp_entity_id": "example unique name",
                "sso_endpoint": "https://example.cloudflareaccess.com/cdn-cgi/access/sso/saml/b3f58a2b414e0b51d45c8c2af26fccca0e27c63763c426fa52f98dcf0b3b3bfd",
            },
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            tags=["engineers"],
            type="saas",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                domain="test.example.com/admin",
                type="ssh",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="ssh",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="ssh",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                domain="test.example.com/admin",
                type="vnc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="vnc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="vnc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            auto_redirect_to_identity=True,
            bg_color="#ff0000",
            footer_links=[
                {
                    "name": "Cloudflare's Privacy Policy",
                    "url": "https://www.cloudflare.com/privacypolicy/",
                }
            ],
            header_bg_color="#ff0000",
            landing_page_design={
                "button_color": "#ff0000",
                "button_text_color": "#ff0000",
                "image_url": "https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
                "message": "Log in below to reach your applications behind Access.",
                "title": "Welcome back!",
            },
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            session_duration="24h",
            skip_app_launcher_login_page=True,
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
            app_launcher_visible=True,
            domain="https://mybookmark.com",
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            tags=["engineers"],
            type="bookmark",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
            name="Admin Site",
            policies=[
                {
                    "decision": "allow",
                    "include": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "name": "Allow devs",
                    "connection_rules": {
                        "ssh": {
                            "usernames": ["root", "ubuntu"],
                            "allow_email_alias": True,
                        }
                    },
                    "exclude": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "require": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                }
            ],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="self_hosted",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="self_hosted",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            allowed_idps=["699d98642c564d2e855e9661899b7252"],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            cors_headers={
                "allow_all_headers": True,
                "allow_all_methods": True,
                "allow_all_origins": True,
                "allow_credentials": True,
                "allowed_headers": ["string"],
                "allowed_methods": ["GET"],
                "allowed_origins": ["https://example.com"],
                "max_age": -1,
            },
            custom_deny_message="custom_deny_message",
            custom_deny_url="custom_deny_url",
            custom_non_identity_deny_url="custom_non_identity_deny_url",
            custom_pages=["699d98642c564d2e855e9661899b7252"],
            destinations=[
                {
                    "type": "public",
                    "uri": "test.example.com/admin",
                },
                {
                    "type": "public",
                    "uri": "test.anotherexample.com/staff",
                },
                {
                    "cidr": "10.5.0.0/24",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80-90",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "10.5.0.3/32",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "80",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
                {
                    "cidr": "cidr",
                    "hostname": "hostname",
                    "l4_protocol": "tcp",
                    "port_range": "port_range",
                    "type": "private",
                    "vnet_id": "vnet_id",
                },
            ],
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            options_preflight_bypass=True,
            path_cookie_attribute=True,
            policies=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "precedence": 0,
                }
            ],
            same_site_cookie_attribute="strict",
            scim_config={
                "idp_uid": "idp_uid",
                "remote_uri": "remote_uri",
                "authentication": {
                    "password": "password",
                    "scheme": "httpbasic",
                    "user": "user",
                },
                "deactivate_on_delete": True,
                "enabled": True,
                "mappings": [
                    {
                        "schema": "urn:ietf:params:scim:schemas:core:2.0:User",
                        "enabled": True,
                        "filter": 'title pr or userType eq "Intern"',
                        "operations": {
                            "create": True,
                            "delete": True,
                            "update": True,
                        },
                        "strictness": "strict",
                        "transform_jsonata": "$merge([$, {'userName': $substringBefore($.userName, '@') & '+test@' & $substringAfter($.userName, '@')}])",
                    }
                ],
            },
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            target_criteria=[
                {
                    "port": 22,
                    "protocol": "ssh",
                    "target_attributes": {"hostname": ["test-server", "production-server"]},
                }
            ],
            type="rdp",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="",
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                target_criteria=[
                    {
                        "port": 22,
                        "protocol": "ssh",
                        "target_attributes": {"hostname": ["test-server", "production-server"]},
                    }
                ],
                type="rdp",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.list(
            account_id="account_id",
            aud="aud",
            domain="domain",
            name="name",
            search="search",
        )
        assert_matches_type(AsyncSinglePage[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(AsyncSinglePage[ApplicationListResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(AsyncSinglePage[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationDeleteResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationDeleteResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationDeleteResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationDeleteResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.delete(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.delete(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.delete(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.get(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.get(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.get(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_revoke_tokens(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.revoke_tokens(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_revoke_tokens_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.access.applications.revoke_tokens(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_revoke_tokens(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.with_raw_response.revoke_tokens(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(object, application, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_revoke_tokens(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.with_streaming_response.revoke_tokens(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_revoke_tokens(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.zero_trust.access.applications.with_raw_response.revoke_tokens(
                app_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.revoke_tokens(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.applications.with_raw_response.revoke_tokens(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="account_id",
            )
