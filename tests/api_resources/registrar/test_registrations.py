# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.registrar import (
    Registration,
    WorkflowStatus,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegistrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        registration = client.registrar.registrations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain_name="my-new-startup.com",
        )
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        registration = client.registrar.registrations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain_name="my-new-startup.com",
            auto_renew=False,
            contacts={
                "registrant": {
                    "email": "ada@example.com",
                    "phone": "+1.5555555555",
                    "postal_info": {
                        "address": {
                            "city": "Austin",
                            "country_code": "US",
                            "postal_code": "78701",
                            "state": "TX",
                            "street": "123 Main St",
                        },
                        "name": "Ada Lovelace",
                        "organization": "Example Inc",
                    },
                    "fax": "+1.5555555555",
                }
            },
            privacy_mode="redaction",
            years=1,
            prefer="Prefer",
        )
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.registrar.registrations.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain_name="my-new-startup.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.registrar.registrations.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain_name="my-new-startup.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(WorkflowStatus, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.registrar.registrations.with_raw_response.create(
                account_id="",
                domain_name="my-new-startup.com",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        registration = client.registrar.registrations.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncCursorPagination[Registration], registration, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        registration = client.registrar.registrations.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="cursor",
            direction="asc",
            per_page=1,
            sort_by="registry_created_at",
        )
        assert_matches_type(SyncCursorPagination[Registration], registration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.registrar.registrations.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(SyncCursorPagination[Registration], registration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.registrar.registrations.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(SyncCursorPagination[Registration], registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.registrar.registrations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        registration = client.registrar.registrations.edit(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        registration = client.registrar.registrations.edit(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            auto_renew=False,
            prefer="respond-async",
        )
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.registrar.registrations.with_raw_response.edit(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.registrar.registrations.with_streaming_response.edit(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(WorkflowStatus, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.registrar.registrations.with_raw_response.edit(
                domain_name="example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.registrar.registrations.with_raw_response.edit(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        registration = client.registrar.registrations.get(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Registration, registration, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.registrar.registrations.with_raw_response.get(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = response.parse()
        assert_matches_type(Registration, registration, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.registrar.registrations.with_streaming_response.get(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = response.parse()
            assert_matches_type(Registration, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.registrar.registrations.with_raw_response.get(
                domain_name="example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.registrar.registrations.with_raw_response.get(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRegistrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.registrar.registrations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain_name="my-new-startup.com",
        )
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.registrar.registrations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain_name="my-new-startup.com",
            auto_renew=False,
            contacts={
                "registrant": {
                    "email": "ada@example.com",
                    "phone": "+1.5555555555",
                    "postal_info": {
                        "address": {
                            "city": "Austin",
                            "country_code": "US",
                            "postal_code": "78701",
                            "state": "TX",
                            "street": "123 Main St",
                        },
                        "name": "Ada Lovelace",
                        "organization": "Example Inc",
                    },
                    "fax": "+1.5555555555",
                }
            },
            privacy_mode="redaction",
            years=1,
            prefer="Prefer",
        )
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.registrar.registrations.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain_name="my-new-startup.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.registrar.registrations.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            domain_name="my-new-startup.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(WorkflowStatus, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.registrar.registrations.with_raw_response.create(
                account_id="",
                domain_name="my-new-startup.com",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.registrar.registrations.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncCursorPagination[Registration], registration, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.registrar.registrations.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="cursor",
            direction="asc",
            per_page=1,
            sort_by="registry_created_at",
        )
        assert_matches_type(AsyncCursorPagination[Registration], registration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.registrar.registrations.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(AsyncCursorPagination[Registration], registration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.registrar.registrations.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(AsyncCursorPagination[Registration], registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.registrar.registrations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.registrar.registrations.edit(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.registrar.registrations.edit(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            auto_renew=False,
            prefer="respond-async",
        )
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.registrar.registrations.with_raw_response.edit(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(WorkflowStatus, registration, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.registrar.registrations.with_streaming_response.edit(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(WorkflowStatus, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.registrar.registrations.with_raw_response.edit(
                domain_name="example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.registrar.registrations.with_raw_response.edit(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        registration = await async_client.registrar.registrations.get(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Registration, registration, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.registrar.registrations.with_raw_response.get(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        registration = await response.parse()
        assert_matches_type(Registration, registration, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.registrar.registrations.with_streaming_response.get(
            domain_name="example.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            registration = await response.parse()
            assert_matches_type(Registration, registration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.registrar.registrations.with_raw_response.get(
                domain_name="example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.registrar.registrations.with_raw_response.get(
                domain_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
