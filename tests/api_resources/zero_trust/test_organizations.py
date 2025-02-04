# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust import (
    Organization,
    OrganizationRevokeUsersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        organization = client.zero_trust.organizations.create(
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
            account_id="account_id",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        organization = client.zero_trust.organizations.create(
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            auto_redirect_to_identity=True,
            is_ui_read_only=True,
            login_design={
                "background_color": "#c5ed1b",
                "footer_text": "This is an example description.",
                "header_text": "This is an example description.",
                "logo_path": "https://example.com/logo.png",
                "text_color": "#c5ed1b",
            },
            session_duration="24h",
            ui_read_only_toggle_reason="Temporarily turn off the UI read only lock to make a change via the UI",
            user_seat_expiration_inactive_time="730h",
            warp_auth_session_duration="24h",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.organizations.with_raw_response.create(
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.organizations.with_streaming_response.create(
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Optional[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.organizations.with_raw_response.create(
                auth_domain="test.cloudflareaccess.com",
                name="Widget Corps Internal Applications",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.organizations.with_raw_response.create(
                auth_domain="test.cloudflareaccess.com",
                name="Widget Corps Internal Applications",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        organization = client.zero_trust.organizations.update(
            account_id="account_id",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        organization = client.zero_trust.organizations.update(
            account_id="account_id",
            allow_authenticate_via_warp=True,
            auth_domain="test.cloudflareaccess.com",
            auto_redirect_to_identity=True,
            custom_pages={
                "forbidden": "699d98642c564d2e855e9661899b7252",
                "identity_denied": "699d98642c564d2e855e9661899b7252",
            },
            is_ui_read_only=True,
            login_design={
                "background_color": "#c5ed1b",
                "footer_text": "This is an example description.",
                "header_text": "This is an example description.",
                "logo_path": "https://example.com/logo.png",
                "text_color": "#c5ed1b",
            },
            name="Widget Corps Internal Applications",
            session_duration="24h",
            ui_read_only_toggle_reason="Temporarily turn off the UI read only lock to make a change via the UI",
            user_seat_expiration_inactive_time="730h",
            warp_auth_session_duration="24h",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.organizations.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.organizations.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Optional[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.organizations.with_raw_response.update(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.organizations.with_raw_response.update(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        organization = client.zero_trust.organizations.list(
            account_id="account_id",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        organization = client.zero_trust.organizations.list(
            account_id="account_id",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.organizations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.organizations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Optional[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.organizations.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.organizations.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_revoke_users(self, client: Cloudflare) -> None:
        organization = client.zero_trust.organizations.revoke_users(
            email="test@example.com",
            account_id="account_id",
        )
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_revoke_users_with_all_params(self, client: Cloudflare) -> None:
        organization = client.zero_trust.organizations.revoke_users(
            email="test@example.com",
            account_id="account_id",
            query_devices=True,
            body_devices=True,
            user_uid="699d98642c564d2e855e9661899b7252",
            warp_session_reauth=True,
        )
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_revoke_users(self, client: Cloudflare) -> None:
        response = client.zero_trust.organizations.with_raw_response.revoke_users(
            email="test@example.com",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_revoke_users(self, client: Cloudflare) -> None:
        with client.zero_trust.organizations.with_streaming_response.revoke_users(
            email="test@example.com",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_revoke_users(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.organizations.with_raw_response.revoke_users(
                email="test@example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.organizations.with_raw_response.revoke_users(
                email="test@example.com",
                account_id="account_id",
            )


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.zero_trust.organizations.create(
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
            account_id="account_id",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.zero_trust.organizations.create(
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
            account_id="account_id",
            allow_authenticate_via_warp=True,
            auto_redirect_to_identity=True,
            is_ui_read_only=True,
            login_design={
                "background_color": "#c5ed1b",
                "footer_text": "This is an example description.",
                "header_text": "This is an example description.",
                "logo_path": "https://example.com/logo.png",
                "text_color": "#c5ed1b",
            },
            session_duration="24h",
            ui_read_only_toggle_reason="Temporarily turn off the UI read only lock to make a change via the UI",
            user_seat_expiration_inactive_time="730h",
            warp_auth_session_duration="24h",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.organizations.with_raw_response.create(
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.organizations.with_streaming_response.create(
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Optional[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.organizations.with_raw_response.create(
                auth_domain="test.cloudflareaccess.com",
                name="Widget Corps Internal Applications",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.organizations.with_raw_response.create(
                auth_domain="test.cloudflareaccess.com",
                name="Widget Corps Internal Applications",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.zero_trust.organizations.update(
            account_id="account_id",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.zero_trust.organizations.update(
            account_id="account_id",
            allow_authenticate_via_warp=True,
            auth_domain="test.cloudflareaccess.com",
            auto_redirect_to_identity=True,
            custom_pages={
                "forbidden": "699d98642c564d2e855e9661899b7252",
                "identity_denied": "699d98642c564d2e855e9661899b7252",
            },
            is_ui_read_only=True,
            login_design={
                "background_color": "#c5ed1b",
                "footer_text": "This is an example description.",
                "header_text": "This is an example description.",
                "logo_path": "https://example.com/logo.png",
                "text_color": "#c5ed1b",
            },
            name="Widget Corps Internal Applications",
            session_duration="24h",
            ui_read_only_toggle_reason="Temporarily turn off the UI read only lock to make a change via the UI",
            user_seat_expiration_inactive_time="730h",
            warp_auth_session_duration="24h",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.organizations.with_raw_response.update(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.organizations.with_streaming_response.update(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Optional[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.organizations.with_raw_response.update(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.organizations.with_raw_response.update(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.zero_trust.organizations.list(
            account_id="account_id",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.zero_trust.organizations.list(
            account_id="account_id",
        )
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.organizations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Optional[Organization], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.organizations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Optional[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.organizations.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.organizations.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_revoke_users(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.zero_trust.organizations.revoke_users(
            email="test@example.com",
            account_id="account_id",
        )
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_revoke_users_with_all_params(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.zero_trust.organizations.revoke_users(
            email="test@example.com",
            account_id="account_id",
            query_devices=True,
            body_devices=True,
            user_uid="699d98642c564d2e855e9661899b7252",
            warp_session_reauth=True,
        )
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_revoke_users(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.organizations.with_raw_response.revoke_users(
            email="test@example.com",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_revoke_users(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.organizations.with_streaming_response.revoke_users(
            email="test@example.com",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_revoke_users(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.organizations.with_raw_response.revoke_users(
                email="test@example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.organizations.with_raw_response.revoke_users(
                email="test@example.com",
                account_id="account_id",
            )
