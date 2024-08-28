# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.devices.policies import (
    CertificateGetResponse,
    CertificateUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.devices.policies.certificates.update(
            zone_tag="699d98642c564d2e855e9661899b7252",
            enabled=True,
        )
        assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.certificates.with_raw_response.update(
            zone_tag="699d98642c564d2e855e9661899b7252",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.certificates.with_streaming_response.update(
            zone_tag="699d98642c564d2e855e9661899b7252",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_tag` but received ''"):
            client.zero_trust.devices.policies.certificates.with_raw_response.update(
                zone_tag="",
                enabled=True,
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.devices.policies.certificates.get(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.devices.policies.certificates.with_raw_response.get(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.devices.policies.certificates.with_streaming_response.get(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_tag` but received ''"):
            client.zero_trust.devices.policies.certificates.with_raw_response.get(
                "",
            )


class TestAsyncCertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.devices.policies.certificates.update(
            zone_tag="699d98642c564d2e855e9661899b7252",
            enabled=True,
        )
        assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.certificates.with_raw_response.update(
            zone_tag="699d98642c564d2e855e9661899b7252",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.certificates.with_streaming_response.update(
            zone_tag="699d98642c564d2e855e9661899b7252",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_tag` but received ''"):
            await async_client.zero_trust.devices.policies.certificates.with_raw_response.update(
                zone_tag="",
                enabled=True,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.devices.policies.certificates.get(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.devices.policies.certificates.with_raw_response.get(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.devices.policies.certificates.with_streaming_response.get(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_tag` but received ''"):
            await async_client.zero_trust.devices.policies.certificates.with_raw_response.get(
                "",
            )
