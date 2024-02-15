# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.access import (
    AppCreateResponse,
    AppUpdateResponse,
    AppListResponse,
    AppDeleteResponse,
    AppGetResponse,
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
from cloudflare.types.access import app_create_params
from cloudflare.types.access import app_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="self_hosted",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="self_hosted",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="self_hosted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="self_hosted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                domain="test.example.com/admin",
                type="self_hosted",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                domain="test.example.com/admin",
                type="self_hosted",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            custom_pages=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
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
            tags=["engineers", "engineers", "engineers"],
            type="saas",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_3(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="ssh",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="ssh",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_3(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="ssh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="ssh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                domain="test.example.com/admin",
                type="ssh",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                domain="test.example.com/admin",
                type="ssh",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_4(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="vnc",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="vnc",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_4(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="vnc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="vnc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                domain="test.example.com/admin",
                type="vnc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                domain="test.example.com/admin",
                type="vnc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_5(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="app_launcher",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="app_launcher",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_5(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="app_launcher",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="app_launcher",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                type="app_launcher",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                type="app_launcher",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_6(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="warp",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="warp",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_6(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="warp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="warp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                type="warp",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                type="warp",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_7(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="biso",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="biso",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_7(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="biso",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="biso",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                type="biso",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                type="biso",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_8(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Cloudflare) -> None:
        app = client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            app_launcher_visible={},
            domain="https://mybookmark.com",
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            tags=["engineers", "engineers", "engineers"],
            type="bookmark",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_8(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="self_hosted",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                domain="test.example.com/admin",
                type="self_hosted",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            custom_pages=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
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
            tags=["engineers", "engineers", "engineers"],
            type="saas",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="ssh",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                domain="test.example.com/admin",
                type="ssh",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_4(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_4(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="vnc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                domain="test.example.com/admin",
                type="vnc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_5(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="app_launcher",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="app_launcher",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_5(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="app_launcher",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_5(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="app_launcher",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="app_launcher",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                type="app_launcher",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_6(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="warp",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="warp",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_6(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="warp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_6(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="warp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="warp",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                type="warp",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_7(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="biso",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="biso",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_7(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="biso",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_7(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="biso",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="biso",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                type="biso",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_8(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: Cloudflare) -> None:
        app = client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_launcher_visible={},
            domain="https://mybookmark.com",
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            tags=["engineers", "engineers", "engineers"],
            type="bookmark",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_8(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_8(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        app = client.access.apps.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(Optional[AppListResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppListResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppListResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.list(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        app = client.access.apps.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppDeleteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        app = client.access.apps.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppGetResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.access.apps.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppGetResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.access.apps.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppGetResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="self_hosted",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="self_hosted",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="self_hosted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="self_hosted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                domain="test.example.com/admin",
                type="self_hosted",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                domain="test.example.com/admin",
                type="self_hosted",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            custom_pages=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
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
            tags=["engineers", "engineers", "engineers"],
            type="saas",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="ssh",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="ssh",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="ssh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="ssh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                domain="test.example.com/admin",
                type="ssh",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                domain="test.example.com/admin",
                type="ssh",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="vnc",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="vnc",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="vnc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            domain="test.example.com/admin",
            type="vnc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                domain="test.example.com/admin",
                type="vnc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                domain="test.example.com/admin",
                type="vnc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="app_launcher",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="app_launcher",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="app_launcher",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="app_launcher",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                type="app_launcher",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                type="app_launcher",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="warp",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="warp",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="warp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="warp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                type="warp",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                type="warp",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="biso",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="biso",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="biso",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            type="biso",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                type="biso",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
                type="biso",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            app_launcher_visible={},
            domain="https://mybookmark.com",
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            tags=["engineers", "engineers", "engineers"],
            type="bookmark",
        )
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppCreateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppCreateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.create(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="self_hosted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="self_hosted",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                domain="test.example.com/admin",
                type="self_hosted",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
            auto_redirect_to_identity=True,
            custom_pages=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
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
            tags=["engineers", "engineers", "engineers"],
            type="saas",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="ssh",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="ssh",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                domain="test.example.com/admin",
                type="ssh",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
            allow_authenticate_via_warp=True,
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            app_launcher_visible=True,
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
            enable_binding_cookie=True,
            http_only_cookie_attribute=True,
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            path_cookie_attribute=True,
            same_site_cookie_attribute="strict",
            self_hosted_domains=["test.example.com/admin", "test.anotherexample.com/staff"],
            service_auth_401_redirect=True,
            session_duration="24h",
            skip_interstitial=True,
            tags=["engineers", "engineers", "engineers"],
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain="test.example.com/admin",
            type="vnc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                domain="test.example.com/admin",
                type="vnc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                domain="test.example.com/admin",
                type="vnc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="app_launcher",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="app_launcher",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="app_launcher",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="app_launcher",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="app_launcher",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                type="app_launcher",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="warp",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="warp",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="warp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="warp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="warp",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                type="warp",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="biso",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="biso",
            allowed_idps=[
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
                "699d98642c564d2e855e9661899b7252",
            ],
            auto_redirect_to_identity=True,
            session_duration="24h",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="biso",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="biso",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="biso",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
                type="biso",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_launcher_visible={},
            domain="https://mybookmark.com",
            logo_url="https://www.cloudflare.com/img/logo-web-badges/cf-logo-on-white-bg.svg",
            name="Admin Site",
            tags=["engineers", "engineers", "engineers"],
            type="bookmark",
        )
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppUpdateResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppUpdateResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(Optional[AppListResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppListResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppListResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.list(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppDeleteResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppDeleteResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.access.apps.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppGetResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppGetResponse, app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppGetResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
            )
