# CONTEXTO DE CONTINUIDADE — VPC-WEBSISTEMAS E GEOINFORMAÇÃO

**Data de consolidação:** 03 de setembro de 2026  
**Responsável:** Vinicius do Prado Capanema  
**Prioridade:** desenvolvimento da presença institucional da VPC  
**Finalidade deste arquivo:** permitir que o Codex continue imediatamente o planejamento, desenvolvimento e publicação do site institucional, sem refazer discussões ou alterar decisões já tomadas.

**Atualização de implementação:** 03 de setembro de 2026. Para regras operacionais detalhadas e invariantes visuais vigentes, ler também `AGENTS.md`, `README.md` e `ESPECIFICACAO_SITE_INSTITUCIONAL_OFICIAL_VPC.md`. As decisões mais recentes registradas nesses arquivos substituem descrições históricas incompatíveis deste contexto.

---

## 1. Orientação de trabalho

- Trabalhar com objetividade, precisão e iniciativa.
- Evitar perguntas desnecessárias e não transformar riscos ou pendências em impedimentos.
- Quando houver uma decisão confirmada neste documento, não voltar a questioná-la.
- Não inventar informações institucionais, experiências, tecnologias, clientes ou resultados.
- Diferenciar fatos comprovados, decisões confirmadas e itens ainda pendentes.
- Priorizar uma versão institucional publicável hoje; melhorias não essenciais podem ser feitas posteriormente.

---

## 2. Identidade institucional — DEFINIDA

### Nome oficial da empresa

**VPC-WEBSISTEMAS E GEOINFORMAÇÃO**

Não utilizar “VPC-GEOSER” como nome oficial do site ou da documentação atual.

### Razão social

**Vinicius do Prado Capanema Ltda.**

### CNPJ

**57.286.005/0001-40**

### Slogan oficial

**“Inteligência em geoprocessamento e sensoriamento remoto.”**

### Descrição institucional aprovada

**Empresa que atua com soluções geotecnológicas, websistemas e análise de dados.**

### Responsável

**Vinicius do Prado Capanema**, engenheiro e desenvolvedor de soluções geoespaciais.

### Formação relevante do responsável

- Engenharia Florestal — UNEMAT;
- Especialização em Georreferenciamento — AJES/INCRA;
- MBA em Gestão de Projetos — UNOPAR;
- Mestrado em Sensoriamento Remoto — INPE;
- Doutorado em Sensoriamento Remoto — INPE.

### Posicionamento institucional consolidado

A empresa reúne geoprocessamento, sensoriamento remoto, análise de dados e engenharia de software para transformar dados técnicos e territoriais em sistemas digitais operacionais. Atua na construção de WebGIS, dashboards, sistemas de gestão territorial, plataformas de dados e automação de processos técnicos e administrativos.

A comunicação deve ser técnica, institucional e profissional. Evitar linguagem promocional genérica, exageros comerciais ou alteração arbitrária da descrição da empresa.

---

## 3. Padrão técnico e de engenharia — DEFINIDO

### Onze princípios de engenharia

1. Soberania tecnológica e preferência por soluções abertas.
2. Modularidade e baixo acoplamento.
3. Padronização estrutural.
4. Segurança desde a concepção.
5. Observabilidade, rastreabilidade e auditabilidade.
6. Soberania, interoperabilidade e portabilidade dos dados.
7. Reprodutibilidade e automação.
8. Customização sem fragmentação.
9. Qualidade e testabilidade.
10. Experiência consistente, preservando a identidade do cliente.
11. Geoinformação como capacidade nativa sempre que houver dimensão espacial relevante.

### Arquitetura de referência

Sete blocos:

1. Experiência;
2. Aplicação;
3. Domínio;
4. Dados;
5. Integrações;
6. Plataforma;
7. IA e Agentes, com atuação transversal.

Classificação de pertencimento dos componentes:

- Core;
- Shared Capabilities;
- Solution Domain;
- Client Layer.

### Diretriz de IA

A IA deve ser abstraída por provedores substituíveis. Decisões críticas não devem depender exclusivamente de modelos generativos. Manter regras determinísticas, avaliação, monitoramento, fallback e operação degradada quando necessário.

### Capacidades e tecnologias demonstráveis

