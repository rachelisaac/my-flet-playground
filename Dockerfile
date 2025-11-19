FROM python:3.11-slim

WORKDIR /app

COPY . /app

# Install packages while bypassing PyPI SSL verification (for NetFree)
RUN pip install --no-cache-dir "flet[all]" --trusted-host pypi.org --trusted-host files.pythonhosted.org

EXPOSE 8500

CMD ["python", "index.py"]
