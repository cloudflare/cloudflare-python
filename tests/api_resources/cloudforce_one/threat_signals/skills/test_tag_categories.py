# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_signals.skills import (
    TagCategoryGetResponse,
    TagCategoryUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTagCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        tag_category = client.cloudforce_one.threat_signals.skills.tag_categories.update(
            skill_id="default-tagging-skill",
            account_id="account_id",
            category_uuids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(TagCategoryUpdateResponse, tag_category, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.skills.tag_categories.with_raw_response.update(
            skill_id="default-tagging-skill",
            account_id="account_id",
            category_uuids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_category = response.parse()
        assert_matches_type(TagCategoryUpdateResponse, tag_category, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.skills.tag_categories.with_streaming_response.update(
            skill_id="default-tagging-skill",
            account_id="account_id",
            category_uuids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_category = response.parse()
            assert_matches_type(TagCategoryUpdateResponse, tag_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.tag_categories.with_raw_response.update(
                skill_id="default-tagging-skill",
                account_id="",
                category_uuids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        tag_category = client.cloudforce_one.threat_signals.skills.tag_categories.get(
            skill_id="default-tagging-skill",
            account_id="account_id",
        )
        assert_matches_type(TagCategoryGetResponse, tag_category, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.skills.tag_categories.with_raw_response.get(
            skill_id="default-tagging-skill",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_category = response.parse()
        assert_matches_type(TagCategoryGetResponse, tag_category, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.skills.tag_categories.with_streaming_response.get(
            skill_id="default-tagging-skill",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_category = response.parse()
            assert_matches_type(TagCategoryGetResponse, tag_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.tag_categories.with_raw_response.get(
                skill_id="default-tagging-skill",
                account_id="",
            )


class TestAsyncTagCategories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        tag_category = await async_client.cloudforce_one.threat_signals.skills.tag_categories.update(
            skill_id="default-tagging-skill",
            account_id="account_id",
            category_uuids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(TagCategoryUpdateResponse, tag_category, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.skills.tag_categories.with_raw_response.update(
            skill_id="default-tagging-skill",
            account_id="account_id",
            category_uuids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_category = await response.parse()
        assert_matches_type(TagCategoryUpdateResponse, tag_category, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.skills.tag_categories.with_streaming_response.update(
            skill_id="default-tagging-skill",
            account_id="account_id",
            category_uuids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_category = await response.parse()
            assert_matches_type(TagCategoryUpdateResponse, tag_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.tag_categories.with_raw_response.update(
                skill_id="default-tagging-skill",
                account_id="",
                category_uuids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        tag_category = await async_client.cloudforce_one.threat_signals.skills.tag_categories.get(
            skill_id="default-tagging-skill",
            account_id="account_id",
        )
        assert_matches_type(TagCategoryGetResponse, tag_category, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.skills.tag_categories.with_raw_response.get(
            skill_id="default-tagging-skill",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag_category = await response.parse()
        assert_matches_type(TagCategoryGetResponse, tag_category, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.skills.tag_categories.with_streaming_response.get(
            skill_id="default-tagging-skill",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag_category = await response.parse()
            assert_matches_type(TagCategoryGetResponse, tag_category, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.tag_categories.with_raw_response.get(
                skill_id="default-tagging-skill",
                account_id="",
            )
