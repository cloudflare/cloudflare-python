# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access.certificates import CertificateSettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        setting = client.zero_trust.access.certificates.settings.update(
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                }
            ],
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        setting = client.zero_trust.access.certificates.settings.update(
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                }
            ],
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.certificates.settings.with_raw_response.update(
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                }
            ],
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.certificates.settings.with_streaming_response.update(
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                }
            ],
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SyncSinglePage[CertificateSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.settings.with_raw_response.update(
                settings=[
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    }
                ],
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.settings.with_raw_response.update(
                settings=[
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    }
                ],
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        setting = client.zero_trust.access.certificates.settings.get(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        setting = client.zero_trust.access.certificates.settings.get(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.certificates.settings.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.certificates.settings.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SyncSinglePage[CertificateSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.settings.with_raw_response.get(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.settings.with_raw_response.get(
                account_id="account_id",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.access.certificates.settings.update(
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                }
            ],
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.access.certificates.settings.update(
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                }
            ],
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.certificates.settings.with_raw_response.update(
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                }
            ],
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(AsyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.certificates.settings.with_streaming_response.update(
            settings=[
                {
                    "china_network": False,
                    "client_certificate_forwarding": True,
                    "hostname": "admin.example.com",
                }
            ],
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(AsyncSinglePage[CertificateSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.settings.with_raw_response.update(
                settings=[
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    }
                ],
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.settings.with_raw_response.update(
                settings=[
                    {
                        "china_network": False,
                        "client_certificate_forwarding": True,
                        "hostname": "admin.example.com",
                    }
                ],
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.access.certificates.settings.get(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        setting = await async_client.zero_trust.access.certificates.settings.get(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.certificates.settings.with_raw_response.get(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(AsyncSinglePage[CertificateSettings], setting, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.certificates.settings.with_streaming_response.get(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(AsyncSinglePage[CertificateSettings], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.settings.with_raw_response.get(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.settings.with_raw_response.get(
                account_id="account_id",
            )
