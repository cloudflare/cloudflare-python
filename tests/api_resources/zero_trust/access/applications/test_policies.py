# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.access.applications import (
    ZeroTrustPolicies,
    PolicyListResponse,
    PolicyDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
            approval_groups=[
                {
                    "approvals_needed": 1,
                    "email_addresses": ["test1@cloudflare.com", "test2@cloudflare.com"],
                    "email_list_uuid": "string",
                },
                {
                    "approvals_needed": 3,
                    "email_addresses": ["test@cloudflare.com", "test2@cloudflare.com"],
                    "email_list_uuid": "597147a1-976b-4ef2-9af0-81d5d007fc34",
                },
            ],
            approval_required=True,
            exclude=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            isolation_required=False,
            precedence=0,
            purpose_justification_prompt="Please enter a justification for entering this protected domain.",
            purpose_justification_required=True,
            require=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            session_duration="24h",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.policies.with_raw_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.policies.with_streaming_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.create(
                "",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
            approval_groups=[
                {
                    "approvals_needed": 1,
                    "email_addresses": ["test1@cloudflare.com", "test2@cloudflare.com"],
                    "email_list_uuid": "string",
                },
                {
                    "approvals_needed": 3,
                    "email_addresses": ["test@cloudflare.com", "test2@cloudflare.com"],
                    "email_list_uuid": "597147a1-976b-4ef2-9af0-81d5d007fc34",
                },
            ],
            approval_required=True,
            exclude=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            isolation_required=False,
            precedence=0,
            purpose_justification_prompt="Please enter a justification for entering this protected domain.",
            purpose_justification_required=True,
            require=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            session_duration="24h",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.policies.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.policies.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.update(
                "",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Optional[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Optional[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.policies.with_raw_response.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.policies.with_streaming_response.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[PolicyListResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.list(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.list(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.list(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.policies.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.policies.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.delete(
                "",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        policy = client.zero_trust.access.applications.policies.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.applications.policies.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.applications.policies.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.get(
                "",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zero_trust.access.applications.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
            approval_groups=[
                {
                    "approvals_needed": 1,
                    "email_addresses": ["test1@cloudflare.com", "test2@cloudflare.com"],
                    "email_list_uuid": "string",
                },
                {
                    "approvals_needed": 3,
                    "email_addresses": ["test@cloudflare.com", "test2@cloudflare.com"],
                    "email_list_uuid": "597147a1-976b-4ef2-9af0-81d5d007fc34",
                },
            ],
            approval_required=True,
            exclude=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            isolation_required=False,
            precedence=0,
            purpose_justification_prompt="Please enter a justification for entering this protected domain.",
            purpose_justification_required=True,
            require=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            session_duration="24h",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.policies.with_raw_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.policies.with_streaming_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.create(
                "",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
            approval_groups=[
                {
                    "approvals_needed": 1,
                    "email_addresses": ["test1@cloudflare.com", "test2@cloudflare.com"],
                    "email_list_uuid": "string",
                },
                {
                    "approvals_needed": 3,
                    "email_addresses": ["test@cloudflare.com", "test2@cloudflare.com"],
                    "email_list_uuid": "597147a1-976b-4ef2-9af0-81d5d007fc34",
                },
            ],
            approval_required=True,
            exclude=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            isolation_required=False,
            precedence=0,
            purpose_justification_prompt="Please enter a justification for entering this protected domain.",
            purpose_justification_required=True,
            require=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            session_duration="24h",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.policies.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.policies.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.update(
                "",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Optional[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Optional[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.policies.with_raw_response.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyListResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.policies.with_streaming_response.list(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[PolicyListResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.list(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.list(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.list(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.policies.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.policies.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.delete(
                "",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.zero_trust.access.applications.policies.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.applications.policies.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.applications.policies.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(ZeroTrustPolicies, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.get(
                "",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zero_trust.access.applications.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="string",
                zone_id="",
            )
