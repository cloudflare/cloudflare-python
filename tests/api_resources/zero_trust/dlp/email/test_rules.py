# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.dlp.email import (
    RuleGetResponse,
    RuleListResponse,
    RuleCreateResponse,
    RuleDeleteResponse,
    RuleUpdateResponse,
    RuleBulkEditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dlp.email.rules.create(
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dlp.email.rules.create(
            account_id="account_id",
            action={
                "action": "Block",
                "message": "message",
            },
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
            description="description",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.email.rules.with_raw_response.create(
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.email.rules.with_streaming_response.create(
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.email.rules.with_raw_response.create(
                account_id="",
                action={"action": "Block"},
                conditions=[
                    {
                        "operator": "InList",
                        "selector": "Recipients",
                        "value": {},
                    }
                ],
                enabled=True,
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dlp.email.rules.update(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dlp.email.rules.update(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            action={
                "action": "Block",
                "message": "message",
            },
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
            description="description",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.email.rules.with_raw_response.update(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.email.rules.with_streaming_response.update(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.email.rules.with_raw_response.update(
                rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                action={"action": "Block"},
                conditions=[
                    {
                        "operator": "InList",
                        "selector": "Recipients",
                        "value": {},
                    }
                ],
                enabled=True,
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.dlp.email.rules.with_raw_response.update(
                rule_id="",
                account_id="account_id",
                action={"action": "Block"},
                conditions=[
                    {
                        "operator": "InList",
                        "selector": "Recipients",
                        "value": {},
                    }
                ],
                enabled=True,
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dlp.email.rules.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.email.rules.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncSinglePage[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.email.rules.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncSinglePage[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.email.rules.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dlp.email.rules.delete(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.email.rules.with_raw_response.delete(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.email.rules.with_streaming_response.delete(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.email.rules.with_raw_response.delete(
                rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.dlp.email.rules.with_raw_response.delete(
                rule_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_bulk_edit(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dlp.email.rules.bulk_edit(
            account_id="account_id",
            new_priorities={"foo": 0},
        )
        assert_matches_type(Optional[RuleBulkEditResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_bulk_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.email.rules.with_raw_response.bulk_edit(
            account_id="account_id",
            new_priorities={"foo": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleBulkEditResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_bulk_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.email.rules.with_streaming_response.bulk_edit(
            account_id="account_id",
            new_priorities={"foo": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleBulkEditResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.email.rules.with_raw_response.bulk_edit(
                account_id="",
                new_priorities={"foo": 0},
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dlp.email.rules.get(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.email.rules.with_raw_response.get(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.email.rules.with_streaming_response.get(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.email.rules.with_raw_response.get(
                rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.dlp.email.rules.with_raw_response.get(
                rule_id="",
                account_id="account_id",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dlp.email.rules.create(
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dlp.email.rules.create(
            account_id="account_id",
            action={
                "action": "Block",
                "message": "message",
            },
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
            description="description",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.email.rules.with_raw_response.create(
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.email.rules.with_streaming_response.create(
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.email.rules.with_raw_response.create(
                account_id="",
                action={"action": "Block"},
                conditions=[
                    {
                        "operator": "InList",
                        "selector": "Recipients",
                        "value": {},
                    }
                ],
                enabled=True,
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dlp.email.rules.update(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dlp.email.rules.update(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            action={
                "action": "Block",
                "message": "message",
            },
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
            description="description",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.email.rules.with_raw_response.update(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.email.rules.with_streaming_response.update(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            action={"action": "Block"},
            conditions=[
                {
                    "operator": "InList",
                    "selector": "Recipients",
                    "value": {},
                }
            ],
            enabled=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.email.rules.with_raw_response.update(
                rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                action={"action": "Block"},
                conditions=[
                    {
                        "operator": "InList",
                        "selector": "Recipients",
                        "value": {},
                    }
                ],
                enabled=True,
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.dlp.email.rules.with_raw_response.update(
                rule_id="",
                account_id="account_id",
                action={"action": "Block"},
                conditions=[
                    {
                        "operator": "InList",
                        "selector": "Recipients",
                        "value": {},
                    }
                ],
                enabled=True,
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dlp.email.rules.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.email.rules.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncSinglePage[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.email.rules.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncSinglePage[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.email.rules.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dlp.email.rules.delete(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.email.rules.with_raw_response.delete(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.email.rules.with_streaming_response.delete(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.email.rules.with_raw_response.delete(
                rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.dlp.email.rules.with_raw_response.delete(
                rule_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dlp.email.rules.bulk_edit(
            account_id="account_id",
            new_priorities={"foo": 0},
        )
        assert_matches_type(Optional[RuleBulkEditResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.email.rules.with_raw_response.bulk_edit(
            account_id="account_id",
            new_priorities={"foo": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleBulkEditResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.email.rules.with_streaming_response.bulk_edit(
            account_id="account_id",
            new_priorities={"foo": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleBulkEditResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.email.rules.with_raw_response.bulk_edit(
                account_id="",
                new_priorities={"foo": 0},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dlp.email.rules.get(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.email.rules.with_raw_response.get(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.email.rules.with_streaming_response.get(
            rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.email.rules.with_raw_response.get(
                rule_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.dlp.email.rules.with_raw_response.get(
                rule_id="",
                account_id="account_id",
            )
