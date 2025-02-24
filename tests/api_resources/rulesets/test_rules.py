# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rulesets import (
    RuleEditResponse,
    RuleCreateResponse,
    RuleDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
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
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="challenge",
            action_parameters={},
            description="Issue an Interactive Challenge if the visitor had not solved an Interactive Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="compress_response",
            action_parameters={"algorithms": [{"name": "none"}]},
            description="Disable compression when address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="execute",
            action_parameters={
                "id": "4814384a9e5d4991b9815dcfc25d2f1f",
                "matched_data": {"public_key": "iGqBmyIUxuWt1rvxoAharN9FUXneUBxA/Y19PyyrEG0="},
                "overrides": {
                    "action": "log",
                    "categories": [
                        {
                            "category": "directory-traversal",
                            "action": "log",
                            "enabled": True,
                            "sensitivity_level": "default",
                        }
                    ],
                    "enabled": True,
                    "rules": [
                        {
                            "id": "8ac8bc2a661e475d940980f9317f28e1",
                            "action": "log",
                            "enabled": True,
                            "score_threshold": 0,
                            "sensitivity_level": "default",
                        }
                    ],
                    "sensitivity_level": "default",
                },
            },
            description="Execute the OWASP ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_5(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="js_challenge",
            action_parameters={},
            description="Issue a non-interactive Javascript Challenge if the visitor had not solved a Interactive Challenge, Managed Challenge, or Javascript Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_6(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_6(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_7(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="managed_challenge",
            action_parameters={},
            description="Issue a Managed Challenge if the visitor had not solved a Managed Challenge or Interactive Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_7(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_8(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="redirect",
            action_parameters={
                "from_list": {
                    "key": "http.request.full_uri",
                    "name": "list1",
                },
                "from_value": {
                    "preserve_query_string": True,
                    "status_code": 301,
                    "target_url": {"value": "x"},
                },
            },
            description="Redirect when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_8(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_9(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="rewrite",
            action_parameters={
                "headers": {
                    "client-http-version": {
                        "expression": "http.request.version",
                        "operation": "set",
                    }
                },
                "uri": {
                    "path": {"value": "/images"},
                    "query": {"value": "/images"},
                },
            },
            description="Add a header when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_9(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_9(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_10(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="route",
            action_parameters={
                "host_header": "static.example.com",
                "origin": {
                    "host": "static.example.com",
                    "port": 1,
                },
                "sni": {"value": "static.example.com"},
            },
            description="Select origin server when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_10(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_10(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_11(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_11(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="score",
            action_parameters={"increment": 3},
            description="Increment score when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_11(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_11(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_12(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_12(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="serve_error",
            action_parameters={
                "content": '{"error": "1xxx error occurred"}\n',
                "content_type": "application/json",
                "status_code": 500,
            },
            description="Serve a JSON response to api users on error",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_12(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_12(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_13(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_13(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="set_config",
            action_parameters={
                "automatic_https_rewrites": True,
                "autominify": {
                    "css": True,
                    "html": True,
                    "js": True,
                },
                "bic": True,
                "disable_apps": True,
                "disable_rum": True,
                "disable_zaraz": True,
                "email_obfuscation": True,
                "fonts": True,
                "hotlink_protection": True,
                "mirage": True,
                "opportunistic_encryption": True,
                "polish": "off",
                "rocket_loader": True,
                "security_level": "off",
                "server_side_excludes": True,
                "ssl": "off",
                "sxg": True,
            },
            description="Disable Zaraz when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_13(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_13(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_14(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_14(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="skip",
            action_parameters={
                "phases": ["ddos_l4"],
                "products": ["bic"],
                "rules": {"4814384a9e5d4991b9815dcfc25d2f1f": ["8ac8bc2a661e475d940980f9317f28e1"]},
                "ruleset": "current",
                "rulesets": ["4814384a9e5d4991b9815dcfc25d2f1f"],
            },
            description="Skip the current ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_14(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_14(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_15(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_15(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="set_cache_settings",
            action_parameters={
                "additional_cacheable_ports": [0],
                "browser_ttl": {
                    "mode": "respect_origin",
                    "default": 0,
                },
                "cache": True,
                "cache_key": {
                    "cache_by_device_type": True,
                    "cache_deception_armor": True,
                    "custom_key": {
                        "cookie": {
                            "check_presence": ["string"],
                            "include": ["string"],
                        },
                        "header": {
                            "check_presence": ["string"],
                            "contains": {"foo": ["string"]},
                            "exclude_origin": True,
                            "include": ["string"],
                        },
                        "host": {"resolved": True},
                        "query_string": {"include": {"list": ["foo", "bar"]}},
                        "user": {
                            "device_type": True,
                            "geo": True,
                            "lang": True,
                        },
                    },
                    "ignore_query_strings_order": True,
                },
                "cache_reserve": {
                    "eligible": True,
                    "minimum_file_size": 0,
                },
                "edge_ttl": {
                    "default": 0,
                    "mode": "respect_origin",
                    "status_code_ttl": [
                        {
                            "value": 0,
                            "status_code_range": {
                                "from": 0,
                                "to": 0,
                            },
                            "status_code_value": 0,
                        }
                    ],
                },
                "origin_cache_control": True,
                "origin_error_page_passthru": True,
                "read_timeout": 900,
                "respect_strong_etags": True,
                "serve_stale": {"disable_stale_while_updating": True},
            },
            description="Set cache settings when the hostname  address is not example.com",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_15(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_15(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_15(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_16(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_16(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log_custom_field",
            action_parameters={
                "cookie_fields": [{"name": "cookie_name_1"}],
                "raw_response_fields": [
                    {
                        "name": "http_response_header_name_1_in_lower_case",
                        "preserve_duplicates": True,
                    }
                ],
                "request_fields": [{"name": "http_request_header_name_1_in_lower_case"}],
                "response_fields": [
                    {
                        "name": "http_response_header_name_1_in_lower_case",
                        "preserve_duplicates": True,
                    }
                ],
                "transformed_request_fields": [{"name": "http_request_header_name_1_in_lower_case"}],
            },
            description="Log custom field when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_16(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_16(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_16(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_17(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_17(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="ddos_dynamic",
            action_parameters={},
            description="Performs a specific action according to a set of internal guidelines defined by Cloudflare.",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_17(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_17(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_17(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_overload_18(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params_overload_18(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="force_connection_close",
            action_parameters={},
            description="Closes ongoing HTTP connections. This action does not block a request, but it forces the client to reconnect. For HTTP/2 and HTTP/3 connections, the connection will be closed even if it breaks other requests running on the same connection.",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create_overload_18(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create_overload_18(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create_overload_18(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.delete(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.delete(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.delete(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.delete(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.delete(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.delete(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_1(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
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
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_1(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_1(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_2(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="challenge",
            action_parameters={},
            description="Issue an Interactive Challenge if the visitor had not solved an Interactive Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_2(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_2(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_3(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="compress_response",
            action_parameters={"algorithms": [{"name": "none"}]},
            description="Disable compression when address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_3(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_3(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_4(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="execute",
            action_parameters={
                "id": "4814384a9e5d4991b9815dcfc25d2f1f",
                "matched_data": {"public_key": "iGqBmyIUxuWt1rvxoAharN9FUXneUBxA/Y19PyyrEG0="},
                "overrides": {
                    "action": "log",
                    "categories": [
                        {
                            "category": "directory-traversal",
                            "action": "log",
                            "enabled": True,
                            "sensitivity_level": "default",
                        }
                    ],
                    "enabled": True,
                    "rules": [
                        {
                            "id": "8ac8bc2a661e475d940980f9317f28e1",
                            "action": "log",
                            "enabled": True,
                            "score_threshold": 0,
                            "sensitivity_level": "default",
                        }
                    ],
                    "sensitivity_level": "default",
                },
            },
            description="Execute the OWASP ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_4(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_4(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_5(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_5(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="js_challenge",
            action_parameters={},
            description="Issue a non-interactive Javascript Challenge if the visitor had not solved a Interactive Challenge, Managed Challenge, or Javascript Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_5(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_5(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_6(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_6(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_6(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_6(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_7(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_7(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="managed_challenge",
            action_parameters={},
            description="Issue a Managed Challenge if the visitor had not solved a Managed Challenge or Interactive Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_7(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_7(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_8(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_8(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="redirect",
            action_parameters={
                "from_list": {
                    "key": "http.request.full_uri",
                    "name": "list1",
                },
                "from_value": {
                    "preserve_query_string": True,
                    "status_code": 301,
                    "target_url": {"value": "x"},
                },
            },
            description="Redirect when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_8(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_8(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_9(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_9(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="rewrite",
            action_parameters={
                "headers": {
                    "client-http-version": {
                        "expression": "http.request.version",
                        "operation": "set",
                    }
                },
                "uri": {
                    "path": {"value": "/images"},
                    "query": {"value": "/images"},
                },
            },
            description="Add a header when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_9(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_9(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_10(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_10(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="route",
            action_parameters={
                "host_header": "static.example.com",
                "origin": {
                    "host": "static.example.com",
                    "port": 1,
                },
                "sni": {"value": "static.example.com"},
            },
            description="Select origin server when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_10(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_10(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_11(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_11(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="score",
            action_parameters={"increment": 3},
            description="Increment score when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_11(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_11(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_12(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_12(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="serve_error",
            action_parameters={
                "content": '{"error": "1xxx error occurred"}\n',
                "content_type": "application/json",
                "status_code": 500,
            },
            description="Serve a JSON response to api users on error",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_12(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_12(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_13(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_13(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="set_config",
            action_parameters={
                "automatic_https_rewrites": True,
                "autominify": {
                    "css": True,
                    "html": True,
                    "js": True,
                },
                "bic": True,
                "disable_apps": True,
                "disable_rum": True,
                "disable_zaraz": True,
                "email_obfuscation": True,
                "fonts": True,
                "hotlink_protection": True,
                "mirage": True,
                "opportunistic_encryption": True,
                "polish": "off",
                "rocket_loader": True,
                "security_level": "off",
                "server_side_excludes": True,
                "ssl": "off",
                "sxg": True,
            },
            description="Disable Zaraz when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_13(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_13(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_14(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_14(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="skip",
            action_parameters={
                "phases": ["ddos_l4"],
                "products": ["bic"],
                "rules": {"4814384a9e5d4991b9815dcfc25d2f1f": ["8ac8bc2a661e475d940980f9317f28e1"]},
                "ruleset": "current",
                "rulesets": ["4814384a9e5d4991b9815dcfc25d2f1f"],
            },
            description="Skip the current ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_14(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_14(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_15(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_15(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="set_cache_settings",
            action_parameters={
                "additional_cacheable_ports": [0],
                "browser_ttl": {
                    "mode": "respect_origin",
                    "default": 0,
                },
                "cache": True,
                "cache_key": {
                    "cache_by_device_type": True,
                    "cache_deception_armor": True,
                    "custom_key": {
                        "cookie": {
                            "check_presence": ["string"],
                            "include": ["string"],
                        },
                        "header": {
                            "check_presence": ["string"],
                            "contains": {"foo": ["string"]},
                            "exclude_origin": True,
                            "include": ["string"],
                        },
                        "host": {"resolved": True},
                        "query_string": {"include": {"list": ["foo", "bar"]}},
                        "user": {
                            "device_type": True,
                            "geo": True,
                            "lang": True,
                        },
                    },
                    "ignore_query_strings_order": True,
                },
                "cache_reserve": {
                    "eligible": True,
                    "minimum_file_size": 0,
                },
                "edge_ttl": {
                    "default": 0,
                    "mode": "respect_origin",
                    "status_code_ttl": [
                        {
                            "value": 0,
                            "status_code_range": {
                                "from": 0,
                                "to": 0,
                            },
                            "status_code_value": 0,
                        }
                    ],
                },
                "origin_cache_control": True,
                "origin_error_page_passthru": True,
                "read_timeout": 900,
                "respect_strong_etags": True,
                "serve_stale": {"disable_stale_while_updating": True},
            },
            description="Set cache settings when the hostname  address is not example.com",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_15(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_15(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_15(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_16(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_16(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log_custom_field",
            action_parameters={
                "cookie_fields": [{"name": "cookie_name_1"}],
                "raw_response_fields": [
                    {
                        "name": "http_response_header_name_1_in_lower_case",
                        "preserve_duplicates": True,
                    }
                ],
                "request_fields": [{"name": "http_request_header_name_1_in_lower_case"}],
                "response_fields": [
                    {
                        "name": "http_response_header_name_1_in_lower_case",
                        "preserve_duplicates": True,
                    }
                ],
                "transformed_request_fields": [{"name": "http_request_header_name_1_in_lower_case"}],
            },
            description="Log custom field when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_16(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_16(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_16(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_17(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_17(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="ddos_dynamic",
            action_parameters={},
            description="Performs a specific action according to a set of internal guidelines defined by Cloudflare.",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_17(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_17(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_17(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_overload_18(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params_overload_18(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="force_connection_close",
            action_parameters={},
            description="Closes ongoing HTTP connections. This action does not block a request, but it forces the client to reconnect. For HTTP/2 and HTTP/3 connections, the connection will be closed even if it breaks other requests running on the same connection.",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit_overload_18(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit_overload_18(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit_overload_18(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
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
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="challenge",
            action_parameters={},
            description="Issue an Interactive Challenge if the visitor had not solved an Interactive Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="compress_response",
            action_parameters={"algorithms": [{"name": "none"}]},
            description="Disable compression when address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="execute",
            action_parameters={
                "id": "4814384a9e5d4991b9815dcfc25d2f1f",
                "matched_data": {"public_key": "iGqBmyIUxuWt1rvxoAharN9FUXneUBxA/Y19PyyrEG0="},
                "overrides": {
                    "action": "log",
                    "categories": [
                        {
                            "category": "directory-traversal",
                            "action": "log",
                            "enabled": True,
                            "sensitivity_level": "default",
                        }
                    ],
                    "enabled": True,
                    "rules": [
                        {
                            "id": "8ac8bc2a661e475d940980f9317f28e1",
                            "action": "log",
                            "enabled": True,
                            "score_threshold": 0,
                            "sensitivity_level": "default",
                        }
                    ],
                    "sensitivity_level": "default",
                },
            },
            description="Execute the OWASP ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="js_challenge",
            action_parameters={},
            description="Issue a non-interactive Javascript Challenge if the visitor had not solved a Interactive Challenge, Managed Challenge, or Javascript Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="managed_challenge",
            action_parameters={},
            description="Issue a Managed Challenge if the visitor had not solved a Managed Challenge or Interactive Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="redirect",
            action_parameters={
                "from_list": {
                    "key": "http.request.full_uri",
                    "name": "list1",
                },
                "from_value": {
                    "preserve_query_string": True,
                    "status_code": 301,
                    "target_url": {"value": "x"},
                },
            },
            description="Redirect when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="rewrite",
            action_parameters={
                "headers": {
                    "client-http-version": {
                        "expression": "http.request.version",
                        "operation": "set",
                    }
                },
                "uri": {
                    "path": {"value": "/images"},
                    "query": {"value": "/images"},
                },
            },
            description="Add a header when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="route",
            action_parameters={
                "host_header": "static.example.com",
                "origin": {
                    "host": "static.example.com",
                    "port": 1,
                },
                "sni": {"value": "static.example.com"},
            },
            description="Select origin server when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="score",
            action_parameters={"increment": 3},
            description="Increment score when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="serve_error",
            action_parameters={
                "content": '{"error": "1xxx error occurred"}\n',
                "content_type": "application/json",
                "status_code": 500,
            },
            description="Serve a JSON response to api users on error",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="set_config",
            action_parameters={
                "automatic_https_rewrites": True,
                "autominify": {
                    "css": True,
                    "html": True,
                    "js": True,
                },
                "bic": True,
                "disable_apps": True,
                "disable_rum": True,
                "disable_zaraz": True,
                "email_obfuscation": True,
                "fonts": True,
                "hotlink_protection": True,
                "mirage": True,
                "opportunistic_encryption": True,
                "polish": "off",
                "rocket_loader": True,
                "security_level": "off",
                "server_side_excludes": True,
                "ssl": "off",
                "sxg": True,
            },
            description="Disable Zaraz when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="skip",
            action_parameters={
                "phases": ["ddos_l4"],
                "products": ["bic"],
                "rules": {"4814384a9e5d4991b9815dcfc25d2f1f": ["8ac8bc2a661e475d940980f9317f28e1"]},
                "ruleset": "current",
                "rulesets": ["4814384a9e5d4991b9815dcfc25d2f1f"],
            },
            description="Skip the current ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="set_cache_settings",
            action_parameters={
                "additional_cacheable_ports": [0],
                "browser_ttl": {
                    "mode": "respect_origin",
                    "default": 0,
                },
                "cache": True,
                "cache_key": {
                    "cache_by_device_type": True,
                    "cache_deception_armor": True,
                    "custom_key": {
                        "cookie": {
                            "check_presence": ["string"],
                            "include": ["string"],
                        },
                        "header": {
                            "check_presence": ["string"],
                            "contains": {"foo": ["string"]},
                            "exclude_origin": True,
                            "include": ["string"],
                        },
                        "host": {"resolved": True},
                        "query_string": {"include": {"list": ["foo", "bar"]}},
                        "user": {
                            "device_type": True,
                            "geo": True,
                            "lang": True,
                        },
                    },
                    "ignore_query_strings_order": True,
                },
                "cache_reserve": {
                    "eligible": True,
                    "minimum_file_size": 0,
                },
                "edge_ttl": {
                    "default": 0,
                    "mode": "respect_origin",
                    "status_code_ttl": [
                        {
                            "value": 0,
                            "status_code_range": {
                                "from": 0,
                                "to": 0,
                            },
                            "status_code_value": 0,
                        }
                    ],
                },
                "origin_cache_control": True,
                "origin_error_page_passthru": True,
                "read_timeout": 900,
                "respect_strong_etags": True,
                "serve_stale": {"disable_stale_while_updating": True},
            },
            description="Set cache settings when the hostname  address is not example.com",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log_custom_field",
            action_parameters={
                "cookie_fields": [{"name": "cookie_name_1"}],
                "raw_response_fields": [
                    {
                        "name": "http_response_header_name_1_in_lower_case",
                        "preserve_duplicates": True,
                    }
                ],
                "request_fields": [{"name": "http_request_header_name_1_in_lower_case"}],
                "response_fields": [
                    {
                        "name": "http_response_header_name_1_in_lower_case",
                        "preserve_duplicates": True,
                    }
                ],
                "transformed_request_fields": [{"name": "http_request_header_name_1_in_lower_case"}],
            },
            description="Log custom field when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="ddos_dynamic",
            action_parameters={},
            description="Performs a specific action according to a set of internal guidelines defined by Cloudflare.",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="force_connection_close",
            action_parameters={},
            description="Closes ongoing HTTP connections. This action does not block a request, but it forces the client to reconnect. For HTTP/2 and HTTP/3 connections, the connection will be closed even if it breaks other requests running on the same connection.",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.create(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.delete(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.delete(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.delete(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.delete(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.delete(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.delete(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
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
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="challenge",
            action_parameters={},
            description="Issue an Interactive Challenge if the visitor had not solved an Interactive Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="compress_response",
            action_parameters={"algorithms": [{"name": "none"}]},
            description="Disable compression when address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="execute",
            action_parameters={
                "id": "4814384a9e5d4991b9815dcfc25d2f1f",
                "matched_data": {"public_key": "iGqBmyIUxuWt1rvxoAharN9FUXneUBxA/Y19PyyrEG0="},
                "overrides": {
                    "action": "log",
                    "categories": [
                        {
                            "category": "directory-traversal",
                            "action": "log",
                            "enabled": True,
                            "sensitivity_level": "default",
                        }
                    ],
                    "enabled": True,
                    "rules": [
                        {
                            "id": "8ac8bc2a661e475d940980f9317f28e1",
                            "action": "log",
                            "enabled": True,
                            "score_threshold": 0,
                            "sensitivity_level": "default",
                        }
                    ],
                    "sensitivity_level": "default",
                },
            },
            description="Execute the OWASP ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="js_challenge",
            action_parameters={},
            description="Issue a non-interactive Javascript Challenge if the visitor had not solved a Interactive Challenge, Managed Challenge, or Javascript Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log",
            action_parameters={},
            description="Log when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="managed_challenge",
            action_parameters={},
            description="Issue a Managed Challenge if the visitor had not solved a Managed Challenge or Interactive Challenge prior to the request when the address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="redirect",
            action_parameters={
                "from_list": {
                    "key": "http.request.full_uri",
                    "name": "list1",
                },
                "from_value": {
                    "preserve_query_string": True,
                    "status_code": 301,
                    "target_url": {"value": "x"},
                },
            },
            description="Redirect when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="rewrite",
            action_parameters={
                "headers": {
                    "client-http-version": {
                        "expression": "http.request.version",
                        "operation": "set",
                    }
                },
                "uri": {
                    "path": {"value": "/images"},
                    "query": {"value": "/images"},
                },
            },
            description="Add a header when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="route",
            action_parameters={
                "host_header": "static.example.com",
                "origin": {
                    "host": "static.example.com",
                    "port": 1,
                },
                "sni": {"value": "static.example.com"},
            },
            description="Select origin server when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="score",
            action_parameters={"increment": 3},
            description="Increment score when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="serve_error",
            action_parameters={
                "content": '{"error": "1xxx error occurred"}\n',
                "content_type": "application/json",
                "status_code": 500,
            },
            description="Serve a JSON response to api users on error",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="set_config",
            action_parameters={
                "automatic_https_rewrites": True,
                "autominify": {
                    "css": True,
                    "html": True,
                    "js": True,
                },
                "bic": True,
                "disable_apps": True,
                "disable_rum": True,
                "disable_zaraz": True,
                "email_obfuscation": True,
                "fonts": True,
                "hotlink_protection": True,
                "mirage": True,
                "opportunistic_encryption": True,
                "polish": "off",
                "rocket_loader": True,
                "security_level": "off",
                "server_side_excludes": True,
                "ssl": "off",
                "sxg": True,
            },
            description="Disable Zaraz when IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="skip",
            action_parameters={
                "phases": ["ddos_l4"],
                "products": ["bic"],
                "rules": {"4814384a9e5d4991b9815dcfc25d2f1f": ["8ac8bc2a661e475d940980f9317f28e1"]},
                "ruleset": "current",
                "rulesets": ["4814384a9e5d4991b9815dcfc25d2f1f"],
            },
            description="Skip the current ruleset when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="set_cache_settings",
            action_parameters={
                "additional_cacheable_ports": [0],
                "browser_ttl": {
                    "mode": "respect_origin",
                    "default": 0,
                },
                "cache": True,
                "cache_key": {
                    "cache_by_device_type": True,
                    "cache_deception_armor": True,
                    "custom_key": {
                        "cookie": {
                            "check_presence": ["string"],
                            "include": ["string"],
                        },
                        "header": {
                            "check_presence": ["string"],
                            "contains": {"foo": ["string"]},
                            "exclude_origin": True,
                            "include": ["string"],
                        },
                        "host": {"resolved": True},
                        "query_string": {"include": {"list": ["foo", "bar"]}},
                        "user": {
                            "device_type": True,
                            "geo": True,
                            "lang": True,
                        },
                    },
                    "ignore_query_strings_order": True,
                },
                "cache_reserve": {
                    "eligible": True,
                    "minimum_file_size": 0,
                },
                "edge_ttl": {
                    "default": 0,
                    "mode": "respect_origin",
                    "status_code_ttl": [
                        {
                            "value": 0,
                            "status_code_range": {
                                "from": 0,
                                "to": 0,
                            },
                            "status_code_value": 0,
                        }
                    ],
                },
                "origin_cache_control": True,
                "origin_error_page_passthru": True,
                "read_timeout": 900,
                "respect_strong_etags": True,
                "serve_stale": {"disable_stale_while_updating": True},
            },
            description="Set cache settings when the hostname  address is not example.com",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_15(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="log_custom_field",
            action_parameters={
                "cookie_fields": [{"name": "cookie_name_1"}],
                "raw_response_fields": [
                    {
                        "name": "http_response_header_name_1_in_lower_case",
                        "preserve_duplicates": True,
                    }
                ],
                "request_fields": [{"name": "http_request_header_name_1_in_lower_case"}],
                "response_fields": [
                    {
                        "name": "http_response_header_name_1_in_lower_case",
                        "preserve_duplicates": True,
                    }
                ],
                "transformed_request_fields": [{"name": "http_request_header_name_1_in_lower_case"}],
            },
            description="Log custom field when the IP address is not 1.1.1.1",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_16(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="ddos_dynamic",
            action_parameters={},
            description="Performs a specific action according to a set of internal guidelines defined by Cloudflare.",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_17(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            id="3a03d665bac047339bb530ecb439a90d",
            action="force_connection_close",
            action_parameters={},
            description="Closes ongoing HTTP connections. This action does not block a request, but it forces the client to reconnect. For HTTP/2 and HTTP/3 connections, the connection will be closed even if it breaks other requests running on the same connection.",
            enabled=True,
            exposed_credential_check={
                "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
            },
            expression="ip.src ne 1.1.1.1",
            logging={"enabled": True},
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
            ratelimit={
                "characteristics": ["ip.src"],
                "period": 10,
                "counting_expression": 'http.request.body.raw eq "abcd"',
                "mitigation_timeout": 600,
                "requests_per_period": 1000,
                "requests_to_origin": True,
                "score_per_period": 400,
                "score_response_header_name": "my-score",
            },
            ref="my_ref",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            rule_id="3a03d665bac047339bb530ecb439a90d",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit_overload_18(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.rules.with_raw_response.edit(
                rule_id="3a03d665bac047339bb530ecb439a90d",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )
