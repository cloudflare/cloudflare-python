# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.firewalls import (
    RuleGetResponse,
    RuleEditResponse,
    RuleListResponse,
    RuleCreateResponse,
    RuleDeleteResponse,
    RuleUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.firewalls.rules.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.firewalls.rules.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.firewalls.rules.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.rules.with_raw_response.create(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.firewalls.rules.update(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.firewalls.rules.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.firewalls.rules.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.rules.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.rules.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.firewalls.rules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        rule = client.firewalls.rules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            description="mir",
            page=1,
            paused=False,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.firewalls.rules.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.firewalls.rules.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.rules.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.firewalls.rules.delete(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        rule = client.firewalls.rules.delete(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            delete_filter_if_unused=True,
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.firewalls.rules.with_raw_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.firewalls.rules.with_streaming_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.rules.with_raw_response.delete(
                "372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        rule = client.firewalls.rules.edit(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.firewalls.rules.with_raw_response.edit(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.firewalls.rules.with_streaming_response.edit(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.rules.with_raw_response.edit(
                "372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.rules.with_raw_response.edit(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.firewalls.rules.get(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewalls.rules.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewalls.rules.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.rules.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.rules.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.rules.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.rules.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.rules.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.rules.with_raw_response.create(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.rules.update(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.rules.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.rules.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.rules.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.rules.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.rules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.rules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            description="mir",
            page=1,
            paused=False,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.rules.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.rules.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.rules.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.rules.delete(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.rules.delete(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            delete_filter_if_unused=True,
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.rules.with_raw_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.rules.with_streaming_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.rules.with_raw_response.delete(
                "372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.rules.edit(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.rules.with_raw_response.edit(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.rules.with_streaming_response.edit(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.rules.with_raw_response.edit(
                "372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.rules.with_raw_response.edit(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.rules.get(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.rules.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.rules.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b60",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.rules.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.rules.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
