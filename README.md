# Things 3 MCP Server

[![smithery badge](https://smithery.ai/badge/@vimtor/things-3)](https://smithery.ai/server/@vimtor/things-3)

A Model Context Protocol (MCP) server for interacting with Things 3, allowing you to manage todos and projects.

## Features

- Search across todos, projects and areas
- Create todos and projects
- Update existing todos and projects

## Installation

1. Ensure you have Python 3.8+ installed
2. Install UV if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
3. Install the required dependencies:
   ```bash
   uv pip install -e .
   ```
4. Set up your Things 3 token as an environment variable:
   ```bash
   export THINGS_TOKEN='your-token-here'
   ```

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
