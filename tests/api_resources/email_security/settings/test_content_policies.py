# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.email_security.settings import (
    ContentPolicyGetResponse,
    ContentPolicyEditResponse,
    ContentPolicyListResponse,
    ContentPolicyBatchResponse,
    ContentPolicyCreateResponse,
    ContentPolicyDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContentPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        content_policy = client.email_security.settings.content_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
        )
        assert_matches_type(Optional[ContentPolicyCreateResponse], content_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        content_policy = client.email_security.settings.content_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
            notes="Blocks common phishing subject lines",
        )
        assert_matches_type(Optional[ContentPolicyCreateResponse], content_policy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.email_security.settings.content_policies.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = response.parse()
        assert_matches_type(Optional[ContentPolicyCreateResponse], content_policy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.email_security.settings.content_policies.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = response.parse()
            assert_matches_type(Optional[ContentPolicyCreateResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.content_policies.with_raw_response.create(
                account_id="",
                enabled=True,
                name="Block phishing keywords",
                pattern="urgent.*verify.*account",
                targets=["SUBJECT"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        content_policy = client.email_security.settings.content_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[ContentPolicyListResponse], content_policy, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        content_policy = client.email_security.settings.content_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            enabled=True,
            name="name",
            order="name",
            page=1,
            per_page=20,
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[ContentPolicyListResponse], content_policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_security.settings.content_policies.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ContentPolicyListResponse], content_policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.settings.content_policies.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[ContentPolicyListResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.content_policies.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        content_policy = client.email_security.settings.content_policies.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ContentPolicyDeleteResponse], content_policy, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.email_security.settings.content_policies.with_raw_response.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = response.parse()
        assert_matches_type(Optional[ContentPolicyDeleteResponse], content_policy, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_security.settings.content_policies.with_streaming_response.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = response.parse()
            assert_matches_type(Optional[ContentPolicyDeleteResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.content_policies.with_raw_response.delete(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.email_security.settings.content_policies.with_raw_response.delete(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_batch(self, client: Cloudflare) -> None:
        content_policy = client.email_security.settings.content_policies.batch(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deletes=[{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"}],
            patches=[{}],
            posts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
            puts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
        )
        assert_matches_type(Optional[ContentPolicyBatchResponse], content_policy, path=["response"])

    @parametrize
    def test_raw_response_batch(self, client: Cloudflare) -> None:
        response = client.email_security.settings.content_policies.with_raw_response.batch(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deletes=[{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"}],
            patches=[{}],
            posts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
            puts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = response.parse()
        assert_matches_type(Optional[ContentPolicyBatchResponse], content_policy, path=["response"])

    @parametrize
    def test_streaming_response_batch(self, client: Cloudflare) -> None:
        with client.email_security.settings.content_policies.with_streaming_response.batch(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deletes=[{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"}],
            patches=[{}],
            posts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
            puts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = response.parse()
            assert_matches_type(Optional[ContentPolicyBatchResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_batch(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.content_policies.with_raw_response.batch(
                account_id="",
                deletes=[{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"}],
                patches=[{}],
                posts=[
                    {
                        "enabled": True,
                        "name": "Block phishing keywords",
                        "pattern": "urgent.*verify.*account",
                        "targets": ["SUBJECT"],
                    }
                ],
                puts=[
                    {
                        "enabled": True,
                        "name": "Block phishing keywords",
                        "pattern": "urgent.*verify.*account",
                        "targets": ["SUBJECT"],
                    }
                ],
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        content_policy = client.email_security.settings.content_policies.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ContentPolicyEditResponse], content_policy, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        content_policy = client.email_security.settings.content_policies.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            notes="Blocks common phishing subject lines",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
        )
        assert_matches_type(Optional[ContentPolicyEditResponse], content_policy, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.email_security.settings.content_policies.with_raw_response.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = response.parse()
        assert_matches_type(Optional[ContentPolicyEditResponse], content_policy, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.email_security.settings.content_policies.with_streaming_response.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = response.parse()
            assert_matches_type(Optional[ContentPolicyEditResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.content_policies.with_raw_response.edit(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.email_security.settings.content_policies.with_raw_response.edit(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        content_policy = client.email_security.settings.content_policies.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ContentPolicyGetResponse], content_policy, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_security.settings.content_policies.with_raw_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = response.parse()
        assert_matches_type(Optional[ContentPolicyGetResponse], content_policy, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.settings.content_policies.with_streaming_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = response.parse()
            assert_matches_type(Optional[ContentPolicyGetResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.content_policies.with_raw_response.get(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.email_security.settings.content_policies.with_raw_response.get(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncContentPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        content_policy = await async_client.email_security.settings.content_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
        )
        assert_matches_type(Optional[ContentPolicyCreateResponse], content_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        content_policy = await async_client.email_security.settings.content_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
            notes="Blocks common phishing subject lines",
        )
        assert_matches_type(Optional[ContentPolicyCreateResponse], content_policy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.content_policies.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = await response.parse()
        assert_matches_type(Optional[ContentPolicyCreateResponse], content_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.content_policies.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = await response.parse()
            assert_matches_type(Optional[ContentPolicyCreateResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.content_policies.with_raw_response.create(
                account_id="",
                enabled=True,
                name="Block phishing keywords",
                pattern="urgent.*verify.*account",
                targets=["SUBJECT"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        content_policy = await async_client.email_security.settings.content_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ContentPolicyListResponse], content_policy, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        content_policy = await async_client.email_security.settings.content_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            enabled=True,
            name="name",
            order="name",
            page=1,
            per_page=20,
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ContentPolicyListResponse], content_policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.content_policies.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ContentPolicyListResponse], content_policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.content_policies.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[ContentPolicyListResponse], content_policy, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.content_policies.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        content_policy = await async_client.email_security.settings.content_policies.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ContentPolicyDeleteResponse], content_policy, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.content_policies.with_raw_response.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = await response.parse()
        assert_matches_type(Optional[ContentPolicyDeleteResponse], content_policy, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.content_policies.with_streaming_response.delete(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = await response.parse()
            assert_matches_type(Optional[ContentPolicyDeleteResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.content_policies.with_raw_response.delete(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.email_security.settings.content_policies.with_raw_response.delete(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_batch(self, async_client: AsyncCloudflare) -> None:
        content_policy = await async_client.email_security.settings.content_policies.batch(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deletes=[{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"}],
            patches=[{}],
            posts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
            puts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
        )
        assert_matches_type(Optional[ContentPolicyBatchResponse], content_policy, path=["response"])

    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.content_policies.with_raw_response.batch(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deletes=[{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"}],
            patches=[{}],
            posts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
            puts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = await response.parse()
        assert_matches_type(Optional[ContentPolicyBatchResponse], content_policy, path=["response"])

    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.content_policies.with_streaming_response.batch(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            deletes=[{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"}],
            patches=[{}],
            posts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
            puts=[
                {
                    "enabled": True,
                    "name": "Block phishing keywords",
                    "pattern": "urgent.*verify.*account",
                    "targets": ["SUBJECT"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = await response.parse()
            assert_matches_type(Optional[ContentPolicyBatchResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_batch(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.content_policies.with_raw_response.batch(
                account_id="",
                deletes=[{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415"}],
                patches=[{}],
                posts=[
                    {
                        "enabled": True,
                        "name": "Block phishing keywords",
                        "pattern": "urgent.*verify.*account",
                        "targets": ["SUBJECT"],
                    }
                ],
                puts=[
                    {
                        "enabled": True,
                        "name": "Block phishing keywords",
                        "pattern": "urgent.*verify.*account",
                        "targets": ["SUBJECT"],
                    }
                ],
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        content_policy = await async_client.email_security.settings.content_policies.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ContentPolicyEditResponse], content_policy, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        content_policy = await async_client.email_security.settings.content_policies.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            name="Block phishing keywords",
            notes="Blocks common phishing subject lines",
            pattern="urgent.*verify.*account",
            targets=["SUBJECT"],
        )
        assert_matches_type(Optional[ContentPolicyEditResponse], content_policy, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.content_policies.with_raw_response.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = await response.parse()
        assert_matches_type(Optional[ContentPolicyEditResponse], content_policy, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.content_policies.with_streaming_response.edit(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = await response.parse()
            assert_matches_type(Optional[ContentPolicyEditResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.content_policies.with_raw_response.edit(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.email_security.settings.content_policies.with_raw_response.edit(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        content_policy = await async_client.email_security.settings.content_policies.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ContentPolicyGetResponse], content_policy, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.content_policies.with_raw_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_policy = await response.parse()
        assert_matches_type(Optional[ContentPolicyGetResponse], content_policy, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.content_policies.with_streaming_response.get(
            policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_policy = await response.parse()
            assert_matches_type(Optional[ContentPolicyGetResponse], content_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.content_policies.with_raw_response.get(
                policy_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.email_security.settings.content_policies.with_raw_response.get(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
