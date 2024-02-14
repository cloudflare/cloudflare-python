# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.users.tokens import PermissionGroupPermissionGroupsListPermissionGroupsResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPermissionGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_permission_groups_list_permission_groups(self, client: Cloudflare) -> None:
        permission_group = client.users.tokens.permission_groups.permission_groups_list_permission_groups()
        assert_matches_type(
            Optional[PermissionGroupPermissionGroupsListPermissionGroupsResponse], permission_group, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_permission_groups_list_permission_groups(self, client: Cloudflare) -> None:
        response = client.users.tokens.permission_groups.with_raw_response.permission_groups_list_permission_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission_group = response.parse()
        assert_matches_type(
            Optional[PermissionGroupPermissionGroupsListPermissionGroupsResponse], permission_group, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_permission_groups_list_permission_groups(self, client: Cloudflare) -> None:
        with client.users.tokens.permission_groups.with_streaming_response.permission_groups_list_permission_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission_group = response.parse()
            assert_matches_type(
                Optional[PermissionGroupPermissionGroupsListPermissionGroupsResponse],
                permission_group,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncPermissionGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_permission_groups_list_permission_groups(self, async_client: AsyncCloudflare) -> None:
        permission_group = await async_client.users.tokens.permission_groups.permission_groups_list_permission_groups()
        assert_matches_type(
            Optional[PermissionGroupPermissionGroupsListPermissionGroupsResponse], permission_group, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_permission_groups_list_permission_groups(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.tokens.permission_groups.with_raw_response.permission_groups_list_permission_groups()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission_group = await response.parse()
        assert_matches_type(
            Optional[PermissionGroupPermissionGroupsListPermissionGroupsResponse], permission_group, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_permission_groups_list_permission_groups(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.tokens.permission_groups.with_streaming_response.permission_groups_list_permission_groups() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission_group = await response.parse()
            assert_matches_type(
                Optional[PermissionGroupPermissionGroupsListPermissionGroupsResponse],
                permission_group,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
