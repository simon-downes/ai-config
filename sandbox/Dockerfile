FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y curl unzip ca-certificates git procps wget dnsutils yamllint shellcheck nano && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:${PATH}"
ENV EDITOR=nano

RUN ARCH=$(uname -m) && \
    curl -fsSL https://awscli.amazonaws.com/awscli-exe-linux-${ARCH}.zip -o awscliv2.zip && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

RUN curl -fsSL https://github.com/jqlang/jq/releases/latest/download/jq-linux-amd64 -o /usr/local/bin/jq && \
    chmod +x /usr/local/bin/jq

RUN curl -fsSL https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -o /usr/local/bin/yq && \
    chmod +x /usr/local/bin/yq

RUN curl -fsSL https://get.opentofu.org/install-opentofu.sh -o install-opentofu.sh && \
    chmod +x install-opentofu.sh && \
    ./install-opentofu.sh --install-method deb && \
    rm install-opentofu.sh

RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "x86_64" ]; then \
        TF_DOCS_ARCH="amd64"; \
    elif [ "$ARCH" = "aarch64" ]; then \
        TF_DOCS_ARCH="arm64"; \
    fi && \
    TF_DOCS_VERSION=$(curl -fsSL https://api.github.com/repos/terraform-docs/terraform-docs/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")') && \
    curl -fsSL "https://github.com/terraform-docs/terraform-docs/releases/download/${TF_DOCS_VERSION}/terraform-docs-${TF_DOCS_VERSION}-linux-${TF_DOCS_ARCH}.tar.gz" -o terraform-docs.tar.gz && \
    tar -xzf terraform-docs.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/terraform-docs && \
    rm terraform-docs.tar.gz

RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "x86_64" ]; then \
        GH_ARCH="amd64"; \
    elif [ "$ARCH" = "aarch64" ]; then \
        GH_ARCH="arm64"; \
    fi && \
    GH_VERSION=$(curl -fsSL https://api.github.com/repos/cli/cli/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")') && \
    curl -fsSL "https://github.com/cli/cli/releases/download/${GH_VERSION}/gh_${GH_VERSION#v}_linux_${GH_ARCH}.tar.gz" -o gh.tar.gz && \
    tar -xzf gh.tar.gz && \
    mv "gh_${GH_VERSION#v}_linux_${GH_ARCH}/bin/gh" /usr/local/bin/ && \
    rm -rf gh.tar.gz "gh_${GH_VERSION#v}_linux_${GH_ARCH}"

RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "x86_64" ]; then \
        SCALR_ARCH="amd64"; \
    elif [ "$ARCH" = "aarch64" ]; then \
        SCALR_ARCH="arm64"; \
    fi && \
    SCALR_VERSION=$(curl -fsSL https://api.github.com/repos/Scalr/scalr-cli/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")') && \
    curl -fsSL "https://github.com/Scalr/scalr-cli/releases/download/${SCALR_VERSION}/scalr-cli_${SCALR_VERSION#v}_linux_${SCALR_ARCH}.zip" -o scalr.zip && \
    unzip scalr.zip -d /tmp/scalr && \
    mv /tmp/scalr/scalr /usr/local/bin/scalr && \
    chmod +x /usr/local/bin/scalr && \
    rm -rf scalr.zip /tmp/scalr

RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    PYTHON_VERSION=$(uv python list | grep -oiE 'cpython-[0-9]+\.[0-9]+\.[0-9]+-' | cut -d- -f2 | awk -F. '{print $1"."$2}' | sort -uV | tail -n1) && \
    uv python install "$PYTHON_VERSION" && \
    PYTHON_PATH=$(find /root/.local/share/uv/python -name "cpython-${PYTHON_VERSION}*" -type d | head -1) && \
    ln -s "$PYTHON_PATH/bin/python3" /usr/local/bin/python3 && \
    ln -s /usr/local/bin/python3 /usr/local/bin/python

RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "x86_64" ]; then \
        URL="https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-x86_64-linux.zip"; \
    elif [ "$ARCH" = "aarch64" ]; then \
        URL="https://desktop-release.q.us-east-1.amazonaws.com/latest/kirocli-aarch64-linux.zip"; \
    else \
        echo "Unsupported architecture: $ARCH" && exit 1; \
    fi && \
    curl --proto '=https' --tlsv1.2 -sSf "$URL" -o kirocli.zip && \
    unzip kirocli.zip && \
    ./kirocli/install.sh --force --no-confirm && \
    rm -rf kirocli.zip kirocli

ENV PATH="/root/.local/bin:${PATH}"

RUN kiro-cli --version

RUN uv tool install git+https://github.com/simon-downes/cli-tools.git#subdirectory=kv
RUN uv tool install git+https://github.com/simon-downes/cli-tools.git#subdirectory=oauth
RUN uv tool install git+https://github.com/simon-downes/cli-tools.git#subdirectory=notion

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
