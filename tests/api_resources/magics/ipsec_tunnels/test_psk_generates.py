# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magics.ipsec_tunnels import (
    PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPskGenerates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self, client: Cloudflare
    ) -> None:
        psk_generate = client.magics.ipsec_tunnels.psk_generates.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse, psk_generate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self, client: Cloudflare
    ) -> None:
        response = client.magics.ipsec_tunnels.psk_generates.with_raw_response.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        psk_generate = response.parse()
        assert_matches_type(
            PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse, psk_generate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self, client: Cloudflare
    ) -> None:
        with client.magics.ipsec_tunnels.psk_generates.with_streaming_response.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            psk_generate = response.parse()
            assert_matches_type(
                PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse,
                psk_generate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magics.ipsec_tunnels.psk_generates.with_raw_response.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magics.ipsec_tunnels.psk_generates.with_raw_response.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPskGenerates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        psk_generate = await async_client.magics.ipsec_tunnels.psk_generates.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse, psk_generate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.magics.ipsec_tunnels.psk_generates.with_raw_response.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        psk_generate = await response.parse()
        assert_matches_type(
            PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse, psk_generate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.magics.ipsec_tunnels.psk_generates.with_streaming_response.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            psk_generate = await response.parse()
            assert_matches_type(
                PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse,
                psk_generate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.psk_generates.with_raw_response.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magics.ipsec_tunnels.psk_generates.with_raw_response.magic_i_psec_tunnels_generate_pre_shared_key_psk_for_i_psec_tunnels(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
