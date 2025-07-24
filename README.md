<div align="center">

# 🚀 Rich Run

[![GitHub License](https://img.shields.io/github/license/tanganke/rich-run)](https://github.com/tanganke/rich-run/blob/main/LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/rich-run)](https://pypi.org/project/rich-run/)
[![Downloads](https://static.pepy.tech/badge/rich-run/month)](https://pepy.tech/project/rich-run)
[![GitHub stars](https://img.shields.io/github/stars/tanganke/rich-run?style=social)](https://github.com/tanganke/rich-run)

**Transform your command-line experience with beautiful, informative output**

English | [中文](README.zh.md) | [日本語](README.ja.md)

</div>

Rich Run is a command-line wrapper that elevates your terminal experience by wrapping commands in elegant, colorful panels with timestamps, clear success/failure indicators, and beautiful formatting. Say goodbye to plain, boring command output!

## 📋 Table of Contents

- [✨ Features](#-features)
- [📦 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📸 Examples](#-examples)
- [🎯 Use Cases](#-use-cases)
- [🛠️ Development](#️-development)
- [❓ FAQ](#-faq)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

<div align="center">
<img src="docs/images/example.png" alt="Rich Run Demo" width="350">
</div>

## ✨ Features

- 🎨 **Beautiful Output**: Commands wrapped in elegant, colored panels
- ⏰ **Timestamps**: See exactly when your commands started and finished
- ✅ **Status Indicators**: Clear visual feedback for success/failure with exit codes
- 🌈 **Rich Formatting**: Leverages the powerful `rich` library for stunning terminal output
- 📦 **Easy Installation**: Install via pip or pipx with zero configuration
- 🚀 **Drop-in Replacement**: Simply prepend `rich-run` to any existing command
- 🔧 **Universal Compatibility**: Works with any command-line tool or script
- 📊 **Progress Visualization**: See command execution flow at a glance

## 📦 Installation

### Option 1: pipx (Recommended)

[pipx](https://pipx.pypa.io/) installs packages in isolated environments, preventing dependency conflicts:

```bash
# if pipx is not installed, you can install it first using `pip install pipx`
pipx install rich-run
```

### Option 2: pip

```bash
pip install rich-run
```

### Option 3: From Source

```bash
git clone https://github.com/tanganke/rich-run.git
cd rich-run
pip install -e .
```

> [!NOTE]  
> Rich Run depends on `rich-cli`. It will be automatically installed with the package, but if you encounter issues, you can install it manually:
>
> ```bash
> pipx install rich-cli  # or pip install rich-cli
> ```

## 🚀 Usage

Rich Run is designed to be a drop-in replacement for running any command. Simply prepend `rich-run` to your existing commands:

### Basic Syntax

```bash
rich-run <your-command-here>
```

### Quick Examples

```bash
# Simple commands
rich-run echo "Hello, Rich World!"
rich-run ls -la
rich-run pwd

# Python scripts
rich-run python my_script.py
rich-run python -c "print('Hello from Python!')"

# System commands
rich-run wget https://example.com/file.zip

# Complex commands with pipes and redirections (use quotes)
rich-run "ls -la | grep .py | wc -l"
rich-run "echo 'data' > output.txt && cat output.txt"
```

## 📸 Examples

### What You'll See

When you run a command with Rich Run, you get:

1. **📋 Command Panel**: A blue header showing the exact command and start timestamp
2. **📄 Clean Output**: Your command's output displayed clearly
3. **✅ Status Panel**: A colored footer with success/failure status and execution time

### Example Outputs

**Successful Command:**

```bash
rich-run echo "Success!"
```

Shows a green success panel with exit code 0.

**Failed Command:**

```bash
rich-run ls /nonexistent
```

Shows a red error panel with the actual exit code.

**Long-running Command:**

```bash
rich-run sleep 3 && echo "Done!"
```

Shows timestamps to track execution time.

## 🎯 Use Cases

Rich Run is perfect for:

- **📊 Monitoring Scripts**: Track execution status of automation scripts
- **🔍 Debugging**: Clearly see command success/failure in complex workflows
- **📚 Learning**: Better understand command execution and exit codes
- **🎨 Presentations**: Make terminal demos more visually appealing
- **📝 Documentation**: Generate clean, formatted command examples
- **🔧 CI/CD**: Enhance build script output readability
- **👥 Team Collaboration**: Share more informative command outputs

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/tanganke/rich-run.git
cd rich-run

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies (if you add them)
pip install -e ".[dev]"  # If you add dev dependencies to pyproject.toml
```

### Project Structure

```
rich-run/
├── rich_run/           # Main package
├── docs/               # Documentation assets
├── pyproject.toml      # Project configuration
└── README.md
```

## ❓ FAQ

<details>
<summary><strong>Q: Does Rich Run work with all commands?</strong></summary>

A: Yes! Rich Run works with any command-line tool, script, or binary. It simply wraps execution and formatting.
</details>

<details>
<summary><strong>Q: Can I use Rich Run in scripts and CI/CD?</strong></summary>

A: Absolutely! Rich Run preserves exit codes and works well in automated environments.
</details>

<details>
<summary><strong>Q: Does Rich Run affect command performance?</strong></summary>

A: The overhead is minimal - just the time to format and display panels.
</details>

<details>
<summary><strong>Q: Can I customize the output format?</strong></summary>

A: Currently, Rich Run uses a fixed format, but customization features may be added in future versions.
</details>

<details>
<summary><strong>Q: What if my command requires interactive input?</strong></summary>

A: Rich Run passes through stdin, so interactive commands work normally.
</details>

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Bug Reports**: Found an issue? [Open an issue](https://github.com/tanganke/rich-run/issues)
- 📝 **Documentation**: Help improve our docs
- 🔧 **Code**: Submit pull requests for bug fixes or new features

### Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests if applicable
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Rich](https://github.com/Textualize/rich)**: The amazing library that powers our beautiful terminal output
- **[Rich-CLI](https://github.com/Textualize/rich-cli)**: Command-line interface for Rich
- **Community**: Thanks to all contributors and users who help improve Rich Run
