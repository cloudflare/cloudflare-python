# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.firewalls import (
    LockdownGetResponse,
    LockdownDeleteResponse,
    LockdownUpdateResponse,
    LockdownZoneLockdownListZoneLockdownRulesResponse,
    LockdownZoneLockdownCreateAZoneLockdownRuleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLockdowns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        lockdown = client.firewalls.lockdowns.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[LockdownUpdateResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.firewalls.lockdowns.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Optional[LockdownUpdateResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.firewalls.lockdowns.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Optional[LockdownUpdateResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.lockdowns.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.lockdowns.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        lockdown = client.firewalls.lockdowns.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.firewalls.lockdowns.with_raw_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.firewalls.lockdowns.with_streaming_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.lockdowns.with_raw_response.delete(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.lockdowns.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        lockdown = client.firewalls.lockdowns.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownGetResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewalls.lockdowns.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Optional[LockdownGetResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewalls.lockdowns.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(Optional[LockdownGetResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.lockdowns.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.lockdowns.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_lockdown_create_a_zone_lockdown_rule(self, client: Cloudflare) -> None:
        lockdown = client.firewalls.lockdowns.zone_lockdown_create_a_zone_lockdown_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_lockdown_create_a_zone_lockdown_rule(self, client: Cloudflare) -> None:
        response = client.firewalls.lockdowns.with_raw_response.zone_lockdown_create_a_zone_lockdown_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_lockdown_create_a_zone_lockdown_rule(self, client: Cloudflare) -> None:
        with client.firewalls.lockdowns.with_streaming_response.zone_lockdown_create_a_zone_lockdown_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(
                Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse], lockdown, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_lockdown_create_a_zone_lockdown_rule(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.lockdowns.with_raw_response.zone_lockdown_create_a_zone_lockdown_rule(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_lockdown_list_zone_lockdown_rules(self, client: Cloudflare) -> None:
        lockdown = client.firewalls.lockdowns.zone_lockdown_list_zone_lockdown_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownZoneLockdownListZoneLockdownRulesResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_lockdown_list_zone_lockdown_rules_with_all_params(self, client: Cloudflare) -> None:
        lockdown = client.firewalls.lockdowns.zone_lockdown_list_zone_lockdown_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="endpoints",
            description_search="endpoints",
            ip="1.2.3.4",
            ip_range_search="1.2.3.0/16",
            ip_search="1.2.3.4",
            page=1,
            per_page=1,
            priority=5,
            uri_search="/some/path",
        )
        assert_matches_type(Optional[LockdownZoneLockdownListZoneLockdownRulesResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_lockdown_list_zone_lockdown_rules(self, client: Cloudflare) -> None:
        response = client.firewalls.lockdowns.with_raw_response.zone_lockdown_list_zone_lockdown_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = response.parse()
        assert_matches_type(Optional[LockdownZoneLockdownListZoneLockdownRulesResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_lockdown_list_zone_lockdown_rules(self, client: Cloudflare) -> None:
        with client.firewalls.lockdowns.with_streaming_response.zone_lockdown_list_zone_lockdown_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = response.parse()
            assert_matches_type(
                Optional[LockdownZoneLockdownListZoneLockdownRulesResponse], lockdown, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_lockdown_list_zone_lockdown_rules(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.lockdowns.with_raw_response.zone_lockdown_list_zone_lockdown_rules(
                "",
            )


class TestAsyncLockdowns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewalls.lockdowns.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[LockdownUpdateResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.lockdowns.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Optional[LockdownUpdateResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.lockdowns.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Optional[LockdownUpdateResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.lockdowns.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.lockdowns.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewalls.lockdowns.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.lockdowns.with_raw_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.lockdowns.with_streaming_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Optional[LockdownDeleteResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.lockdowns.with_raw_response.delete(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.lockdowns.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewalls.lockdowns.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownGetResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.lockdowns.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Optional[LockdownGetResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.lockdowns.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(Optional[LockdownGetResponse], lockdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.lockdowns.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.lockdowns.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_lockdown_create_a_zone_lockdown_rule(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewalls.lockdowns.zone_lockdown_create_a_zone_lockdown_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_lockdown_create_a_zone_lockdown_rule(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.lockdowns.with_raw_response.zone_lockdown_create_a_zone_lockdown_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_lockdown_create_a_zone_lockdown_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.firewalls.lockdowns.with_streaming_response.zone_lockdown_create_a_zone_lockdown_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(
                Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse], lockdown, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_lockdown_create_a_zone_lockdown_rule(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.lockdowns.with_raw_response.zone_lockdown_create_a_zone_lockdown_rule(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_lockdown_list_zone_lockdown_rules(self, async_client: AsyncCloudflare) -> None:
        lockdown = await async_client.firewalls.lockdowns.zone_lockdown_list_zone_lockdown_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LockdownZoneLockdownListZoneLockdownRulesResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_lockdown_list_zone_lockdown_rules_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        lockdown = await async_client.firewalls.lockdowns.zone_lockdown_list_zone_lockdown_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="endpoints",
            description_search="endpoints",
            ip="1.2.3.4",
            ip_range_search="1.2.3.0/16",
            ip_search="1.2.3.4",
            page=1,
            per_page=1,
            priority=5,
            uri_search="/some/path",
        )
        assert_matches_type(Optional[LockdownZoneLockdownListZoneLockdownRulesResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_lockdown_list_zone_lockdown_rules(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.lockdowns.with_raw_response.zone_lockdown_list_zone_lockdown_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lockdown = await response.parse()
        assert_matches_type(Optional[LockdownZoneLockdownListZoneLockdownRulesResponse], lockdown, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_lockdown_list_zone_lockdown_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.firewalls.lockdowns.with_streaming_response.zone_lockdown_list_zone_lockdown_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lockdown = await response.parse()
            assert_matches_type(
                Optional[LockdownZoneLockdownListZoneLockdownRulesResponse], lockdown, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_lockdown_list_zone_lockdown_rules(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.lockdowns.with_raw_response.zone_lockdown_list_zone_lockdown_rules(
                "",
            )
