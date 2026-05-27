# Week 7 – Exploring AI Code Review Using Graphite

> **中文翻译：** 第七周 — 使用 Graphite 探索 AI 代码审查（Code Review）

## Assignment Overview

> **中文翻译：** 作业概述

In this assignment, you will practice agent-driven development and AI-assisted code review on a more advanced codebase. You will implement the tasks in `week7/docs/TASKS.md`, validate your work with tests and manual review, and compare your own review notes with AI-generated code reviews.

> **中文翻译：** 在本次作业中，你将在一个更高级的代码库上练习代理驱动开发（agent-driven development）和 AI 辅助代码审查（AI-assisted code review）。你将实现 `week7/docs/TASKS.md` 中的任务，通过测试和手动审查来验证你的工作，并将你自己的审查笔记与 AI 生成的代码审查进行对比。

## Get Started with Graphite

> **中文翻译：** 开始使用 Graphite

1. Sign up for Graphite: https://app.graphite.dev/signup
2. Upon sign up, you can claim your 30-day free trial.
3. After the 30 days, you can use code **CS146S** to claim free Graphite under their education program.

> **中文翻译：**
> 1. 注册 Graphite：https://app.graphite.dev/signup
> 2. 注册后，你可以申请 30 天免费试用。
> 3. 30 天后，你可以使用代码 **CS146S** 通过他们的教育计划免费使用 Graphite。


## What to do

> **中文翻译：** 要做什么

Implement the tasks from `week7/docs/TASKS.md` using an AI coding tool of your choice (e.g. Cursor, Copilot, Claude, etc.).

> **中文翻译：** 使用你选择的 AI 编码工具（如 Cursor、Copilot、Claude 等）实现 `week7/docs/TASKS.md` 中的任务。

### For each task:

> **中文翻译：** 对于每个任务：

   1. Create a separate branch.
   2. Implement the task with your AI tool using a 1-shot prompt.
   3. Manually review the changes line-by-line. Fix issues you notice and add explanatory commit messages where helpful. You may also pair with a classmate to review each other's code instead of reviewing your own changes.
   4. Open a Pull Request (PR) for the task. Ensure your PRs include:
      - Description of the problem and your approach.
      - Summary of testing performed (include commands and results) and any added/updated tests.
      - Notable tradeoffs, limitations, or follow-ups.
   5. Use Graphite Diamond to generate an AI-assisted code review on the PR.
   6. Document the results of your PR in the `writeup.md`.

> **中文翻译：**
> 1. 创建一个独立的分支（branch）。
> 2. 使用你的 AI 工具通过单次提示词（1-shot prompt）实现任务。
> 3. 逐行手动审查更改。修复你发现的问题，并在有帮助的地方添加解释性的提交消息（commit messages）。你也可以与同学结对审查彼此的代码，而不是审查自己的更改。
> 4. 为任务开启一个 Pull Request（PR）。确保你的 PR 包含：
>    - 问题描述和你的方案。
>    - 执行的测试摘要（包括命令和结果）以及任何添加/更新的测试。
>    - 值得注意的权衡（tradeoffs）、限制（limitations）或后续事项（follow-ups）。
> 5. 使用 Graphite Diamond 在 PR 上生成 AI 辅助代码审查。
> 6. 在 `writeup.md` 中记录你的 PR 结果。


## Deliverables

> **中文翻译：** 交付物

In your `writeup.md`, we are looking for the follwoing:

> **中文翻译：** 在你的 `writeup.md` 中，我们需要看到以下内容：

- Four PRs, one per completed task, each with:
  - Clear PR description
  - Links to relevant commits/issues.
  - Graphite Diamond AI review comments visible on the PR

> **中文翻译：**
> - 四个 PR，每个完成的任务一个，每个包含：
>   - 清晰的 PR 描述
>   - 相关提交/issues 的链接
>   - 在 PR 上可见的 Graphite Diamond AI 审查评论

- A brief reflection addressing the following:
  - The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).
  - A comparison of **your** comments vs. **Graphite's** AI-generated comments for each PR.
  - When the AI reviews were better/worse than yours (cite specific examples)
  - Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.

> **中文翻译：**
> - 一篇简短的反思（reflection），涉及以下内容：
>   - 你在手动审查中通常做出的评论类型（例如：正确性、性能、安全、命名、测试缺口（test gaps）、API 形态（API shape）、用户体验（UX）、文档）。
>   - **你的**评论与 **Graphite 的** AI 生成评论在每个 PR 上的对比。
>   - AI 审查在哪些方面比你的更好/更差（引用具体示例）
>   - 你未来对信任 AI 审查的舒适度，以及何时依赖它们的经验法则（heuristics）。

## Evaluation criteria (100 points total)

> **中文翻译：** 评分标准（总分 100 分）

- 20 points per completed task
  - Technical correctness and completeness of each task.
  - Code quality: readability, naming, structure, error handling, and tests.
  - Thoughtfulness and depth of manual review notes
  - Graphite Diamond AI generated code review
- 20 points for the brief reflection
  - Insightful comparison between your review and Graphite's AI review
  - Description of your personal comfort level with AI Reviews

> **中文翻译：**
> - 每个完成的任务 20 分
>   - 每个任务的技术正确性和完整性。
>   - 代码质量：可读性、命名、结构、错误处理和测试。
>   - 手动审查笔记的深度和周全性
>   - Graphite Diamond AI 生成的代码审查
> - 简短反思 20 分
>   - 对你的审查和 Graphite AI 审查之间有深度的对比
>   - 描述你对 AI 审查的个人舒适度


## Submission Instructions

> **中文翻译：** 提交说明

1. Make sure you have all changes pushed to your remote repository for grading.
2. Make sure you've added both brentju and febielin as collaborators on your assignment repository.
2. Submit via Gradescope.

> **中文翻译：**
> 1. 确保你已将所有更改推送到远程仓库以便评分。
> 2. 确保你已将 brentju 和 febielin 添加为你的作业仓库的协作者（collaborators）。
> 2. 通过 Gradescope 提交。
