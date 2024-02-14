# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.access.apps import (
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyDeleteResponse,
    PolicyAccessPoliciesCreateAnAccessPolicyResponse,
    PolicyAccessPoliciesListAccessPoliciesResponse,
    PolicyGetResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access.apps import policy_create_params
from cloudflare.types.access.apps import policy_update_params
from cloudflare.types.access.apps import policy_access_policies_create_an_access_policy_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        policy = client.access.apps.policies.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(PolicyCreateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        policy = client.access.apps.policies.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
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
        assert_matches_type(PolicyCreateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.access.apps.policies.with_raw_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyCreateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.access.apps.policies.with_streaming_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyCreateResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.policies.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.policies.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.apps.policies.with_raw_response.create(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        policy = client.access.apps.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(PolicyUpdateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        policy = client.access.apps.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
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
        assert_matches_type(PolicyUpdateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.apps.policies.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyUpdateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.apps.policies.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyUpdateResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            client.access.apps.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.apps.policies.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        policy = client.access.apps.policies.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.access.apps.policies.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.access.apps.policies.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            client.access.apps.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.apps.policies.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_policies_create_an_access_policy(self, client: Cloudflare) -> None:
        policy = client.access.apps.policies.access_policies_create_an_access_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(PolicyAccessPoliciesCreateAnAccessPolicyResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_access_policies_create_an_access_policy_with_all_params(self, client: Cloudflare) -> None:
        policy = client.access.apps.policies.access_policies_create_an_access_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
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
        assert_matches_type(PolicyAccessPoliciesCreateAnAccessPolicyResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_policies_create_an_access_policy(self, client: Cloudflare) -> None:
        response = client.access.apps.policies.with_raw_response.access_policies_create_an_access_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyAccessPoliciesCreateAnAccessPolicyResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_policies_create_an_access_policy(self, client: Cloudflare) -> None:
        with client.access.apps.policies.with_streaming_response.access_policies_create_an_access_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyAccessPoliciesCreateAnAccessPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_policies_create_an_access_policy(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.policies.with_raw_response.access_policies_create_an_access_policy(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.policies.with_raw_response.access_policies_create_an_access_policy(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.apps.policies.with_raw_response.access_policies_create_an_access_policy(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_policies_list_access_policies(self, client: Cloudflare) -> None:
        policy = client.access.apps.policies.access_policies_list_access_policies(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PolicyAccessPoliciesListAccessPoliciesResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_policies_list_access_policies(self, client: Cloudflare) -> None:
        response = client.access.apps.policies.with_raw_response.access_policies_list_access_policies(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(Optional[PolicyAccessPoliciesListAccessPoliciesResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_policies_list_access_policies(self, client: Cloudflare) -> None:
        with client.access.apps.policies.with_streaming_response.access_policies_list_access_policies(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(Optional[PolicyAccessPoliciesListAccessPoliciesResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_policies_list_access_policies(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.policies.with_raw_response.access_policies_list_access_policies(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.policies.with_raw_response.access_policies_list_access_policies(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.apps.policies.with_raw_response.access_policies_list_access_policies(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        policy = client.access.apps.policies.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(PolicyGetResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.access.apps.policies.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = response.parse()
        assert_matches_type(PolicyGetResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.access.apps.policies.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = response.parse()
            assert_matches_type(PolicyGetResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            client.access.apps.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.apps.policies.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )


class TestAsyncPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.access.apps.policies.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(PolicyCreateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.access.apps.policies.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
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
        assert_matches_type(PolicyCreateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.policies.with_raw_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyCreateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.policies.with_streaming_response.create(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyCreateResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.policies.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.policies.with_raw_response.create(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.apps.policies.with_raw_response.create(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.access.apps.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(PolicyUpdateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.access.apps.policies.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
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
        assert_matches_type(PolicyUpdateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.policies.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyUpdateResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.policies.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyUpdateResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            await async_client.access.apps.policies.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.apps.policies.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.access.apps.policies.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.policies.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.policies.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyDeleteResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            await async_client.access.apps.policies.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.apps.policies.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_policies_create_an_access_policy(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.access.apps.policies.access_policies_create_an_access_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )
        assert_matches_type(PolicyAccessPoliciesCreateAnAccessPolicyResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_policies_create_an_access_policy_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        policy = await async_client.access.apps.policies.access_policies_create_an_access_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
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
        assert_matches_type(PolicyAccessPoliciesCreateAnAccessPolicyResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_policies_create_an_access_policy(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.policies.with_raw_response.access_policies_create_an_access_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyAccessPoliciesCreateAnAccessPolicyResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_policies_create_an_access_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.apps.policies.with_streaming_response.access_policies_create_an_access_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            decision="allow",
            include=[
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
                {"email": {"email": "test@example.com"}},
            ],
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyAccessPoliciesCreateAnAccessPolicyResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_policies_create_an_access_policy(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.policies.with_raw_response.access_policies_create_an_access_policy(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.policies.with_raw_response.access_policies_create_an_access_policy(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.apps.policies.with_raw_response.access_policies_create_an_access_policy(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                decision="allow",
                include=[
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                    {"email": {"email": "test@example.com"}},
                ],
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_policies_list_access_policies(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.access.apps.policies.access_policies_list_access_policies(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PolicyAccessPoliciesListAccessPoliciesResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_policies_list_access_policies(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.policies.with_raw_response.access_policies_list_access_policies(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(Optional[PolicyAccessPoliciesListAccessPoliciesResponse], policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_policies_list_access_policies(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.policies.with_streaming_response.access_policies_list_access_policies(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(Optional[PolicyAccessPoliciesListAccessPoliciesResponse], policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_policies_list_access_policies(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.policies.with_raw_response.access_policies_list_access_policies(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.policies.with_raw_response.access_policies_list_access_policies(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.apps.policies.with_raw_response.access_policies_list_access_policies(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        policy = await async_client.access.apps.policies.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(PolicyGetResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.policies.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        policy = await response.parse()
        assert_matches_type(PolicyGetResponse, policy, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.apps.policies.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            policy = await response.parse()
            assert_matches_type(PolicyGetResponse, policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.apps.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.apps.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid1` but received ''"):
            await async_client.access.apps.policies.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.apps.policies.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                uuid1="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )
