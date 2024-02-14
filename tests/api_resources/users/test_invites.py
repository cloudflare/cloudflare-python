# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users import (
    InviteGetResponse,
    InviteUpdateResponse,
    InviteUserSInvitesListInvitationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        invite = client.users.invites.update(
            "4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        )
        assert_matches_type(InviteUpdateResponse, invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.users.invites.with_raw_response.update(
            "4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(InviteUpdateResponse, invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.users.invites.with_streaming_response.update(
            "4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(InviteUpdateResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            client.users.invites.with_raw_response.update(
                "",
                status="accepted",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        invite = client.users.invites.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        )
        assert_matches_type(InviteGetResponse, invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.users.invites.with_raw_response.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(InviteGetResponse, invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.users.invites.with_streaming_response.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(InviteGetResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            client.users.invites.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_s_invites_list_invitations(self, client: Cloudflare) -> None:
        invite = client.users.invites.user_s_invites_list_invitations()
        assert_matches_type(Optional[InviteUserSInvitesListInvitationsResponse], invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_s_invites_list_invitations(self, client: Cloudflare) -> None:
        response = client.users.invites.with_raw_response.user_s_invites_list_invitations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(Optional[InviteUserSInvitesListInvitationsResponse], invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_s_invites_list_invitations(self, client: Cloudflare) -> None:
        with client.users.invites.with_streaming_response.user_s_invites_list_invitations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(Optional[InviteUserSInvitesListInvitationsResponse], invite, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvites:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        invite = await async_client.users.invites.update(
            "4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        )
        assert_matches_type(InviteUpdateResponse, invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.invites.with_raw_response.update(
            "4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(InviteUpdateResponse, invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.invites.with_streaming_response.update(
            "4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(InviteUpdateResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            await async_client.users.invites.with_raw_response.update(
                "",
                status="accepted",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        invite = await async_client.users.invites.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        )
        assert_matches_type(InviteGetResponse, invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.invites.with_raw_response.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(InviteGetResponse, invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.invites.with_streaming_response.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(InviteGetResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            await async_client.users.invites.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_s_invites_list_invitations(self, async_client: AsyncCloudflare) -> None:
        invite = await async_client.users.invites.user_s_invites_list_invitations()
        assert_matches_type(Optional[InviteUserSInvitesListInvitationsResponse], invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_s_invites_list_invitations(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.invites.with_raw_response.user_s_invites_list_invitations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(Optional[InviteUserSInvitesListInvitationsResponse], invite, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_s_invites_list_invitations(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.invites.with_streaming_response.user_s_invites_list_invitations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(Optional[InviteUserSInvitesListInvitationsResponse], invite, path=["response"])

        assert cast(Any, response.is_closed) is True
