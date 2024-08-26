# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.dns import SettingEditResponse, SettingGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dns import setting_edit_params
from cloudflare.types.dns import DNSSetting

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        setting = client.dns.settings.edit(
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        setting = client.dns.settings.edit(
            account_id="account_id",
            zone_defaults={
                "foundation_dns": False,
                "multi_provider": False,
                "nameservers": {
                    "type": "cloudflare.standard"
                },
                "ns_ttl": 86400,
                "secondary_overrides": False,
                "soa": {
                    "expire": 604800,
                    "min_ttl": 1800,
                    "mname": "kristina.ns.cloudflare.com",
                    "refresh": 10000,
                    "retry": 2400,
                    "rname": "admin.example.com",
                    "ttl": 3600,
                },
                "zone_mode": "standard",
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:

        response = client.dns.settings.with_raw_response.edit(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        setting = response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.dns.settings.with_streaming_response.edit(
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            setting = response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.dns.settings.with_raw_response.edit(
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.dns.settings.with_raw_response.edit(
              account_id="account_id",
          )

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        setting = client.dns.settings.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingGetResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        setting = client.dns.settings.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingGetResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.dns.settings.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        setting = response.parse()
        assert_matches_type(Optional[SettingGetResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns.settings.with_streaming_response.get(
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            setting = response.parse()
            assert_matches_type(Optional[SettingGetResponse], setting, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.dns.settings.with_raw_response.get(
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.dns.settings.with_raw_response.get(
              account_id="account_id",
          )
class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.dns.settings.edit(
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.dns.settings.edit(
            account_id="account_id",
            zone_defaults={
                "foundation_dns": False,
                "multi_provider": False,
                "nameservers": {
                    "type": "cloudflare.standard"
                },
                "ns_ttl": 86400,
                "secondary_overrides": False,
                "soa": {
                    "expire": 604800,
                    "min_ttl": 1800,
                    "mname": "kristina.ns.cloudflare.com",
                    "refresh": 10000,
                    "retry": 2400,
                    "rname": "admin.example.com",
                    "ttl": 3600,
                },
                "zone_mode": "standard",
            },
        )
        assert_matches_type(Optional[SettingEditResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.dns.settings.with_raw_response.edit(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        setting = await response.parse()
        assert_matches_type(Optional[SettingEditResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.settings.with_streaming_response.edit(
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            setting = await response.parse()
            assert_matches_type(Optional[SettingEditResponse], setting, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.dns.settings.with_raw_response.edit(
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.dns.settings.with_raw_response.edit(
              account_id="account_id",
          )

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.dns.settings.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingGetResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.dns.settings.get(
            account_id="account_id",
        )
        assert_matches_type(Optional[SettingGetResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.dns.settings.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        setting = await response.parse()
        assert_matches_type(Optional[SettingGetResponse], setting, path=['response'])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.settings.with_streaming_response.get(
            account_id="account_id",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            setting = await response.parse()
            assert_matches_type(Optional[SettingGetResponse], setting, path=['response'])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.dns.settings.with_raw_response.get(
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.dns.settings.with_raw_response.get(
              account_id="account_id",
          )