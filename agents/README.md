# Platform Engineering Agent

AI agent specialized in platform engineering tasks with expertise in AWS, Terraform, Python, Kubernetes, and GitHub Actions.

## Features

- Infrastructure-as-code development and optimization
- Container orchestration and Kubernetes management
- CI/CD pipeline design and troubleshooting
- Cloud architecture and AWS services
- Web development support (PHP, Sass, HTMX, JavaScript)

## Resources Loaded

The agent automatically loads rules and documentation from:

- **Project Documentation**: `README.md`, `README.*.md`, `docs/**/*.md`
- **Cursor Rules**: `.cursor/rules/*.md`
- **Agent Documentation**: `AGENTS.md`
- **Shared Platform Rules**: `/opt/platform-rules/*.md`
- **Local Rules**: `.amazonq/rules/**/*.md`

## Tools Available

- File operations (`fs_read`, `fs_write`)
- Bash command execution
- AWS CLI integration
- AWS documentation lookup
- HTTP fetch capabilities

## Usage

```bash
q chat --agent platform-engineering
```

The agent strictly follows all coding standards and best practices defined in the loaded rule files, with particular attention to organizational standards that override general practices.
