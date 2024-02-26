# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import (
    OrganizationListResponse,
    OrganizationCreateResponse,
    OrganizationUpdateResponse,
    OrganizationRevokeUsersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        organization = client.access.organizations.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        organization = client.access.organizations.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
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
            user_seat_expiration_inactive_time="720h",
            warp_auth_session_duration="24h",
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.access.organizations.with_raw_response.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.access.organizations.with_streaming_response.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.organizations.with_raw_response.create(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                auth_domain="test.cloudflareaccess.com",
                name="Widget Corps Internal Applications",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.organizations.with_raw_response.create(
                account_id="string",
                zone_id="",
                auth_domain="test.cloudflareaccess.com",
                name="Widget Corps Internal Applications",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        organization = client.access.organizations.update(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        organization = client.access.organizations.update(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
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
            user_seat_expiration_inactive_time="720h",
            warp_auth_session_duration="24h",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.organizations.with_raw_response.update(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.organizations.with_streaming_response.update(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.organizations.with_raw_response.update(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.organizations.with_raw_response.update(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        organization = client.access.organizations.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.access.organizations.with_raw_response.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.access.organizations.with_streaming_response.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationListResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.organizations.with_raw_response.list(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.organizations.with_raw_response.list(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_revoke_users(self, client: Cloudflare) -> None:
        organization = client.access.organizations.revoke_users(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="test@example.com",
        )
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_revoke_users(self, client: Cloudflare) -> None:
        response = client.access.organizations.with_raw_response.revoke_users(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="test@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_revoke_users(self, client: Cloudflare) -> None:
        with client.access.organizations.with_streaming_response.revoke_users(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="test@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_revoke_users(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.access.organizations.with_raw_response.revoke_users(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                email="test@example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.access.organizations.with_raw_response.revoke_users(
                account_id="string",
                zone_id="",
                email="test@example.com",
            )


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.access.organizations.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.access.organizations.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
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
            user_seat_expiration_inactive_time="720h",
            warp_auth_session_duration="24h",
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.organizations.with_raw_response.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.organizations.with_streaming_response.create(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            auth_domain="test.cloudflareaccess.com",
            name="Widget Corps Internal Applications",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.organizations.with_raw_response.create(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                auth_domain="test.cloudflareaccess.com",
                name="Widget Corps Internal Applications",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.organizations.with_raw_response.create(
                account_id="string",
                zone_id="",
                auth_domain="test.cloudflareaccess.com",
                name="Widget Corps Internal Applications",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.access.organizations.update(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.access.organizations.update(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
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
            user_seat_expiration_inactive_time="720h",
            warp_auth_session_duration="24h",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.organizations.with_raw_response.update(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.organizations.with_streaming_response.update(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.organizations.with_raw_response.update(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.organizations.with_raw_response.update(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.access.organizations.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.organizations.with_raw_response.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.organizations.with_streaming_response.list(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationListResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.organizations.with_raw_response.list(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.organizations.with_raw_response.list(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_revoke_users(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.access.organizations.revoke_users(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="test@example.com",
        )
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_revoke_users(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.organizations.with_raw_response.revoke_users(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="test@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_revoke_users(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.organizations.with_streaming_response.revoke_users(
            account_id="string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="test@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(Optional[OrganizationRevokeUsersResponse], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_revoke_users(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.access.organizations.with_raw_response.revoke_users(
                account_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                email="test@example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.access.organizations.with_raw_response.revoke_users(
                account_id="string",
                zone_id="",
                email="test@example.com",
            )
