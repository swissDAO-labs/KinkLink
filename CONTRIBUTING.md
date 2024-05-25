# Contributing to KinkLink

Thank you for considering contributing to KinkLink! Your involvement is highly appreciated.

## Creating A Pull Request

0. A PR should address one thing, and one thing only.
1. Fork the repository or create a new branch directly from the target branch to work on your changes.
2. Ensure the branch name follows kebab-case with no more than two or three words. The branch name should be prefixed with one of these tags as shown in these examples:
   - `feat/new-feature`
   - `fix/zero-day-exploit`
   - `test/some-feature`
   - `refactor/extract-function`
   - `docs/user-manual`
   - `chore/bump-package`
3. When opening a PR ensure that you are targetting the correct base branch.
4. Include a description that enables reviewers to easily understand the purpose of the PR. Tag relevant issues and PRs, and comment on non-obvious code changes to avoid confusion and expedite the review process.
5. In case of bug fixes, create a ticket first, explaining the issue, and accompany it with a PR that demonstrates the problem. If you have suggestions on how to address the issue, please include these. Only proceed with submitting a PR to address the issue after the associated ticket has been approved.
6. Run the test suite to confirm that your changes do not break existing functionality.
7. Update or add necessary documentation for your changes, ensuring it aligns with the code modifications made in the PR.
8. Ensure your code passes linting and formatting checks.


## Best Coding Practices

When contributing to KinkLink, consider the following best coding practices to ensure the quality and maintainability of the codebase:

1. **Adhere to the Single Responsibility Principle (SRP):** Not only should we aim to have each function, class, or module focused on a single responsibility, the PR itself should follow the Single Responsibility Principle. Each PR should have a single, clear purpose, whether it's introducing a new feature, fixing a bug, or addressing a specific concern.

2.  **Version Control Etiquette:** Adhere to best practices when using Git. Commit small, logical changes with clear commit messages. This helps in tracking and understanding the evolution of the codebase.

3. **Keep It Simple, Stupid (KISS):** Embrace simplicity in your code. Strive for clarity and straightforward solutions without unnecessary complexity. Prioritize code clarity over cleverness. Embrace an iterative development approach. Start with a simple, functional solution, and iteratively refine it based on feedback and evolving requirements. Regular refactoring ensures the code remains clean and adaptable.

4.  **Concise and Purposeful Documentation:** Document code sparingly and focus on adding value. Avoid redundant information that merely restates what is evident from the code itself. Documentation should provide insights, explanations, or considerations not immediately apparent in the code.

5.  **Effective Error Handling:** Implement robust error-handling strategies to gracefully manage exceptions. Be mindful of constructs that resemble GOTO statements, as they can introduce additional control flow complexities. In situations where multiple layers of code handle similar exceptions, exercise caution to avoid the possibility of unintended control flow execution. For instance, a function deep in the call stack may encounter an exception. If higher-level code catches this exception without distinguishing the context, this will lead to unexpected behavior. Consider adopting a robust error-handling approach, such as the Railway-Oriented Programming paradigm. This involves functions returning a result type indicating success or failure. This separation of the "happy path" from error handling enhances code clarity and maintainability.

6. **Minimize Dependencies:** Aim to reduce additional dependencies to reduce complexity, facilitate maintainance and reduce the risk of security vulnerabilities. Explore existing tools and libraries within the project's ecosystem to fulfill your requirements efficiently. Leverage language-specific features and built-in modules to achieve functionality without unnecessary external dependencies.

7. **Use Stateless Over Stateful Objects:** Whenever possible, opt for stateless functions over stateful classes. Stateless code is generally easier to reason about and test.

8. **Embrace Immutability:** Opt for immutable objects, particularly in data structures, to enhance code reliability. Immutability reduces complexity, minimizes bugs, and mitigates unexpected side effects. It ensures thread safety, facilitates hashing and caching, simplifies serialization and deserialization, and eliminates unintended side effects.

9.  **Prefer Composition Over Inheritance:** Favor composition as a design principle. This approach leads to more flexible and maintainable code compared to heavy reliance on inheritance.

10. **Explicit Type Definitions:** Ensure clarity in variable, function parameter, and return type definitions, particularly in dynamically typed languages. Explicitly define types to enhance code understanding and avoid ambiguity. In languages without strict type enforcement providing explicit type information becomes crucial. When annotating types of containers, ensure to specify their content type as well, otherwise this can lead to ambiguity and hinder effective type checking.

11. **Model Data Objects Using Type-Checked Structures:** When defining data objects, leverage language-specific constructs, such as enums and dedicated structures tailored for modeling data, to ensure a robust and type-checked approach. This practice not only enhances data integrity but also reduces the likelihood of runtime errors.

12.  **Avoid Indentation:** Minimize the level of indentation in your code. Deeply nested structures can make the code harder to read and understand.
