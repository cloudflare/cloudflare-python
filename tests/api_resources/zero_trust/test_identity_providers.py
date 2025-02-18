# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust import (
    IdentityProvider,
    IdentityProviderListResponse,
    IdentityProviderDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdentityProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "conditional_access_enabled": True,
                "directory_id": "<your azure directory uuid>",
                "email_claim_name": "custom_claim_name",
                "prompt": "login",
                "support_groups": True,
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "centrify_account": "https://abc123.my.centrify.com/",
                "centrify_app_id": "exampleapp",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_3(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_4(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_5(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_6(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "apps_domain": "mycompany.com",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_6(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_7(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_7(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_8(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "auth_url": "https://accounts.google.com/o/oauth2/auth",
                "certs_url": "https://www.googleapis.com/oauth2/v3/certs",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "pkce_enabled": True,
                "scopes": ["openid", "email", "profile"],
                "token_url": "https://accounts.google.com/o/oauth2/token",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_8(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_9(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "authorization_server_id": "aus9o8wzkhckw9TLa0h7z",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "okta_account": "https://dev-abc123.oktapreview.com",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_9(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_9(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_10(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "onelogin_account": "https://mycompany.onelogin.com",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_10(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_10(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_11(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_11(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "ping_env_id": "342b5660-0c32-4936-a5a4-ce21fae57b0a",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_11(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_11(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_12(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_12(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "attributes": ["group", "department_code", "divison"],
                "email_attribute_name": "Email",
                "header_attributes": [
                    {
                        "attribute_name": "attribute_name",
                        "header_name": "header_name",
                    }
                ],
                "idp_public_certs": ["string"],
                "issuer_url": "https://whoami.com",
                "sign_request": True,
                "sso_target_url": "https://edgeaccess.org/idp/saml/login",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_12(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_12(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_13(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_13(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_13(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_13(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_14(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_14(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_14(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_14(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "conditional_access_enabled": True,
                "directory_id": "<your azure directory uuid>",
                "email_claim_name": "custom_claim_name",
                "prompt": "login",
                "support_groups": True,
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "centrify_account": "https://abc123.my.centrify.com/",
                "centrify_app_id": "exampleapp",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_4(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_4(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_5(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_5(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_5(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_6(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "apps_domain": "mycompany.com",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_6(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_6(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_7(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_7(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_7(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_8(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "auth_url": "https://accounts.google.com/o/oauth2/auth",
                "certs_url": "https://www.googleapis.com/oauth2/v3/certs",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "pkce_enabled": True,
                "scopes": ["openid", "email", "profile"],
                "token_url": "https://accounts.google.com/o/oauth2/token",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_8(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_8(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_9(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_9(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "authorization_server_id": "aus9o8wzkhckw9TLa0h7z",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "okta_account": "https://dev-abc123.oktapreview.com",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_9(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_9(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_10(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_10(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "onelogin_account": "https://mycompany.onelogin.com",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_10(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_10(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_11(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_11(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "ping_env_id": "342b5660-0c32-4936-a5a4-ce21fae57b0a",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_11(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_11(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_12(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_12(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "attributes": ["group", "department_code", "divison"],
                "email_attribute_name": "Email",
                "header_attributes": [
                    {
                        "attribute_name": "attribute_name",
                        "header_name": "header_name",
                    }
                ],
                "idp_public_certs": ["string"],
                "issuer_url": "https://whoami.com",
                "sign_request": True,
                "sso_target_url": "https://edgeaccess.org/idp/saml/login",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_12(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_12(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_13(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_13(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_13(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_13(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_14(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_14(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_14(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_14(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.list(
            account_id="account_id",
            scim_enabled="scim_enabled",
        )
        assert_matches_type(SyncSinglePage[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(SyncSinglePage[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(SyncSinglePage[IdentityProviderListResponse], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.delete(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProviderDeleteResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.delete(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProviderDeleteResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.delete(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProviderDeleteResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.delete(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProviderDeleteResponse], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.delete(
                identity_provider_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.delete(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.delete(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.get(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        identity_provider = client.zero_trust.identity_providers.get(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.identity_providers.with_raw_response.get(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.identity_providers.with_streaming_response.get(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            client.zero_trust.identity_providers.with_raw_response.get(
                identity_provider_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.get(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.identity_providers.with_raw_response.get(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )


class TestAsyncIdentityProviders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "conditional_access_enabled": True,
                "directory_id": "<your azure directory uuid>",
                "email_claim_name": "custom_claim_name",
                "prompt": "login",
                "support_groups": True,
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "centrify_account": "https://abc123.my.centrify.com/",
                "centrify_app_id": "exampleapp",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "apps_domain": "mycompany.com",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "auth_url": "https://accounts.google.com/o/oauth2/auth",
                "certs_url": "https://www.googleapis.com/oauth2/v3/certs",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "pkce_enabled": True,
                "scopes": ["openid", "email", "profile"],
                "token_url": "https://accounts.google.com/o/oauth2/token",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "authorization_server_id": "aus9o8wzkhckw9TLa0h7z",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "okta_account": "https://dev-abc123.oktapreview.com",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "onelogin_account": "https://mycompany.onelogin.com",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "ping_env_id": "342b5660-0c32-4936-a5a4-ce21fae57b0a",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "attributes": ["group", "department_code", "divison"],
                "email_attribute_name": "Email",
                "header_attributes": [
                    {
                        "attribute_name": "attribute_name",
                        "header_name": "header_name",
                    }
                ],
                "idp_public_certs": ["string"],
                "issuer_url": "https://whoami.com",
                "sign_request": True,
                "sso_target_url": "https://edgeaccess.org/idp/saml/login",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.create(
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.create(
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "conditional_access_enabled": True,
                "directory_id": "<your azure directory uuid>",
                "email_claim_name": "custom_claim_name",
                "prompt": "login",
                "support_groups": True,
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "centrify_account": "https://abc123.my.centrify.com/",
                "centrify_app_id": "exampleapp",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "apps_domain": "mycompany.com",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "auth_url": "https://accounts.google.com/o/oauth2/auth",
                "certs_url": "https://www.googleapis.com/oauth2/v3/certs",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "pkce_enabled": True,
                "scopes": ["openid", "email", "profile"],
                "token_url": "https://accounts.google.com/o/oauth2/token",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "authorization_server_id": "aus9o8wzkhckw9TLa0h7z",
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "okta_account": "https://dev-abc123.oktapreview.com",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "onelogin_account": "https://mycompany.onelogin.com",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "claims": ["email_verified", "preferred_username", "custom_claim_name"],
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
                "email_claim_name": "custom_claim_name",
                "ping_env_id": "342b5660-0c32-4936-a5a4-ce21fae57b0a",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "attributes": ["group", "department_code", "divison"],
                "email_attribute_name": "Email",
                "header_attributes": [
                    {
                        "attribute_name": "attribute_name",
                        "header_name": "header_name",
                    }
                ],
                "idp_public_certs": ["string"],
                "issuer_url": "https://whoami.com",
                "sign_request": True,
                "sso_target_url": "https://edgeaccess.org/idp/saml/login",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={
                "client_id": "<your client id>",
                "client_secret": "<your client secret>",
            },
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
            scim_config={
                "enabled": True,
                "identity_update_behavior": "automatic",
                "seat_deprovision": True,
                "user_deprovision": True,
            },
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.update(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            config={},
            name="Widget Corps IDP",
            type="onetimepin",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.update(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                config={},
                name="Widget Corps IDP",
                type="onetimepin",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.list(
            account_id="account_id",
            scim_enabled="scim_enabled",
        )
        assert_matches_type(AsyncSinglePage[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(AsyncSinglePage[IdentityProviderListResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(AsyncSinglePage[IdentityProviderListResponse], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.delete(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProviderDeleteResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.delete(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProviderDeleteResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.delete(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProviderDeleteResponse], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.delete(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProviderDeleteResponse], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.delete(
                identity_provider_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.delete(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.delete(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.get(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        identity_provider = await async_client.zero_trust.identity_providers.get(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.identity_providers.with_raw_response.get(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity_provider = await response.parse()
        assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.identity_providers.with_streaming_response.get(
            identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity_provider = await response.parse()
            assert_matches_type(Optional[IdentityProvider], identity_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identity_provider_id` but received ''"):
            await async_client.zero_trust.identity_providers.with_raw_response.get(
                identity_provider_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.get(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.identity_providers.with_raw_response.get(
                identity_provider_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )
