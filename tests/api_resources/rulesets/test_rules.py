# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.rulesets import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleAccountRulesetsCreateAnAccountRulesetRuleResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rulesets import rule_update_params
from cloudflare.types.rulesets import rule_account_rulesets_create_an_account_ruleset_rule_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            id="3a03d665bac047339bb530ecb439a90d",
            action="block",
            action_parameters={
                "response": {
                    "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                    "content_type": "application/json",
                    "status_code": 400,
                }
            },
            description="Block when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            id="3a03d665bac047339bb530ecb439a90d",
            action="execute",
            action_parameters={
                "id": "4814384a9e5d4991b9815dcfc25d2f1f",
                "matched_data": {"public_key": "iGqBmyIUxuWt1rvxoAharN9FUXneUBxA/Y19PyyrEG0="},
                "overrides": {
                    "action": "log",
                    "categories": [
                        {
                            "action": "log",
                            "category": "directory-traversal",
                            "enabled": True,
                            "sensitivity_level": "default",
                        }
                    ],
                    "enabled": True,
                    "rules": [
                        {
                            "action": "log",
                            "enabled": True,
                            "id": "8ac8bc2a661e475d940980f9317f28e1",
                            "score_threshold": 0,
                            "sensitivity_level": "default",
                        }
                    ],
                    "sensitivity_level": "default",
                },
            },
            description="Execute the OWASP ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            id="3a03d665bac047339bb530ecb439a90d",
            action="skip",
            action_parameters={
                "phases": ["http_request_firewall_custom"],
                "products": ["bic"],
                "rules": {"4814384a9e5d4991b9815dcfc25d2f1f": ["8ac8bc2a661e475d940980f9317f28e1"]},
                "ruleset": "current",
                "rulesets": ["4814384a9e5d4991b9815dcfc25d2f1f"],
            },
            description="Skip the current ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_4(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.update(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_or_zone="string",
                account_or_zone_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_rulesets_create_an_account_ruleset_rule_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_rulesets_create_an_account_ruleset_rule_with_all_params_overload_1(
        self, client: Cloudflare
    ) -> None:
        rule = client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="3a03d665bac047339bb530ecb439a90d",
            action="block",
            action_parameters={
                "response": {
                    "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                    "content_type": "application/json",
                    "status_code": 400,
                }
            },
            description="Block when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_rulesets_create_an_account_ruleset_rule_overload_1(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_rulesets_create_an_account_ruleset_rule_overload_1(
        self, client: Cloudflare
    ) -> None:
        with client.rulesets.rules.with_streaming_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_rulesets_create_an_account_ruleset_rule_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_rulesets_create_an_account_ruleset_rule_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_rulesets_create_an_account_ruleset_rule_with_all_params_overload_2(
        self, client: Cloudflare
    ) -> None:
        rule = client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="3a03d665bac047339bb530ecb439a90d",
            action="execute",
            action_parameters={
                "id": "4814384a9e5d4991b9815dcfc25d2f1f",
                "matched_data": {"public_key": "iGqBmyIUxuWt1rvxoAharN9FUXneUBxA/Y19PyyrEG0="},
                "overrides": {
                    "action": "log",
                    "categories": [
                        {
                            "action": "log",
                            "category": "directory-traversal",
                            "enabled": True,
                            "sensitivity_level": "default",
                        }
                    ],
                    "enabled": True,
                    "rules": [
                        {
                            "action": "log",
                            "enabled": True,
                            "id": "8ac8bc2a661e475d940980f9317f28e1",
                            "score_threshold": 0,
                            "sensitivity_level": "default",
                        }
                    ],
                    "sensitivity_level": "default",
                },
            },
            description="Execute the OWASP ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_rulesets_create_an_account_ruleset_rule_overload_2(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_rulesets_create_an_account_ruleset_rule_overload_2(
        self, client: Cloudflare
    ) -> None:
        with client.rulesets.rules.with_streaming_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_rulesets_create_an_account_ruleset_rule_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_rulesets_create_an_account_ruleset_rule_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_rulesets_create_an_account_ruleset_rule_with_all_params_overload_3(
        self, client: Cloudflare
    ) -> None:
        rule = client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_rulesets_create_an_account_ruleset_rule_overload_3(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_rulesets_create_an_account_ruleset_rule_overload_3(
        self, client: Cloudflare
    ) -> None:
        with client.rulesets.rules.with_streaming_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_rulesets_create_an_account_ruleset_rule_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_rulesets_create_an_account_ruleset_rule_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_rulesets_create_an_account_ruleset_rule_with_all_params_overload_4(
        self, client: Cloudflare
    ) -> None:
        rule = client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="3a03d665bac047339bb530ecb439a90d",
            action="skip",
            action_parameters={
                "phases": ["http_request_firewall_custom"],
                "products": ["bic"],
                "rules": {"4814384a9e5d4991b9815dcfc25d2f1f": ["8ac8bc2a661e475d940980f9317f28e1"]},
                "ruleset": "current",
                "rulesets": ["4814384a9e5d4991b9815dcfc25d2f1f"],
            },
            description="Skip the current ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_rulesets_create_an_account_ruleset_rule_overload_4(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_rulesets_create_an_account_ruleset_rule_overload_4(
        self, client: Cloudflare
    ) -> None:
        with client.rulesets.rules.with_streaming_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_rulesets_create_an_account_ruleset_rule_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            id="3a03d665bac047339bb530ecb439a90d",
            action="block",
            action_parameters={
                "response": {
                    "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                    "content_type": "application/json",
                    "status_code": 400,
                }
            },
            description="Block when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            id="3a03d665bac047339bb530ecb439a90d",
            action="execute",
            action_parameters={
                "id": "4814384a9e5d4991b9815dcfc25d2f1f",
                "matched_data": {"public_key": "iGqBmyIUxuWt1rvxoAharN9FUXneUBxA/Y19PyyrEG0="},
                "overrides": {
                    "action": "log",
                    "categories": [
                        {
                            "action": "log",
                            "category": "directory-traversal",
                            "enabled": True,
                            "sensitivity_level": "default",
                        }
                    ],
                    "enabled": True,
                    "rules": [
                        {
                            "action": "log",
                            "enabled": True,
                            "id": "8ac8bc2a661e475d940980f9317f28e1",
                            "score_threshold": 0,
                            "sensitivity_level": "default",
                        }
                    ],
                    "sensitivity_level": "default",
                },
            },
            description="Execute the OWASP ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            id="3a03d665bac047339bb530ecb439a90d",
            action="skip",
            action_parameters={
                "phases": ["http_request_firewall_custom"],
                "products": ["bic"],
                "rules": {"4814384a9e5d4991b9815dcfc25d2f1f": ["8ac8bc2a661e475d940980f9317f28e1"]},
                "ruleset": "current",
                "rulesets": ["4814384a9e5d4991b9815dcfc25d2f1f"],
            },
            description="Skip the current ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.update(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.update(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_or_zone="string",
                account_or_zone_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_rulesets_create_an_account_ruleset_rule_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_rulesets_create_an_account_ruleset_rule_with_all_params_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="3a03d665bac047339bb530ecb439a90d",
            action="block",
            action_parameters={
                "response": {
                    "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                    "content_type": "application/json",
                    "status_code": 400,
                }
            },
            description="Block when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_rulesets_create_an_account_ruleset_rule_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_rulesets_create_an_account_ruleset_rule_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.rulesets.rules.with_streaming_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_rulesets_create_an_account_ruleset_rule_overload_1(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_rulesets_create_an_account_ruleset_rule_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_rulesets_create_an_account_ruleset_rule_with_all_params_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="3a03d665bac047339bb530ecb439a90d",
            action="execute",
            action_parameters={
                "id": "4814384a9e5d4991b9815dcfc25d2f1f",
                "matched_data": {"public_key": "iGqBmyIUxuWt1rvxoAharN9FUXneUBxA/Y19PyyrEG0="},
                "overrides": {
                    "action": "log",
                    "categories": [
                        {
                            "action": "log",
                            "category": "directory-traversal",
                            "enabled": True,
                            "sensitivity_level": "default",
                        }
                    ],
                    "enabled": True,
                    "rules": [
                        {
                            "action": "log",
                            "enabled": True,
                            "id": "8ac8bc2a661e475d940980f9317f28e1",
                            "score_threshold": 0,
                            "sensitivity_level": "default",
                        }
                    ],
                    "sensitivity_level": "default",
                },
            },
            description="Execute the OWASP ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_rulesets_create_an_account_ruleset_rule_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_rulesets_create_an_account_ruleset_rule_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.rulesets.rules.with_streaming_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_rulesets_create_an_account_ruleset_rule_overload_2(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_rulesets_create_an_account_ruleset_rule_overload_3(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_rulesets_create_an_account_ruleset_rule_with_all_params_overload_3(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_rulesets_create_an_account_ruleset_rule_overload_3(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_rulesets_create_an_account_ruleset_rule_overload_3(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.rulesets.rules.with_streaming_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_rulesets_create_an_account_ruleset_rule_overload_3(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_rulesets_create_an_account_ruleset_rule_overload_4(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_rulesets_create_an_account_ruleset_rule_with_all_params_overload_4(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.rulesets.rules.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="3a03d665bac047339bb530ecb439a90d",
            action="skip",
            action_parameters={
                "phases": ["http_request_firewall_custom"],
                "products": ["bic"],
                "rules": {"4814384a9e5d4991b9815dcfc25d2f1f": ["8ac8bc2a661e475d940980f9317f28e1"]},
                "ruleset": "current",
                "rulesets": ["4814384a9e5d4991b9815dcfc25d2f1f"],
            },
            description="Skip the current ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_rulesets_create_an_account_ruleset_rule_overload_4(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_rulesets_create_an_account_ruleset_rule_overload_4(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.rulesets.rules.with_streaming_response.account_rulesets_create_an_account_ruleset_rule(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleAccountRulesetsCreateAnAccountRulesetRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_rulesets_create_an_account_ruleset_rule_overload_4(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.account_rulesets_create_an_account_ruleset_rule(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )
