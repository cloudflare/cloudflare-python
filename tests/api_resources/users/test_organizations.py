# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.users import (
    OrganizationDeleteResponse,
    OrganizationGetResponse,
    OrganizationUserSOrganizationsListOrganizationsResponse,
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
from cloudflare.types.users import organization_user_s_organizations_list_organizations_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        organization = client.users.organizations.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.users.organizations.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.users.organizations.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.users.organizations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        organization = client.users.organizations.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OrganizationGetResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.users.organizations.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationGetResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.users.organizations.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationGetResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.users.organizations.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_s_organizations_list_organizations(self, client: Cloudflare) -> None:
        organization = client.users.organizations.user_s_organizations_list_organizations()
        assert_matches_type(
            Optional[OrganizationUserSOrganizationsListOrganizationsResponse], organization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_s_organizations_list_organizations_with_all_params(self, client: Cloudflare) -> None:
        organization = client.users.organizations.user_s_organizations_list_organizations(
            direction="desc",
            match="any",
            name="Cloudflare, Inc.",
            order="status",
            page=1,
            per_page=5,
            status="member",
        )
        assert_matches_type(
            Optional[OrganizationUserSOrganizationsListOrganizationsResponse], organization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_s_organizations_list_organizations(self, client: Cloudflare) -> None:
        response = client.users.organizations.with_raw_response.user_s_organizations_list_organizations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(
            Optional[OrganizationUserSOrganizationsListOrganizationsResponse], organization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_s_organizations_list_organizations(self, client: Cloudflare) -> None:
        with client.users.organizations.with_streaming_response.user_s_organizations_list_organizations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(
                Optional[OrganizationUserSOrganizationsListOrganizationsResponse], organization, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.users.organizations.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.organizations.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.organizations.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationDeleteResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.users.organizations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.users.organizations.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OrganizationGetResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.organizations.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationGetResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.organizations.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationGetResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.users.organizations.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_s_organizations_list_organizations(self, async_client: AsyncCloudflare) -> None:
        organization = await async_client.users.organizations.user_s_organizations_list_organizations()
        assert_matches_type(
            Optional[OrganizationUserSOrganizationsListOrganizationsResponse], organization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_s_organizations_list_organizations_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        organization = await async_client.users.organizations.user_s_organizations_list_organizations(
            direction="desc",
            match="any",
            name="Cloudflare, Inc.",
            order="status",
            page=1,
            per_page=5,
            status="member",
        )
        assert_matches_type(
            Optional[OrganizationUserSOrganizationsListOrganizationsResponse], organization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_s_organizations_list_organizations(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.organizations.with_raw_response.user_s_organizations_list_organizations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(
            Optional[OrganizationUserSOrganizationsListOrganizationsResponse], organization, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_s_organizations_list_organizations(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.organizations.with_streaming_response.user_s_organizations_list_organizations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(
                Optional[OrganizationUserSOrganizationsListOrganizationsResponse], organization, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
