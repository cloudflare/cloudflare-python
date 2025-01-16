# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.email_security.settings import (
    ImpersonationRegistryGetResponse,
    ImpersonationRegistryEditResponse,
    ImpersonationRegistryListResponse,
    ImpersonationRegistryCreateResponse,
    ImpersonationRegistryDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImpersonationRegistry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        impersonation_registry = client.email_security.settings.impersonation_registry.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            is_email_regex=True,
            name="name",
        )
        assert_matches_type(ImpersonationRegistryCreateResponse, impersonation_registry, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.email_security.settings.impersonation_registry.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            is_email_regex=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = response.parse()
        assert_matches_type(ImpersonationRegistryCreateResponse, impersonation_registry, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.email_security.settings.impersonation_registry.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            is_email_regex=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = response.parse()
            assert_matches_type(ImpersonationRegistryCreateResponse, impersonation_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.impersonation_registry.with_raw_response.create(
                account_id="",
                email="email",
                is_email_regex=True,
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        impersonation_registry = client.email_security.settings.impersonation_registry.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            SyncV4PagePaginationArray[ImpersonationRegistryListResponse], impersonation_registry, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        impersonation_registry = client.email_security.settings.impersonation_registry.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="name",
            page=1,
            per_page=1,
            provenance="A1S_INTERNAL",
            search="search",
        )
        assert_matches_type(
            SyncV4PagePaginationArray[ImpersonationRegistryListResponse], impersonation_registry, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_security.settings.impersonation_registry.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = response.parse()
        assert_matches_type(
            SyncV4PagePaginationArray[ImpersonationRegistryListResponse], impersonation_registry, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.settings.impersonation_registry.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = response.parse()
            assert_matches_type(
                SyncV4PagePaginationArray[ImpersonationRegistryListResponse], impersonation_registry, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.impersonation_registry.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        impersonation_registry = client.email_security.settings.impersonation_registry.delete(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ImpersonationRegistryDeleteResponse, impersonation_registry, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.email_security.settings.impersonation_registry.with_raw_response.delete(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = response.parse()
        assert_matches_type(ImpersonationRegistryDeleteResponse, impersonation_registry, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_security.settings.impersonation_registry.with_streaming_response.delete(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = response.parse()
            assert_matches_type(ImpersonationRegistryDeleteResponse, impersonation_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.impersonation_registry.with_raw_response.delete(
                display_name_id=2403,
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        impersonation_registry = client.email_security.settings.impersonation_registry.edit(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ImpersonationRegistryEditResponse, impersonation_registry, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        impersonation_registry = client.email_security.settings.impersonation_registry.edit(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            is_email_regex=True,
            name="name",
        )
        assert_matches_type(ImpersonationRegistryEditResponse, impersonation_registry, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.email_security.settings.impersonation_registry.with_raw_response.edit(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = response.parse()
        assert_matches_type(ImpersonationRegistryEditResponse, impersonation_registry, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.email_security.settings.impersonation_registry.with_streaming_response.edit(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = response.parse()
            assert_matches_type(ImpersonationRegistryEditResponse, impersonation_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.impersonation_registry.with_raw_response.edit(
                display_name_id=2403,
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        impersonation_registry = client.email_security.settings.impersonation_registry.get(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ImpersonationRegistryGetResponse, impersonation_registry, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_security.settings.impersonation_registry.with_raw_response.get(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = response.parse()
        assert_matches_type(ImpersonationRegistryGetResponse, impersonation_registry, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.settings.impersonation_registry.with_streaming_response.get(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = response.parse()
            assert_matches_type(ImpersonationRegistryGetResponse, impersonation_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.impersonation_registry.with_raw_response.get(
                display_name_id=2403,
                account_id="",
            )


class TestAsyncImpersonationRegistry:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        impersonation_registry = await async_client.email_security.settings.impersonation_registry.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            is_email_regex=True,
            name="name",
        )
        assert_matches_type(ImpersonationRegistryCreateResponse, impersonation_registry, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.impersonation_registry.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            is_email_regex=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = await response.parse()
        assert_matches_type(ImpersonationRegistryCreateResponse, impersonation_registry, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.impersonation_registry.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            is_email_regex=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = await response.parse()
            assert_matches_type(ImpersonationRegistryCreateResponse, impersonation_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.impersonation_registry.with_raw_response.create(
                account_id="",
                email="email",
                is_email_regex=True,
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        impersonation_registry = await async_client.email_security.settings.impersonation_registry.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[ImpersonationRegistryListResponse], impersonation_registry, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        impersonation_registry = await async_client.email_security.settings.impersonation_registry.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="name",
            page=1,
            per_page=1,
            provenance="A1S_INTERNAL",
            search="search",
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[ImpersonationRegistryListResponse], impersonation_registry, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.impersonation_registry.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = await response.parse()
        assert_matches_type(
            AsyncV4PagePaginationArray[ImpersonationRegistryListResponse], impersonation_registry, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.impersonation_registry.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[ImpersonationRegistryListResponse], impersonation_registry, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.impersonation_registry.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        impersonation_registry = await async_client.email_security.settings.impersonation_registry.delete(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ImpersonationRegistryDeleteResponse, impersonation_registry, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.impersonation_registry.with_raw_response.delete(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = await response.parse()
        assert_matches_type(ImpersonationRegistryDeleteResponse, impersonation_registry, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.impersonation_registry.with_streaming_response.delete(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = await response.parse()
            assert_matches_type(ImpersonationRegistryDeleteResponse, impersonation_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.impersonation_registry.with_raw_response.delete(
                display_name_id=2403,
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        impersonation_registry = await async_client.email_security.settings.impersonation_registry.edit(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ImpersonationRegistryEditResponse, impersonation_registry, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        impersonation_registry = await async_client.email_security.settings.impersonation_registry.edit(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            email="email",
            is_email_regex=True,
            name="name",
        )
        assert_matches_type(ImpersonationRegistryEditResponse, impersonation_registry, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.impersonation_registry.with_raw_response.edit(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = await response.parse()
        assert_matches_type(ImpersonationRegistryEditResponse, impersonation_registry, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.impersonation_registry.with_streaming_response.edit(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = await response.parse()
            assert_matches_type(ImpersonationRegistryEditResponse, impersonation_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.impersonation_registry.with_raw_response.edit(
                display_name_id=2403,
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        impersonation_registry = await async_client.email_security.settings.impersonation_registry.get(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ImpersonationRegistryGetResponse, impersonation_registry, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.impersonation_registry.with_raw_response.get(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        impersonation_registry = await response.parse()
        assert_matches_type(ImpersonationRegistryGetResponse, impersonation_registry, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.impersonation_registry.with_streaming_response.get(
            display_name_id=2403,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            impersonation_registry = await response.parse()
            assert_matches_type(ImpersonationRegistryGetResponse, impersonation_registry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.impersonation_registry.with_raw_response.get(
                display_name_id=2403,
                account_id="",
            )
