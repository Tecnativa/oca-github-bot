# Copyright 2021 Tecnativa - Víctor Martínez
# Distributed under the MIT License (http://opensource.org/licenses/MIT).

import pytest

from oca_github_bot.tasks.migration_issue_bot import (
    _create_or_find_branch_milestone,
    _find_issue,
    _set_lines_issue,
)


def _get_repository(gh, org, repo):
    return gh.repository(org, repo)


@pytest.mark.vcr()
def test_create_or_find_branch_milestone(gh):
    repo = _get_repository(gh, "OCA", "contract")
    milestone = _create_or_find_branch_milestone(repo, "8.0")
    assert milestone.name == "8.0"


@pytest.mark.vcr()
def test_find_issue(gh):
    repo = _get_repository(gh, "OCA", "contract")
    milestone = _create_or_find_branch_milestone(repo, "8.0")
    issue = _find_issue(repo, milestone, "14.0")
    assert issue.name == "Migration to version 14.0"


@pytest.mark.vcr()
def test_set_lines_issue(gh):
    repo = _get_repository(gh, "OCA", "contract")
    milestone = _create_or_find_branch_milestone(repo, "13.0")
    issue = _find_issue(repo, milestone, "14.0")
    lines = _set_lines_issue(gh, issue, "contract")
    assert len(lines) > 0