- Python e FastAPI;
- JavaScript/TypeScript;
- React;
- HTML e CSS;
- PostgreSQL/PostGIS;
- GeoServer e QGIS Server;
- Leaflet;
- APIs REST;
- WMS e WFS;
- ETL/ELT geoespacial;
- AWS EC2 e RDS;
- Docker;
- Git e GitHub;
- CI/CD;
- PyMuPDF e Tesseract;
- autenticação e controle de acesso;
- monitoramento, logs e auditoria.

Não afirmar uso comprovado de uma tecnologia que não esteja documentada em projeto ou currículo.

---

## 4. Portfólio-base — DEFINIDO

### 4.1 SIGMA-PLI

Plataforma centralizadora do PLI-SP 2050 para organização, governança, publicação e consulta de dados, documentos e informações geoespaciais. Inclui autenticação, dashboards, dicionário de dados, metadados, versionamento, repositório, gestão de usuários, monitoramento de serviços, relatórios e exploração de relacionamentos com Neo4j.

Tecnologias e capacidades relacionadas: PostgreSQL, integração de dados, APIs, autenticação JWT, observabilidade, CI/CD, dashboards e recursos geoespaciais.

### 4.2 FAD / FAD-STATS

Ferramenta de Análise Dinamizada de Dados Estatísticos, voltada a análises temporais, territoriais e temáticas. Trabalha com dados estatísticos e geoespaciais, filtros multidimensionais, indicadores, visualizações e diferentes estratégias analíticas.

Capacidades relacionadas: WebGIS, dashboards, dados vetoriais e raster, indicadores, análise multicritério e serviços geoespaciais.

### 4.3 Sistema de Gestão e Extração de Atas

Sistema criado no contexto SEMIL/PLI para organização, extração e indexação de atas, conectando decisões, temas, responsáveis e ações.

Capacidades relacionadas: automação documental, extração de texto, organização da informação, busca e rastreabilidade.

### 4.4 Infraestrutura geoespacial em nuvem

Experiência com GeoServer/GeoWebCache em AWS EC2, publicação e consumo de serviços WMS/WFS e integração com aplicações web.

### 4.5 Materiais demonstrativos previstos

- vídeo de demonstração do FAD;
- vídeo do Sistema de Gestão/Extração de Atas;
- capturas de tela e imagens dos sistemas;
- link do currículo/portfólio pessoal existente:
  `https://vpcapanema.github.io/curriculo_viniciuscapanema/`

Antes de publicar logotipos de clientes, documentos internos ou dados sensíveis, verificar se o material é publicável. A ausência de confirmação não impede a inclusão de uma descrição técnica sem logotipo ou informação sigilosa.

---

## 5. Site institucional

### 5.1 Objetivo

Publicar uma presença institucional profissional da **VPC-WEBSISTEMAS E GEOINFORMAÇÃO**, demonstrando capacidade técnica e aderência a projetos de geotecnologia, WebGIS, visualização de dados e engenharia de software.

### 5.2 Público principal

- instituições públicas;
- organizações socioambientais;
- empresas de engenharia, planejamento e infraestrutura;
- equipes que necessitem de WebGIS, sistemas de dados e automação;

### 5.3 Arquitetura definida para a primeira versão

Site institucional de página única, leve, responsivo e publicável com rapidez.

Seções vigentes:

1. **Início** — nome, slogan e apresentação objetiva;
2. **Áreas de atuação** — geoinformação, websistemas, dados e automação;
3. **Soluções sob medida** — grafo informativo com `Soluções inteligentes` no núcleo;
4. **Engenharia VPC** — síntese dos princípios e capacidades técnicas;
5. **Experiências relacionadas** — SIGMA-PLI, SICARD e FAD-Stats;
6. **VPC-ITA** — chamada integralmente clicável para a página comercial `/ita`;
7. **Produtos em atividade** — aplicações em produção e desenvolvimento;
8. **Clientes atendidos** — Governo do Estado de São Paulo, SEMIL/SLT, DER/SP e PLI-SP 2050;
9. **Sobre a VPC** — empresa e apresentação de Vinicius do Prado Capanema;
10. **Contato comercial** — canal comercial confirmado e retorno ao início.

Decisões visuais e verbais vigentes:

