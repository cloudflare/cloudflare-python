# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.casb.posture.finding_types import (
    RemediationTypeListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRemediationTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        remediation_type = client.zero_trust.casb.posture.finding_types.remediation_types.list(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(SyncV4PagePaginationArray[RemediationTypeListResponse], remediation_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        remediation_type = client.zero_trust.casb.posture.finding_types.remediation_types.list(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            cursor="cursor",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=0,
            per_page=0,
        )
        assert_matches_type(SyncV4PagePaginationArray[RemediationTypeListResponse], remediation_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.finding_types.remediation_types.with_raw_response.list(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation_type = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[RemediationTypeListResponse], remediation_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.finding_types.remediation_types.with_streaming_response.list(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation_type = response.parse()
            assert_matches_type(
                SyncV4PagePaginationArray[RemediationTypeListResponse], remediation_type, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.remediation_types.with_raw_response.list(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.remediation_types.with_raw_response.list(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )


class TestAsyncRemediationTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        remediation_type = await async_client.zero_trust.casb.posture.finding_types.remediation_types.list(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[RemediationTypeListResponse], remediation_type, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        remediation_type = await async_client.zero_trust.casb.posture.finding_types.remediation_types.list(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            cursor="cursor",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page=0,
            per_page=0,
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[RemediationTypeListResponse], remediation_type, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.finding_types.remediation_types.with_raw_response.list(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remediation_type = await response.parse()
        assert_matches_type(
            AsyncV4PagePaginationArray[RemediationTypeListResponse], remediation_type, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.finding_types.remediation_types.with_streaming_response.list(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remediation_type = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[RemediationTypeListResponse], remediation_type, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.remediation_types.with_raw_response.list(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.remediation_types.with_raw_response.list(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )
