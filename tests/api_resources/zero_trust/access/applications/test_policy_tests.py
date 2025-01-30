# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.access.applications import (
    PolicyTestGetResponse,
    PolicyTestCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicyTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        policy_test = client.zero_trust.access.applications.policy_tests.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PolicyTestCreateResponse], policy_test, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        policy_test = client.zero_trust.access.applications.policy_tests.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            policies=[
                {
                    "decision": "allow",
                    "include": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "name": "Allow devs",
                    "approval_groups": [
                        {
                            "approvals_needed": 1,
                            "email_addresses": ["test1@cloudflare.com", "test2@cloudflare.com"],
                            "email_list_uuid": "email_list_uuid",
                        },
                        {
                            "approvals_needed": 3,
                            "email_addresses": ["test@cloudflare.com", "test2@cloudflare.com"],
                            "email_list_uuid": "597147a1-976b-4ef2-9af0-81d5d007fc34",
                        },
                    ],
                    "approval_required": True,
                    "exclude": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "isolation_required": False,
                    "purpose_justification_prompt": "Please enter a justification for entering this protected domain.",
                    "purpose_justification_required": True,
                    "require": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "session_duration": "24h",
                }
            ],
        )
        assert_matches_type(Optional[PolicyTestCreateResponse], policy_test, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.policy_tests.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_test = response.parse()
        assert_matches_type(Optional[PolicyTestCreateResponse], policy_test, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.policy_tests.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_test = response.parse()
            assert_matches_type(Optional[PolicyTestCreateResponse], policy_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.applications.policy_tests.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        policy_test = client.zero_trust.access.applications.policy_tests.get(
            policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PolicyTestGetResponse], policy_test, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        policy_test = client.zero_trust.access.applications.policy_tests.get(
            policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
        )
        assert_matches_type(Optional[PolicyTestGetResponse], policy_test, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.policy_tests.with_raw_response.get(
            policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_test = response.parse()
        assert_matches_type(Optional[PolicyTestGetResponse], policy_test, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.policy_tests.with_streaming_response.get(
            policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_test = response.parse()
            assert_matches_type(Optional[PolicyTestGetResponse], policy_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.applications.policy_tests.with_raw_response.get(
                policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_test_id` but received ''"):
            client.zero_trust.access.applications.policy_tests.with_raw_response.get(
                policy_test_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPolicyTests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        policy_test = await async_client.zero_trust.access.applications.policy_tests.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PolicyTestCreateResponse], policy_test, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy_test = await async_client.zero_trust.access.applications.policy_tests.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            policies=[
                {
                    "decision": "allow",
                    "include": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "name": "Allow devs",
                    "approval_groups": [
                        {
                            "approvals_needed": 1,
                            "email_addresses": ["test1@cloudflare.com", "test2@cloudflare.com"],
                            "email_list_uuid": "email_list_uuid",
                        },
                        {
                            "approvals_needed": 3,
                            "email_addresses": ["test@cloudflare.com", "test2@cloudflare.com"],
                            "email_list_uuid": "597147a1-976b-4ef2-9af0-81d5d007fc34",
                        },
                    ],
                    "approval_required": True,
                    "exclude": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "isolation_required": False,
                    "purpose_justification_prompt": "Please enter a justification for entering this protected domain.",
                    "purpose_justification_required": True,
                    "require": [{"group": {"id": "aa0a4aab-672b-4bdb-bc33-a59f1130a11f"}}],
                    "session_duration": "24h",
                }
            ],
        )
        assert_matches_type(Optional[PolicyTestCreateResponse], policy_test, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.policy_tests.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_test = await response.parse()
        assert_matches_type(Optional[PolicyTestCreateResponse], policy_test, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.policy_tests.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_test = await response.parse()
            assert_matches_type(Optional[PolicyTestCreateResponse], policy_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.applications.policy_tests.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        policy_test = await async_client.zero_trust.access.applications.policy_tests.get(
            policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PolicyTestGetResponse], policy_test, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy_test = await async_client.zero_trust.access.applications.policy_tests.get(
            policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
        )
        assert_matches_type(Optional[PolicyTestGetResponse], policy_test, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.policy_tests.with_raw_response.get(
            policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy_test = await response.parse()
        assert_matches_type(Optional[PolicyTestGetResponse], policy_test, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.policy_tests.with_streaming_response.get(
            policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy_test = await response.parse()
            assert_matches_type(Optional[PolicyTestGetResponse], policy_test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.applications.policy_tests.with_raw_response.get(
                policy_test_id="f1a8b3c9d4e5f6789a0b1c2d3e4f5678a9b0c1d2e3f4a5b67890c1d2e3f4b5a6",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_test_id` but received ''"):
            await async_client.zero_trust.access.applications.policy_tests.with_raw_response.get(
                policy_test_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
