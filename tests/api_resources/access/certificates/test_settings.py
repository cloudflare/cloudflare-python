# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.access.certificates import SettingUpdateResponse, SettingListResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access.certificates import setting_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        setting = client.access.certificates.settings.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
            ],
        )
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.certificates.settings.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.certificates.settings.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.certificates.settings.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                settings=[
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.certificates.settings.with_raw_response.update(
                "",
                account_or_zone="string",
                settings=[
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        setting = client.access.certificates.settings.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.access.certificates.settings.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.access.certificates.settings.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.certificates.settings.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.certificates.settings.with_raw_response.list(
                "",
                account_or_zone="string",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.access.certificates.settings.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
            ],
        )
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.certificates.settings.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.certificates.settings.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingUpdateResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.certificates.settings.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                settings=[
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.certificates.settings.with_raw_response.update(
                "",
                account_or_zone="string",
                settings=[
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.access.certificates.settings.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.certificates.settings.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.certificates.settings.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Optional[SettingListResponse], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.certificates.settings.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.certificates.settings.with_raw_response.list(
                "",
                account_or_zone="string",
            )
