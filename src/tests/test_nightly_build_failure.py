"""
Intentional failing test to verify nightly build failure path.

When the nightly workflow runs (schedule or workflow_dispatch):
- This test fails → test job fails
- build-and-push is skipped (needs: test)
- notify-on-failure runs and sends email (if ETHEREAL_* secrets are set)

Delete this file (or remove/skip this test) after verifying the pipeline.
"""

import pytest


def test_nightly_build_failure_intentional_remove_after_verification():
    """Fail on purpose to verify: nightly fails, no image push, notification sent."""
    pytest.fail(
        "INTENTIONAL: Nightly build failure test. "
        "Delete src/tests/test_nightly_build_failure.py after verifying pipeline."
    )
