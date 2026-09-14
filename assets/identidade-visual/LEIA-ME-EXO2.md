# Identidade visual — Exo 2

Aprovada em 06/09/2026. Nome em Exo 2 Semibold (600); slogan em Exo 2 Regular (400). Os textos, incluindo a pontuação própria de cada ativo, permanecem como aprovados.

- `assinaturas-verticais/`: opção 5 aprovada, com e sem slogan, transparente e com fundo azul.
- Raiz: logos completas de satélite e monitor e assinaturas horizontais em PNG atualizadas nos mesmos caminhos.
- `vetorial/`: assinaturas horizontais com letras em contornos Exo 2, sem depender de fonte instalada. Os caminhos do símbolo permanecem iguais.
- `tipografia/exo-2/`: fonte variável oficial e licença SIL OFL. Origem: https://github.com/google/fonts/tree/main/ofl/exo2
- `monocromaticas/`: os 140 símbolos permanecem iguais; apenas a tipografia das legendas de `PREVIA-MONOCROMATICAS.png` foi atualizada. O ZIP contém a mesma atualização.
- `AUDITORIA_TIPOGRAFIA_EXO2.csv`: exame dos 163 arquivos que existiam antes da atualização.

Os símbolos, os favicons e suas matrizes não foram redesenhados. Nas variantes claras, o azul-marinho substitui o branco do texto para permitir leitura. A mudança não aplica Exo 2 ao texto corrido do site ou dos documentos.

Para gerar assinaturas horizontais novamente, o script `scripts/generate_brand_derivatives.py` usa a fonte local e os contornos Exo 2; sua execução completa também refaz o tratamento técnico do símbolo. Para alterar somente assinaturas, utilizar as funções `make_signature` e `make_png_signature` com o SVG existente, sem executar `clean_master` ou `vectorize_master`. Dependências: Pillow, fontTools e vtracer.
