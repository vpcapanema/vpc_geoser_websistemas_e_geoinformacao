# VPC-WEBSISTEMAS E GEOINFORMAÇÃO

Repositório institucional da **VPC-WEBSISTEMAS E GEOINFORMAÇÃO**, empresa que desenvolve soluções digitais e geotecnológicas sob medida. O site público está em `site/` e inclui a página institucional e a página comercial da VPC-ITA.

## Leitura obrigatória antes de alterar

Todo agente ou desenvolvedor deve ler, nesta ordem:

1. `AGENTS.md`;
2. `CONTEXTO_CODEX_VPC_WEBSISTEMAS.md`;
3. `IDENTIDADE_INSTITUCIONAL_OFICIAL_VPC.md`;
4. `DIRETRIZES_ENGENHARIA_OFICIAL_VPC.md`;
5. `ESPECIFICACAO_SITE_INSTITUCIONAL_OFICIAL_VPC.md`;
6. `PLANO_PUBLICACAO_E_INFRAESTRUTURA_OFICIAL_VPC.md`, somente quando a tarefa envolver publicação ou infraestrutura.

Arquivos em `legado/` e `documentacao/adiado/` não são especificações vigentes.

## Estado atual do site

- aplicação web em `site/`;
- página institucional em `/`;
- página comercial da VPC-ITA em `/ita`;
- conteúdo estático, sem back-end;
- identidade institucional baseada exclusivamente na marca aprovada;
- versão local não equivale à versão publicada.

## Decisões de interface que devem ser preservadas

- A alternância visual das seções segue o zebrado azul e branco.
- **Experiências relacionadas** e **Produtos em atividade** usam cards-botão: toda a área de cada card é clicável.
- Cards-botão não possuem numeração, classificação ou ícone de ação no canto superior direito.
- Os títulos dos cards usam ícone e nome centralizados e próximos verticalmente.
- **Soluções sob medida** não usa cards. A seção é um grafo informativo, com **Soluções inteligentes** no núcleo e as capacidades distribuídas ao redor.
- Somente nesse grafo, cada ícone fica na mesma linha e ao lado do título.
- A VPC-ITA é tratada gramaticalmente no feminino.
- Nome: **VPC-ITA — Inteligência Territorial e Auditoria Ambiental**.
- Chamada aprovada: **Conheça antes, decida depois.**
- Usar **imóvel rural**, e não “propriedade”, para abranger propriedade e posse.
- O bloco da VPC-ITA na página inicial é integralmente clicável e leva a `/ita`.
- Em **Clientes atendidos**, as marcas oficiais devem manter proporção e dimensão visual equilibrada.
- O PLI-SP 2050 não usa imagem de logotipo no site: usa composição tipográfica com azul `#1C3D59` e verde `#00B86E`.
- O rodapé da página institucional e o da página da VPC-ITA têm exatamente a mesma estrutura e altura.
- No rodapé, o ícone fica à esquerda das duas linhas da assinatura; as duas linhas ficam alinhadas à direita entre si; o conjunto completo fica centralizado.
- O botão **Voltar ao início** pertence à seção **Contato comercial**, no canto inferior direito, e não ao rodapé.

## Desenvolvimento local

No Windows:

```powershell
cd site
npm.cmd run dev
```

Abrir `http://localhost:3000/` e `http://localhost:3000/ita`.

Antes de concluir qualquer alteração:

```powershell
npm.cmd run lint
npm.cmd run build
```

Além dos comandos, é obrigatória a inspeção visual da página institucional e da página da VPC-ITA em desktop e celular. Não declarar entrega, publicação ou correção visual com base apenas no build.

## Limites de alteração

- Alterar somente o conteúdo e as regiões solicitadas pelo usuário.
- Não aproveitar uma tarefa localizada para reescrever outras seções.
- Não inventar fatos, clientes, aplicações, integrações, resultados ou funcionalidades.
- Não redesenhar a marca institucional.
- Não publicar nem alterar DNS sem solicitação explícita e validação prevista no plano de infraestrutura.
- Depois de criar, remover ou mover arquivos, executar `python scripts/generate_repository_tree.py` na raiz.