- preservar o zebrado azul e branco;
- experiências e produtos usam cards integralmente clicáveis, sem ação no canto superior direito;
- soluções sob medida não usa cards: usa grafo, com ícones ao lado dos títulos;
- a VPC-ITA é tratada no feminino;
- nome: `VPC-ITA — Inteligência Territorial e Auditoria Ambiental`;
- chamada: `Conheça antes, decida depois.`;
- usar `imóvel rural`, não `propriedade`, como expressão fundiária geral;
- o PLI-SP 2050 usa composição tipográfica nas cores `#1C3D59` e `#00B86E`, sem logotipo inventado;
- os rodapés de `/` e `/ita` são idênticos, compactos e centralizados.

### 5.4 Requisitos mínimos

- responsividade para computador e celular;
- acessibilidade semântica;
- carregamento rápido;
- HTTPS;
- links e navegação funcionais;
- metadados de SEO;
- imagem e descrição para compartilhamento;
- favicon;
- compatibilidade com navegadores atuais;
- estrutura simples de atualizar;
- nenhuma dependência de back-end para a publicação inicial, salvo se estritamente necessária.

---

## 6. Ativos de identidade visual — FONTES IDENTIFICADAS, ANÁLISE PENDENTE

Os arquivos estão no computador Windows do usuário, dentro do OneDrive:

```text
C:\Users\Vinicius adm\OneDrive\GEOSER-VINICIUS DO PRADO CAPANEMA LTDA\LOGO
C:\Users\Vinicius adm\OneDrive\GEOSER-VINICIUS DO PRADO CAPANEMA LTDA\MODELOS
C:\Users\Vinicius adm\OneDrive\GEOSER-VINICIUS DO PRADO CAPANEMA LTDA\GITHUB ENTERPRISE
```

### Ordem de autoridade

1. `GITHUB ENTERPRISE` — fonte mais atual e principal;
2. `LOGO` — arquivos-base e versões anteriores;
3. `MODELOS` — aplicações e padrões visuais existentes.

### Trabalho necessário

- inventariar os arquivos;
- identificar as versões mais recentes;
- usar `GITHUB ENTERPRISE` como referência em caso de divergência;
- atualizar o nome para **VPC-WEBSISTEMAS E GEOINFORMAÇÃO**;
- manter o slogan oficial;
- consolidar logotipo principal;
- gerar versões horizontal, vertical, monocromática e transparente;
- identificar ou definir paleta oficial;
- identificar ou definir tipografias;
- gerar favicon;
- preparar versões adequadas para fundos claros e escuros;
- selecionar imagens, capturas de sistemas e vídeos para o site.

### Restrição de acesso atual

Esses caminhos são locais do Windows e não estavam montados no ambiente anterior. Ao executar no Codex local, acessar diretamente esses diretórios. Se o ambiente ainda não enxergar o disco, o usuário poderá compactar as três pastas em um ZIP.

---

## 7. Domínio e Microsoft 365 — PARCIALMENTE CONCLUÍDOS

### Domínio oficial

`vpc-websistemas.com.br`

### Endereço principal definido

`https://vpc-websistemas.com.br`

`www.vpc-websistemas.com.br` deverá redirecionar para o endereço principal.

### Infraestrutura já recuperada do histórico

- domínio registrado e administrado na UOL Host;
- tenant Microsoft 365 criado;
- domínio apresentado ao Microsoft 365 para verificação;
- registro TXT de verificação fornecido:
  - host: `@`
  - valor: `MS=ms86323721`
  - TTL: `3600`;
- registro MX registrado no histórico:
  - `vpcwebsistemas-com-br0i.mail.protection.outlook.com`
  - prioridade `0`;
- CNAME:
  - `autodiscover` → `autodiscover.outlook.com`;
- SPF:
  - `v=spf1 include:spf.protection.outlook.com -all`;
- ambiente Microsoft 365 registrado posteriormente como E3, incluindo Exchange Online, SharePoint, OneDrive, Teams, Power Automate, Power Apps, Forms, Planner, Intune e Entra ID.

### Regra crítica de publicação

Não apagar nem substituir os registros MX, SPF, autodiscover ou TXT do Microsoft 365. A publicação do site deve acrescentar ou ajustar apenas os registros destinados ao domínio raiz e ao `www`, de acordo com o provedor de hospedagem.

### Verificações restantes

