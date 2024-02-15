# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types import RoleAccountRolesListRolesResponse, RoleGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_roles_list_roles(self, client: Cloudflare) -> None:
        role = client.roles.account_roles_list_roles(
            {},
        )
        assert_matches_type(Optional[RoleAccountRolesListRolesResponse], role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_roles_list_roles(self, client: Cloudflare) -> None:
        response = client.roles.with_raw_response.account_roles_list_roles(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(Optional[RoleAccountRolesListRolesResponse], role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_roles_list_roles(self, client: Cloudflare) -> None:
        with client.roles.with_streaming_response.account_roles_list_roles(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(Optional[RoleAccountRolesListRolesResponse], role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        role = client.roles.get(
            {},
            account_id={},
        )
        assert_matches_type(RoleGetResponse, role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.roles.with_raw_response.get(
            {},
            account_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = response.parse()
        assert_matches_type(RoleGetResponse, role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.roles.with_streaming_response.get(
            {},
            account_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = response.parse()
            assert_matches_type(RoleGetResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_roles_list_roles(self, async_client: AsyncCloudflare) -> None:
        role = await async_client.roles.account_roles_list_roles(
            {},
        )
        assert_matches_type(Optional[RoleAccountRolesListRolesResponse], role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_roles_list_roles(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.roles.with_raw_response.account_roles_list_roles(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(Optional[RoleAccountRolesListRolesResponse], role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_roles_list_roles(self, async_client: AsyncCloudflare) -> None:
        async with async_client.roles.with_streaming_response.account_roles_list_roles(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(Optional[RoleAccountRolesListRolesResponse], role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        role = await async_client.roles.get(
            {},
            account_id={},
        )
        assert_matches_type(RoleGetResponse, role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.roles.with_raw_response.get(
            {},
            account_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        role = await response.parse()
        assert_matches_type(RoleGetResponse, role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.roles.with_streaming_response.get(
            {},
            account_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            role = await response.parse()
            assert_matches_type(RoleGetResponse, role, path=["response"])

        assert cast(Any, response.is_closed) is True
