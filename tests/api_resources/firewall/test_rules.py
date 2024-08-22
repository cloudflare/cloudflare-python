# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.firewall import RuleCreateResponse, FirewallRule, RuleEditResponse

from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.firewall import rule_create_params
from cloudflare.types.firewall import rule_update_params
from cloudflare.types.firewall import rule_list_params
from cloudflare.types.firewall import rule_get_params
from cloudflare.types.filters import FirewallFilter
from cloudflare.types.filters import FirewallFilter

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert_matches_type(Optional[RuleCreateResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
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
                    "expression": "(http.request.uri.path ~ \".*wp-login.php\" or http.request.uri.path ~ \".*xmlrpc.php\") and ip.addr ne 172.16.22.155",
                    "paused": False,
                    "ref": "FIL-100",
                },
            )

        assert_matches_type(Optional[RuleCreateResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = client.firewall.rules.with_raw_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with client.firewall.rules.with_streaming_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = response.parse()
                assert_matches_type(Optional[RuleCreateResponse], rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              client.firewall.rules.with_raw_response.create(
                  zone_identifier="",
                  action={},
                  filter={},
              )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.update(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.update(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
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
                    "expression": "(http.request.uri.path ~ \".*wp-login.php\" or http.request.uri.path ~ \".*xmlrpc.php\") and ip.addr ne 172.16.22.155",
                    "paused": False,
                    "ref": "FIL-100",
                },
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = client.firewall.rules.with_raw_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = response.parse()
        assert_matches_type(FirewallRule, rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with client.firewall.rules.with_streaming_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = response.parse()
                assert_matches_type(FirewallRule, rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              client.firewall.rules.with_raw_response.update(
                  id="372e67954025e0ba6aaa6d586b9e0b60",
                  zone_identifier="",
                  action={},
                  filter={},
              )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
              client.firewall.rules.with_raw_response.update(
                  id="",
                  zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                  action={},
                  filter={},
              )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(SyncV4PagePaginationArray[FirewallRule], rule, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                id="372e67954025e0ba6aaa6d586b9e0b60",
                action="block",
                description="mir",
                page=1,
                paused=False,
                per_page=5,
            )

        assert_matches_type(SyncV4PagePaginationArray[FirewallRule], rule, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = client.firewall.rules.with_raw_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[FirewallRule], rule, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with client.firewall.rules.with_streaming_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = response.parse()
                assert_matches_type(SyncV4PagePaginationArray[FirewallRule], rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              client.firewall.rules.with_raw_response.list(
                  zone_identifier="",
              )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.delete(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = client.firewall.rules.with_raw_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = response.parse()
        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with client.firewall.rules.with_streaming_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = response.parse()
                assert_matches_type(FirewallRule, rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              client.firewall.rules.with_raw_response.delete(
                  id="372e67954025e0ba6aaa6d586b9e0b60",
                  zone_identifier="",
              )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
              client.firewall.rules.with_raw_response.delete(
                  id="",
                  zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
              )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.edit(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(Optional[RuleEditResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = client.firewall.rules.with_raw_response.edit(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = response.parse()
        assert_matches_type(Optional[RuleEditResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with client.firewall.rules.with_streaming_response.edit(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = response.parse()
                assert_matches_type(Optional[RuleEditResponse], rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              client.firewall.rules.with_raw_response.edit(
                  id="372e67954025e0ba6aaa6d586b9e0b60",
                  zone_identifier="",
              )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
              client.firewall.rules.with_raw_response.edit(
                  id="",
                  zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
              )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.get(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                path_id="372e67954025e0ba6aaa6d586b9e0b60",
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = client.firewall.rules.get(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                path_id="372e67954025e0ba6aaa6d586b9e0b60",
                query_id="372e67954025e0ba6aaa6d586b9e0b60",
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = client.firewall.rules.with_raw_response.get(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                path_id="372e67954025e0ba6aaa6d586b9e0b60",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = response.parse()
        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with client.firewall.rules.with_streaming_response.get(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                path_id="372e67954025e0ba6aaa6d586b9e0b60",
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = response.parse()
                assert_matches_type(FirewallRule, rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
              client.firewall.rules.with_raw_response.get(
                  zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                  path_id="",
                  query_id="",
              )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              client.firewall.rules.with_raw_response.get(
                  zone_identifier="",
                  path_id="372e67954025e0ba6aaa6d586b9e0b60",
              )
class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert_matches_type(Optional[RuleCreateResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
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
                    "expression": "(http.request.uri.path ~ \".*wp-login.php\" or http.request.uri.path ~ \".*xmlrpc.php\") and ip.addr ne 172.16.22.155",
                    "paused": False,
                    "ref": "FIL-100",
                },
            )

        assert_matches_type(Optional[RuleCreateResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = await async_client.firewall.rules.with_raw_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = await response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            async with async_client.firewall.rules.with_streaming_response.create(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = await response.parse()
                assert_matches_type(Optional[RuleCreateResponse], rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              await async_client.firewall.rules.with_raw_response.create(
                  zone_identifier="",
                  action={},
                  filter={},
              )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.update(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.update(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
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
                    "expression": "(http.request.uri.path ~ \".*wp-login.php\" or http.request.uri.path ~ \".*xmlrpc.php\") and ip.addr ne 172.16.22.155",
                    "paused": False,
                    "ref": "FIL-100",
                },
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = await async_client.firewall.rules.with_raw_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = await response.parse()
        assert_matches_type(FirewallRule, rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            async with async_client.firewall.rules.with_streaming_response.update(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action={},
                filter={},
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = await response.parse()
                assert_matches_type(FirewallRule, rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              await async_client.firewall.rules.with_raw_response.update(
                  id="372e67954025e0ba6aaa6d586b9e0b60",
                  zone_identifier="",
                  action={},
                  filter={},
              )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
              await async_client.firewall.rules.with_raw_response.update(
                  id="",
                  zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                  action={},
                  filter={},
              )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], rule, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                id="372e67954025e0ba6aaa6d586b9e0b60",
                action="block",
                description="mir",
                page=1,
                paused=False,
                per_page=5,
            )

        assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], rule, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = await async_client.firewall.rules.with_raw_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], rule, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            async with async_client.firewall.rules.with_streaming_response.list(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = await response.parse()
                assert_matches_type(AsyncV4PagePaginationArray[FirewallRule], rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              await async_client.firewall.rules.with_raw_response.list(
                  zone_identifier="",
              )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.delete(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = await async_client.firewall.rules.with_raw_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = await response.parse()
        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            async with async_client.firewall.rules.with_streaming_response.delete(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = await response.parse()
                assert_matches_type(FirewallRule, rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              await async_client.firewall.rules.with_raw_response.delete(
                  id="372e67954025e0ba6aaa6d586b9e0b60",
                  zone_identifier="",
              )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
              await async_client.firewall.rules.with_raw_response.delete(
                  id="",
                  zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
              )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.edit(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert_matches_type(Optional[RuleEditResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = await async_client.firewall.rules.with_raw_response.edit(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = await response.parse()
        assert_matches_type(Optional[RuleEditResponse], rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            async with async_client.firewall.rules.with_streaming_response.edit(
                id="372e67954025e0ba6aaa6d586b9e0b60",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = await response.parse()
                assert_matches_type(Optional[RuleEditResponse], rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              await async_client.firewall.rules.with_raw_response.edit(
                  id="372e67954025e0ba6aaa6d586b9e0b60",
                  zone_identifier="",
              )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
              await async_client.firewall.rules.with_raw_response.edit(
                  id="",
                  zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
              )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.get(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                path_id="372e67954025e0ba6aaa6d586b9e0b60",
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            rule = await async_client.firewall.rules.get(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                path_id="372e67954025e0ba6aaa6d586b9e0b60",
                query_id="372e67954025e0ba6aaa6d586b9e0b60",
            )

        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        with pytest.warns(DeprecationWarning) :
            response = await async_client.firewall.rules.with_raw_response.get(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                path_id="372e67954025e0ba6aaa6d586b9e0b60",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        rule = await response.parse()
        assert_matches_type(FirewallRule, rule, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            async with async_client.firewall.rules.with_streaming_response.get(
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                path_id="372e67954025e0ba6aaa6d586b9e0b60",
            ) as response :
                assert not response.is_closed
                assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

                rule = await response.parse()
                assert_matches_type(FirewallRule, rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.warns(DeprecationWarning) :
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
              await async_client.firewall.rules.with_raw_response.get(
                  zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                  path_id="",
                  query_id="",
              )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
              await async_client.firewall.rules.with_raw_response.get(
                  zone_identifier="",
                  path_id="372e67954025e0ba6aaa6d586b9e0b60",
              )