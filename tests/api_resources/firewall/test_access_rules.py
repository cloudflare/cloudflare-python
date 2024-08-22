# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.firewall import AccessRuleCreateResponse, AccessRuleDeleteResponse, AccessRuleEditResponse, AccessRuleGetResponse

from typing import Any, cast, Optional

from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.firewall import access_rule_create_params
from cloudflare.types.firewall import access_rule_list_params
from cloudflare.types.firewall import access_rule_edit_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestAccessRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.create(
            configuration={},
            mode="block",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.create(
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:

        response = client.firewall.access_rules.with_raw_response.create(
            configuration={},
            mode="block",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = response.parse()
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.firewall.access_rules.with_streaming_response.create(
            configuration={},
            mode="block",
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = response.parse()
            assert_matches_type(AccessRuleCreateResponse, access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.firewall.access_rules.with_raw_response.create(
              configuration={},
              mode="block",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.firewall.access_rules.with_raw_response.create(
              configuration={},
              mode="block",
              account_id="account_id",
          )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.list(
            account_id="account_id",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            direction="asc",
            match="any",
            mode="block",
            notes="my note",
            order="configuration.target",
            page=1,
            per_page=20,
        )
        assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:

        response = client.firewall.access_rules.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.firewall.access_rules.with_streaming_response.list(
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[object], access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.firewall.access_rules.with_raw_response.list(
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.firewall.access_rules.with_raw_response.list(
              account_id="account_id",
          )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.delete(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.delete(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:

        response = client.firewall.access_rules.with_raw_response.delete(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = response.parse()
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.firewall.access_rules.with_streaming_response.delete(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = response.parse()
            assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          client.firewall.access_rules.with_raw_response.delete(
              identifier="",
              account_id="account_id",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.firewall.access_rules.with_raw_response.delete(
              identifier="de677e5818985db1285d0e80225f06e5",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.firewall.access_rules.with_raw_response.delete(
              identifier="de677e5818985db1285d0e80225f06e5",
              account_id="account_id",
          )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.edit(
            identifier="de677e5818985db1285d0e80225f06e5",
            configuration={},
            mode="block",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleEditResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.edit(
            identifier="de677e5818985db1285d0e80225f06e5",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleEditResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:

        response = client.firewall.access_rules.with_raw_response.edit(
            identifier="de677e5818985db1285d0e80225f06e5",
            configuration={},
            mode="block",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = response.parse()
        assert_matches_type(AccessRuleEditResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.firewall.access_rules.with_streaming_response.edit(
            identifier="de677e5818985db1285d0e80225f06e5",
            configuration={},
            mode="block",
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = response.parse()
            assert_matches_type(AccessRuleEditResponse, access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          client.firewall.access_rules.with_raw_response.edit(
              identifier="",
              configuration={},
              mode="block",
              account_id="account_id",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.firewall.access_rules.with_raw_response.edit(
              identifier="de677e5818985db1285d0e80225f06e5",
              configuration={},
              mode="block",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.firewall.access_rules.with_raw_response.edit(
              identifier="de677e5818985db1285d0e80225f06e5",
              configuration={},
              mode="block",
              account_id="account_id",
          )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.get(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleGetResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewall.access_rules.get(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleGetResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.firewall.access_rules.with_raw_response.get(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = response.parse()
        assert_matches_type(AccessRuleGetResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewall.access_rules.with_streaming_response.get(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = response.parse()
            assert_matches_type(AccessRuleGetResponse, access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          client.firewall.access_rules.with_raw_response.get(
              identifier="",
              account_id="account_id",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.firewall.access_rules.with_raw_response.get(
              identifier="de677e5818985db1285d0e80225f06e5",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.firewall.access_rules.with_raw_response.get(
              identifier="de677e5818985db1285d0e80225f06e5",
              account_id="account_id",
          )
class TestAsyncAccessRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.create(
            configuration={},
            mode="block",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.create(
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.firewall.access_rules.with_raw_response.create(
            configuration={},
            mode="block",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = await response.parse()
        assert_matches_type(AccessRuleCreateResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.create(
            configuration={},
            mode="block",
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = await response.parse()
            assert_matches_type(AccessRuleCreateResponse, access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.create(
              configuration={},
              mode="block",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.create(
              configuration={},
              mode="block",
              account_id="account_id",
          )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.list(
            account_id="account_id",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            direction="asc",
            match="any",
            mode="block",
            notes="my note",
            order="configuration.target",
            page=1,
            per_page=20,
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.firewall.access_rules.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.list(
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[object], access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.list(
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.list(
              account_id="account_id",
          )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.delete(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.delete(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.firewall.access_rules.with_raw_response.delete(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = await response.parse()
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.delete(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = await response.parse()
            assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.delete(
              identifier="",
              account_id="account_id",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.delete(
              identifier="de677e5818985db1285d0e80225f06e5",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.delete(
              identifier="de677e5818985db1285d0e80225f06e5",
              account_id="account_id",
          )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.edit(
            identifier="de677e5818985db1285d0e80225f06e5",
            configuration={},
            mode="block",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleEditResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.edit(
            identifier="de677e5818985db1285d0e80225f06e5",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="block",
            account_id="account_id",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(AccessRuleEditResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.firewall.access_rules.with_raw_response.edit(
            identifier="de677e5818985db1285d0e80225f06e5",
            configuration={},
            mode="block",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = await response.parse()
        assert_matches_type(AccessRuleEditResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.edit(
            identifier="de677e5818985db1285d0e80225f06e5",
            configuration={},
            mode="block",
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = await response.parse()
            assert_matches_type(AccessRuleEditResponse, access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.edit(
              identifier="",
              configuration={},
              mode="block",
              account_id="account_id",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.edit(
              identifier="de677e5818985db1285d0e80225f06e5",
              configuration={},
              mode="block",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.edit(
              identifier="de677e5818985db1285d0e80225f06e5",
              configuration={},
              mode="block",
              account_id="account_id",
          )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.get(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleGetResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewall.access_rules.get(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )
        assert_matches_type(AccessRuleGetResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.firewall.access_rules.with_raw_response.get(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_rule = await response.parse()
        assert_matches_type(AccessRuleGetResponse, access_rule, path=['response'])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.access_rules.with_streaming_response.get(
            identifier="de677e5818985db1285d0e80225f06e5",
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_rule = await response.parse()
            assert_matches_type(AccessRuleGetResponse, access_rule, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.get(
              identifier="",
              account_id="account_id",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.get(
              identifier="de677e5818985db1285d0e80225f06e5",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.firewall.access_rules.with_raw_response.get(
              identifier="de677e5818985db1285d0e80225f06e5",
              account_id="account_id",
          )