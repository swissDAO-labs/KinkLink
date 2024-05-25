# Git Hooks Philosophy

The git hooks plays a critical role in maintaining code quality. However, it's equally important to acknowledge that client-side hooks should be minimally invasive, allowing developers to maintain control over their workflow to their discretion.

## Pre-commit

To strike this balance, we utilize the `pre-commit` tool along with custom hooks defined in the local `.pre-commit-config.yaml`. This tool enables us to perform linting and formatting checks pre-commit, ensuring code consistency, catching errors early, and reducing the need for post-hoc clean-up tasks. Automated fixes are applied whenever possible, streamlining development and enhancing overall code quality.

The pre-commit hook also includes checks to prevent the inadvertent leakage of sensitive information like API keys and secrets, leveraging the `gitleaks` tool. This ensures that such sensitive data is never inadvertently committed, safeguarding against potential security breaches.

## Commit-msg

The commit-msg hook enforces a specific prefix format for commit messages, such as "feat|fix|test|refactor|docs|chore". This format corresponds to different types of changes and aids the review process by categorizing commits, as well as help trace issues back to their origin more easily. Since these tags cannot easily be added after the fact, enforcing them locally on each commit message minimizes overhead and ensures consistency in commit message formatting.

## Pre-push

The pre-push hook performs additional security checks and runs the test suite locally. By conducting these checks before pushing code to the remote repository, developers can catch issues early and avoid unnecessary delays on shared CI resources.
