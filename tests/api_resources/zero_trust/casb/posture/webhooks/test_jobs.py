# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.casb.posture.webhooks import JobCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        job = client.zero_trust.casb.posture.webhooks.jobs.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["770e8400-e29b-41d4-a716-446655440002", "660e8400-e29b-41d4-a716-446655440001"],
            webhook_ids=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440001"],
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.webhooks.jobs.with_raw_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["770e8400-e29b-41d4-a716-446655440002", "660e8400-e29b-41d4-a716-446655440001"],
            webhook_ids=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440001"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.webhooks.jobs.with_streaming_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["770e8400-e29b-41d4-a716-446655440002", "660e8400-e29b-41d4-a716-446655440001"],
            webhook_ids=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440001"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.jobs.with_raw_response.create(
                account_id="",
                finding_instance_ids=["770e8400-e29b-41d4-a716-446655440002", "660e8400-e29b-41d4-a716-446655440001"],
                webhook_ids=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440001"],
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.zero_trust.casb.posture.webhooks.jobs.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["770e8400-e29b-41d4-a716-446655440002", "660e8400-e29b-41d4-a716-446655440001"],
            webhook_ids=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440001"],
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.webhooks.jobs.with_raw_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["770e8400-e29b-41d4-a716-446655440002", "660e8400-e29b-41d4-a716-446655440001"],
            webhook_ids=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440001"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.webhooks.jobs.with_streaming_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["770e8400-e29b-41d4-a716-446655440002", "660e8400-e29b-41d4-a716-446655440001"],
            webhook_ids=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440001"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.jobs.with_raw_response.create(
                account_id="",
                finding_instance_ids=["770e8400-e29b-41d4-a716-446655440002", "660e8400-e29b-41d4-a716-446655440001"],
                webhook_ids=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440001"],
            )
