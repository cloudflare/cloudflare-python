# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers import AIRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_1(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_1(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_1(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                text="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_2(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params_overload_2(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
            guidance=0,
            image=[0, 0, 0],
            mask=[0, 0, 0],
            num_steps=0,
            strength=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_2(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_2(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                prompt="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_3(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sentences=["string", "string", "string"],
            source="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_3(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sentences=["string", "string", "string"],
            source="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_3(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sentences=["string", "string", "string"],
            source="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                sentences=["string", "string", "string"],
                source="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sentences=["string", "string", "string"],
                source="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_4(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_4(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_4(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                text="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_5(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_5(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_5(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_6(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params_overload_6(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_6(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_6(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_7(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_7(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_7(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_8(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params_overload_8(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_8(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_8(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_9(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_9(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_9(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_10(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params_overload_10(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_10(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_10(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_11(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params_overload_11(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
            lora="string",
            max_tokens=0,
            raw=True,
            stream=True,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_11(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_11(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                prompt="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_12(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
            ],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params_overload_12(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
            ],
            max_tokens=0,
            stream=True,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_12(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_12(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "string",
                    },
                    {
                        "content": "string",
                        "role": "string",
                    },
                    {
                        "content": "string",
                        "role": "string",
                    },
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                messages=[
                    {
                        "content": "string",
                        "role": "string",
                    },
                    {
                        "content": "string",
                        "role": "string",
                    },
                    {
                        "content": "string",
                        "role": "string",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_13(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="string",
            text="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params_overload_13(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="string",
            text="string",
            source_lang="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_13(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="string",
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_13(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="string",
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                target_lang="string",
                text="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_lang="string",
                text="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_14(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params_overload_14(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="string",
            max_length=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_14(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_14(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                input_text="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                input_text="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_15(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_15(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_15(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_15(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_run_overload_16(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params_overload_16(self, client: Cloudflare) -> None:
        ai = client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
            max_tokens=0,
            prompt="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_overload_16(self, client: Cloudflare) -> None:
        response = client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_overload_16(self, client: Cloudflare) -> None:
        with client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_run_overload_16(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAI:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                text="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
            guidance=0,
            image=[0, 0, 0],
            mask=[0, 0, 0],
            num_steps=0,
            strength=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                prompt="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sentences=["string", "string", "string"],
            source="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sentences=["string", "string", "string"],
            source="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            sentences=["string", "string", "string"],
            source="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                sentences=["string", "string", "string"],
                source="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                sentences=["string", "string", "string"],
                source="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                text="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
            lora="string",
            max_tokens=0,
            raw=True,
            stream=True,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                prompt="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_12(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
            ],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
            ],
            max_tokens=0,
            stream=True,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
                {
                    "content": "string",
                    "role": "string",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "string",
                    },
                    {
                        "content": "string",
                        "role": "string",
                    },
                    {
                        "content": "string",
                        "role": "string",
                    },
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                messages=[
                    {
                        "content": "string",
                        "role": "string",
                    },
                    {
                        "content": "string",
                        "role": "string",
                    },
                    {
                        "content": "string",
                        "role": "string",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_13(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="string",
            text="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="string",
            text="string",
            source_lang="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="string",
            text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="string",
            text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                target_lang="string",
                text="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_lang="string",
                text="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_14(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="string",
            max_length=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                input_text="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                input_text="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_15(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_15(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_15(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=b"raw file contents",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_overload_16(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.workers.ai.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0, 0, 0],
            max_tokens=0,
            prompt="string",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.ai.with_raw_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_overload_16(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.ai.with_streaming_response.run(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_run_overload_16(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.workers.ai.with_raw_response.run(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
