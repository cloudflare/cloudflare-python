# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.iam import (
    UserGroupGetResponse,
    UserGroupListResponse,
    UserGroupCreateResponse,
    UserGroupDeleteResponse,
    UserGroupUpdateResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        user_group = client.iam.user_groups.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My New User Group",
            policies=[
                {
                    "access": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                }
            ],
        )
        assert_matches_type(Optional[UserGroupCreateResponse], user_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.iam.user_groups.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My New User Group",
            policies=[
                {
                    "access": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = response.parse()
        assert_matches_type(Optional[UserGroupCreateResponse], user_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.iam.user_groups.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My New User Group",
            policies=[
                {
                    "access": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = response.parse()
            assert_matches_type(Optional[UserGroupCreateResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.user_groups.with_raw_response.create(
                account_id="",
                name="My New User Group",
                policies=[
                    {
                        "access": "allow",
                        "permission_groups": [
                            {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                            {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                        ],
                        "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                    }
                ],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        user_group = client.iam.user_groups.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserGroupUpdateResponse], user_group, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        user_group = client.iam.user_groups.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My New User Group",
            policies=[
                {
                    "id": "f267e341f3dd4697bd3b9f71dd96247f",
                    "access": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                }
            ],
        )
        assert_matches_type(Optional[UserGroupUpdateResponse], user_group, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.iam.user_groups.with_raw_response.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = response.parse()
        assert_matches_type(Optional[UserGroupUpdateResponse], user_group, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.iam.user_groups.with_streaming_response.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = response.parse()
            assert_matches_type(Optional[UserGroupUpdateResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.user_groups.with_raw_response.update(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            client.iam.user_groups.with_raw_response.update(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        user_group = client.iam.user_groups.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[UserGroupListResponse], user_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        user_group = client.iam.user_groups.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            fuzzy_name="Foo",
            name="NameOfTheUserGroup",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[UserGroupListResponse], user_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.iam.user_groups.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[UserGroupListResponse], user_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.iam.user_groups.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[UserGroupListResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.user_groups.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        user_group = client.iam.user_groups.delete(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserGroupDeleteResponse], user_group, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.iam.user_groups.with_raw_response.delete(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = response.parse()
        assert_matches_type(Optional[UserGroupDeleteResponse], user_group, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.iam.user_groups.with_streaming_response.delete(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = response.parse()
            assert_matches_type(Optional[UserGroupDeleteResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.user_groups.with_raw_response.delete(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            client.iam.user_groups.with_raw_response.delete(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        user_group = client.iam.user_groups.get(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserGroupGetResponse], user_group, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.iam.user_groups.with_raw_response.get(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = response.parse()
        assert_matches_type(Optional[UserGroupGetResponse], user_group, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.iam.user_groups.with_streaming_response.get(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = response.parse()
            assert_matches_type(Optional[UserGroupGetResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.user_groups.with_raw_response.get(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            client.iam.user_groups.with_raw_response.get(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncUserGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        user_group = await async_client.iam.user_groups.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My New User Group",
            policies=[
                {
                    "access": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                }
            ],
        )
        assert_matches_type(Optional[UserGroupCreateResponse], user_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.user_groups.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My New User Group",
            policies=[
                {
                    "access": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = await response.parse()
        assert_matches_type(Optional[UserGroupCreateResponse], user_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.user_groups.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My New User Group",
            policies=[
                {
                    "access": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = await response.parse()
            assert_matches_type(Optional[UserGroupCreateResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.user_groups.with_raw_response.create(
                account_id="",
                name="My New User Group",
                policies=[
                    {
                        "access": "allow",
                        "permission_groups": [
                            {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                            {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                        ],
                        "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                    }
                ],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        user_group = await async_client.iam.user_groups.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserGroupUpdateResponse], user_group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_group = await async_client.iam.user_groups.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My New User Group",
            policies=[
                {
                    "id": "f267e341f3dd4697bd3b9f71dd96247f",
                    "access": "allow",
                    "permission_groups": [
                        {"id": "c8fed203ed3043cba015a93ad1616f1f"},
                        {"id": "82e64a83756745bbbb1c9c2701bf816b"},
                    ],
                    "resource_groups": [{"id": "6d7f2f5f5b1d4a0e9081fdc98d432fd1"}],
                }
            ],
        )
        assert_matches_type(Optional[UserGroupUpdateResponse], user_group, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.user_groups.with_raw_response.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = await response.parse()
        assert_matches_type(Optional[UserGroupUpdateResponse], user_group, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.user_groups.with_streaming_response.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = await response.parse()
            assert_matches_type(Optional[UserGroupUpdateResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.user_groups.with_raw_response.update(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            await async_client.iam.user_groups.with_raw_response.update(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        user_group = await async_client.iam.user_groups.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[UserGroupListResponse], user_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user_group = await async_client.iam.user_groups.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            fuzzy_name="Foo",
            name="NameOfTheUserGroup",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[UserGroupListResponse], user_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.user_groups.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[UserGroupListResponse], user_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.user_groups.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[UserGroupListResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.user_groups.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        user_group = await async_client.iam.user_groups.delete(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserGroupDeleteResponse], user_group, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.user_groups.with_raw_response.delete(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = await response.parse()
        assert_matches_type(Optional[UserGroupDeleteResponse], user_group, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.user_groups.with_streaming_response.delete(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = await response.parse()
            assert_matches_type(Optional[UserGroupDeleteResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.user_groups.with_raw_response.delete(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            await async_client.iam.user_groups.with_raw_response.delete(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        user_group = await async_client.iam.user_groups.get(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserGroupGetResponse], user_group, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.user_groups.with_raw_response.get(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_group = await response.parse()
        assert_matches_type(Optional[UserGroupGetResponse], user_group, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.user_groups.with_streaming_response.get(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_group = await response.parse()
            assert_matches_type(Optional[UserGroupGetResponse], user_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.user_groups.with_raw_response.get(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            await async_client.iam.user_groups.with_raw_response.get(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
