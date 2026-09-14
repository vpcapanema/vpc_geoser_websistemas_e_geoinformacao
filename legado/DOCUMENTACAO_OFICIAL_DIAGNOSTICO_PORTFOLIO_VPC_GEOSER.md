# Diagnóstico Oficial do Portfólio VPC-GEOSER

**Documento de referência da etapa de diagnóstico**  
**Data da consolidação:** 19 de julho de 2026  
**Fonte primária do inventário:** [PLI Hub](https://vpcapanema.github.io/pli-hub/)  
**Fonte técnica complementar:** repositórios mantidos em `D:\REPOSITORIOS`, incluindo o ativo estratégico `modelo_exploracao_crescimento_florestal`  
**Situação do documento:** planejamento funcional, comercial e arquitetura técnica de referência consolidados na versão 4.5; homologação das tecnologias ainda pendente

## Executive Summary

- **A VPC-GEOSER não comercializará o conjunto atual como uma suíte compartilhada de aplicações.** O produto central será uma plataforma capaz de configurar, gerar e provisionar novas aplicações independentes para cada cliente.
- **O catálogo comercial será formado por modelos de solução configuráveis.** O cliente escolherá um modelo, iniciará ou adquirirá um período de teste, personalizará identidade visual e capacidades funcionais permitidas e receberá uma aplicação própria em outro ambiente.
- **O inventário estratégico contém 15 ativos: 14 entradas do PLI Hub e o Modelo Dinâmico Florestal — MDF.** Eles fornecem modelos de telas, fluxos, motores analíticos, serviços geoespaciais, APIs, estruturas de dados, componentes, referências de domínio e propriedade intelectual científica; não equivalem automaticamente aos itens do catálogo.
- **O MDF terá posição de destaque no portfólio.** Resultado da tese de doutorado de Vinicius Capanema, ele combina modelagem espacialmente explícita, dinâmica florestal, exploração seletiva, fatores econômicos e fiscalização. Sua origem científica constitui diferenciação técnica e comercial da VPC-GEOSER, embora a aplicação web ainda não esteja finalizada.
- **A reanálise aponta nove famílias iniciais de catálogo.** A família de Dinâmica Florestal e Exploração Sustentável passa a integrar a primeira onda ao lado de Geoportal, roteamento inteligente, ocorrências, riscos climáticos, inteligência de dados, apoio à decisão, pesquisas e formulários e segurança viária.
- **A análise de mercado reduz as nove hipóteses especializadas a quatro produtos VPC Specialized.** Forest Dynamics, Inteligência Territorial, Resiliência Climática e de Infraestrutura e Operações Territoriais formam a linha avançada. Segurança viária torna-se edição vertical; BI, formulários, AHP, roteamento e portal documental tornam-se capacidades internas ou módulos.
- **O catálogo completo também terá a linha VPC Business.** Ela oferecerá aplicações empresariais essenciais — site, portfólio, clientes, produtos, serviços, vendas e pós-venda — em pacotes simples, modulares, customizados e implantados de forma independente para cada cliente.

## 1. Finalidade deste documento

Este documento organiza oficialmente os resultados da etapa de diagnóstico do ecossistema de aplicações da VPC-GEOSER e os reinterpreta de acordo com o modelo comercial correto: uma fábrica de aplicações independentes, visual e funcionalmente customizadas para cada cliente.

Seu objetivo é registrar, para cada entrada do PLI Hub:

- finalidade e domínio;
- público usuário provável ou explicitamente indicado pela aplicação;
- problema atendido;
- funcionalidades e fluxos observáveis;
- entradas, saídas e integrações;
- maturidade funcional, técnica e operacional;
- capacidade de reutilização;
- natureza atual do ativo;
- potencial comercial preliminar;
- pontos fortes, limitações, oportunidades e riscos;
- evidências utilizadas e lacunas de validação.

O documento serve como base para a construção do catálogo comercial de modelos de solução. As famílias propostas são uma versão inicial do catálogo e deverão evoluir conforme forem definidos os limites de customização, os pacotes, o trial, o provisionamento e a manutenção das aplicações geradas.

## 2. Limites e princípios da análise

### 2.1 O Hub não é o catálogo comercial

O PLI Hub foi tratado como porta de entrada para o inventário. As categorias exibidas pelo Hub — Sistemas Maiores, Análises Exploratórias e Ferramentas Analíticas e de Produção — são categorias de navegação, não classificações comerciais definitivas.

### 2.2 Uma aplicação não equivale automaticamente a um produto

Cada entrada foi examinada para identificar sua natureza atual. As classificações utilizadas neste diagnóstico incluem:

- plataforma institucional;
- módulo especializado;
- serviço público;
- sistema vertical;
- framework interno;
- ferramenta analítica;
- entrega analítica estática;
- relatório técnico;
- portal documental;
- protótipo ou scaffold.

### 2.3 Evidência funcional e evidência técnica são diferentes

As conclusões distinguem três níveis de comprovação:

1. **Validado em produção:** conteúdo e comportamento observados diretamente na aplicação publicada.
2. **Validado parcialmente:** somente telas públicas ou não autenticadas puderam ser examinadas.
3. **Identificado no repositório:** capacidade encontrada em código, páginas, rotas ou módulos, mas não confirmada na aplicação funcionando.

Nenhuma funcionalidade identificada apenas no repositório deve ser apresentada comercialmente como serviço operacional sem nova validação.

### 2.4 Nenhum serviço foi iniciado localmente

O diagnóstico técnico foi feito por leitura estrutural. Não foram iniciados servidores locais, não foram submetidos formulários, não foram usados logins e nenhum arquivo ou estado de container da VM foi alterado.

### 2.5 Stack obrigatoriamente open source

O site da VPC-GEOSER, o plano de controle, a fábrica e as aplicações geradas para clientes deverão utilizar uma stack principal integralmente open source. Serviços proprietários somente poderão existir como integrações externas opcionais, substituíveis e não obrigatórias ao funcionamento básico.

## 3. Metodologia aplicada

### 3.1 Inventário

Foram lidos os 14 cards publicados no PLI Hub, incluindo título, categoria, descrição e URL de destino.

Além dos cards, foi incorporado ao inventário o repositório `D:\REPOSITORIOS\modelo_exploracao_crescimento_florestal`, indicado pelo autor como ativo estratégico originado de sua tese de doutorado. Como ele ainda não está representado no Hub, sua inclusão demonstra que o Hub permanece apenas como uma das fontes do inventário, e não como limite do portfólio.

### 3.2 Exploração das aplicações publicadas

As URLs foram acessadas para verificar:

- disponibilidade;
- títulos e seções;
- menus e rotas públicas;
- formulários e controles;
- mapas e painéis;
- entradas solicitadas;
- formatos de saída;
- documentação e APIs expostas;
- mensagens de falha ou indisponibilidade.

### 3.3 Cruzamento com os repositórios

Os repositórios candidatos foram examinados para identificar:

- linguagens e tecnologias predominantes;
- organização dos módulos;
- telas e templates;
- rotas e APIs;
- persistência e migrações;
- testes identificáveis;
- pipelines analíticos;
- versões ou gerações duplicadas;
- indícios de reutilização.

Ambientes virtuais, dependências instaladas e metadados Git foram desconsiderados na contagem de arquivos-fonte.

### 3.4 Critérios de maturidade

A maturidade foi avaliada em dimensões separadas:

- **funcional:** amplitude e coerência dos fluxos;
- **técnica:** modularidade, persistência, APIs, testes e organização;
- **operacional:** disponibilidade e capacidade de funcionar na publicação oficial;
- **comercial:** clareza do problema, público, entregável e possibilidade de implantação repetível.

## 4. Inventário consolidado

| # | Ativo inventariado | Estado observado | Natureza atual diagnosticada | Maturidade relativa | Reutilização |
|---:|---|---|---|---|---|
| 1 | SIGMA-PLI | Ativo, acesso autenticado | Plataforma institucional | Média-alta, com validação interna pendente | Alta |
| 2 | PLI Smart Router | Ativo | Módulo geoespacial de roteamento | Média | Alta |
| 3 | PLI Reporta | Ativo | Serviço público e módulo operacional | Média-alta | Alta |
| 4 | PLI-HazardTrack | Ativo | Módulo de inteligência de risco | Média-alta | Alta |
| 5 | FAD-Stats 2.0 | Ativo | Plataforma analítica | Alta relativa | Alta |
| 6 | Acidentes Infosiga | Suspenso | Entrega analítica estática | Baixa operacional | Média |
| 7 | Acidentes DER | Suspenso | Entrega analítica estática | Baixa operacional | Média |
| 8 | Densidade Malha SP | Suspenso | Relatório técnico geoespacial | Baixa como aplicação | Média |
| 9 | SRA PLI Starter | Suspenso | Protótipo ou scaffold | Baixa | Média |
| 10 | Sistema Apoio Decisão | Suspenso | Framework interno de decisão | Média-alta técnica | Muito alta |
| 11 | Calculadora Aderência 2.0 | Suspenso | Calculadora web estática | Baixa-média | Média |
| 12 | AHP Tool Calculator | Suspenso | Ferramenta analítica estática | Média funcional | Alta |
| 13 | Formulário Embarcadores | Suspenso | Sistema de coleta e análise | Média-alta técnica | Alta |
| 14 | Relatórios D11 | Ativo | Portal documental | Média como publicação | Baixa como software |
| 15 | Modelo Dinâmico Florestal — MDF | Em desenvolvimento, com núcleo web implementado | Modelo científico espacial e família estratégica de produto | Média técnica; baixa operacional; alta diferenciação científica | Muito alta |

## 5. Diagnóstico individual das aplicações

## 5.1 SIGMA-PLI

### Objetivo, domínio e problema atendido

O SIGMA-PLI se apresenta como Sistema Integrado de Gestão, Monitoramento e Apoio Técnico ao PLI/SP. Seu domínio é a gestão institucional do Plano de Logística e Investimentos, com diferentes níveis de acesso e funções operacionais.

### Usuários observáveis

A tela de autenticação diferencia os seguintes perfis:

- Gestor;
- Analista;
- Operador de Sistema;
- Visualizador, com acesso somente para leitura.

### Fluxos e funcionalidades validados

Foi possível validar a entrada da plataforma, composta por:

- identificação por e-mail ou nome de usuário;
- senha;
- seleção de tipo de usuário;
- recuperação de senha;
- criação de conta.

Os fluxos posteriores ao login não foram examinados, pois exigem credenciais.

### Evidência técnica complementar

O repositório `sigma-pli` possui amplo escopo, com backend, templates, módulos, banco de dados versionado, migrações, scripts, infraestrutura, documentação e recursos geoespaciais. Foram identificados aproximadamente 2.695 arquivos-fonte e 28 arquivos com características de teste, além de 51 arquivos relacionados a migrações ou versionamento de banco.

### Entradas, saídas e integrações

- **Entradas confirmadas:** credenciais e perfil de acesso.
- **Saídas confirmadas:** sessão autenticada, condicionada à validação das credenciais.
- **Integrações indicadas:** autenticação compartilhada com o PLI Reporta; demais integrações precisam ser confirmadas dentro do sistema.

### Diagnóstico de maturidade

- **Funcional:** não mensurável integralmente sem acesso autenticado.
- **Técnica:** média-alta devido à amplitude e à presença de persistência versionada.
- **Operacional:** ativo na tela de acesso.
- **Reutilização:** alta, especialmente como núcleo de identidade, gestão e integração.

### Natureza atual

Plataforma institucional e principal candidata a núcleo de gestão do ecossistema. Esta é uma classificação diagnóstica, não uma decisão comercial definitiva.

### Potencial comercial preliminar

Possui potencial para oferta institucional B2G ou B2B de gestão integrada, mas sua vendabilidade depende da comprovação dos módulos internos, separação entre código genérico e regras específicas do PLI-SP, governança de dados e capacidade de implantação multi-instituição.

### Pontos fortes

- autenticação estruturada por perfil;
- escopo técnico amplo;
- base potencial para serviços compartilhados;
- persistência e migrações identificadas.

### Limitações e riscos

- ausência de validação dos fluxos internos;
- possível concentração excessiva de responsabilidades;
- grande volume de arquivos, documentos, legados e artefatos no mesmo repositório;
- necessidade de identificar módulos canônicos e código histórico.

## 5.2 PLI Smart Router

### Objetivo, domínio e problema atendido

O PLI Smart Router calcula e compara rotas rodoviárias. O problema atendido é a definição de trajetos convencionais ou ajustados por adversidades geoespaciais.

### Usuários prováveis

- analistas de transporte;
- planejadores logísticos;
- operadores rodoviários;
- equipes de planejamento territorial;
- usuários técnicos que necessitam exportar uma rota.

### Fluxos e funcionalidades validados

- definição de origem e destino por latitude e longitude;
- busca por cidade, endereço ou CEP;
- seleção de pontos diretamente no mapa;
- resolução de coordenadas;
- cálculo de rota convencional;
- cálculo de rota Smart, considerando camadas ativas;
- reset dos pontos;
- exportação de rota em JSON;
- exportação de rota em Shapefile compactado;
- mapa Leaflet com fundos cartográficos.

### Entradas, saídas e integrações

- **Entradas:** coordenadas, localidade, endereço, CEP e pontos selecionados no mapa.
- **Saídas:** rota cartográfica, metadados, JSON e Shapefile.
- **Integrações declaradas na própria aplicação:** OpenStreetMap, OSRM e ViaCEP.

### Diagnóstico de maturidade

- **Funcional:** média; o fluxo principal é claro e acessível.
- **Técnica:** média; o repositório contém aproximadamente 236 arquivos-fonte e 77 evidências de teste.
- **Operacional:** ativo, porém o catálogo de camadas permaneceu em carregamento durante a inspeção.
- **Reutilização:** alta, pois roteamento, geocodificação e exportação podem atender diferentes produtos.

### Natureza atual

Módulo geoespacial especializado, com possibilidade de uso autônomo, integração por serviço ou incorporação a uma plataforma maior.

### Potencial comercial preliminar

Pode ser comercializado como componente de roteamento com análise de restrições e riscos. O diferencial não está no cálculo convencional, amplamente disponível no mercado, mas na composição com camadas próprias, eventos, riscos e regras institucionais.

### Pontos fortes

- múltiplas formas de definir a rota;
- comparação entre rota convencional e rota Smart;
- exportação geoespacial;
- arquitetura funcional facilmente compreensível.

### Limitações e riscos

- dependência de serviços externos;
- catálogo de camadas não carregado na inspeção;
- necessidade de comprovar a qualidade da lógica de desvio;
- possível sobreposição com funções geoespaciais de outros sistemas.

## 5.3 PLI Reporta

### Objetivo, domínio e problema atendido

O PLI Reporta organiza relatos cidadãos relacionados ao sistema viário e manifestações gerais. O problema atendido é a captura, localização, moderação e publicação de ocorrências.

### Usuários

- cidadãos;
- operadores de atendimento;
- moderadores;
- gestores públicos;
- equipes responsáveis por manutenção e resposta;
- integradores que consomem a API pública.

### Fluxos e funcionalidades validados

- escolha entre evento de tráfego e manifestação cidadã;
- categorização de eventos, incluindo buraco, alagamento, acidente, incêndio, animal ou objeto na pista, queda de árvore, veículo quebrado, bloqueio, obra, lentidão, sinalização e outros;
- classificação de manifestações em elogio, sugestão ou reclamação;
- descrição textual;
- envio ou captura de fotografia;
- seleção complementar de dados;
- mapa público;
- documentação de API pública;
- acesso restrito integrado ao SIGMA-PLI.

### Entradas, saídas e integrações

- **Entradas:** categoria, descrição, localização, imagem e informações complementares.
- **Saídas:** registro submetido, publicação moderada no mapa e feed GeoJSON.
- **Integrações:** autenticação SIGMA-PLI e API pública geoespacial.

A documentação da API informou endpoints públicos para eventos aprovados e resolvidos. Durante a inspeção, o manifesto dinâmico da API não foi carregado, embora a documentação estática estivesse disponível.

### Diagnóstico de maturidade

- **Funcional:** média-alta no fluxo público.
- **Técnica:** média-alta; aproximadamente 309 arquivos-fonte, 57 evidências de teste e 16 arquivos associados a migrações.
- **Operacional:** parcialmente ativo; páginas públicas respondem, mas uma dependência da API apresentou indisponibilidade.
- **Reutilização:** alta como serviço de ocorrências, moderação e publicação geográfica.

### Natureza atual

Serviço público de relacionamento e módulo operacional de gestão de ocorrências.

### Potencial comercial preliminar

Pode atender municípios, concessionárias, órgãos rodoviários e operadores de infraestrutura. A oferta pode assumir formato SaaS, implantação institucional ou módulo integrado, desde que sejam resolvidos identidade, moderação, proteção de dados, níveis de serviço e isolamento entre clientes.

### Pontos fortes

- fluxo cidadão claro;
- separação entre evento e manifestação;
- moderação e estados de publicação;
- mapa e API pública;
- integração com autenticação institucional.

### Limitações e riscos

- manifesto da API indisponível na inspeção;
- necessidade de políticas de privacidade, retenção e moderação;
- risco de abuso, registros falsos e conteúdo impróprio;
- dependência de operação contínua do backoffice.

## 5.4 PLI-HazardTrack

### Objetivo, domínio e problema atendido

O PLI-HazardTrack apoia o monitoramento de riscos climáticos extremos na malha rodoviária. Combina risco geológico, risco hidrológico e risco de fogo com procedimentos operacionais do PPDC.

### Usuários

- centros de operação rodoviária;
- Defesa Civil;
- equipes do DER-SP;
- concessionárias;
- analistas geotécnicos, hidrológicos e ambientais;
- integradores de dados de risco.

### Fluxos e funcionalidades validados

- mapa integrado de riscos;
- camadas de movimentos de massa, inundação e incêndios;
- filtros por região, rodovia e trecho;
- busca simples;
- busca avançada com critérios;
- consulta histórica;
- linha do tempo;
- seleção de horizonte de risco de fogo;
- camadas de apoio e limites administrativos;
- página de ações operacionais PPDC;
- documentação de ajuda;
- glossário técnico;
- documentação da API pública.

A página de ações indicou 1.618 trechos monitorados, nível vigente de Monitoramento e atualização em 19 de julho de 2026. No painel principal, alguns componentes exibiram mensagens de espera por dados.

### Entradas, saídas e integrações

- **Entradas:** região, rodovia, trecho, camada, horizonte, data histórica e critérios de consulta.
- **Saídas:** mapas, classificações de risco, recomendações PPDC, séries e feeds GeoJSON ou JSON.
- **Integrações indicadas:** MERGE/INPE, WRF/CPTEC/INPE, dados DER-SP, OpenStreetMap e CARTO.

### Diagnóstico de maturidade

- **Funcional:** média-alta, com documentação extensa e fluxos operacionais definidos.
- **Técnica:** média-alta; aproximadamente 1.349 arquivos-fonte e 68 evidências de teste.
- **Operacional:** ativo, mas com sinais de dados incompletos ou carregamento parcial.
- **Reutilização:** alta para monitoramento, alertas, mapas de risco e APIs.

### Natureza atual

Módulo de inteligência de risco climático e apoio operacional.

### Potencial comercial preliminar

Tem potencial para órgãos rodoviários, concessionárias, defesa civil e gestores de infraestrutura. A oferta comercial depende de contratos e licenças das fontes, confiabilidade das previsões, rastreabilidade metodológica e responsabilidade sobre alertas.

### Pontos fortes

- integração de três classes de risco;
- ligação entre análise e protocolo operacional;
- documentação pública detalhada;
- API para integração;
- forte especialização no domínio rodoviário.

### Limitações e riscos

- componentes aguardando dados;
- elevada dependência de fontes externas e atualizações periódicas;
- risco de interpretação indevida de alertas;
- necessidade de disponibilidade, auditoria e monitoramento 24 horas em uso crítico.

## 5.5 FAD-Stats 2.0

### Objetivo, domínio e problema atendido

A FAD-Stats é uma plataforma de análise estatística, espacial e territorial de dados oficiais. Ela reduz o esforço necessário para cruzar fontes públicas e gerar visualizações estruturadas.

### Usuários

- analistas de políticas públicas;
- economistas e estatísticos;
- planejadores territoriais e logísticos;
- pesquisadores;
- gestores que necessitam de evidências para decisão.

### Fluxos e funcionalidades validados

- análise individual de uma fonte;
- análise cruzada entre fontes;
- seleção de foco analítico: evolução, distribuição espacial, ranking, composição, comparação ou modo personalizado;
- filtros encadeados por fonte, pesquisa, produto, variável, período e território;
- múltiplos tipos de gráficos e mapas;
- exportação em PNG, CSV, XLSX, PDF e JSON;
- ajuda detalhada e tutoriais;
- endpoint de integridade.

O endpoint de integridade respondeu com status `ok` e versão `2.0.0`.

### Fontes declaradas

- IBGE;
- SECEX/MDIC;
- MTE;
- ANTT.

### Diagnóstico de maturidade

- **Funcional:** alta relativa dentro do portfólio observado.
- **Técnica:** alta relativa; aproximadamente 638 arquivos-fonte, 139 evidências de teste e uma automação de CI identificada.
- **Operacional:** ativo e com healthcheck funcional.
- **Reutilização:** alta como plataforma transversal de inteligência de dados.

### Natureza atual

Plataforma analítica generalizável.

### Potencial comercial preliminar

Pode assumir modelo SaaS, implantação institucional ou serviço gerenciado de inteligência territorial. A diferenciação dependerá da curadoria das fontes, facilidade de uso, qualidade dos cruzamentos, atualização automatizada e capacidade de atender dados privados do cliente.

### Pontos fortes

- proposta de valor clara;
- múltiplas fontes oficiais;
- análise individual e cruzada;
- territorialidade e exportações;
- documentação de uso;
- maior evidência de testes entre os repositórios examinados.

### Limitações e riscos

- necessidade de validar consultas completas com dados reais;
- dependência de atualização e estabilidade das fontes;
- possibilidade de sobreposição com ferramentas genéricas de BI;
- necessidade de governança de métricas e rastreabilidade das transformações.

## 5.6 Acidentes Infosiga

### Objetivo e escopo

Produzir análises exploratórias e geográficas de acidentes rodoviários a partir de dados do Infosiga SP.

### Evidência disponível

A URL publicada estava suspensa. O repositório contém:

- dashboard principal;
- análise geográfica;
- relatório executivo;
- guia de acesso;
- filtros analíticos;
- rankings de rodovias e subtrechos;
- análises de vítimas, temporalidade e criticidade;
- mapas e tabelas analíticas.

### Diagnóstico

- **Funcional:** não validado em produção.
- **Técnica:** adequada a um pipeline de geração de publicação analítica.
- **Operacional:** baixa, devido à suspensão.
- **Reutilização:** média, principalmente para métodos, indicadores e componentes de análise de segurança viária.

### Natureza atual

Entrega analítica estática ou demonstração de capacidade analítica, e não sistema transacional.

### Potencial comercial preliminar

O valor comercial está mais próximo de um módulo de segurança viária, serviço analítico ou pacote de estudos do que de um SaaS independente em seu estado atual.

### Riscos

- publicação suspensa;
- ausência de testes identificáveis;
- necessidade de validar atualização dos dados;
- possível duplicação com Acidentes DER e módulos futuros do SIGMA ou FAD-Stats.

## 5.7 Acidentes DER

### Objetivo e escopo

Explorar dados de acidentes do DER-SP por rodovia, regional, período, gravidade, tipo e localização.

### Evidência disponível

A aplicação publicada estava suspensa. O repositório contém 29 análises HTML, cobrindo:

- acidentes e vítimas por ano;
- gravidade;
- tipos de acidente;
- rodovias e regionais;
- distribuição por quilômetro;
- sazonalidade;
- densidade;
- mortalidade;
- correlação;
- rankings e resumos estatísticos.

### Diagnóstico

- **Funcional:** não validado em produção.
- **Técnica:** orientada à geração de resultados e relatórios.
- **Operacional:** baixa.
- **Reutilização:** média como biblioteca de análises de segurança viária.

### Natureza atual

Entrega analítica estática.

### Potencial comercial preliminar

Pode compor um módulo unificado de segurança viária ou uma oferta de estudos. Não há evidência suficiente para defendê-lo como produto autônomo.

### Riscos

- sobreposição direta com a análise Infosiga;
- ausência de testes identificáveis;
- grande quantidade de páginas isoladas;
- suspensão da publicação oficial.

## 5.8 Densidade Malha SP

### Objetivo e escopo

Analisar densidade, extensão, acessibilidade, hierarquia e distribuição territorial da malha rodoviária estadual paulista.

### Evidência disponível

A publicação estava suspensa. O repositório contém um relatório estruturado em:

- objetivos;
- metodologia;
- dados;
- resultados;
- discussão;
- conclusão;
- anexos e dezenas de mapas por município, região e recortes territoriais.

Também existem scripts de download, processamento, classificação, geração de mapas, exportação para QGIS e produção de relatórios.

### Diagnóstico

- **Funcional:** publicação de estudo, não fluxo aplicativo.
- **Técnica:** pipeline analítico geoespacial relevante.
- **Operacional:** baixa como serviço publicado.
- **Reutilização:** média para novos estudos e relatórios territoriais.

### Natureza atual

Relatório técnico geoespacial e pipeline de produção cartográfica.

### Potencial comercial preliminar

É mais adequado a uma oferta de consultoria, estudo técnico, observatório ou módulo de geração de indicadores territoriais do que a um produto SaaS independente.

### Riscos

- mapas e resultados podem ficar desatualizados;
- dependência de dados e procedimentos específicos;
- ausência de testes identificáveis;
- ferramentas operacionais misturadas ao conteúdo final.

## 5.9 SRA PLI Starter

### Objetivo declarado

Servir como versão inicial de um Sistema de Recursos Aéreos para gestão de recursos e operações aéreas.

### Evidência disponível

A URL publicada estava suspensa. O repositório candidato `sra_scaffold` contém aproximadamente 14 arquivos-fonte, páginas de modelo canônico, resumo de esquema e uma estrutura Flask mínima.

### Diagnóstico

- **Funcional:** insuficiente para comprovar gestão completa de recursos aéreos.
- **Técnica:** inicial.
- **Operacional:** baixa.
- **Reutilização:** média apenas como ponto de partida estrutural.

### Natureza atual

Protótipo ou scaffold.

### Potencial comercial preliminar

Não está pronto para comercialização. O domínio pode ter valor, mas exige definição de usuários, processos, ativos, missões, segurança, rastreabilidade e integrações aeronáuticas.

### Riscos

- nome e descrição sugerem capacidade superior à evidência encontrada;
- escopo operacional não comprovado;
- publicação suspensa;
- possível existência de outras gerações do SRA ainda não confirmadas como versão canônica.

## 5.10 Sistema Apoio Decisão

### Objetivo, domínio e problema atendido

Estruturar processos de tomada de decisão multicritério, desde o cadastro da demanda até hierarquização, análise AHP, colaboração e parecer.

### Evidência disponível

A aplicação publicada estava suspensa. O repositório apresenta aproximadamente 529 arquivos-fonte e módulos para:

- autenticação e administração;
- demandas;
- domínios e universos de análise;
- planos e programas;
- objetos AHP;
- configuração multicritério;
- comparação colaborativa;
- hierarquização;
- painel;
- geoprocessamento e camadas;
- auditoria e estados de processo.

### Diagnóstico

- **Funcional:** amplo no código, não validado em produção.
- **Técnica:** média-alta e modular.
- **Operacional:** baixa devido à suspensão.
- **Reutilização:** muito alta, pois oferece motores e fluxos aplicáveis a diferentes domínios.

### Natureza atual

Framework interno ou plataforma de apoio à decisão, e não apenas uma ferramenta isolada.

### Potencial comercial preliminar

Pode ser base para uma suíte de priorização de projetos, investimentos, políticas ou ativos. Antes da comercialização, precisa demonstrar o fluxo completo, configurar múltiplas organizações e separar o motor genérico das regras específicas do PLI.

### Pontos fortes

- arquitetura modular;
- amplitude maior que a descrição do card;
- combinação de AHP, colaboração e geoprocessamento;
- repositório com atualização recente.

### Limitações e riscos

- serviço publicado suspenso;
- somente 20 evidências de teste para um escopo amplo;
- possível sobreposição com AHP Tool e Calculadora de Aderência;
- necessidade de confirmar persistência, segurança e auditoria em execução.

## 5.11 Calculadora Aderência 2.0

### Objetivo e fluxo

Avaliar aderência de indicadores, metas ou resultados por um fluxo de páginas:

1. início;
2. avaliação;
3. resultados.

### Evidência disponível

A publicação estava suspensa. O repositório possui aproximadamente 35 arquivos-fonte, predominantemente HTML, JavaScript e CSS, sem backend próprio identificado.

### Diagnóstico

- **Funcional:** fluxo delimitado no código.
- **Técnica:** baixa-média, com arquitetura estática.
- **Operacional:** baixa.
- **Reutilização:** média como componente de avaliação.

### Natureza atual

Calculadora web estática.

### Potencial comercial preliminar

É mais adequada como módulo do Sistema de Apoio à Decisão ou como ferramenta incorporada a projetos de avaliação. A proposta isolada possui barreira comercial limitada.

### Riscos

- nenhuma evidência de testes automatizados;
- publicação suspensa;
- regras de cálculo precisam ser formalmente documentadas e validadas;
- sobreposição com outros ativos multicritério.

## 5.12 AHP Tool Calculator

### Objetivo, domínio e problema atendido

Executar análise hierárquica de processos para ponderar critérios e apoiar priorizações.

### Fluxos identificados

- escolha do número de critérios;
- nomeação dos critérios;
- escolha do método;
- comparação pareada;
- cálculo e apresentação dos resultados;
- entrada manual;
- upload de matriz em CSV ou JSON;
- uso da escala de Saaty.

### Diagnóstico

- **Funcional:** média, com wizard coerente no código.
- **Técnica:** média para ferramenta estática.
- **Operacional:** baixa devido à suspensão.
- **Reutilização:** alta como motor ou componente multicritério.

### Natureza atual

Ferramenta analítica estática e potencial módulo da suíte de apoio à decisão.

### Potencial comercial preliminar

O AHP é amplamente conhecido e possui concorrência consolidada. O valor diferencial dependerá da integração com demandas, colaboração, geoprocessamento, auditoria e relatórios, não apenas do cálculo matemático isolado.

### Riscos

- ausência de testes identificáveis;
- publicação suspensa;
- duplicação funcional com o Sistema de Apoio à Decisão;
- necessidade de validar consistência, tratamento de matrizes inválidas e precisão numérica.

## 5.13 Formulário Embarcadores

### Objetivo, domínio e problema atendido

Capturar, validar, armazenar e analisar entrevistas com embarcadores para estudos logísticos e de transporte.

### Usuários

- entrevistadores;
- coordenadores de pesquisa;
- analistas logísticos;
- gestores do estudo;
- usuários responsáveis por visualizar respostas e indicadores.

### Funcionalidades identificadas

- formulário de entrevista;
- salvamento e validação de respostas;
- consulta e listagem de pesquisas;
- cadastro de entrevistadores;
- listas de estados, municípios, países, instituições e funções;
- validação de CNPJ por serviço externo;
- painel de respostas;
- visualizador de dados;
- analytics de volume, produto, custos, distância, capacidade, modal e dificuldades;
- exportação em PDF e Excel.

### Evidência técnica

O repositório possui aproximadamente 287 arquivos-fonte, frontend, backend FastAPI, modelos, esquemas, persistência, migrações, rotas e 12 evidências de teste.

### Diagnóstico

- **Funcional:** amplo no código, não validado em produção.
- **Técnica:** média-alta.
- **Operacional:** baixa devido à suspensão.
- **Reutilização:** alta para pesquisas estruturadas e levantamentos logísticos.

### Natureza atual

Sistema vertical de coleta e análise de pesquisa.

### Potencial comercial preliminar

Pode ser oferecido como solução de pesquisa logística, aplicação configurável por projeto ou módulo de coleta de uma plataforma maior. Para SaaS multi-instituição, seriam necessários gestão de organizações, permissões, versionamento de questionários e isolamento de dados.

### Pontos fortes

- fluxo completo de coleta e análise;
- backend estruturado;
- validação externa;
- exportações;
- endpoints analíticos.

### Limitações e riscos

- serviço publicado suspenso;
- tratamento de dados empresariais e pessoais;
- dependência de serviços externos de CNPJ;
- presença de backups, testes e scripts operacionais misturados ao código principal;
- necessidade de confirmar segurança e governança da base.

## 5.14 Relatórios D11

### Objetivo e escopo

Organizar e disponibilizar documentos técnicos relativos às atividades D11 do PLI.

### Conteúdo validado

A página pública estava ativa e apresentava:

- sistematização multidimensional dos 31 temas;
- resumo da metodologia;
- sumário dos resultados;
- avaliação de aderência de temas ao termo de referência;
- carteira de 13 projetos relacionados aos temas aéreo e mudanças climáticas.

### Diagnóstico

- **Funcional:** publicação documental ativa.
- **Técnica:** simples, adequada ao papel de índice de documentos.
- **Operacional:** média como conteúdo estático.
- **Reutilização:** baixa como software e alta como conhecimento institucional.

### Natureza atual

Portal documental, não produto de software.

### Potencial comercial preliminar

Pode sustentar ofertas de consultoria, metodologia e estudos, mas não deve ser apresentado como aplicação comercial autônoma.

### Riscos

- documentos podem ficar desatualizados;
- necessidade de controle de versão e autoria;
- risco de o Hub misturar aplicações e conteúdos sem diferenciação visual.

## 5.15 Modelo Dinâmico Florestal — MDF

### Origem e relevância estratégica

O ativo está no repositório `D:\REPOSITORIOS\modelo_exploracao_crescimento_florestal` e materializa resultados da tese de doutorado de Vinicius Capanema, intitulada **“Modelo dinâmico espacial para o estudo do setor florestal extrativista: simulações de diferentes contextos de exploração”**.

Essa origem confere ao MDF uma posição distinta dos demais ativos. Ele não representa somente uma solução de software: reúne pesquisa autoral, formulação científica, conhecimento de domínio, modelo computacional, dados geoespaciais e uma trajetória de reimplementação para a web. Portanto, deve ocupar posição de destaque institucional e comercial no portfólio VPC-GEOSER.

### Objetivo, domínio e problema atendido

O MDF permite estudar como diferentes condições de exploração seletiva, crescimento, regeneração, mortalidade, dano colateral, preço da madeira, multas e intensidade de fiscalização podem modificar a estrutura e a distribuição espacial da floresta ao longo do tempo.

O problema central é apoiar a compreensão e a comparação de cenários de manejo e pressão extrativista sobre paisagens florestais. Seu domínio combina:

- manejo florestal sustentável;
- dinâmica e crescimento florestal;
- exploração seletiva;
- economia e fiscalização ambiental;
- simulação espacial e temporal;
- planejamento, pesquisa e avaliação de políticas públicas.

### Usuários e compradores potenciais

- órgãos ambientais e florestais;
- gestores de concessões e manejo florestal;
- empresas e responsáveis por Planos de Manejo Florestal Sustentável;
- universidades e institutos de pesquisa;
- consultorias ambientais e florestais;
- organizações de conservação;
- financiadores, certificadoras e entidades de controle interessadas em avaliação de cenários.

### Evidências examinadas

Foram examinados, sem alteração ou execução do repositório:

- a tese em PDF e sua extração textual;
- o modelo original `ForestExploitation.lua`, desenvolvido sobre a abordagem celular;
- as matrizes de aderência entre tese e implementação;
- a avaliação dos submodelos espaciais;
- a especificação da V1 web;
- as matrizes de proveniência dos campos da grade;
- os dados geoespaciais de calibração, área de estudo e Juara;
- a implementação `web-mdf`, organizada como monorepo React, TypeScript e Vite;
- o motor `model-core`, o worker de simulação, os tipos compartilhados, o pipeline de dados, a interface e os testes existentes.

### Funcionalidades já identificadas na implementação web

- carregamento de um pacote regional canônico derivado da malha real de Juara;
- representação de células florestais por nove classes diamétricas;
- cenários econômicos EC1, EC2 e EC3;
- cálculo explícito da decisão econômica a partir de preço da madeira, multa e fiscalização;
- execução ordenada dos submodelos de exploração, dano colateral, mortalidade jovem, mortalidade adulta, crescimento e nascimento;
- geração de snapshots temporais;
- indicadores regionais de árvores totais, volume explorável, árvores extraídas e dano colateral;
- processamento em Web Worker para preservar a responsividade da interface;
- mapa celular com MapLibre;
- seleção de cenário e navegação por linha do tempo;
- testes unitários do submodelo econômico, das regras de exploração e da ordem temporal.

### Capacidades previstas, mas ainda não concluídas

- parametrização guiada e avançada pelo usuário;
- importação e validação de novas regiões e inventários;
- comparação lado a lado de cenários;
- perfil estrutural da floresta por célula e região;
- mapas de diferenças e visualizações temporais avançadas;
- persistência, compartilhamento e reprodução de cenários;
- relatórios científicos e executivos;
- gestão de usuários, projetos e permissões;
- calibração regional, rastreabilidade integral dos parâmetros e validação científica ampliada;
- acabamento operacional necessário para trial e provisionamento comercial.

### Entradas, saídas e integrações

**Entradas identificadas:** malhas e inventários florestais, atributos por célula, classes diamétricas, parâmetros de crescimento, recrutamento, mortalidade, dano colateral, diâmetro mínimo de corte, ciclo de corte, volumes, preço da madeira, valor da multa, fiscalização e horizonte temporal.

**Saídas identificadas ou especificadas:** snapshots espaciais e temporais, mapas celulares, totais regionais, estoque e volume explorável, árvores extraídas, dano colateral, estrutura por classe, comparação entre cenários e relatórios.

**Integrações potenciais:** GeoPortal, Data Intelligence, serviços de ingestão geoespacial, armazenamento de cenários, geração de relatórios e módulos de apoio à decisão.

### Diagnóstico de maturidade

- **Científica:** alta como ativo de pesquisa autoral, com tese, formulação conceitual e rastreabilidade documental.
- **Funcional:** média-baixa; há um fluxo web demonstrável no código, mas a experiência completa prevista ainda não foi concluída.
- **Técnica:** média; existe separação entre motor, worker, tipos, pipeline e interface, além de testes focados no núcleo.
- **Operacional:** baixa; não foi identificada neste diagnóstico uma publicação comercial validada, autenticação, persistência multiusuário, provisionamento ou operação assistida.
- **Comercial:** alta em diferenciação e média em prontidão; a oferta é promissora, mas deve ser apresentada inicialmente como produto científico especializado em desenvolvimento ou piloto assistido.

### Natureza atual

**Modelo científico autoral, motor de simulação espacial, aplicação web em desenvolvimento e ativo estratégico de propriedade intelectual.**

### Posição recomendada no portfólio

O MDF deverá originar uma família comercial própria e destacada: **VPC Forest Dynamics — Dinâmica Florestal e Exploração Sustentável**. Não deve ser escondido como simples módulo do GeoPortal ou do Data Intelligence. Esses produtos poderão fornecer componentes, mas o valor central do MDF está no modelo científico e na capacidade de simular cenários florestais espacialmente explícitos.

A posição de destaque deverá ser comunicada por quatro elementos:

1. origem na tese de doutorado;
2. autoria e base metodológica identificadas;
3. demonstração visual da mudança da floresta no espaço e no tempo;
4. oferta inicial controlada como piloto ou projeto assistido, até que o produto alcance maturidade operacional.

### Pontos fortes e oportunidades

- diferenciação difícil de reproduzir apenas com desenvolvimento genérico de software;
- combinação rara de ciência florestal, economia, geoprocessamento e simulação;
- forte potencial visual e demonstrativo;
- parametrização para diferentes regiões, inventários e cenários;
- aplicabilidade em pesquisa, planejamento, manejo, concessões e políticas públicas;
- possibilidade de serviços associados de calibração, preparação de dados, estudos e interpretação;
- capacidade de gerar publicações, relatórios e evidências para projetos científicos e institucionais.

### Limitações e riscos

- aplicação web ainda incompleta;
- necessidade de separar resultados científicos validados de aproximações ou heurísticas de implementação;
- dependência da qualidade e compatibilidade dos inventários regionais;
- risco de uso decisório indevido sem explicitação de hipóteses e incertezas;
- necessidade de validação por região e de versionamento rigoroso dos parâmetros;
- necessidade de definir licenciamento, autoria, citações e proteção da propriedade intelectual;
- custo de suporte especializado superior ao de aplicações puramente cadastrais.

### Regra comercial obrigatória

O MDF não deverá ser vendido como previsão determinística do futuro da floresta. A oferta deverá declarar versão do modelo, região calibrada, dados utilizados, hipóteses, limites, incertezas e finalidade de apoio à análise. Projetos com novos territórios ou inventários deverão passar por validação técnica antes do provisionamento definitivo.

## 6. Capacidades transversais identificadas

O portfólio contém capacidades que aparecem repetidamente e poderão, em etapa posterior, ser tratadas como serviços compartilhados:

- autenticação e perfis de acesso;
- administração e backoffice;
- mapas e componentes cartográficos;
- catálogo de camadas geoespaciais;
- busca espacial e territorial;
- exportação CSV, XLSX, PDF, JSON, GeoJSON e Shapefile;
- APIs públicas;
- pipelines de ingestão e transformação de dados;
- painéis analíticos;
- geração de relatórios;
- motores AHP e multicritério;
- motores de simulação espacial e temporal;
- cenários parametrizados, snapshots e comparação de trajetórias;
- auditoria e estados de processo;
- cabeçalhos e identidade visual institucional.

A existência repetida dessas capacidades não comprova que já exista uma biblioteca comum. Ao contrário, o diagnóstico sugere duplicação de implementações entre os repositórios.

## 7. Fragilidades estruturais do ecossistema

### 7.1 Catálogo e operação estão desalinhados

Oito cards direcionam para serviços suspensos. Um catálogo oficial não deve apresentar como disponível uma aplicação que não pode ser acessada.

### 7.2 Existem múltiplas gerações de aplicações

Foram observadas pastas com nomes semelhantes para SIGMA, SRA, FAD-Stats, Acidentes DER, AHP e Sistema de Apoio à Decisão. Sem indicação canônica, torna-se difícil determinar:

- qual versão está publicada;
- qual versão recebe manutenção;
- qual contém as correções mais recentes;
- qual deve ser usada em uma futura consolidação.

### 7.3 Maturidade técnica e maturidade operacional divergem

Alguns ativos possuem arquitetura técnica substancial, mas estão suspensos. O exemplo mais evidente é o Sistema de Apoio à Decisão, seguido pelo Formulário Embarcadores.

### 7.4 Automação de qualidade é desigual

Há repositórios com quantidade relevante de testes, enquanto outros não apresentam nenhuma evidência de teste automatizado. Automação de CI foi rara na amostra examinada.

### 7.5 Repositórios incluem artefatos que dificultam manutenção

Alguns projetos armazenam ambientes virtuais, dependências instaladas, backups, arquivos temporários, dados pesados e documentação histórica no mesmo espaço do código principal. Isso aumenta volume, reduz clareza e dificulta auditoria.

## 8. Modelo comercial correto: fábrica de aplicações independentes

### 8.1 O que a VPC-GEOSER venderá

A VPC-GEOSER venderá a capacidade de criar uma aplicação completa a partir de um modelo de solução. O cliente não compartilhará uma única aplicação central com todos os demais clientes e não receberá apenas acesso a uma tela já existente.

Cada aquisição resultará em uma nova aplicação:

- gerada a partir de uma base tecnológica mantida pela VPC-GEOSER;
- configurada conforme o modelo selecionado;
- personalizada visual e funcionalmente;
- provisionada em ambiente independente;
- associada a domínio, banco, usuários, segredos e recursos próprios;
- mantida com capacidade de receber atualizações sem perder as customizações autorizadas.

### 8.2 Jornada comercial pretendida

```text
Site comercial da VPC-GEOSER
        ↓
Escolha de uma família de solução
        ↓
Seleção de pacote, módulos e integrações
        ↓
Início ou aquisição do período de teste
        ↓
Customização visual e funcional permitida
        ↓
Geração da aplicação independente
        ↓
Provisionamento em ambiente próprio
        ↓
Homologação pelo cliente
        ↓
Contratação definitiva, operação e evolução
```

### 8.3 O papel do site da empresa

O site comercial deverá acumular funções que normalmente aparecem separadas em um portal de vendas, um configurador e uma plataforma de provisionamento:

- apresentar as famílias de solução;
- demonstrar casos e modelos de referência;
- comparar pacotes e capacidades;
- registrar o cliente e sua organização;
- administrar trial, contratação e cobrança;
- coletar as escolhas de personalização;
- validar combinações de módulos;
- gerar um manifesto completo da aplicação;
- disparar a criação do novo ambiente;
- acompanhar o provisionamento;
- entregar o acesso administrativo ao cliente;
- controlar versões, renovação, suspensão e encerramento.

### 8.4 Separação arquitetural essencial

O modelo exige duas camadas independentes:

1. **Plano de controle VPC-GEOSER:** catálogo, configurador, identidade do comprador, trial, cobrança, geração, provisionamento, versões e suporte.
2. **Aplicações geradas:** sistemas independentes, executados em outros ambientes, com dados e configurações isolados por cliente.

O plano de controle não deve depender do funcionamento diário de uma aplicação gerada. Da mesma forma, a indisponibilidade de uma instância de cliente não deve afetar as demais.

## 9. Reanálise dos 15 ativos como matéria-prima da fábrica

| Ativo atual | Papel na fábrica | Capacidades reaproveitáveis | Famílias do catálogo beneficiadas | Decisão recomendada |
|---|---|---|---|---|
| SIGMA-PLI | Referência de aplicação institucional completa | autenticação, perfis, administração, cadastros, banco, navegação e integração | todas as famílias com backoffice | extrair padrões de aplicação e serviços de gestão; não usar o SIGMA inteiro como molde obrigatório |
| PLI Smart Router | Modelo funcional e motor especializado | roteamento, geocodificação, seleção no mapa, camadas, exportação JSON e Shapefile | Roteamento Inteligente, Geoportal e Riscos | transformar o motor em capacidade selecionável e o front-end em tema de referência |
| PLI Reporta | Modelo de solução de ocorrências | formulário público, categorias, fotografia, geolocalização, moderação, mapa e GeoJSON | Ocorrências e Participação, Operações Territoriais | separar portal público, workflow de moderação, API e backoffice em módulos configuráveis |
| PLI-HazardTrack | Modelo de monitoramento especializado | riscos, alertas, histórico, camadas, PPDC, documentação e feeds | Riscos Climáticos, Geoportal, Operações Territoriais | parametrizar tipos de risco, fontes, níveis, protocolos e territórios |
| FAD-Stats 2.0 | Modelo de aplicação analítica | conectores, filtros encadeados, gráficos, mapas, cruzamentos e exportações | Inteligência de Dados, Segurança Viária, Observatórios | transformar fontes, pesquisas, indicadores, territorialidades e visualizações em configuração |
| Acidentes Infosiga | Pacote de domínio e referência visual | indicadores, rankings, subtrechos, mapas, relatórios e metodologia | Segurança Viária e Inteligência de Dados | reaproveitar métricas e painéis como pacote temático, não como produto isolado |
| Acidentes DER | Biblioteca de análises de segurança viária | 29 análises, gravidade, sazonalidade, densidade, mortalidade e correlações | Segurança Viária | consolidar com Infosiga em um único pacote configurável de segurança viária |
| Densidade Malha SP | Pipeline analítico e modelo de publicação | indicadores territoriais, processamento, mapas, QGIS e relatórios | Geoportal, Inteligência de Dados e Observatórios | converter métodos e mapas em módulos de estudo e publicação, não em aplicação autônoma |
| SRA PLI Starter | Protótipo de um possível modelo vertical | estrutura inicial de recursos e operações aéreas | Operações de Recursos, futura | manter como laboratório até existir fluxo funcional suficiente para catálogo |
| Sistema Apoio Decisão | Motor e framework transversal | demandas, AHP, colaboração, hierarquização, parecer, auditoria e geoprocessamento | Apoio à Decisão e módulos opcionais de outras famílias | decompor em motor multicritério, workflow, colaboração, geoprocessamento e backoffice |
| Calculadora Aderência 2.0 | Componente de cálculo | avaliação, regras de aderência e resultados | Apoio à Decisão e Avaliação | incorporar como módulo; não oferecer isoladamente na primeira versão do catálogo |
| AHP Tool Calculator | Componente analítico | critérios, comparação pareada, consistência, upload e resultados | Apoio à Decisão | unificar com o motor AHP do Sistema de Apoio à Decisão |
| Formulário Embarcadores | Modelo de coleta estruturada | questionários, validações, respostas, CNPJ, analytics, PDF e Excel | Pesquisas e Formulários, Logística | generalizar o questionário e preservar o modelo de embarcadores como pacote vertical |
| Relatórios D11 | Referência de portal de conhecimento | índice documental, metodologia, relatórios e carteira de projetos | Portais de Conhecimento e complemento de todas as famílias | tratar como modelo de publicação e módulo documental, não como produto principal |
| Modelo Dinâmico Florestal — MDF | Modelo científico autoral e base de uma família estratégica | motor ecológico-econômico, simulação celular, cenários EC1–EC3, dinâmica temporal, mapas, indicadores, worker, pipeline e testes | Dinâmica Florestal, Geoportal, Inteligência de Dados e Apoio à Decisão | manter como família própria de destaque; concluir, validar e oferecer inicialmente por piloto assistido |

### 9.1 Conclusão da reanálise

Nenhum dos 15 ativos precisa ser descartado por não constituir um produto autônomo. O valor de alguns está no motor, de outros no fluxo, nos componentes, na metodologia, no conteúdo ou no padrão de apresentação. O MDF distingue-se por reunir esses elementos em torno de propriedade intelectual científica autoral e, por isso, justifica uma família própria de destaque.

A unidade comercial passa a ser a **família de solução configurável**. A unidade técnica passa a ser a **capacidade reutilizável**. A aplicação entregue ao cliente será uma composição versionada dessas capacidades.

## 10. Hipóteses iniciais de catálogo antes da análise de mercado

Os nomes abaixo são nomes de trabalho. A marca comercial definitiva poderá ser definida posteriormente.

**Status desta seção:** registro histórico das nove hipóteses derivadas do diagnóstico técnico. Após confronto com demanda e concorrência, elas foram consolidadas em quatro produtos na seção 20, que prevalece como decisão comercial.

Esta seção é uma **recomendação estratégica derivada do diagnóstico**, e não uma afirmação de que as nove famílias já estejam prontas para venda. A base factual está nas funcionalidades, fluxos, componentes e lacunas registrados nas seções 4 a 9. A transformação dessa base em oferta comercial ainda exige engenharia de produto, validação de mercado, definição contratual e testes do processo de geração.

Para evitar confusão entre evidência e proposta:

- **validado:** capacidades observadas nas aplicações publicadas ou identificadas nos repositórios, sempre com o nível de evidência registrado no diagnóstico individual;
- **inferido:** possibilidade de recombinar capacidades existentes em uma família de solução;
- **proposto:** nome, composição comercial, público-alvo, pacote e posição no catálogo;
- **pendente de validação:** disposição de compra, preço, limites do trial, custo operacional, automação do provisionamento e aderência setorial.

## 10.1 VPC Forest Dynamics — Dinâmica Florestal e Exploração Sustentável

### Posição no catálogo

Produto científico de destaque e expressão direta da pesquisa doutoral que deu origem ao MDF. Deverá receber narrativa própria no site, demonstração visual e identificação explícita de autoria e base metodológica.

### Proposta de valor

Geração de aplicações independentes para simular, visualizar e comparar a evolução espacial e temporal de paisagens florestais sob diferentes condições de manejo, exploração seletiva, crescimento, regeneração, preço da madeira e fiscalização.

### Capacidades-base

- cadastro ou importação de região e grade celular;
- inventário por classes diamétricas;
- presets ecológicos e econômicos;
- cenários EC1, EC2 e EC3;
- parâmetros de manejo, dano, mortalidade, crescimento e recrutamento;
- motor de simulação espacial e temporal;
- mapas animados e linha do tempo;
- indicadores de estoque, volume, extração e dano;
- comparação entre cenários;
- rastreabilidade de dados, parâmetros e versão do modelo;
- relatórios técnicos, científicos e executivos.

### Ativos de origem

Tese de doutorado, modelo `ForestExploitation.lua`, implementação `web-mdf`, dados e matrizes metodológicas do repositório `modelo_exploracao_crescimento_florestal`, complementados por capacidades de GeoPortal, Data Intelligence e Decision Studio.

### Clientes-alvo iniciais

Órgãos ambientais, gestores florestais, concessões, responsáveis por PMFS, universidades, institutos de pesquisa, consultorias, organizações de conservação, certificadoras e financiadores.

### Forma inicial de comercialização

Enquanto a aplicação não alcançar prontidão operacional completa, deverá ser oferecida como **piloto científico assistido**, com preparação ou validação dos dados, calibração regional, configuração do cenário, implantação independente e acompanhamento especializado. A evolução para autosserviço somente deverá ocorrer onde os dados e parâmetros puderem ser validados automaticamente.

## 10.2 VPC GeoPortal

### Proposta de valor

Criação de portais geoespaciais independentes para publicação, consulta, análise e administração de camadas territoriais.

### Capacidades-base

- mapa responsivo;
- catálogo e grupos de camadas;
- busca simples e avançada;
- filtros territoriais e por atributos;
- popups configuráveis;
- legendas e simbologias;
- importação e exportação geoespacial;
- painéis e indicadores vinculados ao mapa;
- área pública e área administrativa;
- portal documental opcional.

### Ativos de origem

Smart Router, HazardTrack, Reporta, Densidade Malha SP, FAD-Stats e componentes geoespaciais do Sistema de Apoio à Decisão.

### Clientes-alvo iniciais

Órgãos públicos, concessionárias, consultorias, empresas de infraestrutura, meio ambiente, logística e planejamento territorial.

## 10.3 VPC Route Intelligence

### Proposta de valor

Aplicações de roteamento customizadas que calculam trajetos convencionais e trajetos condicionados por riscos, restrições ou camadas do cliente.

### Capacidades-base

- origem e destino por coordenadas, endereço, CEP ou mapa;
- múltiplos perfis de rota;
- camadas de restrição;
- cálculo convencional e inteligente;
- comparação de alternativas;
- exportação de rota;
- API de roteamento;
- painel de parâmetros administrativos.

### Ativos de origem

PLI Smart Router, camadas do HazardTrack e eventos do Reporta.

## 10.4 VPC Occurrence & Citizen Portal

### Proposta de valor

Aplicações de registro, triagem, moderação, encaminhamento e publicação de ocorrências ou manifestações territorializadas.

### Capacidades-base

- formulários públicos configuráveis;
- categorias e subcategorias;
- fotografia e anexos;
- geolocalização;
- estados e transições de workflow;
- moderação;
- mapa público;
- relatórios;
- API pública;
- acesso administrativo.

### Ativos de origem

PLI Reporta, autenticação do SIGMA-PLI, mapas compartilhados e mecanismos de analytics.

## 10.5 VPC Climate & Infrastructure Risk

### Proposta de valor

Aplicações de monitoramento de riscos ambientais e operacionais sobre ativos e territórios do cliente.

### Capacidades-base

- cadastro de ativos e unidades de análise;
- ingestão de dados observados e previstos;
- regras de classificação de risco;
- mapas, camadas e séries históricas;
- alertas e níveis operacionais;
- protocolos de ação;
- API de dados;
- glossário e documentação metodológica;
- painel de saúde das fontes.

### Ativos de origem

PLI-HazardTrack, Smart Router, FAD-Stats e padrões de relatório D11.

### Regra comercial importante

As responsabilidades metodológicas, limitações das fontes e caráter de apoio à decisão deverão ser explicitados na configuração e no contrato de cada aplicação.

## 10.6 VPC Data Intelligence

### Proposta de valor

Geração de aplicações analíticas e observatórios de dados adaptados às fontes, indicadores, territórios e identidade do cliente.

### Capacidades-base

- conectores de dados;
- catálogo de fontes e pesquisas;
- filtros encadeados;
- indicadores configuráveis;
- análise individual e cruzada;
- gráficos, rankings, mapas e tabelas;
- exportações;
- metodologia e dicionário de dados;
- painel administrativo das fontes.

### Ativos de origem

FAD-Stats, análises Infosiga e DER, Densidade Malha SP e Relatórios D11.

## 10.7 VPC Decision Studio

### Proposta de valor

Aplicações independentes para estruturar decisões multicritério, priorizar alternativas e documentar pareceres.

### Capacidades-base

- cadastro de demandas;
- definição de critérios e alternativas;
- AHP manual ou por upload;
- cálculo de consistência;
- avaliação de aderência;
- comparação colaborativa;
- hierarquização;
- mapas e critérios geoespaciais opcionais;
- pareceres, trilha de auditoria e relatórios.

### Ativos de origem

Sistema Apoio Decisão, AHP Tool Calculator e Calculadora Aderência 2.0.

## 10.8 VPC Survey & Forms

### Proposta de valor

Aplicações de pesquisa e coleta estruturada, com formulários, validações, gestão de respostas e analytics próprios.

### Capacidades-base

- construtor ou configuração de questionário;
- campos condicionais;
- validações;
- autosave e rascunho;
- listas de domínio;
- integrações cadastrais;
- perfis de entrevistador e gestor;
- acompanhamento de respostas;
- visualizador de dados;
- painéis e exportações.

### Ativos de origem

Formulário Embarcadores, componentes de autenticação do SIGMA-PLI e analytics do FAD-Stats.

### Pacote vertical inicial

Pesquisa com embarcadores e agentes logísticos poderá ser oferecida como configuração pronta dentro desta família.

## 10.9 VPC Road Safety Analytics

### Proposta de valor

Aplicações analíticas dedicadas à segurança viária, configuradas para as bases, indicadores, rodovias e territórios do cliente.

### Capacidades-base

- ingestão de acidentes e vítimas;
- padronização e qualidade dos dados;
- indicadores de frequência, severidade, mortalidade e densidade;
- análise por rodovia, trecho, regional e período;
- rankings e identificação de pontos críticos;
- mapas e séries temporais;
- relatórios executivos;
- exportação e API opcional.

### Ativos de origem

Acidentes Infosiga, Acidentes DER, FAD-Stats e componentes cartográficos compartilhados.

## 10.10 Famílias futuras ou serviços complementares

### VPC Resource Operations

Família futura para gestão de recursos, equipes, ativos e missões. O SRA PLI Starter ainda não oferece evidência suficiente para entrada imediata no catálogo.

### VPC Knowledge Portal

Modelo leve para portais de relatórios, metodologias, projetos e documentos. Pode ser vendido como complemento das demais famílias ou como entrega de consultoria, utilizando Relatórios D11 como referência.

## 11. Matriz de customização oferecida ao cliente

### 11.1 Customização visual em autosserviço

O cliente poderá configurar, dentro de limites validados:

- nome da aplicação;
- logotipo e ícone;
- cores principais, secundárias e de destaque;
- tipografia entre opções aprovadas;
- imagens de capa e identidade institucional;
- domínio ou subdomínio;
- textos institucionais;
- nomenclatura de menus e seções;
- tema claro, escuro ou automático quando suportado.

### 11.2 Customização funcional em autosserviço

- ativação de módulos compatíveis com o pacote;
- campos e rótulos de formulários;
- categorias, estados e listas de domínio;
- perfis e permissões predefinidos;
- indicadores e visualizações disponíveis;
- camadas e grupos de camadas;
- formatos de exportação;
- páginas de ajuda, glossário e conteúdo;
- regras simples declarativas;
- alertas e notificações predefinidos.

### 11.3 Customização assistida ou profissional

Deverá exigir análise e orçamento específico:

- nova integração externa;
- regra de negócio complexa;
- novo algoritmo;
- novo tipo de visualização;
- migração de base legada;
- modelagem geoespacial especializada;
- autenticação corporativa específica;
- infraestrutura dedicada com requisitos especiais;
- alteração estrutural fora das capacidades do modelo.

### 11.4 Customizações que não devem ser permitidas livremente

- remoção de controles de segurança;
- alteração manual de segredos;
- execução arbitrária de código;
- combinações incompatíveis de módulos;
- mudança de contratos de API protegidos;
- modificação de componentes centrais que impeça atualizações futuras;
- uso de dados ou integrações sem licença válida.

## 12. Manifesto da aplicação gerada

Cada aplicação deverá ser representada por um manifesto versionado. Esse manifesto será a fonte de verdade entre o configurador comercial e o mecanismo de geração.

### 12.1 Conteúdo mínimo do manifesto

- identificador do cliente e da organização;
- família e versão do modelo;
- pacote comercial;
- módulos ativados;
- identidade visual;
- domínio e região de implantação;
- perfis e permissões;
- esquema de dados selecionado;
- formulários e campos;
- mapas, camadas e territórios;
- indicadores e relatórios;
- integrações;
- parâmetros de trial e cobrança;
- requisitos de infraestrutura;
- política de atualização;
- recursos profissionais adicionais.

### 12.2 Princípio de geração

O gerador não deve copiar indiscriminadamente um repositório antigo. Ele deverá combinar uma base de aplicação versionada com capacidades reutilizáveis e configuração declarativa. Customizações específicas deverão ficar separadas do núcleo atualizável.

## 13. Ciclo de vida da aplicação do cliente

### 13.1 Configuração

O cliente seleciona o modelo, o pacote, os módulos, a identidade e as configurações permitidas. O sistema valida dependências e incompatibilidades.

### 13.2 Trial

Após o início ou aquisição do período de teste, a plataforma gera uma instância com:

- prazo definido;
- limites de recursos;
- marcação de ambiente de avaliação quando aplicável;
- dados de demonstração ou dados fornecidos de forma autorizada;
- administrador inicial;
- telemetria e critérios de conversão.

### 13.3 Provisionamento

O mecanismo cria ou configura:

- projeto ou ambiente independente;
- aplicação e serviços necessários;
- banco de dados;
- armazenamento;
- domínio e certificados;
- segredos;
- monitoramento;
- backups;
- usuário administrador;
- registro da versão implantada.

### 13.4 Homologação e contratação

O cliente valida a instância. Na conversão do trial, os dados e customizações autorizadas são preservados, e os limites passam a seguir o plano contratado.

### 13.5 Atualização

Atualizações do núcleo e dos módulos devem ser aplicadas por versão, com migrações testadas, possibilidade de rollback e preservação do manifesto do cliente.

### 13.6 Suspensão e encerramento

O ciclo deverá prever inadimplência, expiração do trial, exportação de dados, retenção temporária, reativação e exclusão controlada conforme contrato e legislação.

## 14. Estrutura inicial dos pacotes comerciais

Cada família poderá utilizar uma estrutura de pacotes comum, ajustada à complexidade do produto.

### Starter

- modelo visual padrão;
- conjunto essencial de módulos;
- limites de usuários, dados ou recursos;
- subdomínio VPC-GEOSER;
- suporte básico;
- integrações predefinidas.

### Professional

- maior número de usuários e recursos;
- identidade visual ampliada;
- domínio próprio;
- módulos adicionais;
- exportações e APIs;
- suporte e backups superiores;
- customizações declarativas avançadas.

### Enterprise

- ambiente dedicado;
- autenticação corporativa;
- integrações específicas;
- requisitos de segurança e disponibilidade;
- observabilidade e SLA contratual;
- implantação regional ou infraestrutura escolhida;
- serviços profissionais e governança de versão.

Os nomes, preços e limites definitivos ainda deverão ser calculados a partir de custo de provisionamento, suporte, atualização e consumo de serviços externos.

## 15. Priorização técnica anterior à análise de mercado

Esta priorização registrou a prontidão percebida antes da pesquisa externa. Ela foi substituída pela ordem de execução da seção 20.10 e não deve ser utilizada como catálogo comercial vigente.

### Primeira onda

1. **VPC Forest Dynamics:** prioridade estratégica e institucional pela origem doutoral, diferenciação científica e potencial de propriedade intelectual; entrada comercial inicial por piloto assistido.
2. **VPC GeoPortal:** maior capacidade de combinar componentes existentes e atender vários setores.
3. **VPC Data Intelligence:** FAD-Stats fornece uma base funcional relativamente madura e generalizável.
4. **VPC Decision Studio:** forte reaproveitamento do Sistema de Apoio à Decisão, AHP e aderência.
5. **VPC Survey & Forms:** fluxo comercial claro e possibilidade de pacotes verticais.

### Segunda onda

6. **VPC Occurrence & Citizen Portal:** exige amadurecimento de moderação, privacidade e backoffice.
7. **VPC Route Intelligence:** depende da consolidação do motor, das camadas e das integrações de geocodificação.
8. **VPC Road Safety Analytics:** depende da unificação dos dois projetos de acidentes em um pacote de domínio.
9. **VPC Climate & Infrastructure Risk:** alto valor, porém maior responsabilidade operacional, metodológica e contratual.

### Laboratório

- VPC Resource Operations;
- novos modelos derivados de projetos futuros;
- capacidades experimentais que ainda não possam receber compromisso comercial.

## 16. O que precisa ser construído para a fábrica funcionar

1. **Catálogo de capacidades:** inventário versionado de cada módulo, dependências e compatibilidades.
2. **Design system parametrizável:** componentes visuais capazes de receber temas sem bifurcar o código.
3. **Esquemas de configuração:** contratos para identidade, menus, formulários, mapas, indicadores e permissões.
4. **Bases de aplicação:** estruturas canônicas por família ou por combinação tecnológica.
5. **Gerador:** composição de código, configuração, banco e infraestrutura a partir do manifesto.
6. **Provisionador:** criação segura dos ambientes independentes.
7. **Plano de controle:** clientes, catálogo, trial, cobrança, versões e suporte.
8. **Registro de instâncias:** relação entre cliente, manifesto, ambiente, versão e estado operacional.
9. **Sistema de atualização:** aplicação de novas versões sem sobrescrever customizações.
10. **Governança e segurança:** segredos, isolamento, backups, auditoria, LGPD e encerramento.

## 17. Decisões já estabelecidas por esta correção

- O principal produto é a capacidade de gerar aplicações independentes.
- O site comercial também será configurador e entrada do provisionamento.
- Cada cliente terá sua própria aplicação em outro ambiente.
- As customizações serão registradas em configuração versionada.
- As aplicações atuais serão decompostas em capacidades reutilizáveis.
- O catálogo será organizado por famílias de solução, não pelos 14 cards do Hub.
- O catálogo completo será organizado nas linhas VPC Business e VPC Specialized.
- Os pacotes Business serão composições de módulos comuns, não aplicações mantidas em bases de código separadas.
- Ativos estratégicos externos ao Hub também integrarão o inventário quando sustentados por evidência real.
- O MDF será uma família própria de destaque, com comunicação explícita de sua origem na tese de doutorado e comercialização inicial assistida.
- AHP, aderência, relatórios e análises temáticas poderão compor produtos maiores.
- Conteúdos e metodologias continuam tendo valor mesmo quando não constituem software autônomo.

## 18. Questões ainda abertas

- O baseline gratuito de 14 dias sem cartão será confirmado, ajustado ou segmentado após os pilotos?
- Quais famílias aceitarão criação automática imediata e quais exigirão aprovação técnica?
- Quais provedores e regiões poderão receber as aplicações geradas?
- Haverá opção de ambiente pertencente ao cliente?
- Quais módulos poderão ser combinados entre famílias?
- Qual será o limite de customização em autosserviço por pacote?
- Como serão precificados consumo, armazenamento, mapas e integrações externas?
- Quais dados de demonstração poderão ser usados no trial?
- Como será realizada a conversão do trial sem perda de dados?
- Qual será a política de atualização para clientes que recusarem uma nova versão?
- Quais recursos exigirão responsabilidade técnica ou cláusulas específicas?

## 19. Conclusão da etapa diagnóstica anterior à análise de mercado

O portfólio atual deve ser entendido como o acervo inicial de uma fábrica de aplicações digitais. O valor da VPC-GEOSER não está somente nas aplicações já publicadas, mas na capacidade de decompor esse acervo em modelos, motores, módulos, componentes e metodologias reutilizáveis.

O catálogo comercial não deverá reproduzir o PLI Hub. Ele deverá apresentar famílias de solução orientadas ao problema do cliente, permitir escolhas controladas de aparência e funcionalidade e gerar uma aplicação independente, provisionada em ambiente próprio. O inventário passa a incluir também ativos estratégicos externos ao Hub, desde que efetivamente analisados.

A etapa diagnóstica produziu nove hipóteses de família e duas extensões futuras para teste. A análise de mercado da seção 20 concluiu que somente quatro devem permanecer como produtos expostos; as demais devem ser fundidas, convertidas em módulos, tratadas como edições verticais ou mantidas em incubação.

## 20. Análise de mercado e decisão do catálogo

### 20.1 Executive Summary

- **A linha especializada não deve lançar nove produtos.** A amplitude fragmentaria desenvolvimento, suporte, comunicação e vendas, além de colocar a VPC-GEOSER em competição direta com plataformas globais em categorias genéricas.
- **Quatro produtos especializados fazem sentido comercial:** VPC Forest Dynamics, VPC Territorial Intelligence, VPC Climate & Infrastructure Resilience e VPC Territorial Operations. Eles combinam geografia, conhecimento de domínio, customização e implantação independente — áreas nas quais a VPC pode sustentar diferenciação.
- **Cinco hipóteses deixam de ser produtos isolados.** Route Intelligence, Data Intelligence, Decision Studio e Survey & Forms tornam-se módulos; Road Safety Analytics torna-se edição vertical do Territorial Intelligence. Knowledge Portal permanece módulo e Resource Operations permanece incubado.
- **A entrada no mercado deve ser híbrida.** Territorial Intelligence e Territorial Operations podem caminhar para trials configuráveis; Forest Dynamics e Climate & Infrastructure Resilience devem começar como pilotos assistidos, devido a dados, calibração, responsabilidade metodológica e risco operacional.

### 20.2 Escopo e método

A análise considera o Brasil como mercado primário, com expansão latino-americana posterior. A decisão foi tomada por comparação entre:

1. intensidade e recorrência do problema;
2. existência de compradores e sinais de contratação;
3. concorrência e substitutos;
4. diferenciação alcançável pela VPC-GEOSER;
5. repetibilidade no modelo de geração de aplicações;
6. maturidade dos ativos atuais;
7. esforço de implantação, suporte e responsabilidade;
8. aderência à propriedade intelectual e às competências da empresa.

A análise de mercado é atualizada até **19 de julho de 2026**. Números de organizações e contratos são usados como sinais de mercado, não como previsão automática de receita.

### 20.3 Evidências de demanda

#### Transformação digital e contratação pública

A Lei nº 14.129/2021 estabelece modernização, serviços digitais, interoperabilidade, participação social e dados abertos como diretrizes da administração pública. Isso sustenta demanda estrutural por portais, fluxos digitais, dados e sistemas próprios, mas não garante orçamento para cada município. Fonte: [Lei do Governo Digital](https://www.gov.br/governodigital/pt-br/legislacao/lei-do-governo-digital).

O Portal Nacional de Contratações Públicas concentra contratações da União, estados e municípios e permite observar compras reais de software, implantação, hospedagem, suporte e treinamento. Exemplos encontrados confirmam contratação de licença de geoprocessamento, sistema de ocorrências e soluções de BI, mas os valores variam fortemente conforme escopo e não devem ser tratados como tabela de preços. Fontes: [PNCP](https://www.gov.br/pncp/), [licença anual de geoprocessamento da Sudene](https://pncp.gov.br/app/contratos/09263130000191/2024/7) e [consulta de contratos de software](https://pncp.gov.br/app/contratos?q=software).

**Implicação:** vender para o setor público é viável, porém exige produto acompanhado de implantação, suporte, treinamento, segurança, LGPD e documentação para contratação. Um checkout simples não substitui o processo comercial e administrativo.

#### Risco climático e infraestrutura

O Cemaden ampliou o monitoramento para 1.133 municípios prioritários e envia alertas às defesas civis. O AdaptaBrasil disponibiliza indicadores para os 5.570 municípios e o AdaptaCidades apoia diretamente 581 municípios. O AdaptaVias analisou mais de 100 mil quilômetros de rodovias e ferrovias quanto a riscos climáticos. Fontes: [municípios monitorados pelo Cemaden](https://www.gov.br/cemaden/pt-br/assuntos/noticias-cemaden/cemaden-amplia-a-lista-de-municipios-monitorados-de-1038-para-1133), [Painel Cidades do AdaptaBrasil](https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/adaptabrasil-lanca-painel-cidades-para-facilitar-a-consulta-sobre-risco-climatico), [AdaptaCidades](https://adaptabrasil.mcti.gov.br/noticia/adaptabrasil-apoia-definicao-dos-260-municipios-da-primeira-etapa-do-adaptacidades) e [riscos sobre infraestrutura rodoviária](https://adaptabrasil.mcti.gov.br/detalhes-rodovias).

**Implicação:** existe dor, prioridade pública e universo comprador. Entretanto, a VPC não deve competir com Cemaden ou AdaptaBrasil como fonte nacional de alertas ou índices. A oportunidade é transformar fontes oficiais e dados locais em inventário de ativos, protocolos, acompanhamento operacional, priorização e aplicação independente do cliente.

#### Segurança viária

O Pnatrans determina reduzir pela metade, até 2030, o índice de mortes por habitante em relação a 2020 e contém 70 ações. Em 2025, a PRF registrou aproximadamente 72,5 mil sinistros, 6 mil mortes e 83,5 mil feridos somente em rodovias federais. O DNIT desenvolveu seu próprio Sistema de Gestão de Segurança Viária, com mapas, acidentes, classificação, investimentos e custo-benefício. Fontes: [Pnatrans](https://www.gov.br/transportes/pt-br/assuntos/transito/pnatrans/pnatrans), [Anuário PRF 2025](https://www.gov.br/prf/pt-br/noticias/nacionais/2026/maio/prf-divulga-anuario-estatistico-de-2025-com-aumento-de-infracoes-e-reducao-de-mortes-nas-rodovias-federais) e [Relatório de Gestão DNIT 2025](https://www.gov.br/dnit/pt-br/acesso-a-informacao/auditoria/relatorio-de-gestao/RelatriodeGesto2025.pdf).

**Implicação:** o problema e os dados justificam uma oferta vertical, mas órgãos federais e grandes operadores já desenvolvem painéis próprios. A entrada mais defensável é atender estados, municípios, concessionárias e consultorias que precisam integrar bases, territorializar análises e publicar observatórios próprios.

#### Manejo e dinâmica florestal

Em dezembro de 2025, o Serviço Florestal Brasileiro registrava 24 contratos de concessão em andamento e aproximadamente 1,33 milhão de hectares concedidos. A política envolve produção, arrecadação, emprego, monitoramento e planejamento. Ao mesmo tempo, existem modelos científicos internacionais consolidados, como LANDIS-II, capazes de simular sucessão, manejo e distúrbios em grandes paisagens. Fontes: [Boletim do SNIF sobre concessões](https://www.gov.br/florestal/pt-br/assuntos/noticias/2025/dezembro/boletins-do-snif-reunem-indicadores-de-concessoes-florestais-acesso-ao-credito-e-participacao-feminina-no-setor), [concessões em andamento](https://www.gov.br/florestal/pt-br/assuntos/concessoes-e-monitoramento/concessoes-florestais-em-andamento) e [LANDIS-II](https://www.landis-ii.org/).

**Implicação:** Forest Dynamics atende um nicho menor que o mercado municipal genérico, porém possui maior diferenciação e autoridade científica. O produto não deve prometer ser o único simulador florestal; deve se diferenciar pela formulação da tese, contexto brasileiro de exploração seletiva, interface web, implantação dedicada, rastreabilidade e serviço de calibração.

### 20.4 Pressão competitiva e substitutos

| Categoria genérica | Concorrência ou substituto | Consequência para a VPC-GEOSER |
|---|---|---|
| Geoportal | ArcGIS Online/Enterprise e GeoNode aberto | não vender “mapa com camadas”; vender aplicação territorial orientada ao domínio, implantada e customizada |
| BI | Power BI, Microsoft Fabric, Qlik e ferramentas abertas | não manter Data Intelligence genérico; integrar analytics a produtos territoriais e metodologias próprias |
| Formulários | Google Forms, Microsoft Forms, Power Apps e ArcGIS Survey123 | não vender construtor genérico; usar formulários como entrada de fluxos, fiscalização, pesquisa e ocorrência |
| Roteamento | Google Routes, Mapbox e motores abertos | não competir por rota comum; usar roteamento condicionado a risco, restrição e ativos do cliente |
| Apoio à decisão | planilhas, BI, ferramentas AHP e consultorias | não lançar calculadoras isoladas; incorporar priorização, AHP e aderência nos produtos que geram decisões reais |
| Simulação florestal | LANDIS-II e modelos acadêmicos | competir por aderência ao problema brasileiro, usabilidade web, implantação, calibração e explicabilidade |

O ArcGIS oferece SaaS e implantação própria, enquanto o GeoNode já entrega gratuitamente gestão, publicação, permissões e compartilhamento geoespacial. O Power BI oferece conta gratuita e plano Pro por usuário. Google Workspace já inclui Forms, e Survey123 combina formulários inteligentes, mapa e trabalho offline. Google Routes cobra por requisição ou elemento processado. Fontes: [ArcGIS Online](https://www.esri.com/pt-br/arcgis/products/arcgis-online/buy), [GeoNode](https://geonode.org/), [Power BI](https://www.microsoft.com/pt-br/power-platform/products/power-bi/pricing), [Google Workspace](https://workspace.google.com/intl/pt-BR/), [ArcGIS Survey123](https://www.esri.com/en-us/arcgis/products/arcgis-survey123/overview) e [Google Routes](https://developers.google.com/maps/documentation/routes/usage-and-billing).

**Conclusão competitiva:** componentes horizontais são necessários para construir produtos, mas são fracos como categorias comerciais da VPC. A empresa deve cobrar pela solução de domínio, configuração, dados, implantação e continuidade — não pela existência isolada de mapa, gráfico, formulário ou algoritmo conhecido.

### 20.5 Avaliação comparativa das nove hipóteses

Escala de 1 a 5. A pontuação pondera dor do comprador (20%), evidência de compra (15%), diferenciação (20%), repetibilidade (15%), aderência estratégica (15%) e prontidão atual (15%). A pontuação apoia a decisão, mas não substitui os bloqueios qualitativos de competição, responsabilidade e posicionamento.

| Hipótese anterior | Dor | Compra | Diferenciação | Repetição | Aderência | Prontidão | Nota | Decisão |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| VPC Forest Dynamics | 5 | 3 | 5 | 2 | 5 | 2 | 3,8 | **manter como produto de destaque e piloto assistido** |
| VPC GeoPortal | 4 | 4 | 3 | 4 | 5 | 4 | 4,0 | **fundir com Data Intelligence em Territorial Intelligence** |
| VPC Route Intelligence | 3 | 3 | 1 | 4 | 3 | 3 | 2,8 | **retirar como produto e manter módulo de rota condicionada** |
| VPC Occurrence & Citizen Portal | 4 | 4 | 3 | 4 | 4 | 4 | 3,8 | **fundir com formulários em Territorial Operations** |
| VPC Climate & Infrastructure Risk | 5 | 4 | 4 | 3 | 5 | 3 | 4,1 | **manter, reposicionar e vender de forma assistida** |
| VPC Data Intelligence | 5 | 4 | 1 | 5 | 4 | 4 | 3,8 | **retirar como produto genérico e fundir com GeoPortal** |
| VPC Decision Studio | 3 | 2 | 2 | 3 | 4 | 3 | 2,8 | **retirar como produto e transformar em módulo transversal** |
| VPC Survey & Forms | 4 | 3 | 1 | 5 | 3 | 4 | 3,3 | **retirar como produto e incorporar a Operations** |
| VPC Road Safety Analytics | 5 | 4 | 4 | 3 | 5 | 3 | 4,1 | **manter como edição vertical de Territorial Intelligence** |

As notas de 1 a 5 são julgamentos comparativos baseados nas evidências disponíveis, não medições estatísticas de mercado. “Compra” representa evidência de orçamento ou contratação para a categoria; “repetição” representa a possibilidade de gerar novas instâncias sem reconstrução integral.

### 20.6 Catálogo comercial especializado recomendado

#### Produto 1 — VPC Forest Dynamics

**Posição:** flagship científico da empresa.

**Compra:** projeto ou assinatura assistida por região, inventário ou programa de pesquisa.

**Entrega:** aplicação independente, modelo versionado, dados validados, cenários, mapas, comparação e relatórios.

**Entrada no mercado:** universidades, institutos, órgãos florestais, concessionárias, consultorias e projetos financiados. Não oferecer trial irrestrito com dados reais; usar demonstração guiada e piloto contratado.

#### Produto 2 — VPC Territorial Intelligence

**Origem:** fusão de GeoPortal e Data Intelligence.

**Compra:** observatório ou plataforma territorial independente, configurada para dados, indicadores, mapas, relatórios e identidade do cliente.

**Edições iniciais:** Observatório Municipal ou Regional, Infraestrutura e Investimentos e **Road Safety**.

**Motivo:** mapa e BI separados são facilmente substituíveis; juntos, aplicados a um domínio e acompanhados de ingestão, governança e publicação, formam uma solução defensável.

#### Produto 3 — VPC Climate & Infrastructure Resilience

**Ajuste de posição:** substituir a promessa ampla de “monitoramento climático” por gestão territorial de exposição, vulnerabilidade, ativos, ocorrências, protocolos e medidas de adaptação.

**Compra:** implantação independente para município, concessionária, operador ou proprietário de infraestrutura.

**Módulos opcionais:** rota condicionada a risco, ocorrências de campo, alertas baseados em fontes contratadas, planos de ação e priorização multicritério.

**Limite:** não substituir alertas oficiais nem vender índices de terceiros como metodologia própria.

#### Produto 4 — VPC Territorial Operations

**Origem:** fusão de Occurrence & Citizen Portal com Survey & Forms.

**Compra:** aplicação própria para coleta territorial, fiscalização, inspeção, manifestação, ocorrência, triagem e acompanhamento.

**Edições iniciais:** Ocorrências Urbanas, Inspeção de Campo e Pesquisa Territorial. O pacote de embarcadores pode existir como configuração vertical, não como produto independente.

**Diferenciação:** formulário + geolocalização + anexos + workflow + mapa + backoffice + API + identidade do cliente.

### 20.7 Produtos retirados, ajustados e preservados

| Elemento anterior | Nova posição | O que acontece com o ativo |
|---|---|---|
| GeoPortal | parte central do Territorial Intelligence | preservado e fortalecido |
| Data Intelligence | analytics do Territorial Intelligence e dos demais produtos | preservado como capacidade transversal |
| Road Safety Analytics | edição vertical do Territorial Intelligence | preservado como pacote de domínio |
| Occurrence Portal | núcleo do Territorial Operations | preservado e combinado com workflow |
| Survey & Forms | módulo de entrada e coleta do Territorial Operations | preservado; deixa de disputar com formulários genéricos |
| Route Intelligence | módulo de rota condicionada em Resilience e Operations | preservado; rota genérica sai do catálogo |
| Decision Studio | módulo de priorização, AHP, aderência e parecer | preservado como capacidade transversal e serviço consultivo |
| Knowledge Portal | módulo documental e de publicação | preservado como complemento |
| Resource Operations | incubação | fora do catálogo até existir fluxo funcional e comprador validado |

Nenhum código precisa ser descartado por essa decisão. O corte é comercial: reduz nomes e promessas externas, enquanto mantém motores e componentes no catálogo técnico interno.

### 20.8 Dimensionamento prudente da oportunidade

Não existe base suficiente para publicar um TAM financeiro confiável. Ainda faltam preços definidos, custo de implantação por família, duração do ciclo de vendas, taxa de conversão, capacidade da equipe e quantidade de compradores qualificados. Multiplicar 5.570 municípios por um preço arbitrário produziria falsa precisão.

Os universos verificáveis para prospecção são:

| Mercado | Universo factual útil | Interpretação correta |
|---|---:|---|
| Administração municipal | 5.570 municípios | TAM institucional máximo para soluções territoriais; não representa compradores prontos |
| Risco e adaptação | 1.133 municípios monitorados pelo Cemaden; 581 apoiados pelo AdaptaCidades | lista prioritária para Resilience, com sobreposição entre programas |
| Segurança viária | União, 27 unidades federativas, municípios integrados ao trânsito, concessionárias e consultorias | mercado relevante, mas sem contagem consolidada de compradores qualificados nesta análise |
| Concessões florestais federais | 24 contratos em andamento e cerca de 1,33 milhão de hectares em 2025 | núcleo inicial verificável para Forest Dynamics; não inclui todo o manejo privado, estadual ou acadêmico |

**Modelo recomendado de sizing:** primeiro construir uma lista nominal de 50 a 100 contas prioritárias por produto, entrevistar compradores e testar faixas de preço. Somente depois calcular SAM e SOM financeiros. Até lá, os números acima servem para ordenar prospecção, não para prometer receita.

### 20.9 Arquitetura comercial decorrente da análise

#### Trials configuráveis

- Territorial Intelligence;
- Territorial Operations.

Esses trials podem usar dados demonstrativos e limites de usuários, camadas, formulários, armazenamento e integrações.

#### Demonstração e piloto assistido

- Forest Dynamics;
- Climate & Infrastructure Resilience;
- edição Road Safety quando depender de tratamento de bases reais.

Essas ofertas exigem diagnóstico dos dados, definição metodológica e validação antes da implantação definitiva.

#### Receita

A receita deverá combinar:

1. implantação e configuração inicial;
2. assinatura recorrente por aplicação independente;
3. consumo de infraestrutura e APIs externas;
4. suporte e SLA;
5. preparação, integração e qualidade de dados;
6. calibração, estudos e serviços especializados;
7. módulos e edições verticais.

Cobrança somente por usuário não representa adequadamente o custo das aplicações independentes. A unidade comercial principal deve ser **instância + pacote + capacidade + consumo + serviço**.

### 20.10 Prioridade de execução

Esta prioridade organiza somente a linha VPC Specialized. A ordem global entre Business, fábrica e Specialized é definida na seção 21.14.

1. **Construir a base comum de Territorial Intelligence**, porque mapas, dados, autenticação, relatórios e provisionamento serão usados por quase todo o catálogo.
2. **Concluir um piloto demonstrável de Forest Dynamics**, preservando fidelidade científica e criando a principal narrativa de diferenciação da empresa.
3. **Transformar Reporta e Formulário Embarcadores em Territorial Operations**, com schema configurável e workflow único.
4. **Reposicionar HazardTrack como Resilience**, integrando ativos, riscos, fontes, protocolos e planos de ação.
5. **Criar Road Safety como primeira edição vertical de Territorial Intelligence**, consolidando Infosiga, DER e FAD-Stats.
6. **Extrair AHP, aderência, roteamento e documentos como módulos**, sem abrir frentes comerciais independentes.

### 20.11 Validação e grau de confiança

**Avaliação geral: utilizável para decisão de portfólio, com ressalvas para projeções financeiras.**

As decisões de fusão e corte são sustentadas por concorrência observável, sinais reais de contratação, políticas públicas e aderência aos ativos analisados. A confiança é alta quanto à necessidade de reduzir o catálogo e média quanto à ordem exata de entrada no mercado, pois ainda não foram realizadas entrevistas de compradores, testes de mensagem, propostas comerciais ou vendas-piloto.

Antes de fixar preços ou metas de receita, deverão ser validados:

- orçamento e autoridade de compra por persona;
- exigências mínimas de contratação pública e privada;
- disposição de pagar pela aplicação independente;
- custo real de provisionamento e suporte;
- tempo de preparação dos dados;
- conversão de demonstração, trial e piloto;
- objeções frente a ArcGIS, Power BI, ferramentas abertas e desenvolvimento sob medida.

## 21. Arquitetura completa do catálogo: VPC Business e VPC Specialized

### 21.1 Decisão executiva

O catálogo comercial da VPC-GEOSER será organizado em duas linhas complementares:

1. **VPC Business:** aplicações empresariais essenciais, de menor complexidade, aquisição mais simples, configuração rápida e mercado amplo.
2. **VPC Specialized:** aplicações científicas, geoespaciais, territoriais e analíticas, com maior especialização, valor agregado e necessidade de implantação assistida.

As duas linhas utilizarão a mesma fábrica de aplicações. Cada aquisição produzirá uma aplicação independente, com identidade, domínio, banco, usuários, configurações, segredos, ambiente e ciclo de vida próprios.

Essa arquitetura evita dois extremos: limitar a empresa a projetos complexos de venda lenta ou transformá-la em fornecedora de sites genéricos sem diferenciação. A linha Business cria recorrência, escala e porta de entrada; a linha Specialized concentra autoridade técnica, margem e diferenciação.

### 21.2 Estrutura oficial do catálogo

| Linha | Oferta | Complexidade | Forma de entrada | Modelo de entrega |
|---|---|---:|---|---|
| VPC Business | sistemas empresariais essenciais | baixa a média | configuração e trial | provisionamento majoritariamente automatizado |
| VPC Specialized | quatro produtos especializados e suas edições | média a alta | demonstração, trial controlado ou piloto | provisionamento automatizado com etapas assistidas |

### 21.3 VPC Business não será apenas criação de sites

O produto-base será uma aplicação empresarial modular. O site público será uma das interfaces da aplicação, conectado ao cadastro, catálogo e operação interna do cliente.

Uma configuração poderá combinar:

- página inicial e páginas institucionais;
- catálogo público de produtos e serviços;
- formulários de contato e geração de oportunidades;
- área administrativa;
- clientes e contatos;
- produtos, serviços e portfólio;
- propostas, pedidos e vendas;
- execução de serviços;
- atendimento e pós-venda;
- relatórios gerenciais.

O cliente não comprará páginas isoladas. Ele comprará um sistema próprio cuja apresentação pública e operação interna compartilham a mesma fonte de dados.

### 21.4 Pacotes comerciais da linha VPC Business

Os nomes são de trabalho. Os pacotes representam combinações dos mesmos módulos e não deverão gerar bases de código diferentes.

#### VPC Business Start

**Finalidade:** presença digital e organização comercial inicial.

**Inclui:**

- página inicial;
- páginas sobre a empresa;
- contatos e localização;
- portfólio de produtos e serviços;
- formulário de contato;
- cadastro básico de clientes e oportunidades;
- painel administrativo;
- identidade visual e domínio próprios.

**Público inicial:** profissionais, microempresas, empresas recém-formadas e prestadores que ainda operam apenas por redes sociais, planilhas ou mensagens.

#### VPC Sales

**Finalidade:** organizar a jornada entre oportunidade, proposta, negociação e venda.

**Inclui:**

- clientes, contatos e histórico;
- produtos e serviços;
- oportunidades e etapas comerciais;
- propostas e orçamentos;
- pedidos ou contratos;
- acompanhamento de vendas;
- tarefas e agenda;
- documentos e relatórios comerciais;
- site e catálogo como módulos opcionais.

**Público inicial:** comércio consultivo, distribuidores, consultorias, escritórios e empresas de serviços com processo comercial recorrente.

#### VPC Service

**Finalidade:** organizar a contratação, execução e continuidade dos serviços.

**Inclui:**

- clientes e unidades atendidas;
- catálogo de serviços;
- solicitações e ordens de serviço;
- agenda, responsáveis e prazos;
- estados de execução;
- anexos, registros e evidências;
- aceite ou conclusão;
- atendimento e pós-venda;
- histórico do cliente;
- indicadores operacionais.

**Público inicial:** manutenção, assistência, consultorias, empresas técnicas, engenharia, instalações e prestadores com atendimento agendado ou execução controlada.

#### VPC Business Complete

**Finalidade:** reunir presença digital, relacionamento, vendas, execução e pós-venda em uma aplicação única.

**Inclui:** módulos Start, Sales e Service, administração ampliada, permissões, relatórios integrados e integrações contratadas.

**Público inicial:** pequenas e médias empresas que precisam substituir a combinação desarticulada de site, planilhas, mensagens e ferramentas isoladas.

### 21.5 Catálogo técnico de módulos VPC Business

| Domínio | Módulo | Função | Start | Sales | Service | Complete |
|---|---|---|:---:|:---:|:---:|:---:|
| Presença | Site institucional | páginas públicas, marca e contatos | obrigatório | opcional | opcional | obrigatório |
| Presença | Portfólio | exibição de produtos, serviços e casos | obrigatório | opcional | opcional | obrigatório |
| Relacionamento | Clientes e contatos | cadastro e histórico central | básico | obrigatório | obrigatório | obrigatório |
| Relacionamento | Leads e oportunidades | entrada e qualificação comercial | básico | obrigatório | opcional | obrigatório |
| Catálogo | Produtos | itens, categorias e informações comerciais | básico | obrigatório | opcional | obrigatório |
| Catálogo | Serviços | serviços, escopo e condições | básico | obrigatório | obrigatório | obrigatório |
| Comercial | Propostas e orçamentos | elaboração, envio, revisão e aceite | — | obrigatório | opcional | obrigatório |
| Comercial | Pedidos e vendas | registro e acompanhamento da venda | — | obrigatório | opcional | obrigatório |
| Operação | Agenda e tarefas | compromissos, prazos e responsáveis | opcional | obrigatório | obrigatório | obrigatório |
| Operação | Ordens de serviço | abertura, execução, evidências e conclusão | — | — | obrigatório | obrigatório |
| Relacionamento | Atendimento e pós-venda | solicitações, acompanhamento e histórico | básico | opcional | obrigatório | obrigatório |
| Gestão | Usuários e permissões | acesso por perfil e função | básico | obrigatório | obrigatório | obrigatório |
| Gestão | Documentos | arquivos, propostas, termos e anexos | opcional | obrigatório | obrigatório | obrigatório |
| Gestão | Relatórios | indicadores do pacote contratado | básico | comercial | operacional | integrado |
| Plataforma | Notificações | avisos por canais contratados | opcional | opcional | opcional | opcional |
| Plataforma | Integrações | pagamentos, mensagens, fiscal, agenda ou APIs | opcional | opcional | opcional | opcional |

O símbolo “—” significa fora do escopo padrão, não impossibilidade técnica. A inclusão dependerá de upgrade ou configuração contratada.

### 21.6 Edições por segmento são presets, não produtos novos

A fábrica poderá oferecer edições prontas que alteram terminologia, campos, etapas, permissões, relatórios e módulos padrão.

| Edição | Base recomendada | Ajustes principais |
|---|---|---|
| Comércio | Business Start ou Sales | produtos, pedidos, clientes e acompanhamento |
| Prestador de serviços | Service ou Complete | agenda, ordem de serviço, execução e pós-venda |
| Consultoria | Sales ou Complete | oportunidades, propostas, projetos, entregas e documentos |
| Escritório técnico | Complete | clientes, propostas, serviços, responsáveis e documentos técnicos |
| Engenharia e manutenção | Service ou Complete | ativos atendidos, ordens, equipes, evidências e aceite |
| Profissional autônomo | Business Start | presença, portfólio, contatos, agenda e propostas simples |
| Pesquisa e levantamento | Service com módulo de formulários | questionários, coleta, respostas e relatórios |

Clínicas e segmentos sujeitos a regras sensíveis somente deverão ser incluídos após análise específica de dados, responsabilidade profissional, integrações e legislação. Não entrarão automaticamente como simples preset.

### 21.7 Customização permitida ao cliente

#### Visual

- nome comercial da aplicação;
- logotipo, ícone e imagens;
- paleta de cores;
- tipografia entre opções homologadas;
- textos institucionais;
- domínio ou subdomínio;
- organização da página inicial;
- exibição do portfólio.

#### Funcional

- módulos contratados;
- nomes de menus e entidades;
- campos adicionais permitidos;
- categorias de produtos e serviços;
- etapas do funil comercial;
- estados das ordens de serviço;
- regras de obrigatoriedade;
- perfis e permissões;
- modelos de propostas e documentos;
- notificações;
- indicadores e relatórios disponíveis no pacote.

#### Assistida

- migração de dados;
- integrações externas;
- automações específicas;
- relatórios exclusivos;
- regras de negócio fora dos presets;
- identidade visual avançada;
- infraestrutura ou requisitos de segurança especiais.

A customização deverá ocorrer por manifesto e extensões controladas. O cliente não poderá editar livremente o código-fonte da base canônica pela interface comercial.

### 21.8 Jornada comercial da linha VPC Business

```text
Escolha do pacote ou segmento
              ↓
Seleção dos módulos e limites
              ↓
Customização visual e funcional permitida
              ↓
Validação automática do manifesto
              ↓
Criação da aplicação independente de trial
              ↓
Uso, alimentação e avaliação pelo cliente
              ↓
Contratação, upgrade ou encerramento
              ↓
Continuidade da mesma aplicação e dos dados
```

O trial não deve ser apenas uma demonstração compartilhada. Sempre que técnica e economicamente viável, será uma instância real do cliente, com limites e dados próprios. A contratação deverá converter essa mesma instância, evitando recadastro e perda de configuração.

### 21.9 Regras recomendadas para o trial

- período configurável definido comercialmente;
- aplicação identificada como trial;
- limites de usuários, armazenamento, registros e integrações;
- domínio provisório até a contratação;
- dados demonstrativos opcionais;
- possibilidade de inserir dados reais mediante aceite dos termos;
- avisos de expiração;
- exportação ou política clara de retenção;
- conversão sem reconstrução;
- suspensão automática após o prazo;
- exclusão somente conforme política comunicada e janela de recuperação.

O baseline V1 foi definido em 14 dias, gratuito e sem cartão. Ele deverá ser testado por segmento antes da abertura pública e poderá evoluir por política versionada.

### 21.10 Modelo de cobrança da linha VPC Business

A estrutura deverá separar:

1. **implantação:** configuração, identidade, domínio, preparação e eventual migração;
2. **assinatura da instância:** direito de uso, hospedagem, manutenção e atualizações;
3. **pacote funcional:** Start, Sales, Service ou Complete;
4. **limites:** usuários, armazenamento, volume de registros e consumo;
5. **módulos adicionais:** funcionalidades fora do pacote;
6. **integrações e consumo externo:** mensagens, mapas, pagamentos ou APIs;
7. **serviços profissionais:** migração, treinamento, automação e customização assistida;
8. **suporte e SLA:** níveis de atendimento contratados.

O preço final não deverá ser definido antes de medir custo de provisionamento, suporte, armazenamento, integrações e aquisição de clientes.

### 21.11 Progressão comercial do cliente

A linha Business deverá permitir evolução sem troca abrupta de sistema:

```text
Business Start
      ↓
Sales ou Service
      ↓
Business Complete
      ↓
Edição setorial ou módulo geoespacial
      ↓
Solução VPC Specialized quando houver necessidade real
```

Exemplos:

- uma empresa de manutenção começa com Service e adiciona mapa de ativos;
- uma consultoria começa com Sales e adiciona formulários de pesquisa;
- uma empresa de engenharia evolui para Territorial Intelligence;
- uma operadora de infraestrutura evolui para Climate & Infrastructure Resilience.

Essa progressão aumenta retenção e permite que capacidades avançadas sejam vendidas à base existente.

### 21.12 Catálogo oficial completo após a correção

#### Linha VPC Business

- VPC Business Start;
- VPC Sales;
- VPC Service;
- VPC Business Complete;
- edições setoriais construídas como presets.

#### Linha VPC Specialized

- VPC Forest Dynamics;
- VPC Territorial Intelligence;
- VPC Climate & Infrastructure Resilience;
- VPC Territorial Operations;
- Road Safety como edição vertical;
- demais capacidades especializadas como módulos.

### 21.13 Arquitetura comum da fábrica

As duas linhas deverão compartilhar:

- conta e identidade do cliente no plano de controle;
- catálogo comercial;
- configurador;
- manifesto versionado;
- design system parametrizável;
- autenticação e permissões;
- serviço de geração;
- provisionamento de ambiente e banco independentes;
- domínio e certificados;
- segredos e configurações;
- registro de instâncias;
- cobrança e assinaturas;
- telemetria e observabilidade;
- backups e restauração;
- atualização sem perda das customizações;
- suporte, suspensão e encerramento.

Os módulos Business e Specialized poderão compartilhar componentes técnicos, mas não deverão criar dependência operacional entre aplicações de clientes diferentes.

### 21.14 Ordem de planejamento e construção

1. especificar o manifesto canônico de uma aplicação VPC Business;
2. definir entidades e contratos dos módulos comuns;
3. estabelecer design system e customizações seguras;
4. construir Business Start como primeira composição mínima;
5. acrescentar clientes, produtos, serviços e oportunidades;
6. evoluir para Sales e Service;
7. validar a conversão de trial para assinatura;
8. consolidar Business Complete;
9. reutilizar plano de controle e provisionamento na linha Specialized;
10. desenvolver as soluções especializadas conforme a prioridade da seção 20.10.

Essa ordem é uma decisão de arquitetura de produto, não autorização para iniciar desenvolvimento nesta etapa.

### 21.14.1 Especificações oficiais produzidas

- [Especificação Oficial do VPC Business Start](ESPECIFICACAO_OFICIAL_VPC_BUSINESS_START.md);
- [Especificação Oficial do Manifesto Canônico VPC](ESPECIFICACAO_OFICIAL_MANIFESTO_CANONICO_VPC.md);
- [Matriz Comercial Oficial VPC Business](MATRIZ_COMERCIAL_OFICIAL_VPC_BUSINESS.md);
- [Especificação Oficial do Trial VPC Business](ESPECIFICACAO_OFICIAL_TRIAL_VPC_BUSINESS.md);
- [Especificação Oficial do Configurador Comercial VPC](ESPECIFICACAO_OFICIAL_CONFIGURADOR_COMERCIAL_VPC.md);
- [Modelo Funcional Comum Oficial VPC](MODELO_FUNCIONAL_COMUM_OFICIAL_VPC.md);
- [Diretriz Oficial de Stack Open Source VPC](DIRETRIZ_OFICIAL_STACK_OPEN_SOURCE_VPC.md).
- [Arquitetura Técnica Open Source Oficial VPC](ARQUITETURA_TECNICA_OPEN_SOURCE_OFICIAL_VPC.md).

Esses documentos passam a controlar o escopo da primeira composição, o contrato entre configurador, gerador e provisionamento, os pacotes, o trial, a jornada de aquisição e os conceitos funcionais compartilhados. Com esse conjunto, o planejamento funcional mínimo anterior à arquitetura técnica está concluído.

### 21.15 Critérios de sucesso antes do desenvolvimento em escala

- cada pacote possuir escopo obrigatório e opcional fechado;
- inexistência de bifurcações de código por cliente;
- customizações representáveis no manifesto;
- trial provisionável e conversível;
- custos de infraestrutura mensuráveis por instância;
- política de atualização definida;
- backup, exportação e encerramento testáveis;
- pelo menos um segmento e uma persona definidos por pacote;
- proposta de valor compreensível sem explicação técnica;
- processo comercial compatível com o custo e a complexidade da oferta.

### 21.16 Questões comerciais ainda abertas

- nomes comerciais definitivos;
- validação dos baselines de duração, recuperação e limites do trial;
- validação de custo dos limites propostos para cada pacote;
- integrações incluídas;
- faixas de implantação e mensalidade;
- canais de venda;
- segmentos prioritários para os primeiros presets;
- política de migração de dados;
- suporte padrão e premium;
- condições para customização assistida;
- critérios para evolução de um cliente Business para Specialized.

Essas questões não impedem a definição arquitetural, mas precisam ser resolvidas antes da publicação de preços e abertura das vendas.

## 22. Controle de alterações

| Data | Versão | Alteração |
|---|---:|---|
| 19/07/2026 | 1.0 | Criação da documentação oficial do diagnóstico consolidado do portfólio VPC-GEOSER. |
| 19/07/2026 | 2.0 | Correção do modelo comercial: reanálise dos ativos como matéria-prima de uma fábrica de aplicações independentes e inclusão da proposta inicial de catálogo configurável. |
| 19/07/2026 | 2.1 | Inclusão do Modelo Dinâmico Florestal, originado da tese de doutorado de Vinicius Capanema, como 15º ativo e família estratégica de destaque do catálogo. |
| 19/07/2026 | 3.0 | Análise de mercado, redução de nove hipóteses para quatro produtos, definição de edições verticais, módulos, cortes comerciais e estratégia de entrada. |
| 19/07/2026 | 4.0 | Inclusão da linha VPC Business, definição dos pacotes Start, Sales, Service e Complete, matriz de módulos, presets setoriais, customização, trial, cobrança, progressão comercial e arquitetura comum com a linha VPC Specialized. |
| 19/07/2026 | 4.1 | Criação e vinculação das especificações oficiais do VPC Business Start e do Manifesto Canônico VPC. |
| 19/07/2026 | 4.2 | Criação da matriz comercial dos pacotes VPC Business e da especificação oficial do trial de 14 dias, sem cartão, com instância independente e conversão preservada. |
| 19/07/2026 | 4.3 | Criação da especificação do Configurador Comercial e do Modelo Funcional Comum, encerrando os contratos funcionais mínimos anteriores à arquitetura técnica. |
| 19/07/2026 | 4.4 | Estabelecimento da obrigatoriedade de stack principal integralmente open source para o site, a fábrica e todas as aplicações geradas. |
| 21/07/2026 | 4.5 | Definição da arquitetura técnica open source de referência, incluindo planos de controle e dados, stack candidata, isolamento, segurança, portabilidade, operação e roadmap técnico. |
