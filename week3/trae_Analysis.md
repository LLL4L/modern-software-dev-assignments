# CS146 Week 3 作业分析：构建自定义 MCP Server

## 作业目标

设计和实现一个 **Model Context Protocol (MCP) 服务器**，包装一个真实的外部 API。

---

## 学习目标 (Learning Goals)

通过完成这个作业，你将学会：

| 技能 | 说明 |
|------|------|
| **MCP 核心能力** | 理解 MCP 的 tools、resources、prompts 三大核心概念 |
| **工具定义** | 实现带有类型参数和健壮错误处理的 MCP 工具 |
| **最佳实践** | 遵循日志记录和传输最佳实践（STDIO 服务器不使用 stdout） |
| **授权流程** | 可选：为 HTTP 传输实现授权流程（OAuth2/API Key） |

---

## 作业要求

1. **选择外部 API**：天气、GitHub Issues、Notion、电影数据库、日历、任务管理、金融/加密货币、旅行、体育数据等
2. **暴露至少 2 个 MCP 工具**
3. **实现基本弹性**：
   - 优雅处理 HTTP 失败、超时和空结果
   - 尊重 API 速率限制（简单退避或用户警告）
4. **打包和文档**：
   - 清晰的设置说明、环境变量和运行命令
   - 示例调用流程
5. **选择部署模式**：
   - **本地模式**：STDIO 服务器，可被 Claude Desktop 或 Cursor 发现
   - **远程模式**：HTTP 服务器，可被 MCP 客户端调用（更难，但有额外加分）

---

## 交付物

```
week3/
├── server/          # 源代码（建议 main.py 或 app.py 作为入口）
└── README.md        # 包含：
                     #   - 前置条件、环境设置、运行说明
                     #   - MCP 客户端配置方法
                     #   - 工具参考文档
```

---

## 评分标准 (90分)

| 类别 | 分值 | 说明 |
|------|------|------|
| **功能性** | 35分 | 实现 2+ 工具，正确的 API 集成，有意义的输出 |
| **可靠性** | 20分 | 输入验证、错误处理、日志记录、速率限制意识 |
| **开发者体验** | 20分 | 清晰的设置/文档，易于本地运行，合理的文件夹结构 |
| **代码质量** | 15分 | 可读代码，描述性命名，最小复杂度，类型提示 |
| **额外加分** | 10分 | +5 远程 HTTP MCP 服务器；+5 正确实现认证 |

---

## 有用资源

- [MCP Server Quickstart](https://modelcontextprotocol.io/quickstart/server)
- [MCP Authorization (HTTP)](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- [Remote MCP on Cloudflare](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)
- [Deploy MCP Servers to Vercel](https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel)

---

## 建议的 API 选择

- **天气 API**（OpenWeatherMap）- 简单、文档完善
- **GitHub API** - 熟悉度高，无需额外注册
- **电影数据库**（TMDB）- 有趣且实用

test-4.16