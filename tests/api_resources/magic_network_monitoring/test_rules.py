# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_network_monitoring import RuleListResponse, MagicVisibilityMNMRule

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.magic_network_monitoring.rules.create(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.rules.with_raw_response.create(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.rules.with_streaming_response.create(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.magic_network_monitoring.rules.update(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.rules.with_raw_response.update(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.rules.with_streaming_response.update(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.magic_network_monitoring.rules.list(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.rules.with_raw_response.list(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.rules.with_streaming_response.list(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.magic_network_monitoring.rules.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.rules.with_raw_response.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.rules.with_streaming_response.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        rule = client.magic_network_monitoring.rules.edit(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.rules.with_raw_response.edit(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.rules.with_streaming_response.edit(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.magic_network_monitoring.rules.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.rules.with_raw_response.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.rules.with_streaming_response.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.magic_network_monitoring.rules.create(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.rules.with_raw_response.create(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.rules.with_streaming_response.create(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.magic_network_monitoring.rules.update(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.rules.with_raw_response.update(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.rules.with_streaming_response.update(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.magic_network_monitoring.rules.list(
            "6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.rules.with_raw_response.list(
            "6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.rules.with_streaming_response.list(
            "6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.magic_network_monitoring.rules.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.rules.with_raw_response.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.rules.with_streaming_response.delete(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.magic_network_monitoring.rules.edit(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.rules.with_raw_response.edit(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.rules.with_streaming_response.edit(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.magic_network_monitoring.rules.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.rules.with_raw_response.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.rules.with_streaming_response.get(
            "2890e6fa406311ed9b5a23f70f6fb8cf",
            account_identifier="6f91088a406011ed95aed352566e8d4c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[MagicVisibilityMNMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True
