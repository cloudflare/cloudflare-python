# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.iam.user_groups import (
    MemberListResponse,
    MemberCreateResponse,
    MemberDeleteResponse,
    MemberUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        member = client.iam.user_groups.members.create(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        )
        assert_matches_type(Optional[MemberCreateResponse], member, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.iam.user_groups.members.with_raw_response.create(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(Optional[MemberCreateResponse], member, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.iam.user_groups.members.with_streaming_response.create(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(Optional[MemberCreateResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.user_groups.members.with_raw_response.create(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            client.iam.user_groups.members.with_raw_response.create(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        member = client.iam.user_groups.members.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        )
        assert_matches_type(SyncSinglePage[MemberUpdateResponse], member, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.iam.user_groups.members.with_raw_response.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(SyncSinglePage[MemberUpdateResponse], member, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.iam.user_groups.members.with_streaming_response.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(SyncSinglePage[MemberUpdateResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.user_groups.members.with_raw_response.update(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            client.iam.user_groups.members.with_raw_response.update(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        member = client.iam.user_groups.members.list(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[MemberListResponse], member, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        member = client.iam.user_groups.members.list(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[MemberListResponse], member, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.iam.user_groups.members.with_raw_response.list(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[MemberListResponse], member, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.iam.user_groups.members.with_streaming_response.list(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[MemberListResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.user_groups.members.with_raw_response.list(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            client.iam.user_groups.members.with_raw_response.list(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        member = client.iam.user_groups.members.delete(
            member_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.iam.user_groups.members.with_raw_response.delete(
            member_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.iam.user_groups.members.with_streaming_response.delete(
            member_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.iam.user_groups.members.with_raw_response.delete(
                member_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            client.iam.user_groups.members.with_raw_response.delete(
                member_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.iam.user_groups.members.with_raw_response.delete(
                member_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.iam.user_groups.members.create(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        )
        assert_matches_type(Optional[MemberCreateResponse], member, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.user_groups.members.with_raw_response.create(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(Optional[MemberCreateResponse], member, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.user_groups.members.with_streaming_response.create(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(Optional[MemberCreateResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.user_groups.members.with_raw_response.create(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            await async_client.iam.user_groups.members.with_raw_response.create(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.iam.user_groups.members.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        )
        assert_matches_type(AsyncSinglePage[MemberUpdateResponse], member, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.user_groups.members.with_raw_response.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(AsyncSinglePage[MemberUpdateResponse], member, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.user_groups.members.with_streaming_response.update(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(AsyncSinglePage[MemberUpdateResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.user_groups.members.with_raw_response.update(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            await async_client.iam.user_groups.members.with_raw_response.update(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{"id": "023e105f4ecef8ad9ca31a8372d0c353"}],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.iam.user_groups.members.list(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[MemberListResponse], member, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.iam.user_groups.members.list(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[MemberListResponse], member, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.user_groups.members.with_raw_response.list(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[MemberListResponse], member, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.user_groups.members.with_streaming_response.list(
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[MemberListResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.user_groups.members.with_raw_response.list(
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            await async_client.iam.user_groups.members.with_raw_response.list(
                user_group_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.iam.user_groups.members.delete(
            member_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.iam.user_groups.members.with_raw_response.delete(
            member_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.iam.user_groups.members.with_streaming_response.delete(
            member_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.iam.user_groups.members.with_raw_response.delete(
                member_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_group_id` but received ''"):
            await async_client.iam.user_groups.members.with_raw_response.delete(
                member_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_group_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.iam.user_groups.members.with_raw_response.delete(
                member_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                user_group_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
