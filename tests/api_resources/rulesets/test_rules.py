# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import Ruleset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_3(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_4(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.delete(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.delete(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit_overload_1(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit_overload_1(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit_overload_2(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit_overload_2(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit_overload_3(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit_overload_3(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit_overload_4(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit_overload_4(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.delete(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.delete(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            ref="my_ref",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Ruleset, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Ruleset, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )
