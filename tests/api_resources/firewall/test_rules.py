# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.firewall import (
    FirewallRule,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={
                    "mode": "simulate",
                    "response": {
                        "body": "<error>This request has been rate-limited.</error>",
                        "content_type": "text/xml",
                    },
                    "timeout": 86400,
                },
                filter={
                    "description": "Restrict access from these browsers on this address range.",
                    "expression": '(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
                    "paused": False,
                    "ref": "FIL-100",
                },
            )

        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.firewall.rules.with_raw_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.firewall.rules.with_streaming_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = response.parse()
                assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.firewall.rules.with_raw_response.create(
                    zone_id="",
                    action={},
                    filter={},
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.update(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert_matches_type(FirewallRule, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.update(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={
                    "mode": "simulate",
                    "response": {
                        "body": "<error>This request has been rate-limited.</error>",
                        "content_type": "text/xml",
                    },
                    "timeout": 86400,
                },
                filter={
                    "description": "Restrict access from these browsers on this address range.",
                    "expression": '(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
                    "paused": False,
                    "ref": "FIL-100",
                },
            )

        assert_matches_type(FirewallRule, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.firewall.rules.with_raw_response.update(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(FirewallRule, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.firewall.rules.with_streaming_response.update(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = response.parse()
                assert_matches_type(FirewallRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.firewall.rules.with_raw_response.update(
                    rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                    zone_id="",
                    action={},
                    filter={},
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
                client.firewall.rules.with_raw_response.update(
                    rule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                    action={},
                    filter={},
                )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncV4PagePaginationArray[FirewallRule], rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="372e67954025e0ba6aaa6d586b9e0b60",
                action="block",
                description="mir",
                page=1,
                paused=False,
                per_page=5,
            )

        assert_matches_type(SyncV4PagePaginationArray[FirewallRule], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.firewall.rules.with_raw_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[FirewallRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.firewall.rules.with_streaming_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = response.parse()
                assert_matches_type(SyncV4PagePaginationArray[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.firewall.rules.with_raw_response.list(
                    zone_id="",
                )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.delete(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallRule, rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.firewall.rules.with_raw_response.delete(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(FirewallRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.firewall.rules.with_streaming_response.delete(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = response.parse()
                assert_matches_type(FirewallRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.firewall.rules.with_raw_response.delete(
                    rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
                client.firewall.rules.with_raw_response.delete(
                    rule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.firewall.rules.with_raw_response.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.firewall.rules.with_streaming_response.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = response.parse()
                assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.firewall.rules.with_raw_response.bulk_delete(
                    zone_id="",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_bulk_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.bulk_edit(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_bulk_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.firewall.rules.with_raw_response.bulk_edit(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_bulk_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.firewall.rules.with_streaming_response.bulk_edit(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = response.parse()
                assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_bulk_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.firewall.rules.with_raw_response.bulk_edit(
                    zone_id="",
                    body={},
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_bulk_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_bulk_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.firewall.rules.with_raw_response.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_bulk_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.firewall.rules.with_streaming_response.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = response.parse()
                assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_bulk_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.firewall.rules.with_raw_response.bulk_update(
                    zone_id="",
                    body={},
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.edit(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.firewall.rules.with_raw_response.edit(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.firewall.rules.with_streaming_response.edit(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = response.parse()
                assert_matches_type(SyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.firewall.rules.with_raw_response.edit(
                    rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
                client.firewall.rules.with_raw_response.edit(
                    rule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = client.firewall.rules.get(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallRule, rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.firewall.rules.with_raw_response.get(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(FirewallRule, rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with client.firewall.rules.with_streaming_response.get(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = response.parse()
                assert_matches_type(FirewallRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                client.firewall.rules.with_raw_response.get(
                    rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
                client.firewall.rules.with_raw_response.get(
                    rule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={
                    "mode": "simulate",
                    "response": {
                        "body": "<error>This request has been rate-limited.</error>",
                        "content_type": "text/xml",
                    },
                    "timeout": 86400,
                },
                filter={
                    "description": "Restrict access from these browsers on this address range.",
                    "expression": '(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
                    "paused": False,
                    "ref": "FIL-100",
                },
            )

        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.firewall.rules.with_raw_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.firewall.rules.with_streaming_response.create(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = await response.parse()
                assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.create(
                    zone_id="",
                    action={},
                    filter={},
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.update(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert_matches_type(FirewallRule, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.update(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={
                    "mode": "simulate",
                    "response": {
                        "body": "<error>This request has been rate-limited.</error>",
                        "content_type": "text/xml",
                    },
                    "timeout": 86400,
                },
                filter={
                    "description": "Restrict access from these browsers on this address range.",
                    "expression": '(http.request.uri.path ~ ".*wp-login.php" or http.request.uri.path ~ ".*xmlrpc.php") and ip.addr ne 172.16.22.155',
                    "paused": False,
                    "ref": "FIL-100",
                },
            )

        assert_matches_type(FirewallRule, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.firewall.rules.with_raw_response.update(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(FirewallRule, rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.firewall.rules.with_streaming_response.update(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = await response.parse()
                assert_matches_type(FirewallRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.update(
                    rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                    zone_id="",
                    action={},
                    filter={},
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.update(
                    rule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                    action={},
                    filter={},
                )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="372e67954025e0ba6aaa6d586b9e0b60",
                action="block",
                description="mir",
                page=1,
                paused=False,
                per_page=5,
            )

        assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.firewall.rules.with_raw_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.firewall.rules.with_streaming_response.list(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = await response.parse()
                assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.list(
                    zone_id="",
                )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.delete(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.firewall.rules.with_raw_response.delete(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(FirewallRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.firewall.rules.with_streaming_response.delete(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = await response.parse()
                assert_matches_type(FirewallRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.delete(
                    rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.delete(
                    rule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.firewall.rules.with_raw_response.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.firewall.rules.with_streaming_response.bulk_delete(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = await response.parse()
                assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.bulk_delete(
                    zone_id="",
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.bulk_edit(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.firewall.rules.with_raw_response.bulk_edit(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.firewall.rules.with_streaming_response.bulk_edit(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = await response.parse()
                assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.bulk_edit(
                    zone_id="",
                    body={},
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.firewall.rules.with_raw_response.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.firewall.rules.with_streaming_response.bulk_update(
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = await response.parse()
                assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.bulk_update(
                    zone_id="",
                    body={},
                )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.edit(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.firewall.rules.with_raw_response.edit(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.firewall.rules.with_streaming_response.edit(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = await response.parse()
                assert_matches_type(AsyncSinglePage[FirewallRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.edit(
                    rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.edit(
                    rule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            rule = await async_client.firewall.rules.get(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallRule, rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.firewall.rules.with_raw_response.get(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(FirewallRule, rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.firewall.rules.with_streaming_response.get(
                rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                rule = await response.parse()
                assert_matches_type(FirewallRule, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.get(
                    rule_id="372e67954025e0ba6aaa6d586b9e0b60",
                    zone_id="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
                await async_client.firewall.rules.with_raw_response.get(
                    rule_id="",
                    zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )
