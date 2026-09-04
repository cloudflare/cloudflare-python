# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.email_sending import (
    SuppressionGetResponse,
    SuppressionEditResponse,
    SuppressionListResponse,
    SuppressionCreateResponse,
    SuppressionDeleteResponse,
    SuppressionImportResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuppressions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        suppression = client.email_sending.suppressions.create(
            account_id="54442216",
            email="user@example.com",
        )
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        suppression = client.email_sending.suppressions.create(
            account_id="54442216",
            email="user@example.com",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            note="Imported from CRM",
        )
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.email_sending.suppressions.with_raw_response.create(
            account_id="54442216",
            email="user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.email_sending.suppressions.with_streaming_response.create(
            account_id="54442216",
            email="user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_sending.suppressions.with_raw_response.create(
                account_id="",
                email="user@example.com",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        suppression = client.email_sending.suppressions.list(
            account_id="54442216",
        )
        assert_matches_type(SyncCursorPagination[SuppressionListResponse], suppression, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        suppression = client.email_sending.suppressions.list(
            account_id="54442216",
            cursor="eyJ0IjozLCJwIjoxMjMsImMiOiJjM2RjNWYwYjM0YTE0ZmY4ZTFiM2VjMDQ4OTVlMWIyMiJ9",
            email="user@example.com",
            per_page=1,
            reason="manual",
            search="billing@",
        )
        assert_matches_type(SyncCursorPagination[SuppressionListResponse], suppression, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_sending.suppressions.with_raw_response.list(
            account_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SyncCursorPagination[SuppressionListResponse], suppression, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_sending.suppressions.with_streaming_response.list(
            account_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SyncCursorPagination[SuppressionListResponse], suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_sending.suppressions.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        suppression = client.email_sending.suppressions.delete(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.email_sending.suppressions.with_raw_response.delete(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_sending.suppressions.with_streaming_response.delete(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_sending.suppressions.with_raw_response.delete(
                suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suppression_id` but received ''"):
            client.email_sending.suppressions.with_raw_response.delete(
                suppression_id="",
                account_id="54442216",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        suppression = client.email_sending.suppressions.edit(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )
        assert_matches_type(SuppressionEditResponse, suppression, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        suppression = client.email_sending.suppressions.edit(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            note="Customer re-confirmed opt-in",
        )
        assert_matches_type(SuppressionEditResponse, suppression, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.email_sending.suppressions.with_raw_response.edit(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SuppressionEditResponse, suppression, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.email_sending.suppressions.with_streaming_response.edit(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SuppressionEditResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_sending.suppressions.with_raw_response.edit(
                suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suppression_id` but received ''"):
            client.email_sending.suppressions.with_raw_response.edit(
                suppression_id="",
                account_id="54442216",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        suppression = client.email_sending.suppressions.get(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )
        assert_matches_type(SuppressionGetResponse, suppression, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_sending.suppressions.with_raw_response.get(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SuppressionGetResponse, suppression, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_sending.suppressions.with_streaming_response.get(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SuppressionGetResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_sending.suppressions.with_raw_response.get(
                suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suppression_id` but received ''"):
            client.email_sending.suppressions.with_raw_response.get(
                suppression_id="",
                account_id="54442216",
            )

    @parametrize
    def test_method_import(self, client: Cloudflare) -> None:
        suppression = client.email_sending.suppressions.import_(
            account_id="54442216",
            items=[{"email": "email"}],
        )
        assert_matches_type(SuppressionImportResponse, suppression, path=["response"])

    @parametrize
    def test_raw_response_import(self, client: Cloudflare) -> None:
        response = client.email_sending.suppressions.with_raw_response.import_(
            account_id="54442216",
            items=[{"email": "email"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SuppressionImportResponse, suppression, path=["response"])

    @parametrize
    def test_streaming_response_import(self, client: Cloudflare) -> None:
        with client.email_sending.suppressions.with_streaming_response.import_(
            account_id="54442216",
            items=[{"email": "email"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SuppressionImportResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_import(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_sending.suppressions.with_raw_response.import_(
                account_id="",
                items=[{"email": "email"}],
            )


class TestAsyncSuppressions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        suppression = await async_client.email_sending.suppressions.create(
            account_id="54442216",
            email="user@example.com",
        )
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        suppression = await async_client.email_sending.suppressions.create(
            account_id="54442216",
            email="user@example.com",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            note="Imported from CRM",
        )
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.suppressions.with_raw_response.create(
            account_id="54442216",
            email="user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.suppressions.with_streaming_response.create(
            account_id="54442216",
            email="user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_sending.suppressions.with_raw_response.create(
                account_id="",
                email="user@example.com",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        suppression = await async_client.email_sending.suppressions.list(
            account_id="54442216",
        )
        assert_matches_type(AsyncCursorPagination[SuppressionListResponse], suppression, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        suppression = await async_client.email_sending.suppressions.list(
            account_id="54442216",
            cursor="eyJ0IjozLCJwIjoxMjMsImMiOiJjM2RjNWYwYjM0YTE0ZmY4ZTFiM2VjMDQ4OTVlMWIyMiJ9",
            email="user@example.com",
            per_page=1,
            reason="manual",
            search="billing@",
        )
        assert_matches_type(AsyncCursorPagination[SuppressionListResponse], suppression, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.suppressions.with_raw_response.list(
            account_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(AsyncCursorPagination[SuppressionListResponse], suppression, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.suppressions.with_streaming_response.list(
            account_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(AsyncCursorPagination[SuppressionListResponse], suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_sending.suppressions.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        suppression = await async_client.email_sending.suppressions.delete(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.suppressions.with_raw_response.delete(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.suppressions.with_streaming_response.delete(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_sending.suppressions.with_raw_response.delete(
                suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suppression_id` but received ''"):
            await async_client.email_sending.suppressions.with_raw_response.delete(
                suppression_id="",
                account_id="54442216",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        suppression = await async_client.email_sending.suppressions.edit(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )
        assert_matches_type(SuppressionEditResponse, suppression, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        suppression = await async_client.email_sending.suppressions.edit(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            note="Customer re-confirmed opt-in",
        )
        assert_matches_type(SuppressionEditResponse, suppression, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.suppressions.with_raw_response.edit(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(SuppressionEditResponse, suppression, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.suppressions.with_streaming_response.edit(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(SuppressionEditResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_sending.suppressions.with_raw_response.edit(
                suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suppression_id` but received ''"):
            await async_client.email_sending.suppressions.with_raw_response.edit(
                suppression_id="",
                account_id="54442216",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        suppression = await async_client.email_sending.suppressions.get(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )
        assert_matches_type(SuppressionGetResponse, suppression, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.suppressions.with_raw_response.get(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(SuppressionGetResponse, suppression, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.suppressions.with_streaming_response.get(
            suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
            account_id="54442216",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(SuppressionGetResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_sending.suppressions.with_raw_response.get(
                suppression_id="396a5436-d4b0-42a6-b3fc-48e8fa522321",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suppression_id` but received ''"):
            await async_client.email_sending.suppressions.with_raw_response.get(
                suppression_id="",
                account_id="54442216",
            )

    @parametrize
    async def test_method_import(self, async_client: AsyncCloudflare) -> None:
        suppression = await async_client.email_sending.suppressions.import_(
            account_id="54442216",
            items=[{"email": "email"}],
        )
        assert_matches_type(SuppressionImportResponse, suppression, path=["response"])

    @parametrize
    async def test_raw_response_import(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.suppressions.with_raw_response.import_(
            account_id="54442216",
            items=[{"email": "email"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(SuppressionImportResponse, suppression, path=["response"])

    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.suppressions.with_streaming_response.import_(
            account_id="54442216",
            items=[{"email": "email"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(SuppressionImportResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_import(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_sending.suppressions.with_raw_response.import_(
                account_id="",
                items=[{"email": "email"}],
            )
