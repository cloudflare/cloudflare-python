# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.shared import Member
from cloudflare.types.accounts import (
    MemberDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        member = client.accounts.members.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
            roles=["3536bcfad5faccb999b47003c79917fb"],
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        member = client.accounts.members.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
            roles=["3536bcfad5faccb999b47003c79917fb"],
            status="accepted",
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.accounts.members.with_raw_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
            roles=["3536bcfad5faccb999b47003c79917fb"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.accounts.members.with_streaming_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
            roles=["3536bcfad5faccb999b47003c79917fb"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.members.with_raw_response.create(
                account_id="",
                email="user@example.com",
                roles=["3536bcfad5faccb999b47003c79917fb"],
            )

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        member = client.accounts.members.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
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
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        member = client.accounts.members.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
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
            status="accepted",
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.accounts.members.with_raw_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
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
        member = response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.accounts.members.with_streaming_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
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

            member = response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.members.with_raw_response.create(
                account_id="",
                email="user@example.com",
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

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        member = client.accounts.members.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        member = client.accounts.members.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            roles=[{"id": "3536bcfad5faccb999b47003c79917fb"}],
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.accounts.members.with_raw_response.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.accounts.members.with_streaming_response.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.members.with_raw_response.update(
                member_id="4536bcfad5faccb111b47003c79917fa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.accounts.members.with_raw_response.update(
                member_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        member = client.accounts.members.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
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
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.accounts.members.with_raw_response.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
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
        member = response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.accounts.members.with_streaming_response.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
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

            member = response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.members.with_raw_response.update(
                member_id="4536bcfad5faccb111b47003c79917fa",
                account_id="",
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.accounts.members.with_raw_response.update(
                member_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
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
    def test_method_list(self, client: Cloudflare) -> None:
        member = client.accounts.members.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(SyncV4PagePaginationArray[Member], member, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        member = client.accounts.members.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            direction="asc",
            order="user.first_name",
            page=1,
            per_page=5,
            status="accepted",
        )
        assert_matches_type(SyncV4PagePaginationArray[Member], member, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.accounts.members.with_raw_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Member], member, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.accounts.members.with_streaming_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.members.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        member = client.accounts.members.delete(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.accounts.members.with_raw_response.delete(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.accounts.members.with_streaming_response.delete(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.members.with_raw_response.delete(
                member_id="4536bcfad5faccb111b47003c79917fa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.accounts.members.with_raw_response.delete(
                member_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        member = client.accounts.members.get(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.accounts.members.with_raw_response.get(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.accounts.members.with_streaming_response.get(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.members.with_raw_response.get(
                member_id="4536bcfad5faccb111b47003c79917fa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.accounts.members.with_raw_response.get(
                member_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
            roles=["3536bcfad5faccb999b47003c79917fb"],
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
            roles=["3536bcfad5faccb999b47003c79917fb"],
            status="accepted",
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.accounts.members.with_raw_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
            roles=["3536bcfad5faccb999b47003c79917fb"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.accounts.members.with_streaming_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
            roles=["3536bcfad5faccb999b47003c79917fb"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.members.with_raw_response.create(
                account_id="",
                email="user@example.com",
                roles=["3536bcfad5faccb999b47003c79917fb"],
            )

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
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
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
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
            status="accepted",
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.accounts.members.with_raw_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
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
        member = await response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.accounts.members.with_streaming_response.create(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            email="user@example.com",
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

            member = await response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.members.with_raw_response.create(
                account_id="",
                email="user@example.com",
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

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            roles=[{"id": "3536bcfad5faccb999b47003c79917fb"}],
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.accounts.members.with_raw_response.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.accounts.members.with_streaming_response.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.members.with_raw_response.update(
                member_id="4536bcfad5faccb111b47003c79917fa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.accounts.members.with_raw_response.update(
                member_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
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
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.accounts.members.with_raw_response.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
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
        member = await response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.accounts.members.with_streaming_response.update(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
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

            member = await response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.members.with_raw_response.update(
                member_id="4536bcfad5faccb111b47003c79917fa",
                account_id="",
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.accounts.members.with_raw_response.update(
                member_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
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
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Member], member, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
            direction="asc",
            order="user.first_name",
            page=1,
            per_page=5,
            status="accepted",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Member], member, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.accounts.members.with_raw_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Member], member, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.accounts.members.with_streaming_response.list(
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.members.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.delete(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.accounts.members.with_raw_response.delete(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.accounts.members.with_streaming_response.delete(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(Optional[MemberDeleteResponse], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.members.with_raw_response.delete(
                member_id="4536bcfad5faccb111b47003c79917fa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.accounts.members.with_raw_response.delete(
                member_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        member = await async_client.accounts.members.get(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.accounts.members.with_raw_response.get(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert_matches_type(Optional[Member], member, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.accounts.members.with_streaming_response.get(
            member_id="4536bcfad5faccb111b47003c79917fa",
            account_id="eb78d65290b24279ba6f44721b3ea3c4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert_matches_type(Optional[Member], member, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 error from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.members.with_raw_response.get(
                member_id="4536bcfad5faccb111b47003c79917fa",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.accounts.members.with_raw_response.get(
                member_id="",
                account_id="eb78d65290b24279ba6f44721b3ea3c4",
            )
