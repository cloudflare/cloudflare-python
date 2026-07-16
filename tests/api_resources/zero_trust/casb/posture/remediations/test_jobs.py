# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.casb.posture.remediations import (
    JobListResponse,
    JobCreateResponse,
    JobExportResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        job = client.zero_trust.casb.posture.remediations.jobs.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            remediation_type_id="5a7d9e2f-1b3c-4d5e-8f6a-7b8c9d0e1f2a",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.remediations.jobs.with_raw_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            remediation_type_id="5a7d9e2f-1b3c-4d5e-8f6a-7b8c9d0e1f2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.remediations.jobs.with_streaming_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            remediation_type_id="5a7d9e2f-1b3c-4d5e-8f6a-7b8c9d0e1f2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.remediations.jobs.with_raw_response.create(
                account_id="",
                finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                remediation_type_id="5a7d9e2f-1b3c-4d5e-8f6a-7b8c9d0e1f2a",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        job = client.zero_trust.casb.posture.remediations.jobs.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(SyncV4PagePaginationArray[JobListResponse], job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        job = client.zero_trust.casb.posture.remediations.jobs.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            cursor="cursor",
            direction="asc",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="created_at",
            page=0,
            per_page=0,
            search="search",
            status="pending",
            triggered_by_actor=["user"],
        )
        assert_matches_type(SyncV4PagePaginationArray[JobListResponse], job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.remediations.jobs.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[JobListResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.remediations.jobs.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[JobListResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.remediations.jobs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_export(self, client: Cloudflare) -> None:
        job = client.zero_trust.casb.posture.remediations.jobs.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[JobExportResponse], job, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Cloudflare) -> None:
        job = client.zero_trust.casb.posture.remediations.jobs.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            integration_id=["55d7337e-1d0a-49fc-9826-925ba40df035"],
            max_updated_at=parse_datetime("2025-01-01T00:00:00Z"),
            min_updated_at=parse_datetime("2024-01-01T00:00:00Z"),
            orders=[
                {
                    "direction": "asc",
                    "name": "last_updated_at",
                }
            ],
            search="public access",
            status=["pending", "completed"],
        )
        assert_matches_type(Optional[JobExportResponse], job, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.remediations.jobs.with_raw_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[JobExportResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.remediations.jobs.with_streaming_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[JobExportResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.remediations.jobs.with_raw_response.export(
                account_id="",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.zero_trust.casb.posture.remediations.jobs.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            remediation_type_id="5a7d9e2f-1b3c-4d5e-8f6a-7b8c9d0e1f2a",
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.remediations.jobs.with_raw_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            remediation_type_id="5a7d9e2f-1b3c-4d5e-8f6a-7b8c9d0e1f2a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.remediations.jobs.with_streaming_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            remediation_type_id="5a7d9e2f-1b3c-4d5e-8f6a-7b8c9d0e1f2a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.remediations.jobs.with_raw_response.create(
                account_id="",
                finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                remediation_type_id="5a7d9e2f-1b3c-4d5e-8f6a-7b8c9d0e1f2a",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.zero_trust.casb.posture.remediations.jobs.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(AsyncV4PagePaginationArray[JobListResponse], job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.zero_trust.casb.posture.remediations.jobs.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            cursor="cursor",
            direction="asc",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="created_at",
            page=0,
            per_page=0,
            search="search",
            status="pending",
            triggered_by_actor=["user"],
        )
        assert_matches_type(AsyncV4PagePaginationArray[JobListResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.remediations.jobs.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[JobListResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.remediations.jobs.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[JobListResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.remediations.jobs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_export(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.zero_trust.casb.posture.remediations.jobs.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[JobExportResponse], job, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncCloudflare) -> None:
        job = await async_client.zero_trust.casb.posture.remediations.jobs.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            integration_id=["55d7337e-1d0a-49fc-9826-925ba40df035"],
            max_updated_at=parse_datetime("2025-01-01T00:00:00Z"),
            min_updated_at=parse_datetime("2024-01-01T00:00:00Z"),
            orders=[
                {
                    "direction": "asc",
                    "name": "last_updated_at",
                }
            ],
            search="public access",
            status=["pending", "completed"],
        )
        assert_matches_type(Optional[JobExportResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.remediations.jobs.with_raw_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[JobExportResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.remediations.jobs.with_streaming_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[JobExportResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.remediations.jobs.with_raw_response.export(
                account_id="",
            )
