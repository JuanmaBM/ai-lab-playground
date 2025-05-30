# 🛠️ Tool Calling With MCP

This repository demonstrates how to integrate **Llama Stack** with **MCP (Modular Command Provider)** to enable tool calling in large language models (LLMs), using realistic scenarios. It includes examples of:

* Basic tool use with local tools.
* Chaining tools based on user input.
* Advanced tool use with Kubernetes via a custom client.
* Serving tools via an MCP server over HTTP.

You should start with basic tool use case and then jump to the kubernetes use case notebook

## 📋 Requirements

Before getting started, make sure you have the following installed:

* [Python 3.12+](https://www.python.org/downloads/)
* [Ollama](https://ollama.com) – for local model serving (e.g., `llama3.2:3b-instruct-fp16`)
* [uv](https://github.com/astral-sh/uv) – for fast and reliable Python dependency management
* [Llama Stack CLI](https://github.com/llamaindex/llama-stack) – for managing LLM agents and environments
* [Minikube](https://minikube.sigs.k8s.io/docs/start/) – for the Kubernetes integration example

## 🧰 Installation

First, build your Llama Stack environment using `uv`:

```bash
uv run --with llama-stack llama stack build --template ollama --image-type venv --image-name venv
source venv/bin/activate
uv pip install --reinstall -r requirements.txt
```

## 🚀 Running the MCP Server

To serve tools via HTTP using the MCP server:

```bash
python mcp_server.py
```

This allows LLMs to dynamically access tools over a networked interface, simulating production-level infrastructure.

## ☘️ Minikube Setup

To run the Kubernetes tool integration example, you need a running local Kubernetes cluster with `minikube`. Here's how to get started:

1. **Install minikube:**
   Follow the instructions for your OS at [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)

2. **Start your local cluster:**

   ```bash
   minikube start
   ```

3. **Verify it's working:**

   ```bash
   kubectl get nodes
   ```

4. Make sure your environment is authenticated

## 🤝 Contributing

Contributions are welcome! Feel free to:

* Open issues for bugs or feature suggestions.
* Submit pull requests with improvements or new use cases.
* Suggest better tool implementations or integrations.

Before submitting a PR, make sure your code is clean and tested. We use standard Python formatting and best practices.
