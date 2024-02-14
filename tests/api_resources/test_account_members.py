# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    AccountMemberGetResponse,
    AccountMemberListResponse,
    AccountMemberCreateResponse,
    AccountMemberDeleteResponse,
    AccountMemberUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        account_member = client.account_members.create(
            {},
            email="user@example.com",
            roles=[
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
            ],
        )
        assert_matches_type(AccountMemberCreateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        account_member = client.account_members.create(
            {},
            email="user@example.com",
            roles=[
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
            ],
            status="accepted",
        )
        assert_matches_type(AccountMemberCreateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.account_members.with_raw_response.create(
            {},
            email="user@example.com",
            roles=[
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = response.parse()
        assert_matches_type(AccountMemberCreateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.account_members.with_streaming_response.create(
            {},
            email="user@example.com",
            roles=[
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = response.parse()
            assert_matches_type(AccountMemberCreateResponse, account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        account_member = client.account_members.update(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
            roles=[
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
            ],
        )
        assert_matches_type(AccountMemberUpdateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.account_members.with_raw_response.update(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
            roles=[
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = response.parse()
        assert_matches_type(AccountMemberUpdateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.account_members.with_streaming_response.update(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
            roles=[
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = response.parse()
            assert_matches_type(AccountMemberUpdateResponse, account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.account_members.with_raw_response.update(
                "",
                account_id={},
                roles=[
                    {"id": "3536bcfad5faccb999b47003c79917fb"},
                    {"id": "3536bcfad5faccb999b47003c79917fb"},
                    {"id": "3536bcfad5faccb999b47003c79917fb"},
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        account_member = client.account_members.list(
            {},
        )
        assert_matches_type(Optional[AccountMemberListResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        account_member = client.account_members.list(
            {},
            direction="desc",
            order="status",
            page=1,
            per_page=5,
            status="accepted",
        )
        assert_matches_type(Optional[AccountMemberListResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.account_members.with_raw_response.list(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = response.parse()
        assert_matches_type(Optional[AccountMemberListResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.account_members.with_streaming_response.list(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = response.parse()
            assert_matches_type(Optional[AccountMemberListResponse], account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        account_member = client.account_members.delete(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        )
        assert_matches_type(Optional[AccountMemberDeleteResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.account_members.with_raw_response.delete(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = response.parse()
        assert_matches_type(Optional[AccountMemberDeleteResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.account_members.with_streaming_response.delete(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = response.parse()
            assert_matches_type(Optional[AccountMemberDeleteResponse], account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.account_members.with_raw_response.delete(
                "",
                account_id={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        account_member = client.account_members.get(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        )
        assert_matches_type(AccountMemberGetResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.account_members.with_raw_response.get(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = response.parse()
        assert_matches_type(AccountMemberGetResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.account_members.with_streaming_response.get(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = response.parse()
            assert_matches_type(AccountMemberGetResponse, account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.account_members.with_raw_response.get(
                "",
                account_id={},
            )


class TestAsyncAccountMembers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        account_member = await async_client.account_members.create(
            {},
            email="user@example.com",
            roles=[
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
            ],
        )
        assert_matches_type(AccountMemberCreateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        account_member = await async_client.account_members.create(
            {},
            email="user@example.com",
            roles=[
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
            ],
            status="accepted",
        )
        assert_matches_type(AccountMemberCreateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.account_members.with_raw_response.create(
            {},
            email="user@example.com",
            roles=[
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = await response.parse()
        assert_matches_type(AccountMemberCreateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.account_members.with_streaming_response.create(
            {},
            email="user@example.com",
            roles=[
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
                "3536bcfad5faccb999b47003c79917fb",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = await response.parse()
            assert_matches_type(AccountMemberCreateResponse, account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        account_member = await async_client.account_members.update(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
            roles=[
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
            ],
        )
        assert_matches_type(AccountMemberUpdateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.account_members.with_raw_response.update(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
            roles=[
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = await response.parse()
        assert_matches_type(AccountMemberUpdateResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.account_members.with_streaming_response.update(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
            roles=[
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
                {"id": "3536bcfad5faccb999b47003c79917fb"},
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = await response.parse()
            assert_matches_type(AccountMemberUpdateResponse, account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.account_members.with_raw_response.update(
                "",
                account_id={},
                roles=[
                    {"id": "3536bcfad5faccb999b47003c79917fb"},
                    {"id": "3536bcfad5faccb999b47003c79917fb"},
                    {"id": "3536bcfad5faccb999b47003c79917fb"},
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        account_member = await async_client.account_members.list(
            {},
        )
        assert_matches_type(Optional[AccountMemberListResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        account_member = await async_client.account_members.list(
            {},
            direction="desc",
            order="status",
            page=1,
            per_page=5,
            status="accepted",
        )
        assert_matches_type(Optional[AccountMemberListResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.account_members.with_raw_response.list(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = await response.parse()
        assert_matches_type(Optional[AccountMemberListResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.account_members.with_streaming_response.list(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = await response.parse()
            assert_matches_type(Optional[AccountMemberListResponse], account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        account_member = await async_client.account_members.delete(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        )
        assert_matches_type(Optional[AccountMemberDeleteResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.account_members.with_raw_response.delete(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = await response.parse()
        assert_matches_type(Optional[AccountMemberDeleteResponse], account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.account_members.with_streaming_response.delete(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = await response.parse()
            assert_matches_type(Optional[AccountMemberDeleteResponse], account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.account_members.with_raw_response.delete(
                "",
                account_id={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        account_member = await async_client.account_members.get(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        )
        assert_matches_type(AccountMemberGetResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.account_members.with_raw_response.get(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_member = await response.parse()
        assert_matches_type(AccountMemberGetResponse, account_member, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.account_members.with_streaming_response.get(
            "4536bcfad5faccb111b47003c79917fa",
            account_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_member = await response.parse()
            assert_matches_type(AccountMemberGetResponse, account_member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.account_members.with_raw_response.get(
                "",
                account_id={},
            )
