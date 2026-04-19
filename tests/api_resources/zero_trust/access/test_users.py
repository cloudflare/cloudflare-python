# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.access import (
    UserGetResponse,
    UserListResponse,
    UserCreateResponse,
    UserUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.users.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
        )
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.users.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
            name="Jane Doe",
        )
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.users.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.users.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.users.with_raw_response.create(
                account_id="",
                email="jdoe@example.com",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.users.update(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
            name="Jane Doe",
        )
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.users.with_raw_response.update(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
            name="Jane Doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.users.with_streaming_response.update(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
            name="Jane Doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.users.with_raw_response.update(
                user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                email="jdoe@example.com",
                name="Jane Doe",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.access.users.with_raw_response.update(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                email="jdoe@example.com",
                name="Jane Doe",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.users.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[UserListResponse], user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.users.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            name="name",
            page=0,
            per_page=0,
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[UserListResponse], user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.users.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[UserListResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.users.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[UserListResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.users.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.users.delete(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.users.with_raw_response.delete(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.users.with_streaming_response.delete(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.users.with_raw_response.delete(
                user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.access.users.with_raw_response.delete(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        user = client.zero_trust.access.users.get(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.users.with_raw_response.get(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.users.with_streaming_response.get(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(Optional[UserGetResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.users.with_raw_response.get(
                user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.zero_trust.access.users.with_raw_response.get(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.users.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
        )
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.users.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
            name="Jane Doe",
        )
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.users.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.users.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(Optional[UserCreateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.users.with_raw_response.create(
                account_id="",
                email="jdoe@example.com",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.users.update(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
            name="Jane Doe",
        )
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.users.with_raw_response.update(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
            name="Jane Doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.users.with_streaming_response.update(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="jdoe@example.com",
            name="Jane Doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(Optional[UserUpdateResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.users.with_raw_response.update(
                user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                email="jdoe@example.com",
                name="Jane Doe",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.access.users.with_raw_response.update(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                email="jdoe@example.com",
                name="Jane Doe",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.users.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[UserListResponse], user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.users.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            name="name",
            page=0,
            per_page=0,
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[UserListResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.users.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[UserListResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.users.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[UserListResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.users.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.users.delete(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.users.with_raw_response.delete(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(object, user, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.users.with_streaming_response.delete(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(object, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.users.with_raw_response.delete(
                user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.access.users.with_raw_response.delete(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.zero_trust.access.users.get(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.users.with_raw_response.get(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(Optional[UserGetResponse], user, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.users.with_streaming_response.get(
            user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(Optional[UserGetResponse], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.users.with_raw_response.get(
                user_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.zero_trust.access.users.with_raw_response.get(
                user_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
