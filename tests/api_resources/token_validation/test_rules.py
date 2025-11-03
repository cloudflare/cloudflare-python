# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.token_validation import (
    TokenValidationRule,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.token_validation.rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            selector={},
            title="Example Token Validation Rule",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        rule = client.token_validation.rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            selector={
                "exclude": [
                    {"operation_ids": ["f9c5615e-fe15-48ce-bec6-cfc1946f1bec", "56828eae-035a-4396-ba07-51c66d680a04"]}
                ],
                "include": [{"host": ["v1.example.com", "v2.example.com"]}],
            },
            title="Example Token Validation Rule",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.token_validation.rules.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            selector={},
            title="Example Token Validation Rule",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.token_validation.rules.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            selector={},
            title="Example Token Validation Rule",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(TokenValidationRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.rules.with_raw_response.create(
                zone_id="",
                action="log",
                description="Long description for Token Validation Rule",
                enabled=True,
                expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
                selector={},
                title="Example Token Validation Rule",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.token_validation.rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[TokenValidationRule], rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        rule = client.token_validation.rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            action="log",
            enabled=True,
            host="www.example.com",
            hostname="www.example.com",
            page=1,
            per_page=5,
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            token_configuration=["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"],
        )
        assert_matches_type(SyncV4PagePaginationArray[TokenValidationRule], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.token_validation.rules.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[TokenValidationRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.token_validation.rules.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[TokenValidationRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.rules.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.token_validation.rules.delete(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.token_validation.rules.with_raw_response.delete(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(object, rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.token_validation.rules.with_streaming_response.delete(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(object, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.rules.with_raw_response.delete(
                rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.token_validation.rules.with_raw_response.delete(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        rule = client.token_validation.rules.edit(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        rule = client.token_validation.rules.edit(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            position={"index": 2},
            selector={
                "exclude": [
                    {"operation_ids": ["f9c5615e-fe15-48ce-bec6-cfc1946f1bec", "56828eae-035a-4396-ba07-51c66d680a04"]}
                ],
                "include": [{"host": ["v1.example.com", "v2.example.com"]}],
            },
            title="Example Token Validation Rule",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.token_validation.rules.with_raw_response.edit(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.token_validation.rules.with_streaming_response.edit(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(TokenValidationRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.rules.with_raw_response.edit(
                rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.token_validation.rules.with_raw_response.edit(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.token_validation.rules.get(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.token_validation.rules.with_raw_response.get(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.token_validation.rules.with_streaming_response.get(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(TokenValidationRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.token_validation.rules.with_raw_response.get(
                rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.token_validation.rules.with_raw_response.get(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.token_validation.rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            selector={},
            title="Example Token Validation Rule",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.token_validation.rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            selector={
                "exclude": [
                    {"operation_ids": ["f9c5615e-fe15-48ce-bec6-cfc1946f1bec", "56828eae-035a-4396-ba07-51c66d680a04"]}
                ],
                "include": [{"host": ["v1.example.com", "v2.example.com"]}],
            },
            title="Example Token Validation Rule",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.rules.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            selector={},
            title="Example Token Validation Rule",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.rules.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            selector={},
            title="Example Token Validation Rule",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(TokenValidationRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.rules.with_raw_response.create(
                zone_id="",
                action="log",
                description="Long description for Token Validation Rule",
                enabled=True,
                expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
                selector={},
                title="Example Token Validation Rule",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.token_validation.rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[TokenValidationRule], rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.token_validation.rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            action="log",
            enabled=True,
            host="www.example.com",
            hostname="www.example.com",
            page=1,
            per_page=5,
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            token_configuration=["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"],
        )
        assert_matches_type(AsyncV4PagePaginationArray[TokenValidationRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.rules.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[TokenValidationRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.rules.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[TokenValidationRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.rules.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.token_validation.rules.delete(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.rules.with_raw_response.delete(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(object, rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.rules.with_streaming_response.delete(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(object, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.rules.with_raw_response.delete(
                rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.token_validation.rules.with_raw_response.delete(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.token_validation.rules.edit(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.token_validation.rules.edit(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="log",
            description="Long description for Token Validation Rule",
            enabled=True,
            expression='is_jwt_valid("52973293-cb04-4a97-8f55-e7d2ad1107dd") or is_jwt_valid("46eab8d1-6376-45e3-968f-2c649d77d423")',
            position={"index": 2},
            selector={
                "exclude": [
                    {"operation_ids": ["f9c5615e-fe15-48ce-bec6-cfc1946f1bec", "56828eae-035a-4396-ba07-51c66d680a04"]}
                ],
                "include": [{"host": ["v1.example.com", "v2.example.com"]}],
            },
            title="Example Token Validation Rule",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.rules.with_raw_response.edit(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.rules.with_streaming_response.edit(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(TokenValidationRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.rules.with_raw_response.edit(
                rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.token_validation.rules.with_raw_response.edit(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.token_validation.rules.get(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.token_validation.rules.with_raw_response.get(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(TokenValidationRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.token_validation.rules.with_streaming_response.get(
            rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(TokenValidationRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.token_validation.rules.with_raw_response.get(
                rule_id="4a7ee8d3-dd63-4ceb-9d5f-c27831854ce7",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.token_validation.rules.with_raw_response.get(
                rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