- confirmar o apontamento atual do domínio raiz `@`;
- confirmar o apontamento atual de `www`;
- identificar eventual hospedagem já vinculada;
- configurar redirecionamento de `www` para o domínio raiz;
- validar certificado HTTPS;
- validar que e-mail e serviços Microsoft 365 continuam funcionando após qualquer alteração.

---

## 8. GitHub e publicação — ESTADO CONHECIDO

- conta pessoal principal: `vpcapanema`;
- ambiente empresarial: **VPC-WEBSISTEMAS**;
- há registro histórico de Enterprise/Organization empresarial;
- o repositório específico do site institucional ainda não foi identificado no histórico recuperado;
- não presumir que o repositório privado `sra-pli-3` seja o repositório do site;
- DNS é administrado na UOL Host;
- a hospedagem definitiva do site ainda deve ser identificada ou configurada.

### Etapas de publicação

1. verificar se já existe repositório do site na estrutura empresarial;
2. se não existir, criar repositório específico;
3. implementar a página institucional;
4. incorporar os ativos atualizados;
5. gerar versão de produção;
6. configurar hospedagem;
7. conectar `vpc-websistemas.com.br`;
8. configurar `www` e HTTPS;
9. testar computador, celular, links, vídeos e metadados;
10. validar publicamente o endereço final.

---

## 9. Contatos e governança de e-mail

O padrão corporativo documentado usa:

`nome.sobrenome@vpc-websistemas.com.br`

Contas funcionais previstas:

- `contato@vpc-websistemas.com.br`;
- `comercial@vpc-websistemas.com.br`;
- `financeiro@vpc-websistemas.com.br`;
- `faturamento@vpc-websistemas.com.br`;
- `suporte@vpc-websistemas.com.br`;
- `juridico@vpc-websistemas.com.br`;
- `rh@vpc-websistemas.com.br`;
- `marketing@vpc-websistemas.com.br`;
- `ti@vpc-websistemas.com.br`;
- `diretoria@vpc-websistemas.com.br`;
- `noreply@vpc-websistemas.com.br`.

Contas administrativas previstas:

- `admin@vpc-websistemas.com.br`;
- `devops@vpc-websistemas.com.br`;
- `github@vpc-websistemas.com.br`.

Manter a conta `onmicrosoft.com` como acesso emergencial do tenant.

Antes de publicar um endereço no site, confirmar qual caixa está ativa e monitorada. A opção institucional preferencial é `contato@vpc-websistemas.com.br`, desde que operacional.

---

## 10. Estado consolidado do planejamento

| Frente | Estado |
|---|---|
| Identidade e posicionamento | Fechados |
| Padrão técnico e engenharia | Fechados |
| Portfólio-base | Fechado |
| Arquitetura do site | Definida para a primeira versão |
| Conteúdo conceitual | Definido |
| Textos finais do site | Implementados; alterações futuras somente sob solicitação explícita |
| Ativos visuais | Integrados ao site; preservar matrizes e proporções aprovadas |
| Domínio oficial | Definido |
| Microsoft 365 e e-mail | Configuração principal registrada no histórico |
| DNS específico do site | A verificar conforme hospedagem |
| Repositório do site | Identificado; aplicação em `site/` |
| Hospedagem | A identificar ou configurar |
| Publicação e validação | Pendentes |

---

## 11. Ordem imediata de execução

1. Ler `AGENTS.md`, `README.md` e os documentos oficiais antes de alterar.
2. Preservar o conteúdo e as regiões não incluídas no pedido atual.
3. Implementar somente a alteração solicitada.
4. Executar `npm.cmd run lint` e `npm.cmd run build` em `site/`.
5. Conferir visualmente as áreas alteradas em desktop e celular.
6. Quando houver publicação autorizada, validar domínio, HTTPS, redirecionamento de `www`, conteúdo, links e e-mail.

---

## 12. Pendências que não devem bloquear a versão inicial

Podem ser concluídas após a primeira publicação:

- inclusão de todos os vídeos demonstrativos;
- expansão dos estudos de caso;
- páginas individuais de projetos;
- blog ou área de notícias;
- formulário com back-end próprio;
- versões multilíngues;
- animações avançadas;
- revisão ampliada de SEO;
- consolidação integral do Engineering Standard em documento separado.

Para a versão urgente, priorizar credibilidade institucional, clareza, desempenho e acesso público funcional.
