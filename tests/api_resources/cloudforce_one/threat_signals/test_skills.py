# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePagination, AsyncV4PagePagination
from cloudflare.types.cloudforce_one.threat_signals import (
    SkillGetResponse,
    SkillEditResponse,
    SkillListResponse,
    SkillCreateResponse,
    SkillDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSkills:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        skill = client.cloudforce_one.threat_signals.skills.create(
            account_id="account_id",
            name="x",
            output_schema="x",
            prompt="x",
            type="summary",
        )
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.skills.with_raw_response.create(
            account_id="account_id",
            name="x",
            output_schema="x",
            prompt="x",
            type="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.skills.with_streaming_response.create(
            account_id="account_id",
            name="x",
            output_schema="x",
            prompt="x",
            type="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillCreateResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.with_raw_response.create(
                account_id="",
                name="x",
                output_schema="x",
                prompt="x",
                type="summary",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        skill = client.cloudforce_one.threat_signals.skills.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePagination[SkillListResponse], skill, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        skill = client.cloudforce_one.threat_signals.skills.list(
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePagination[SkillListResponse], skill, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.skills.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SyncV4PagePagination[SkillListResponse], skill, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.skills.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SyncV4PagePagination[SkillListResponse], skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        skill = client.cloudforce_one.threat_signals.skills.delete(
            skill_id="skill_id",
            account_id="account_id",
        )
        assert_matches_type(SkillDeleteResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.skills.with_raw_response.delete(
            skill_id="skill_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillDeleteResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.skills.with_streaming_response.delete(
            skill_id="skill_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillDeleteResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.with_raw_response.delete(
                skill_id="skill_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.with_raw_response.delete(
                skill_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        skill = client.cloudforce_one.threat_signals.skills.edit(
            skill_id="skill_id",
            account_id="account_id",
        )
        assert_matches_type(SkillEditResponse, skill, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        skill = client.cloudforce_one.threat_signals.skills.edit(
            skill_id="skill_id",
            account_id="account_id",
            config="config",
            is_active=True,
            name="x",
            output_schema="x",
            prompt="x",
        )
        assert_matches_type(SkillEditResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.skills.with_raw_response.edit(
            skill_id="skill_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillEditResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.skills.with_streaming_response.edit(
            skill_id="skill_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillEditResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.with_raw_response.edit(
                skill_id="skill_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.with_raw_response.edit(
                skill_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        skill = client.cloudforce_one.threat_signals.skills.get(
            skill_id="skill_id",
            account_id="account_id",
        )
        assert_matches_type(SkillGetResponse, skill, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.skills.with_raw_response.get(
            skill_id="skill_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = response.parse()
        assert_matches_type(SkillGetResponse, skill, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.skills.with_streaming_response.get(
            skill_id="skill_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = response.parse()
            assert_matches_type(SkillGetResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.with_raw_response.get(
                skill_id="skill_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.cloudforce_one.threat_signals.skills.with_raw_response.get(
                skill_id="",
                account_id="account_id",
            )


class TestAsyncSkills:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        skill = await async_client.cloudforce_one.threat_signals.skills.create(
            account_id="account_id",
            name="x",
            output_schema="x",
            prompt="x",
            type="summary",
        )
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.skills.with_raw_response.create(
            account_id="account_id",
            name="x",
            output_schema="x",
            prompt="x",
            type="summary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillCreateResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.skills.with_streaming_response.create(
            account_id="account_id",
            name="x",
            output_schema="x",
            prompt="x",
            type="summary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillCreateResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.with_raw_response.create(
                account_id="",
                name="x",
                output_schema="x",
                prompt="x",
                type="summary",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        skill = await async_client.cloudforce_one.threat_signals.skills.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePagination[SkillListResponse], skill, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        skill = await async_client.cloudforce_one.threat_signals.skills.list(
            account_id="account_id",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePagination[SkillListResponse], skill, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.skills.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(AsyncV4PagePagination[SkillListResponse], skill, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.skills.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(AsyncV4PagePagination[SkillListResponse], skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        skill = await async_client.cloudforce_one.threat_signals.skills.delete(
            skill_id="skill_id",
            account_id="account_id",
        )
        assert_matches_type(SkillDeleteResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.skills.with_raw_response.delete(
            skill_id="skill_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillDeleteResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.skills.with_streaming_response.delete(
            skill_id="skill_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillDeleteResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.with_raw_response.delete(
                skill_id="skill_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.with_raw_response.delete(
                skill_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        skill = await async_client.cloudforce_one.threat_signals.skills.edit(
            skill_id="skill_id",
            account_id="account_id",
        )
        assert_matches_type(SkillEditResponse, skill, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        skill = await async_client.cloudforce_one.threat_signals.skills.edit(
            skill_id="skill_id",
            account_id="account_id",
            config="config",
            is_active=True,
            name="x",
            output_schema="x",
            prompt="x",
        )
        assert_matches_type(SkillEditResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.skills.with_raw_response.edit(
            skill_id="skill_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillEditResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.skills.with_streaming_response.edit(
            skill_id="skill_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillEditResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.with_raw_response.edit(
                skill_id="skill_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.with_raw_response.edit(
                skill_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        skill = await async_client.cloudforce_one.threat_signals.skills.get(
            skill_id="skill_id",
            account_id="account_id",
        )
        assert_matches_type(SkillGetResponse, skill, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.skills.with_raw_response.get(
            skill_id="skill_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill = await response.parse()
        assert_matches_type(SkillGetResponse, skill, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.skills.with_streaming_response.get(
            skill_id="skill_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill = await response.parse()
            assert_matches_type(SkillGetResponse, skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.with_raw_response.get(
                skill_id="skill_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.skills.with_raw_response.get(
                skill_id="",
                account_id="account_id",
            )
