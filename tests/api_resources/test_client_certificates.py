# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import (
    ClientCertificateUpdateResponse,
    ClientCertificateDeleteResponse,
    ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse,
    ClientCertificateClientCertificateForAZoneListClientCertificatesResponse,
    ClientCertificateGetResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import client_certificate_client_certificate_for_a_zone_create_client_certificate_params
from cloudflare.types import client_certificate_client_certificate_for_a_zone_list_client_certificates_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateUpdateResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(ClientCertificateUpdateResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.client_certificates.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(ClientCertificateUpdateResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            client.client_certificates.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.client_certificates.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            client.client_certificates.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_client_certificate_for_a_zone_create_client_certificate(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.client_certificate_for_a_zone_create_client_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        )
        assert_matches_type(
            ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse,
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_client_certificate_for_a_zone_create_client_certificate(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.client_certificate_for_a_zone_create_client_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(
            ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse,
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_client_certificate_for_a_zone_create_client_certificate(
        self, client: Cloudflare
    ) -> None:
        with client.client_certificates.with_streaming_response.client_certificate_for_a_zone_create_client_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(
                ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse,
                client_certificate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_client_certificate_for_a_zone_create_client_certificate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.client_certificate_for_a_zone_create_client_certificate(
                "",
                csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
                validity_days=3650,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_client_certificate_for_a_zone_list_client_certificates(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.client_certificate_for_a_zone_list_client_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_client_certificate_for_a_zone_list_client_certificates_with_all_params(
        self, client: Cloudflare
    ) -> None:
        client_certificate = client.client_certificates.client_certificate_for_a_zone_list_client_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            limit=10,
            offset=10,
            page=1,
            per_page=5,
            status="all",
        )
        assert_matches_type(
            Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_client_certificate_for_a_zone_list_client_certificates(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.client_certificate_for_a_zone_list_client_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(
            Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_client_certificate_for_a_zone_list_client_certificates(
        self, client: Cloudflare
    ) -> None:
        with client.client_certificates.with_streaming_response.client_certificate_for_a_zone_list_client_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(
                Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
                client_certificate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_client_certificate_for_a_zone_list_client_certificates(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.client_certificate_for_a_zone_list_client_certificates(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.client_certificates.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            client.client_certificates.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncClientCertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        client_certificate = await async_client.client_certificates.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateUpdateResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.client_certificates.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(ClientCertificateUpdateResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.client_certificates.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(ClientCertificateUpdateResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            await async_client.client_certificates.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        client_certificate = await async_client.client_certificates.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.client_certificates.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.client_certificates.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            await async_client.client_certificates.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_client_certificate_for_a_zone_create_client_certificate(
        self, async_client: AsyncCloudflare
    ) -> None:
        client_certificate = (
            await async_client.client_certificates.client_certificate_for_a_zone_create_client_certificate(
                "023e105f4ecef8ad9ca31a8372d0c353",
                csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
                validity_days=3650,
            )
        )
        assert_matches_type(
            ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse,
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_client_certificate_for_a_zone_create_client_certificate(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.client_certificates.with_raw_response.client_certificate_for_a_zone_create_client_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(
            ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse,
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_client_certificate_for_a_zone_create_client_certificate(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.client_certificates.with_streaming_response.client_certificate_for_a_zone_create_client_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(
                ClientCertificateClientCertificateForAZoneCreateClientCertificateResponse,
                client_certificate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_client_certificate_for_a_zone_create_client_certificate(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.client_certificate_for_a_zone_create_client_certificate(
                "",
                csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
                validity_days=3650,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_client_certificate_for_a_zone_list_client_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        client_certificate = (
            await async_client.client_certificates.client_certificate_for_a_zone_list_client_certificates(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )
        assert_matches_type(
            Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_client_certificate_for_a_zone_list_client_certificates_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        client_certificate = (
            await async_client.client_certificates.client_certificate_for_a_zone_list_client_certificates(
                "023e105f4ecef8ad9ca31a8372d0c353",
                limit=10,
                offset=10,
                page=1,
                per_page=5,
                status="all",
            )
        )
        assert_matches_type(
            Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_client_certificate_for_a_zone_list_client_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.client_certificates.with_raw_response.client_certificate_for_a_zone_list_client_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(
            Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
            client_certificate,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_client_certificate_for_a_zone_list_client_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.client_certificates.with_streaming_response.client_certificate_for_a_zone_list_client_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(
                Optional[ClientCertificateClientCertificateForAZoneListClientCertificatesResponse],
                client_certificate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_client_certificate_for_a_zone_list_client_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.client_certificate_for_a_zone_list_client_certificates(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        client_certificate = await async_client.client_certificates.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.client_certificates.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.client_certificates.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            await async_client.client_certificates.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
