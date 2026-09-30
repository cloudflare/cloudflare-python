# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_signals.articles import SkillOutputGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSkillOutputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        skill_output = client.cloudforce_one.threat_signals.articles.skill_outputs.get(
            skill_id="skill_id",
            account_id="account_id",
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SkillOutputGetResponse, skill_output, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.articles.skill_outputs.with_raw_response.get(
            skill_id="skill_id",
            account_id="account_id",
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_output = response.parse()
        assert_matches_type(SkillOutputGetResponse, skill_output, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.articles.skill_outputs.with_streaming_response.get(
            skill_id="skill_id",
            account_id="account_id",
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_output = response.parse()
            assert_matches_type(SkillOutputGetResponse, skill_output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.articles.skill_outputs.with_raw_response.get(
                skill_id="skill_id",
                account_id="",
                article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `article_id` but received ''"):
            client.cloudforce_one.threat_signals.articles.skill_outputs.with_raw_response.get(
                skill_id="skill_id",
                account_id="account_id",
                article_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            client.cloudforce_one.threat_signals.articles.skill_outputs.with_raw_response.get(
                skill_id="",
                account_id="account_id",
                article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSkillOutputs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        skill_output = await async_client.cloudforce_one.threat_signals.articles.skill_outputs.get(
            skill_id="skill_id",
            account_id="account_id",
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SkillOutputGetResponse, skill_output, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.articles.skill_outputs.with_raw_response.get(
            skill_id="skill_id",
            account_id="account_id",
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        skill_output = await response.parse()
        assert_matches_type(SkillOutputGetResponse, skill_output, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.articles.skill_outputs.with_streaming_response.get(
            skill_id="skill_id",
            account_id="account_id",
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            skill_output = await response.parse()
            assert_matches_type(SkillOutputGetResponse, skill_output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.articles.skill_outputs.with_raw_response.get(
                skill_id="skill_id",
                account_id="",
                article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `article_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.articles.skill_outputs.with_raw_response.get(
                skill_id="skill_id",
                account_id="account_id",
                article_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `skill_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.articles.skill_outputs.with_raw_response.get(
                skill_id="",
                account_id="account_id",
                article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
