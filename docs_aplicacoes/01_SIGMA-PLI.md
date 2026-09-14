# SIGMA-PLI

**Sistema Integrado de Gestão, Monitoramento e Apoio Técnico ao Plano de Logística e Investimentos**

> Quando o plano acaba, o conhecimento fica.

---

## O problema

Um plano estadual de logística produz, ao longo de anos, milhares de arquivos: estudos, bases cadastrais, camadas geoespaciais, planilhas, relatórios de consultoria, atas. Esse acervo costuma viver em pastas de rede, e-mails e HDs pessoais. Ninguém sabe ao certo o que existe, quem produziu, de qual versão se trata ou se aquele shapefile é o mesmo que o do relatório anterior.

O custo não aparece de imediato. Aparece quando alguém sai da equipe, quando muda a gestão, quando um dado precisa ser defendido em auditoria — ou quando o mesmo estudo é contratado duas vezes porque ninguém achou o primeiro.

## O que é

O SIGMA-PLI é o **repositório estruturado do conhecimento técnico** de um plano ou programa de grande porte. Ele parte de uma diretriz inegociável: *todo arquivo incorporado ao acervo deve estar obrigatoriamente catalogado em um cadastro estruturado de metadados*.

Na prática, isso significa que é possível entender o acervo inteiro sem abrir arquivo por arquivo.

## Arquitetura em quatro camadas

**1. Repositório e catálogo.** O SIGMA Drive guarda o arquivo; o Catálogo guarda a identidade dele. Os metadados são organizados em dois blocos: um canônico, comum a todo arquivo — nome, descrição, palavras-chave, produto vinculado, abrangência territorial, instituição responsável, quem enviou, quando atualizou —, e um especializado, que muda conforme o tipo de dado.

São **dez perfis**, cada um com sua própria tabela de metadados:

| Perfil | Metadados específicos |
|---|---|
| Geoespacial raster | bandas, resolução espacial, temporal, radiométrica e espectral, SRS, escala, tema, ano |
| Geoespacial vetor | tipo de geometria, nº de feições, SRS, tema, periodicidade |
| Nuvem de pontos | nº de pontos, densidade, SRS, tema |
| Geodatabase | tipo, nº de feature classes e tabelas, tema |
| Database | SGBD, versão, nº de tabelas, tamanho, periodicidade |
| Tabular | linhas, colunas, cabeçalho, delimitador, encoding detectado |
| Documentos | nº de páginas, proteção por senha |
| Desenho 2D/3D | tipo de desenho (CAD, BIM, malha) |
| Mídia | tipo, resolução, duração |
| Pacote | nº de arquivos, taxa de compressão |

**2. Identidade e controle de acesso.** Cinco níveis — Visualizador, Operador, Analista, Gestor, Administrador — com uma camada extra: perfis privilegiados fazem **dupla autenticação**, elevando a sessão em um segundo login. CPF armazenado com AES-256-GCM, sessão de 30 minutos renovável, bloqueio automático após cinco tentativas, trilha de auditoria em JSON e retenção de contas desativadas por dois anos, conforme LGPD.

**3. Grafo de relacionamentos.** Um banco de grafos espelha as entidades do plano — pessoas, instituições, arquivos, produtos, etapas — e explicita os vínculos: qual produto derivou de qual, qual instituição originou determinado dado, que etapa depende de que insumo.

**4. WebGIS integrado.** Dado geoespacial depositado é publicado automaticamente e vira camada no mapa. O mapa não é uma coleção paralela: é uma janela sobre o próprio acervo.

## O que o usuário faz

**Deposita** pelo Upload Inteligente, assistente de cinco etapas que valida extensão e tamanho, calcula hash de integridade e **extrai metadados automaticamente** ao analisar o conteúdo. Aceita mais de 35 extensões, até 500 MB por arquivo, com modo em lote para volume.

Cada envio percorre um pipeline de seis estágios: validação → análise e extração → indexação → armazenamento em object storage → indexação no grafo → publicação da camada.

**Consulta** pelo catálogo, com busca facetada, filtro por perfil — que troca automaticamente o conjunto de colunas exibidas —, três modos de exibição e exportação em CSV, JSON, XLSX, TXT e DOCX.

**Explora** pelo Grafo Explorer, aberto ao público sem login: visualização 2D com quatro layouts, 3D com três, além de **PageRank, centralidade de intermediação, detecção de comunidades e caminho mais curto** entre duas entidades. Cores, símbolos, espessura de aresta e parâmetros de física são configuráveis.

**Governa** pelo painel de sincronização, que mostra, para cada tipo de entidade, a quantidade no banco relacional, a quantidade no grafo e o **percentual de correspondência** entre os dois. A sincronização é seletiva, transmitida em tempo real, e cada operação fica registrada em log.

## Por que se diferencia

