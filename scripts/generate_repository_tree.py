from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "ARVORE_COMPLETA_REPOSITORIO.md"
EXCLUDED_DIRS = {".git", ".next", ".vinext", ".wrangler", "dist", "node_modules"}


def included(path: Path) -> bool:
    return not any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts)


def human_size(size: int) -> str:
    if size < 1024:
        return f"{size} B"
    if size < 1024**2:
        return f"{size / 1024:.1f} KiB"
    return f"{size / 1024**2:.1f} MiB"


def tree_lines(directory: Path, prefix: str = "") -> list[str]:
    entries = sorted(directory.iterdir(), key=lambda entry: (not entry.is_dir(), entry.name.casefold()))
    lines: list[str] = []
    for index, entry in enumerate(entries):
        last = index == len(entries) - 1
        branch = "└── " if last else "├── "
        if entry.is_dir() and entry.name in EXCLUDED_DIRS:
            label = f"{entry.name}/ [conteúdo técnico gerado omitido]"
        elif entry.is_dir():
            label = f"{entry.name}/"
        else:
            label = f"{entry.name} ({human_size(entry.stat().st_size)})"
        lines.append(prefix + branch + label)
        if entry.is_dir() and entry.name not in EXCLUDED_DIRS:
            extension = "    " if last else "│   "
            lines.extend(tree_lines(entry, prefix + extension))
    return lines


def main() -> None:
    files = [path for path in ROOT.rglob("*") if path.is_file() and included(path)]
    directories = [path for path in ROOT.rglob("*") if path.is_dir() and included(path)]
    extensions = Counter(path.suffix.lower() or "[sem extensão]" for path in files)
    total_size = sum(path.stat().st_size for path in files)

    lines = [
        "# Árvore completa do repositório",
        "",
        f"**Gerado em:** {datetime.now().astimezone().isoformat(timespec='seconds')}  ",
        f"**Raiz:** `{ROOT}`  ",
        f"**Diretórios inventariados:** {len(directories)}  ",
        f"**Arquivos inventariados:** {len(files)}  ",
        f"**Tamanho inventariado:** {human_size(total_size)}  ",
        "**Exclusão intencional:** conteúdo interno de `.git/`, `node_modules/`, `.next/`, `.vinext/`, `.wrangler/` e `dist/`, por serem metadados, dependências ou artefatos gerados.",
        "",
        "## Distribuição por extensão",
        "",
        "| Extensão | Quantidade |",
        "|---|---:|",
    ]
    lines.extend(f"| `{extension}` | {count} |" for extension, count in extensions.most_common())
    lines.extend([
        "",
        "## Resumo por item da raiz",
        "",
        "| Item | Tipo | Arquivos internos inventariados | Tamanho inventariado |",
        "|---|---|---:|---:|",
    ])
    for item in sorted(ROOT.iterdir(), key=lambda entry: entry.name.casefold()):
        if item.is_dir():
            nested = [path for path in item.rglob("*") if path.is_file() and included(path)]
            nested_size = sum(path.stat().st_size for path in nested)
            lines.append(f"| `{item.name}/` | diretório | {len(nested)} | {human_size(nested_size)} |")
        else:
            lines.append(f"| `{item.name}` | arquivo | 1 | {human_size(item.stat().st_size)} |")
    lines.extend([
        "",
        "## Estrutura completa",
        "",
        "```text",
        f"{ROOT.name}/",
        *tree_lines(ROOT),
        "```",
        "",
    ])
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Gerado: {OUTPUT}")
    print(f"Diretórios: {len(directories)} | Arquivos: {len(files)} | Tamanho: {human_size(total_size)}")


if __name__ == "__main__":
    main()
