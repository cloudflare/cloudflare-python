# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.stream import Audio

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudioTracks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        audio_track = client.stream.audio_tracks.delete(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(str, audio_track, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.audio_tracks.with_raw_response.delete(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio_track = response.parse()
        assert_matches_type(str, audio_track, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.audio_tracks.with_streaming_response.delete(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio_track = response.parse()
            assert_matches_type(str, audio_track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.audio_tracks.with_raw_response.delete(
                audio_identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.audio_tracks.with_raw_response.delete(
                audio_identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audio_identifier` but received ''"):
            client.stream.audio_tracks.with_raw_response.delete(
                audio_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @parametrize
    def test_method_copy(self, client: Cloudflare) -> None:
        audio_track = client.stream.audio_tracks.copy(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            label="director commentary",
        )
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    def test_method_copy_with_all_params(self, client: Cloudflare) -> None:
        audio_track = client.stream.audio_tracks.copy(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            label="director commentary",
            url="https://www.examplestorage.com/audio_file.mp3",
        )
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    def test_raw_response_copy(self, client: Cloudflare) -> None:
        response = client.stream.audio_tracks.with_raw_response.copy(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            label="director commentary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio_track = response.parse()
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    def test_streaming_response_copy(self, client: Cloudflare) -> None:
        with client.stream.audio_tracks.with_streaming_response.copy(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            label="director commentary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio_track = response.parse()
            assert_matches_type(Optional[Audio], audio_track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_copy(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.audio_tracks.with_raw_response.copy(
                identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="",
                label="director commentary",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.audio_tracks.with_raw_response.copy(
                identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                label="director commentary",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        audio_track = client.stream.audio_tracks.edit(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        audio_track = client.stream.audio_tracks.edit(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            default=True,
            label="director commentary",
        )
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.stream.audio_tracks.with_raw_response.edit(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio_track = response.parse()
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.stream.audio_tracks.with_streaming_response.edit(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio_track = response.parse()
            assert_matches_type(Optional[Audio], audio_track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.audio_tracks.with_raw_response.edit(
                audio_identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.audio_tracks.with_raw_response.edit(
                audio_identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audio_identifier` but received ''"):
            client.stream.audio_tracks.with_raw_response.edit(
                audio_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        audio_track = client.stream.audio_tracks.get(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Audio], audio_track, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.stream.audio_tracks.with_raw_response.get(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio_track = response.parse()
        assert_matches_type(SyncSinglePage[Audio], audio_track, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.stream.audio_tracks.with_streaming_response.get(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio_track = response.parse()
            assert_matches_type(SyncSinglePage[Audio], audio_track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.audio_tracks.with_raw_response.get(
                identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.audio_tracks.with_raw_response.get(
                identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAudioTracks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        audio_track = await async_client.stream.audio_tracks.delete(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(str, audio_track, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.audio_tracks.with_raw_response.delete(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio_track = await response.parse()
        assert_matches_type(str, audio_track, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.audio_tracks.with_streaming_response.delete(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio_track = await response.parse()
            assert_matches_type(str, audio_track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.delete(
                audio_identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.delete(
                audio_identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audio_identifier` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.delete(
                audio_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @parametrize
    async def test_method_copy(self, async_client: AsyncCloudflare) -> None:
        audio_track = await async_client.stream.audio_tracks.copy(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            label="director commentary",
        )
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    async def test_method_copy_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audio_track = await async_client.stream.audio_tracks.copy(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            label="director commentary",
            url="https://www.examplestorage.com/audio_file.mp3",
        )
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    async def test_raw_response_copy(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.audio_tracks.with_raw_response.copy(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            label="director commentary",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio_track = await response.parse()
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    async def test_streaming_response_copy(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.audio_tracks.with_streaming_response.copy(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            label="director commentary",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio_track = await response.parse()
            assert_matches_type(Optional[Audio], audio_track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_copy(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.copy(
                identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="",
                label="director commentary",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.copy(
                identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                label="director commentary",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        audio_track = await async_client.stream.audio_tracks.edit(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audio_track = await async_client.stream.audio_tracks.edit(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            default=True,
            label="director commentary",
        )
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.audio_tracks.with_raw_response.edit(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio_track = await response.parse()
        assert_matches_type(Optional[Audio], audio_track, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.audio_tracks.with_streaming_response.edit(
            audio_identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio_track = await response.parse()
            assert_matches_type(Optional[Audio], audio_track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.edit(
                audio_identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.edit(
                audio_identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `audio_identifier` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.edit(
                audio_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        audio_track = await async_client.stream.audio_tracks.get(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Audio], audio_track, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.audio_tracks.with_raw_response.get(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audio_track = await response.parse()
        assert_matches_type(AsyncSinglePage[Audio], audio_track, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.audio_tracks.with_streaming_response.get(
            identifier="ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audio_track = await response.parse()
            assert_matches_type(AsyncSinglePage[Audio], audio_track, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.get(
                identifier="ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.audio_tracks.with_raw_response.get(
                identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
