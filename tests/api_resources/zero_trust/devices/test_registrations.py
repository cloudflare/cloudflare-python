# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.zero_trust.devices import (
    RegistrationGetResponse,
    RegistrationListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegistrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        registration = client.zero_trust.devices.registrations.list(
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPagination[RegistrationListResponse], registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        registration = client.zero_trust.devices.registrations.list(
            account_id="account_id",
            id=["string"],
            cursor="cursor",
            device={"id": "id"},
            include="include",
            per_page=0,
            search="search",
            seen_after="seen_after",
            seen_before="seen_before",
            sort_by="id",
            sort_order="asc",
            status="active",
            user={"id": ["string"]},
        )
        assert_matches_type(SyncCursorPagination[RegistrationListResponse], registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.registrations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(SyncCursorPagination[RegistrationListResponse], registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.registrations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(SyncCursorPagination[RegistrationListResponse], registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.registrations.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        registration = client.zero_trust.devices.registrations.delete(
            registration_id="registration_id",
            account_id="account_id",
        )
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.registrations.with_raw_response.delete(
            registration_id="registration_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.registrations.with_streaming_response.delete(
            registration_id="registration_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(object, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.registrations.with_raw_response.delete(
                registration_id="registration_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            client.zero_trust.devices.registrations.with_raw_response.delete(
                registration_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        registration = client.zero_trust.devices.registrations.bulk_delete(
            account_id="account_id",
            id=["string"],
        )
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.registrations.with_raw_response.bulk_delete(
            account_id="account_id",
            id=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.registrations.with_streaming_response.bulk_delete(
            account_id="account_id",
            id=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(object, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.registrations.with_raw_response.bulk_delete(
                account_id="",
                id=["string"],
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        registration = client.zero_trust.devices.registrations.get(
            registration_id="registration_id",
            account_id="account_id",
        )
        assert_matches_type(RegistrationGetResponse, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.registrations.with_raw_response.get(
            registration_id="registration_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(RegistrationGetResponse, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.registrations.with_streaming_response.get(
            registration_id="registration_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(RegistrationGetResponse, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.registrations.with_raw_response.get(
                registration_id="registration_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            client.zero_trust.devices.registrations.with_raw_response.get(
                registration_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_revoke(self, client: Cloudflare) -> None:
        registration = client.zero_trust.devices.registrations.revoke(
            account_id="account_id",
            id=["string"],
        )
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_revoke(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.registrations.with_raw_response.revoke(
            account_id="account_id",
            id=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_revoke(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.registrations.with_streaming_response.revoke(
            account_id="account_id",
            id=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(object, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_revoke(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.registrations.with_raw_response.revoke(
                account_id="",
                id=["string"],
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_method_unrevoke(self, client: Cloudflare) -> None:
        registration = client.zero_trust.devices.registrations.unrevoke(
            account_id="account_id",
            id=["string"],
        )
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_raw_response_unrevoke(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.registrations.with_raw_response.unrevoke(
            account_id="account_id",
            id=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_streaming_response_unrevoke(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.registrations.with_streaming_response.unrevoke(
            account_id="account_id",
            id=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(object, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    def test_path_params_unrevoke(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.devices.registrations.with_raw_response.unrevoke(
                account_id="",
                id=["string"],
            )


class TestAsyncRegistrations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.zero_trust.devices.registrations.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPagination[RegistrationListResponse], registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.zero_trust.devices.registrations.list(
            account_id="account_id",
            id=["string"],
            cursor="cursor",
            device={"id": "id"},
            include="include",
            per_page=0,
            search="search",
            seen_after="seen_after",
            seen_before="seen_before",
            sort_by="id",
            sort_order="asc",
            status="active",
            user={"id": ["string"]},
        )
        assert_matches_type(AsyncCursorPagination[RegistrationListResponse], registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.registrations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(AsyncCursorPagination[RegistrationListResponse], registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.registrations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(AsyncCursorPagination[RegistrationListResponse], registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.registrations.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.zero_trust.devices.registrations.delete(
            registration_id="registration_id",
            account_id="account_id",
        )
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.registrations.with_raw_response.delete(
            registration_id="registration_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.registrations.with_streaming_response.delete(
            registration_id="registration_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(object, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.registrations.with_raw_response.delete(
                registration_id="registration_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            await async_client.zero_trust.devices.registrations.with_raw_response.delete(
                registration_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.zero_trust.devices.registrations.bulk_delete(
            account_id="account_id",
            id=["string"],
        )
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.registrations.with_raw_response.bulk_delete(
            account_id="account_id",
            id=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.registrations.with_streaming_response.bulk_delete(
            account_id="account_id",
            id=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(object, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.registrations.with_raw_response.bulk_delete(
                account_id="",
                id=["string"],
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.zero_trust.devices.registrations.get(
            registration_id="registration_id",
            account_id="account_id",
        )
        assert_matches_type(RegistrationGetResponse, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.registrations.with_raw_response.get(
            registration_id="registration_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(RegistrationGetResponse, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.registrations.with_streaming_response.get(
            registration_id="registration_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(RegistrationGetResponse, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.registrations.with_raw_response.get(
                registration_id="registration_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `registration_id` but received ''"):
            await async_client.zero_trust.devices.registrations.with_raw_response.get(
                registration_id="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.zero_trust.devices.registrations.revoke(
            account_id="account_id",
            id=["string"],
        )
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.registrations.with_raw_response.revoke(
            account_id="account_id",
            id=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.registrations.with_streaming_response.revoke(
            account_id="account_id",
            id=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(object, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.registrations.with_raw_response.revoke(
                account_id="",
                id=["string"],
            )

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_method_unrevoke(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.zero_trust.devices.registrations.unrevoke(
            account_id="account_id",
            id=["string"],
        )
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_raw_response_unrevoke(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.registrations.with_raw_response.unrevoke(
            account_id="account_id",
            id=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(object, registration, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_streaming_response_unrevoke(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.registrations.with_streaming_response.unrevoke(
            account_id="account_id",
            id=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(object, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate prism error for invalid security scheme used")
    @parametrize
    async def test_path_params_unrevoke(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.devices.registrations.with_raw_response.unrevoke(
                account_id="",
                id=["string"],
            )