- **O metadado é obrigatório, não opcional.** É o que separa um repositório de uma pasta compartilhada.
- **O catálogo se adapta ao dado.** Raster e nuvem de pontos não são descritos pelos mesmos campos.
- **A relação entre os dados é navegável**, não apenas documentada em texto.
- **Publicação geoespacial automática** — não há etapa manual entre depositar e ver no mapa.
- **Rastreabilidade de ponta a ponta**: quem enviou, quando, de onde veio, o que derivou dali.
- **100% tecnologias abertas.**

## Para quem

Órgãos e programas que produzem acervo técnico continuado e precisam garantir que ele sobreviva à rotatividade de equipe e à troca de gestão: secretarias de planejamento e infraestrutura, autarquias, consórcios, unidades gestoras de planos plurianuais e projetos com financiamento que exige prestação de contas documental.

## Base técnica

FastAPI e Python · PostgreSQL com PostGIS · banco de grafos com protocolo Bolt · object storage compatível com S3 · GeoServer para serviços OGC (WMS/WFS) · dashboards em R Shiny · Nginx · Docker · autenticação JWT.

## Escala verificada

**536 endpoints** de API públicos documentados em OpenAPI, distribuídos em onze módulos funcionais, sendo os maiores o de dicionário e catálogo e o de gestão administrativa.

## Fundamento científico

**Ciência da informação aplicada: metadados como condição de existência do dado.** O princípio que estrutura o sistema — nenhum arquivo entra no acervo sem cadastro estruturado de metadados — é a aplicação direta da teoria de organização da informação: um documento sem descrição normalizada é irrecuperável em escala, independentemente de estar armazenado.

O modelo de metadados é **hierárquico e polimórfico**: um núcleo canônico comum a todo item, garantindo interoperabilidade e busca transversal, mais um bloco especializado por perfil de dado, garantindo suficiência descritiva. É a resposta ao dilema clássico do catálogo — padrão único é pobre demais para o dado específico; padrão livre é incomparável entre itens.

**Vocabulário de sensoriamento remoto no perfil raster.** O perfil de dado matricial exige as **quatro resoluções** que caracterizam um produto de observação da Terra — espacial, temporal, radiométrica e espectral — além de sistema de referência espacial e escala. É o descritor mínimo pelo qual um analista decide se a imagem serve para a pergunta dele, sem precisar abri-la.

O mesmo rigor se aplica aos demais perfis: densidade de pontos em nuvem LiDAR, tipo de geometria e número de feições em vetorial, encoding detectado e delimitador em tabular.

**Teoria de grafos aplicada à governança da informação.** O grafo de conhecimento não é visualização decorativa. O sistema executa algoritmos de análise de redes sobre o acervo:

- **PageRank** — centralidade por influência, identificando quais entidades são estruturalmente mais importantes na rede de dependências entre produtos, dados e instituições.
- **Centralidade de intermediação** — identifica as entidades que funcionam como ponte entre grupos. São os pontos de fragilidade: se aquele dado ou aquela instituição sai, subconjuntos inteiros do acervo se desconectam.
- **Detecção de comunidades** — revela agrupamentos de entidades densamente interconectadas, expondo a estrutura temática real do acervo, que raramente coincide com a organização formal em pastas.
- **Caminho mínimo** entre duas entidades — responde por qual cadeia um produto derivou de determinada fonte.

Aplicar essas métricas ao acervo técnico de um plano permite perguntas que nenhum catálogo tabular responde: qual base sustenta mais produtos, qual estudo é um nó crítico, onde o conhecimento está concentrado em uma única fonte.

**Sincronização com verificação quantitativa.** O painel de governança mede o **percentual de correspondência** entre o banco relacional e o banco de grafos, por tipo de entidade. Não é sincronização declarada — é sincronização medida, com log e evidência.

**Proveniência e integridade.** Cada arquivo recebe **hash de integridade** no momento do depósito, e o registro guarda origem, autoria, data de produção, quem enviou, quem atualizou e quando. É a cadeia de custódia do dado técnico — condição para que o acervo seja auditável e para que um resultado possa ser reproduzido anos depois.

**Extração automática de metadados** por análise do conteúdo do arquivo, reduzindo o preenchimento manual e, com ele, a principal fonte de erro e de inconsistência em catálogos institucionais.

**Interoperabilidade por padrões abertos.** A publicação de camadas segue as especificações de serviços geoespaciais do consórcio internacional de padrões abertos, o que permite que o acervo seja consumido por qualquer SIG do mercado sem intermediação — princípio de portabilidade e soberania do dado.

---

**Nota de enquadramento.** Sistema concebido e desenvolvido no contexto de um cliente específico. Este documento descreve a capacidade demonstrada; não constitui oferta de produto de prateleira nem autoriza revenda. Uma implantação para outro cliente é projeto sob medida, com escopo, dados e integrações próprios.

*Base de apuração: central de ajuda pública da aplicação (11 guias), especificação OpenAPI da API, repositório do código e documentação institucional do ecossistema.*
