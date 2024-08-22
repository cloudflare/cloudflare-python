# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.iam import PermissionGroupGetResponse
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPermissionGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        permission_group = client.iam.permission_groups.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(SyncV4PagePaginationArray[object], permission_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        permission_group = client.iam.permission_groups.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            label="labelOfThePermissionGroup",
            name="NameOfThePermissionGroup",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[object], permission_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.iam.permission_groups.with_raw_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission_group = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[object], permission_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.iam.permission_groups.with_streaming_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission_group = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[object], permission_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.permission_groups.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        permission_group = client.iam.permission_groups.get(
            permission_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(PermissionGroupGetResponse, permission_group, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.iam.permission_groups.with_raw_response.get(
            permission_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission_group = response.parse()
        assert_matches_type(PermissionGroupGetResponse, permission_group, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.iam.permission_groups.with_streaming_response.get(
            permission_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission_group = response.parse()
            assert_matches_type(PermissionGroupGetResponse, permission_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.permission_groups.with_raw_response.get(
                permission_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_group_id` but received ''"):
            client.iam.permission_groups.with_raw_response.get(
                permission_group_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )


class TestAsyncPermissionGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        permission_group = await async_client.iam.permission_groups.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], permission_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        permission_group = await async_client.iam.permission_groups.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            label="labelOfThePermissionGroup",
            name="NameOfThePermissionGroup",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], permission_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.permission_groups.with_raw_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission_group = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[object], permission_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.permission_groups.with_streaming_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission_group = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[object], permission_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.permission_groups.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        permission_group = await async_client.iam.permission_groups.get(
            permission_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(PermissionGroupGetResponse, permission_group, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.permission_groups.with_raw_response.get(
            permission_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission_group = await response.parse()
        assert_matches_type(PermissionGroupGetResponse, permission_group, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.permission_groups.with_streaming_response.get(
            permission_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission_group = await response.parse()
            assert_matches_type(PermissionGroupGetResponse, permission_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.permission_groups.with_raw_response.get(
                permission_group_id="6d7f2f5f5b1d4a0e9081fdc98d432fd1",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_group_id` but received ''"):
            await async_client.iam.permission_groups.with_raw_response.get(
                permission_group_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )
