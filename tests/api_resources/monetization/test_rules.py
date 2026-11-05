# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.monetization import (
    MonetizationRule,
    MonetizationRuleCollection,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.monetization.rules.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            rules=[
                {
                    "address": "0x1234567890abcdef1234567890abcdef12345678===",
                    "expression": '(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
                    "price": "250000",
                    "scheme": "exact",
                }
            ],
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.monetization.rules.with_raw_response.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            rules=[
                {
                    "address": "0x1234567890abcdef1234567890abcdef12345678===",
                    "expression": '(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
                    "price": "250000",
                    "scheme": "exact",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.monetization.rules.with_streaming_response.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            rules=[
                {
                    "address": "0x1234567890abcdef1234567890abcdef12345678===",
                    "expression": '(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
                    "price": "250000",
                    "scheme": "exact",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.monetization.rules.with_raw_response.update(
                zone_id="",
                rules=[
                    {
                        "address": "0x1234567890abcdef1234567890abcdef12345678===",
                        "expression": '(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
                        "price": "250000",
                        "scheme": "exact",
                    }
                ],
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.monetization.rules.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.monetization.rules.with_raw_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.monetization.rules.with_streaming_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.monetization.rules.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    def test_method_delete_rule(self, client: Cloudflare) -> None:
        rule = client.monetization.rules.delete_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_raw_response_delete_rule(self, client: Cloudflare) -> None:
        response = client.monetization.rules.with_raw_response.delete_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_streaming_response_delete_rule(self, client: Cloudflare) -> None:
        with client.monetization.rules.with_streaming_response.delete_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_rule(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.monetization.rules.with_raw_response.delete_rule(
                rule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.monetization.rules.with_raw_response.delete_rule(
                rule_id="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )

    @parametrize
    def test_method_edit_rule(self, client: Cloudflare) -> None:
        rule = client.monetization.rules.edit_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_method_edit_rule_with_all_params(self, client: Cloudflare) -> None:
        rule = client.monetization.rules.edit_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            address="0x1234567890abcdef1234567890abcdef12345678===",
            description="Premium API endpoint",
            enabled=True,
            expression='(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
            price="250000",
            scheme="exact",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_raw_response_edit_rule(self, client: Cloudflare) -> None:
        response = client.monetization.rules.with_raw_response.edit_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_streaming_response_edit_rule(self, client: Cloudflare) -> None:
        with client.monetization.rules.with_streaming_response.edit_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_rule(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.monetization.rules.with_raw_response.edit_rule(
                rule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.monetization.rules.with_raw_response.edit_rule(
                rule_id="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.monetization.rules.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.monetization.rules.with_raw_response.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.monetization.rules.with_streaming_response.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.monetization.rules.with_raw_response.get(
                zone_id="",
            )

    @parametrize
    def test_method_get_rule(self, client: Cloudflare) -> None:
        rule = client.monetization.rules.get_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRule, rule, path=["response"])

    @parametrize
    def test_raw_response_get_rule(self, client: Cloudflare) -> None:
        response = client.monetization.rules.with_raw_response.get_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(MonetizationRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_get_rule(self, client: Cloudflare) -> None:
        with client.monetization.rules.with_streaming_response.get_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(MonetizationRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_rule(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.monetization.rules.with_raw_response.get_rule(
                rule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.monetization.rules.with_raw_response.get_rule(
                rule_id="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.monetization.rules.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            rules=[
                {
                    "address": "0x1234567890abcdef1234567890abcdef12345678===",
                    "expression": '(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
                    "price": "250000",
                    "scheme": "exact",
                }
            ],
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.monetization.rules.with_raw_response.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            rules=[
                {
                    "address": "0x1234567890abcdef1234567890abcdef12345678===",
                    "expression": '(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
                    "price": "250000",
                    "scheme": "exact",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.monetization.rules.with_streaming_response.update(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            rules=[
                {
                    "address": "0x1234567890abcdef1234567890abcdef12345678===",
                    "expression": '(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
                    "price": "250000",
                    "scheme": "exact",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.monetization.rules.with_raw_response.update(
                zone_id="",
                rules=[
                    {
                        "address": "0x1234567890abcdef1234567890abcdef12345678===",
                        "expression": '(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
                        "price": "250000",
                        "scheme": "exact",
                    }
                ],
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.monetization.rules.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.monetization.rules.with_raw_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.monetization.rules.with_streaming_response.delete(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.monetization.rules.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    async def test_method_delete_rule(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.monetization.rules.delete_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_raw_response_delete_rule(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.monetization.rules.with_raw_response.delete_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete_rule(self, async_client: AsyncCloudflare) -> None:
        async with async_client.monetization.rules.with_streaming_response.delete_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_rule(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.monetization.rules.with_raw_response.delete_rule(
                rule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.monetization.rules.with_raw_response.delete_rule(
                rule_id="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )

    @parametrize
    async def test_method_edit_rule(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.monetization.rules.edit_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_method_edit_rule_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.monetization.rules.edit_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            address="0x1234567890abcdef1234567890abcdef12345678===",
            description="Premium API endpoint",
            enabled=True,
            expression='(http.request.uri.path eq "/premium" and http.request.method in {"GET" "POST"})',
            price="250000",
            scheme="exact",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_raw_response_edit_rule(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.monetization.rules.with_raw_response.edit_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_streaming_response_edit_rule(self, async_client: AsyncCloudflare) -> None:
        async with async_client.monetization.rules.with_streaming_response.edit_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_rule(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.monetization.rules.with_raw_response.edit_rule(
                rule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.monetization.rules.with_raw_response.edit_rule(
                rule_id="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.monetization.rules.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.monetization.rules.with_raw_response.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.monetization.rules.with_streaming_response.get(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(MonetizationRuleCollection, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.monetization.rules.with_raw_response.get(
                zone_id="",
            )

    @parametrize
    async def test_method_get_rule(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.monetization.rules.get_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(MonetizationRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_get_rule(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.monetization.rules.with_raw_response.get_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(MonetizationRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_get_rule(self, async_client: AsyncCloudflare) -> None:
        async with async_client.monetization.rules.with_streaming_response.get_rule(
            rule_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(MonetizationRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_rule(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.monetization.rules.with_raw_response.get_rule(
                rule_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.monetization.rules.with_raw_response.get_rule(
                rule_id="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )
