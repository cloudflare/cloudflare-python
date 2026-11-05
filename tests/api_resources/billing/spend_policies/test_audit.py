# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.billing.spend_policies import AuditListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        audit = client.billing.spend_policies.audit.list(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[AuditListResponse], audit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        audit = client.billing.spend_policies.audit.list(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            limit=50,
            period="current_billing_cycle",
        )
        assert_matches_type(SyncSinglePage[AuditListResponse], audit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.billing.spend_policies.audit.with_raw_response.list(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = response.parse()
        assert_matches_type(SyncSinglePage[AuditListResponse], audit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.billing.spend_policies.audit.with_streaming_response.list(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = response.parse()
            assert_matches_type(SyncSinglePage[AuditListResponse], audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.billing.spend_policies.audit.with_raw_response.list(
                policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.billing.spend_policies.audit.with_raw_response.list(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAudit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        audit = await async_client.billing.spend_policies.audit.list(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[AuditListResponse], audit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audit = await async_client.billing.spend_policies.audit.list(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            limit=50,
            period="current_billing_cycle",
        )
        assert_matches_type(AsyncSinglePage[AuditListResponse], audit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.billing.spend_policies.audit.with_raw_response.list(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(AsyncSinglePage[AuditListResponse], audit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.billing.spend_policies.audit.with_streaming_response.list(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(AsyncSinglePage[AuditListResponse], audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.billing.spend_policies.audit.with_raw_response.list(
                policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.billing.spend_policies.audit.with_raw_response.list(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
