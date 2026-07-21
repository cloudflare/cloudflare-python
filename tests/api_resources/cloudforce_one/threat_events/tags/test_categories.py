# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events.tags import (
    CategoryEditResponse,
    CategoryListResponse,
    CategoryCreateResponse,
    CategoryDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.tags.categories.create(
            account_id="account_id",
            name="Actor",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.tags.categories.create(
            account_id="account_id",
            name="Actor",
            description="description",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.tags.categories.with_raw_response.create(
            account_id="account_id",
            name="Actor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.tags.categories.with_streaming_response.create(
            account_id="account_id",
            name="Actor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryCreateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.tags.categories.with_raw_response.create(
                account_id="",
                name="Actor",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.tags.categories.list(
            account_id="account_id",
        )
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.tags.categories.list(
            account_id="account_id",
            search="search",
        )
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.tags.categories.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.tags.categories.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.tags.categories.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.tags.categories.delete(
            category_uuid="category_uuid",
            account_id="account_id",
        )
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.tags.categories.with_raw_response.delete(
            category_uuid="category_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.tags.categories.with_streaming_response.delete(
            category_uuid="category_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryDeleteResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.tags.categories.with_raw_response.delete(
                category_uuid="category_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_uuid` but received ''"):
            client.cloudforce_one.threat_events.tags.categories.with_raw_response.delete(
                category_uuid="",
                account_id="account_id",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.tags.categories.edit(
            category_uuid="category_uuid",
            account_id="account_id",
        )
        assert_matches_type(CategoryEditResponse, category, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.tags.categories.edit(
            category_uuid="category_uuid",
            account_id="account_id",
            description="description",
            name="name",
        )
        assert_matches_type(CategoryEditResponse, category, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.tags.categories.with_raw_response.edit(
            category_uuid="category_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryEditResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.tags.categories.with_streaming_response.edit(
            category_uuid="category_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryEditResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.tags.categories.with_raw_response.edit(
                category_uuid="category_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_uuid` but received ''"):
            client.cloudforce_one.threat_events.tags.categories.with_raw_response.edit(
                category_uuid="",
                account_id="account_id",
            )


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.tags.categories.create(
            account_id="account_id",
            name="Actor",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.tags.categories.create(
            account_id="account_id",
            name="Actor",
            description="description",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.create(
            account_id="account_id",
            name="Actor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.tags.categories.with_streaming_response.create(
            account_id="account_id",
            name="Actor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryCreateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.create(
                account_id="",
                name="Actor",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.tags.categories.list(
            account_id="account_id",
        )
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.tags.categories.list(
            account_id="account_id",
            search="search",
        )
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.tags.categories.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.tags.categories.delete(
            category_uuid="category_uuid",
            account_id="account_id",
        )
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.delete(
            category_uuid="category_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.tags.categories.with_streaming_response.delete(
            category_uuid="category_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryDeleteResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.delete(
                category_uuid="category_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_uuid` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.delete(
                category_uuid="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.tags.categories.edit(
            category_uuid="category_uuid",
            account_id="account_id",
        )
        assert_matches_type(CategoryEditResponse, category, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.tags.categories.edit(
            category_uuid="category_uuid",
            account_id="account_id",
            description="description",
            name="name",
        )
        assert_matches_type(CategoryEditResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.edit(
            category_uuid="category_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryEditResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.tags.categories.with_streaming_response.edit(
            category_uuid="category_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryEditResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.edit(
                category_uuid="category_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_uuid` but received ''"):
            await async_client.cloudforce_one.threat_events.tags.categories.with_raw_response.edit(
                category_uuid="",
                account_id="account_id",
            )
