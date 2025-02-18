# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access import (
    Certificate,
    CertificateDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.create(
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            account_id="account_id",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.create(
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            account_id="account_id",
            associated_hostnames=["admin.example.com"],
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.certificates.with_raw_response.create(
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.certificates.with_streaming_response.create(
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[Certificate], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.create(
                certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
                name="Allow devs",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.create(
                certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
                name="Allow devs",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.update(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            associated_hostnames=["admin.example.com"],
            account_id="account_id",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.update(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            associated_hostnames=["admin.example.com"],
            account_id="account_id",
            name="Allow devs",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.certificates.with_raw_response.update(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            associated_hostnames=["admin.example.com"],
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.certificates.with_streaming_response.update(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            associated_hostnames=["admin.example.com"],
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[Certificate], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.zero_trust.access.certificates.with_raw_response.update(
                certificate_id="",
                associated_hostnames=["admin.example.com"],
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.update(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                associated_hostnames=["admin.example.com"],
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.update(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                associated_hostnames=["admin.example.com"],
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.certificates.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SyncSinglePage[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.certificates.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SyncSinglePage[Certificate], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.certificates.with_raw_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.certificates.with_streaming_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.zero_trust.access.certificates.with_raw_response.delete(
                certificate_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.delete(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.delete(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.access.certificates.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.certificates.with_raw_response.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.certificates.with_streaming_response.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[Certificate], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.zero_trust.access.certificates.with_raw_response.get(
                certificate_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.get(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            client.zero_trust.access.certificates.with_raw_response.get(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )


class TestAsyncCertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.create(
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            account_id="account_id",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.create(
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            account_id="account_id",
            associated_hostnames=["admin.example.com"],
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.certificates.with_raw_response.create(
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.certificates.with_streaming_response.create(
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[Certificate], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.create(
                certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
                name="Allow devs",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.create(
                certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
                name="Allow devs",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.update(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            associated_hostnames=["admin.example.com"],
            account_id="account_id",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.update(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            associated_hostnames=["admin.example.com"],
            account_id="account_id",
            name="Allow devs",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.certificates.with_raw_response.update(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            associated_hostnames=["admin.example.com"],
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.certificates.with_streaming_response.update(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            associated_hostnames=["admin.example.com"],
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[Certificate], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.zero_trust.access.certificates.with_raw_response.update(
                certificate_id="",
                associated_hostnames=["admin.example.com"],
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.update(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                associated_hostnames=["admin.example.com"],
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.update(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                associated_hostnames=["admin.example.com"],
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.certificates.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(AsyncSinglePage[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.certificates.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(AsyncSinglePage[Certificate], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.list(
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.list(
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.certificates.with_raw_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.certificates.with_streaming_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.zero_trust.access.certificates.with_raw_response.delete(
                certificate_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.delete(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.delete(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.access.certificates.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.certificates.with_raw_response.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[Certificate], certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.certificates.with_streaming_response.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[Certificate], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.zero_trust.access.certificates.with_raw_response.get(
                certificate_id="",
                account_id="account_id",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.get(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"You must provide either account_id or zone_id"):
            await async_client.zero_trust.access.certificates.with_raw_response.get(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="account_id",
            )
