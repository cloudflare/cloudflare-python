# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.rulesets import (
    RulesetGetResponse,
    RulesetListResponse,
    RulesetCreateResponse,
    RulesetUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRulesets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.create(
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.create(
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            account_id="account_id",
            description="My ruleset to execute managed rulesets",
            rules=[
                {
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "exposed_credential_check": {
                        "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                        "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
                    },
                    "expression": "ip.src ne 1.1.1.1",
                    "logging": {"enabled": True},
                    "ratelimit": {
                        "characteristics": ["ip.src"],
                        "period": 10,
                        "counting_expression": 'http.request.body.raw eq "abcd"',
                        "mitigation_timeout": 600,
                        "requests_per_period": 1000,
                        "requests_to_origin": True,
                        "score_per_period": 400,
                        "score_response_header_name": "my-score",
                    },
                    "ref": "my_ref",
                }
            ],
        )
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.create(
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.create(
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.create(
                kind="managed",
                name="My ruleset",
                phase="ddos_l4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.create(
                kind="managed",
                name="My ruleset",
                phase="ddos_l4",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.update(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.update(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            description="My ruleset to execute managed rulesets",
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            rules=[
                {
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "exposed_credential_check": {
                        "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                        "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
                    },
                    "expression": "ip.src ne 1.1.1.1",
                    "logging": {"enabled": True},
                    "ratelimit": {
                        "characteristics": ["ip.src"],
                        "period": 10,
                        "counting_expression": 'http.request.body.raw eq "abcd"',
                        "mitigation_timeout": 600,
                        "requests_per_period": 1000,
                        "requests_to_origin": True,
                        "score_per_period": 400,
                        "score_response_header_name": "my-score",
                    },
                    "ref": "my_ref",
                }
            ],
        )
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.update(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.update(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.with_raw_response.update(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.update(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.update(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.list(
            account_id="account_id",
        )
        assert_matches_type(SyncCursorPagination[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.list(
            account_id="account_id",
            cursor="dGhpc2lzYW5leGFtcGxlCg",
            per_page=3,
        )
        assert_matches_type(SyncCursorPagination[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(SyncCursorPagination[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(SyncCursorPagination[RulesetListResponse], ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.delete(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert ruleset is None

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.delete(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert ruleset is None

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.delete(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert ruleset is None

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.delete(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert ruleset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.with_raw_response.delete(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.delete(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.delete(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.get(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.get(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.get(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.get(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.with_raw_response.get(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.get(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.rulesets.with_raw_response.get(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )


class TestAsyncRulesets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.create(
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            account_id="account_id",
        )
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.create(
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            account_id="account_id",
            description="My ruleset to execute managed rulesets",
            rules=[
                {
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "exposed_credential_check": {
                        "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                        "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
                    },
                    "expression": "ip.src ne 1.1.1.1",
                    "logging": {"enabled": True},
                    "ratelimit": {
                        "characteristics": ["ip.src"],
                        "period": 10,
                        "counting_expression": 'http.request.body.raw eq "abcd"',
                        "mitigation_timeout": 600,
                        "requests_per_period": 1000,
                        "requests_to_origin": True,
                        "score_per_period": 400,
                        "score_response_header_name": "my-score",
                    },
                    "ref": "my_ref",
                }
            ],
        )
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.create(
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.create(
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.create(
                kind="managed",
                name="My ruleset",
                phase="ddos_l4",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.create(
                kind="managed",
                name="My ruleset",
                phase="ddos_l4",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.update(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.update(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
            description="My ruleset to execute managed rulesets",
            kind="managed",
            name="My ruleset",
            phase="ddos_l4",
            rules=[
                {
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "exposed_credential_check": {
                        "password_expression": 'url_decode(http.request.body.form[\\"password\\"][0])',
                        "username_expression": 'url_decode(http.request.body.form[\\"username\\"][0])',
                    },
                    "expression": "ip.src ne 1.1.1.1",
                    "logging": {"enabled": True},
                    "ratelimit": {
                        "characteristics": ["ip.src"],
                        "period": 10,
                        "counting_expression": 'http.request.body.raw eq "abcd"',
                        "mitigation_timeout": 600,
                        "requests_per_period": 1000,
                        "requests_to_origin": True,
                        "score_per_period": 400,
                        "score_response_header_name": "my-score",
                    },
                    "ref": "my_ref",
                }
            ],
        )
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.update(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.update(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.with_raw_response.update(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.update(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.update(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncCursorPagination[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.list(
            account_id="account_id",
            cursor="dGhpc2lzYW5leGFtcGxlCg",
            per_page=3,
        )
        assert_matches_type(AsyncCursorPagination[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(AsyncCursorPagination[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(AsyncCursorPagination[RulesetListResponse], ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.delete(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert ruleset is None

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.delete(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert ruleset is None

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.delete(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert ruleset is None

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.delete(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert ruleset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.with_raw_response.delete(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.delete(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.delete(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.get(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.get(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.get(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.get(
            ruleset_id="2f2feab2026849078ba485f918791bdc",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.with_raw_response.get(
                ruleset_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.get(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.rulesets.with_raw_response.get(
                ruleset_id="2f2feab2026849078ba485f918791bdc",
                account_id="account_id",
            )
