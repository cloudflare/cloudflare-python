# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.email_security.settings import (
    AllowPolicyGetResponse,
    AllowPolicyEditResponse,
    AllowPolicyListResponse,
    AllowPolicyCreateResponse,
    AllowPolicyDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAllowPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        allow_policy = client.email_security.settings.allow_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_acceptable_sender=False,
            is_exempt_recipient=False,
            is_regex=False,
            is_trusted_sender=True,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        )
        assert_matches_type(AllowPolicyCreateResponse, allow_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        allow_policy = client.email_security.settings.allow_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_acceptable_sender=False,
            is_exempt_recipient=False,
            is_regex=False,
            is_trusted_sender=True,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
            comments="Trust all messages send from test@example.com",
            is_recipient=False,
            is_sender=True,
            is_spoof=False,
        )
        assert_matches_type(AllowPolicyCreateResponse, allow_policy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.email_security.settings.allow_policies.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_acceptable_sender=False,
            is_exempt_recipient=False,
            is_regex=False,
            is_trusted_sender=True,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = response.parse()
        assert_matches_type(AllowPolicyCreateResponse, allow_policy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_policies.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_acceptable_sender=False,
            is_exempt_recipient=False,
            is_regex=False,
            is_trusted_sender=True,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = response.parse()
            assert_matches_type(AllowPolicyCreateResponse, allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.allow_policies.with_raw_response.create(
                account_id="",
                is_acceptable_sender=False,
                is_exempt_recipient=False,
                is_regex=False,
                is_trusted_sender=True,
                pattern="test@example.com",
                pattern_type="EMAIL",
                verify_sender=True,
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        allow_policy = client.email_security.settings.allow_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[AllowPolicyListResponse], allow_policy, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        allow_policy = client.email_security.settings.allow_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            is_acceptable_sender=True,
            is_exempt_recipient=True,
            is_recipient=True,
            is_sender=True,
            is_spoof=True,
            is_trusted_sender=True,
            order="pattern",
            page=1,
            pattern_type="EMAIL",
            per_page=1,
            search="search",
            verify_sender=True,
        )
        assert_matches_type(SyncV4PagePaginationArray[AllowPolicyListResponse], allow_policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_security.settings.allow_policies.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[AllowPolicyListResponse], allow_policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_policies.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[AllowPolicyListResponse], allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.allow_policies.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        allow_policy = client.email_security.settings.allow_policies.delete(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPolicyDeleteResponse, allow_policy, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.email_security.settings.allow_policies.with_raw_response.delete(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = response.parse()
        assert_matches_type(AllowPolicyDeleteResponse, allow_policy, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_policies.with_streaming_response.delete(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = response.parse()
            assert_matches_type(AllowPolicyDeleteResponse, allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.allow_policies.with_raw_response.delete(
                policy_id=2401,
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        allow_policy = client.email_security.settings.allow_policies.edit(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPolicyEditResponse, allow_policy, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        allow_policy = client.email_security.settings.allow_policies.edit(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comments="comments",
            is_acceptable_sender=True,
            is_exempt_recipient=True,
            is_regex=True,
            is_trusted_sender=True,
            pattern="x",
            pattern_type="EMAIL",
            verify_sender=True,
        )
        assert_matches_type(AllowPolicyEditResponse, allow_policy, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.email_security.settings.allow_policies.with_raw_response.edit(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = response.parse()
        assert_matches_type(AllowPolicyEditResponse, allow_policy, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_policies.with_streaming_response.edit(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = response.parse()
            assert_matches_type(AllowPolicyEditResponse, allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.allow_policies.with_raw_response.edit(
                policy_id=2401,
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        allow_policy = client.email_security.settings.allow_policies.get(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPolicyGetResponse, allow_policy, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_security.settings.allow_policies.with_raw_response.get(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = response.parse()
        assert_matches_type(AllowPolicyGetResponse, allow_policy, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.settings.allow_policies.with_streaming_response.get(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = response.parse()
            assert_matches_type(AllowPolicyGetResponse, allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.allow_policies.with_raw_response.get(
                policy_id=2401,
                account_id="",
            )


class TestAsyncAllowPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        allow_policy = await async_client.email_security.settings.allow_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_acceptable_sender=False,
            is_exempt_recipient=False,
            is_regex=False,
            is_trusted_sender=True,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        )
        assert_matches_type(AllowPolicyCreateResponse, allow_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        allow_policy = await async_client.email_security.settings.allow_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_acceptable_sender=False,
            is_exempt_recipient=False,
            is_regex=False,
            is_trusted_sender=True,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
            comments="Trust all messages send from test@example.com",
            is_recipient=False,
            is_sender=True,
            is_spoof=False,
        )
        assert_matches_type(AllowPolicyCreateResponse, allow_policy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.allow_policies.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_acceptable_sender=False,
            is_exempt_recipient=False,
            is_regex=False,
            is_trusted_sender=True,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = await response.parse()
        assert_matches_type(AllowPolicyCreateResponse, allow_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_policies.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            is_acceptable_sender=False,
            is_exempt_recipient=False,
            is_regex=False,
            is_trusted_sender=True,
            pattern="test@example.com",
            pattern_type="EMAIL",
            verify_sender=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = await response.parse()
            assert_matches_type(AllowPolicyCreateResponse, allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.allow_policies.with_raw_response.create(
                account_id="",
                is_acceptable_sender=False,
                is_exempt_recipient=False,
                is_regex=False,
                is_trusted_sender=True,
                pattern="test@example.com",
                pattern_type="EMAIL",
                verify_sender=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        allow_policy = await async_client.email_security.settings.allow_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[AllowPolicyListResponse], allow_policy, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        allow_policy = await async_client.email_security.settings.allow_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            is_acceptable_sender=True,
            is_exempt_recipient=True,
            is_recipient=True,
            is_sender=True,
            is_spoof=True,
            is_trusted_sender=True,
            order="pattern",
            page=1,
            pattern_type="EMAIL",
            per_page=1,
            search="search",
            verify_sender=True,
        )
        assert_matches_type(AsyncV4PagePaginationArray[AllowPolicyListResponse], allow_policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.allow_policies.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[AllowPolicyListResponse], allow_policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_policies.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[AllowPolicyListResponse], allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.allow_policies.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        allow_policy = await async_client.email_security.settings.allow_policies.delete(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPolicyDeleteResponse, allow_policy, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.allow_policies.with_raw_response.delete(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = await response.parse()
        assert_matches_type(AllowPolicyDeleteResponse, allow_policy, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_policies.with_streaming_response.delete(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = await response.parse()
            assert_matches_type(AllowPolicyDeleteResponse, allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.allow_policies.with_raw_response.delete(
                policy_id=2401,
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        allow_policy = await async_client.email_security.settings.allow_policies.edit(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPolicyEditResponse, allow_policy, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        allow_policy = await async_client.email_security.settings.allow_policies.edit(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            comments="comments",
            is_acceptable_sender=True,
            is_exempt_recipient=True,
            is_regex=True,
            is_trusted_sender=True,
            pattern="x",
            pattern_type="EMAIL",
            verify_sender=True,
        )
        assert_matches_type(AllowPolicyEditResponse, allow_policy, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.allow_policies.with_raw_response.edit(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = await response.parse()
        assert_matches_type(AllowPolicyEditResponse, allow_policy, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_policies.with_streaming_response.edit(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = await response.parse()
            assert_matches_type(AllowPolicyEditResponse, allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.allow_policies.with_raw_response.edit(
                policy_id=2401,
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        allow_policy = await async_client.email_security.settings.allow_policies.get(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AllowPolicyGetResponse, allow_policy, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.allow_policies.with_raw_response.get(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        allow_policy = await response.parse()
        assert_matches_type(AllowPolicyGetResponse, allow_policy, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.allow_policies.with_streaming_response.get(
            policy_id=2401,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            allow_policy = await response.parse()
            assert_matches_type(AllowPolicyGetResponse, allow_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.allow_policies.with_raw_response.get(
                policy_id=2401,
                account_id="",
            )
