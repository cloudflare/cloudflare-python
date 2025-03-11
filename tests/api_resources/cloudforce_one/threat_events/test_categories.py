# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import (
    CategoryGetResponse,
    CategoryListResponse,
    CategoryCreateResponse,
    CategoryDeleteResponse,
    CategoryUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.categories.create(
            account_id=0,
            kill_chain=0,
            name="name",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.categories.create(
            account_id=0,
            kill_chain=0,
            name="name",
            mitre_attack=["T1234"],
            shortname="shortname",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.categories.with_raw_response.create(
            account_id=0,
            kill_chain=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.categories.with_streaming_response.create(
            account_id=0,
            kill_chain=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryCreateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.categories.update(
            category_id="categoryId",
            account_id=0,
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.categories.update(
            category_id="categoryId",
            account_id=0,
            kill_chain=0,
            mitre_attack=["T1234"],
            name="name",
            shortname="shortname",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.categories.with_raw_response.update(
            category_id="categoryId",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.categories.with_streaming_response.update(
            category_id="categoryId",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryUpdateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.cloudforce_one.threat_events.categories.with_raw_response.update(
                category_id="",
                account_id=0,
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.categories.list(
            0,
        )
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.categories.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.categories.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.categories.delete(
            category_id="categoryId",
            account_id=0,
        )
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.categories.with_raw_response.delete(
            category_id="categoryId",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.categories.with_streaming_response.delete(
            category_id="categoryId",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryDeleteResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.cloudforce_one.threat_events.categories.with_raw_response.delete(
                category_id="",
                account_id=0,
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        category = client.cloudforce_one.threat_events.categories.get(
            category_id="categoryId",
            account_id=0,
        )
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.categories.with_raw_response.get(
            category_id="categoryId",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.categories.with_streaming_response.get(
            category_id="categoryId",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryGetResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            client.cloudforce_one.threat_events.categories.with_raw_response.get(
                category_id="",
                account_id=0,
            )


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.categories.create(
            account_id=0,
            kill_chain=0,
            name="name",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.categories.create(
            account_id=0,
            kill_chain=0,
            name="name",
            mitre_attack=["T1234"],
            shortname="shortname",
        )
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.categories.with_raw_response.create(
            account_id=0,
            kill_chain=0,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryCreateResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.categories.with_streaming_response.create(
            account_id=0,
            kill_chain=0,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryCreateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.categories.update(
            category_id="categoryId",
            account_id=0,
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.categories.update(
            category_id="categoryId",
            account_id=0,
            kill_chain=0,
            mitre_attack=["T1234"],
            name="name",
            shortname="shortname",
        )
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.categories.with_raw_response.update(
            category_id="categoryId",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryUpdateResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.categories.with_streaming_response.update(
            category_id="categoryId",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryUpdateResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.cloudforce_one.threat_events.categories.with_raw_response.update(
                category_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.categories.list(
            0,
        )
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.categories.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryListResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.categories.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryListResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.categories.delete(
            category_id="categoryId",
            account_id=0,
        )
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.categories.with_raw_response.delete(
            category_id="categoryId",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryDeleteResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.categories.with_streaming_response.delete(
            category_id="categoryId",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryDeleteResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.cloudforce_one.threat_events.categories.with_raw_response.delete(
                category_id="",
                account_id=0,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.cloudforce_one.threat_events.categories.get(
            category_id="categoryId",
            account_id=0,
        )
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.categories.with_raw_response.get(
            category_id="categoryId",
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryGetResponse, category, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.categories.with_streaming_response.get(
            category_id="categoryId",
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryGetResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `category_id` but received ''"):
            await async_client.cloudforce_one.threat_events.categories.with_raw_response.get(
                category_id="",
                account_id=0,
            )
