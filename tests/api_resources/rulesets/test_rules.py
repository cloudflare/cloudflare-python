# File generated from our OpenAPI spec by Stainless.

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

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="string",
            zone_id="string",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="string",
            zone_id="string",
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
            account_id="string",
            zone_id="string",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                zone_id="string",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="string",
                zone_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="string",
                zone_id="string",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.delete(
                "",
                account_id="string",
                zone_id="string",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        rule = client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rulesets.rules.with_raw_response.edit(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
        )
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleCreateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.create(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleCreateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.create(
                "",
                account_id="string",
                zone_id="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="string",
            zone_id="string",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.delete(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="string",
            zone_id="string",
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
            account_id="string",
            zone_id="string",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                zone_id="string",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="string",
                zone_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="string",
                zone_id="string",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.delete(
                "",
                account_id="string",
                zone_id="string",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rulesets.rules.edit(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            position={"before": "da5e8e506c8e7877fe06cdf4c41add54"},
        )
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.rules.with_raw_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEditResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.rules.with_streaming_response.edit(
            "3a03d665bac047339bb530ecb439a90d",
            account_id="abf9b32d38c5f572afde3336ec0ce302",
            ruleset_id="2f2feab2026849078ba485f918791bdc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEditResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "3a03d665bac047339bb530ecb439a90d",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rulesets.rules.with_raw_response.edit(
                "",
                account_id="abf9b32d38c5f572afde3336ec0ce302",
                ruleset_id="2f2feab2026849078ba485f918791bdc",
            )
