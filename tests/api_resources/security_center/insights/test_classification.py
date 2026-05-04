# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.security_center.insights import ClassificationUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        classification = client.security_center.insights.classification.update(
            issue_id="issue_id",
            account_id="account_id",
        )
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        classification = client.security_center.insights.classification.update(
            issue_id="issue_id",
            account_id="account_id",
            classification="false_positive",
            rationale="rationale",
        )
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.security_center.insights.classification.with_raw_response.update(
            issue_id="issue_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = response.parse()
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.security_center.insights.classification.with_streaming_response.update(
            issue_id="issue_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = response.parse()
            assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            client.security_center.insights.classification.with_raw_response.update(
                issue_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.classification.with_raw_response.update(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.security_center.insights.classification.with_raw_response.update(
                issue_id="issue_id",
                account_id="account_id",
            )


class TestAsyncClassification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        classification = await async_client.security_center.insights.classification.update(
            issue_id="issue_id",
            account_id="account_id",
        )
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        classification = await async_client.security_center.insights.classification.update(
            issue_id="issue_id",
            account_id="account_id",
            classification="false_positive",
            rationale="rationale",
        )
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.security_center.insights.classification.with_raw_response.update(
            issue_id="issue_id",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classification = await response.parse()
        assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.security_center.insights.classification.with_streaming_response.update(
            issue_id="issue_id",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classification = await response.parse()
            assert_matches_type(ClassificationUpdateResponse, classification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `issue_id` but received ''"):
            await async_client.security_center.insights.classification.with_raw_response.update(
                issue_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.classification.with_raw_response.update(
                issue_id="issue_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.security_center.insights.classification.with_raw_response.update(
                issue_id="issue_id",
                account_id="account_id",
            )
