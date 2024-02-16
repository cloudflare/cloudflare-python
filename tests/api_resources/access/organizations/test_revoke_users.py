# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.access.organizations import RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access.organizations import (
    revoke_user_zero_trust_organization_revoke_all_access_tokens_for_a_user_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevokeUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_organization_revoke_all_access_tokens_for_a_user(self, client: Cloudflare) -> None:
        revoke_user = (
            client.access.organizations.revoke_users.zero_trust_organization_revoke_all_access_tokens_for_a_user(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                email="test@example.com",
            )
        )
        assert_matches_type(
            Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse],
            revoke_user,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_organization_revoke_all_access_tokens_for_a_user(self, client: Cloudflare) -> None:
        response = client.access.organizations.revoke_users.with_raw_response.zero_trust_organization_revoke_all_access_tokens_for_a_user(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            email="test@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revoke_user = response.parse()
        assert_matches_type(
            Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse],
            revoke_user,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_organization_revoke_all_access_tokens_for_a_user(
        self, client: Cloudflare
    ) -> None:
        with client.access.organizations.revoke_users.with_streaming_response.zero_trust_organization_revoke_all_access_tokens_for_a_user(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            email="test@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revoke_user = response.parse()
            assert_matches_type(
                Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse],
                revoke_user,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zero_trust_organization_revoke_all_access_tokens_for_a_user(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.organizations.revoke_users.with_raw_response.zero_trust_organization_revoke_all_access_tokens_for_a_user(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                email="test@example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.organizations.revoke_users.with_raw_response.zero_trust_organization_revoke_all_access_tokens_for_a_user(
                "",
                account_or_zone="string",
                email="test@example.com",
            )


class TestAsyncRevokeUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_organization_revoke_all_access_tokens_for_a_user(
        self, async_client: AsyncCloudflare
    ) -> None:
        revoke_user = await async_client.access.organizations.revoke_users.zero_trust_organization_revoke_all_access_tokens_for_a_user(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            email="test@example.com",
        )
        assert_matches_type(
            Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse],
            revoke_user,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_organization_revoke_all_access_tokens_for_a_user(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.access.organizations.revoke_users.with_raw_response.zero_trust_organization_revoke_all_access_tokens_for_a_user(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            email="test@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revoke_user = await response.parse()
        assert_matches_type(
            Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse],
            revoke_user,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_organization_revoke_all_access_tokens_for_a_user(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.organizations.revoke_users.with_streaming_response.zero_trust_organization_revoke_all_access_tokens_for_a_user(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            email="test@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revoke_user = await response.parse()
            assert_matches_type(
                Optional[RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserResponse],
                revoke_user,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zero_trust_organization_revoke_all_access_tokens_for_a_user(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.organizations.revoke_users.with_raw_response.zero_trust_organization_revoke_all_access_tokens_for_a_user(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                email="test@example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.organizations.revoke_users.with_raw_response.zero_trust_organization_revoke_all_access_tokens_for_a_user(
                "",
                account_or_zone="string",
                email="test@example.com",
            )
