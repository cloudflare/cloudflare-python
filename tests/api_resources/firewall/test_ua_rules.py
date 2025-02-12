# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.firewall import (
    UARuleGetResponse,
    UARuleListResponse,
    UARuleCreateResponse,
    UARuleDeleteResponse,
    UARuleUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUARules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ua_rule = client.firewall.ua_rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        )
        assert_matches_type(UARuleCreateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        ua_rule = client.firewall.ua_rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
        )
        assert_matches_type(UARuleCreateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.firewall.ua_rules.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(UARuleCreateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.firewall.ua_rules.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(UARuleCreateResponse, ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.ua_rules.with_raw_response.create(
                zone_id="",
                configuration={},
                mode="block",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ua_rule = client.firewall.ua_rules.update(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        )
        assert_matches_type(UARuleUpdateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ua_rule = client.firewall.ua_rules.update(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
        )
        assert_matches_type(UARuleUpdateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.firewall.ua_rules.with_raw_response.update(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(UARuleUpdateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.firewall.ua_rules.with_streaming_response.update(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(UARuleUpdateResponse, ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.ua_rules.with_raw_response.update(
                ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
                configuration={},
                mode="block",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ua_rule_id` but received ''"):
            client.firewall.ua_rules.with_raw_response.update(
                ua_rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                configuration={},
                mode="block",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        ua_rule = client.firewall.ua_rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[UARuleListResponse], ua_rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        ua_rule = client.firewall.ua_rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="abusive",
            description_search="abusive",
            page=1,
            per_page=1,
            ua_search="Safari",
        )
        assert_matches_type(SyncV4PagePaginationArray[UARuleListResponse], ua_rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.firewall.ua_rules.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[UARuleListResponse], ua_rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.firewall.ua_rules.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[UARuleListResponse], ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.ua_rules.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ua_rule = client.firewall.ua_rules.delete(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UARuleDeleteResponse, ua_rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.firewall.ua_rules.with_raw_response.delete(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(UARuleDeleteResponse, ua_rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.firewall.ua_rules.with_streaming_response.delete(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(UARuleDeleteResponse, ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.ua_rules.with_raw_response.delete(
                ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ua_rule_id` but received ''"):
            client.firewall.ua_rules.with_raw_response.delete(
                ua_rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ua_rule = client.firewall.ua_rules.get(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UARuleGetResponse, ua_rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewall.ua_rules.with_raw_response.get(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(UARuleGetResponse, ua_rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewall.ua_rules.with_streaming_response.get(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(UARuleGetResponse, ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.ua_rules.with_raw_response.get(
                ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ua_rule_id` but received ''"):
            client.firewall.ua_rules.with_raw_response.get(
                ua_rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncUARules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewall.ua_rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        )
        assert_matches_type(UARuleCreateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewall.ua_rules.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
        )
        assert_matches_type(UARuleCreateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.ua_rules.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(UARuleCreateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.ua_rules.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(UARuleCreateResponse, ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.ua_rules.with_raw_response.create(
                zone_id="",
                configuration={},
                mode="block",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewall.ua_rules.update(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        )
        assert_matches_type(UARuleUpdateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewall.ua_rules.update(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
        )
        assert_matches_type(UARuleUpdateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.ua_rules.with_raw_response.update(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(UARuleUpdateResponse, ua_rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.ua_rules.with_streaming_response.update(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            configuration={},
            mode="block",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(UARuleUpdateResponse, ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.ua_rules.with_raw_response.update(
                ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
                configuration={},
                mode="block",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ua_rule_id` but received ''"):
            await async_client.firewall.ua_rules.with_raw_response.update(
                ua_rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                configuration={},
                mode="block",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewall.ua_rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[UARuleListResponse], ua_rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewall.ua_rules.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="abusive",
            description_search="abusive",
            page=1,
            per_page=1,
            ua_search="Safari",
        )
        assert_matches_type(AsyncV4PagePaginationArray[UARuleListResponse], ua_rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.ua_rules.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[UARuleListResponse], ua_rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.ua_rules.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[UARuleListResponse], ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.ua_rules.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewall.ua_rules.delete(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UARuleDeleteResponse, ua_rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.ua_rules.with_raw_response.delete(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(UARuleDeleteResponse, ua_rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.ua_rules.with_streaming_response.delete(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(UARuleDeleteResponse, ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.ua_rules.with_raw_response.delete(
                ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ua_rule_id` but received ''"):
            await async_client.firewall.ua_rules.with_raw_response.delete(
                ua_rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewall.ua_rules.get(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(UARuleGetResponse, ua_rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.ua_rules.with_raw_response.get(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(UARuleGetResponse, ua_rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.ua_rules.with_streaming_response.get(
            ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(UARuleGetResponse, ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.ua_rules.with_raw_response.get(
                ua_rule_id="372e67954025e0ba6aaa6d586b9e0b59",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ua_rule_id` but received ''"):
            await async_client.firewall.ua_rules.with_raw_response.get(
                ua_rule_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
