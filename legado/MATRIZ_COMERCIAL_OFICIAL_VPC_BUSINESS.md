# Matriz Comercial Oficial — VPC Business

**Versão:** 1.0  
**Data:** 19 de julho de 2026  
**Estado:** baseline para validação comercial e cálculo de custos  
**Pacotes:** Business Start, Sales, Service e Complete  
**Documento superior:** `DOCUMENTACAO_OFICIAL_DIAGNOSTICO_PORTFOLIO_VPC_GEOSER.md`

## Executive Summary

- **A VPC Business será uma única família modular, não quatro bases de código.** Start, Sales, Service e Complete são pacotes comerciais formados por capacidades comuns e ativados por manifesto.
- **Start é a porta de entrada.** Sales amplia relacionamento e venda; Service amplia execução e pós-venda; Complete reúne a jornada empresarial.
- **Limites iniciais foram definidos para teste de custo e aderência.** Eles não constituem preços ou compromissos públicos até que pilotos confirmem infraestrutura, suporte e comportamento de uso.
- **A cobrança deverá combinar implantação, assinatura da instância, pacote, adicionais e consumo externo.** Preço somente por usuário não representa adequadamente uma aplicação independente.

## 1. Objetivo

Esta matriz define:

- composição funcional dos pacotes;
- capacidades obrigatórias, opcionais e adicionais;
- limites iniciais de validação;
- implantação e suporte;
- caminhos de upgrade;
- itens que não serão incluídos silenciosamente;
- estrutura que futuramente sustentará a formação de preços.

## 2. Princípios comerciais

1. cada cliente recebe uma aplicação independente;
2. pacotes ativam módulos da mesma plataforma;
3. edições setoriais são presets, não novos produtos técnicos;
4. customização dentro do catálogo não gera projeto de software sob medida;
5. customização fora do catálogo exige análise e proposta;
6. integrações com custo variável são cobradas separadamente ou por franquia;
7. limites são aplicados por instância;
8. upgrade preserva aplicação, usuários e dados compatíveis;
9. downgrade depende de compatibilidade com uso, dados e módulos ativos;
10. nenhum preço será publicado antes de validar o custo total de servir.

## 3. Posicionamento dos pacotes

| Pacote | Problema principal | Resultado | Cliente típico |
|---|---|---|---|
| Business Start | empresa sem presença integrada e organização básica | site, portfólio, contatos e clientes no mesmo sistema | autônomo, microempresa, prestador inicial |
| Sales | vendas controladas por mensagens e planilhas | oportunidades, propostas, pedidos e acompanhamento | consultoria, comércio consultivo, escritório |
| Service | execução e pós-venda sem rastreabilidade | solicitações, agenda, ordens, evidências e atendimento | manutenção, assistência, serviço técnico |
| Complete | ferramentas isoladas entre divulgação, venda e execução | jornada integrada da captação ao pós-venda | pequena ou média empresa em crescimento |

## 4. Matriz funcional

Legenda: **I** incluído; **B** incluído em modo básico; **O** opcional contratável; **—** fora do pacote padrão.

| Capacidade | Start | Sales | Service | Complete |
|---|:---:|:---:|:---:|:---:|
| Site institucional | I | O | O | I |
| Página inicial configurável | I | O | O | I |
| Páginas institucionais | I | O | O | I |
| Portfólio público | I | O | O | I |
| Produtos | B | I | O | I |
| Serviços | B | I | I | I |
| Projetos ou casos | O | O | O | I |
| Formulário público de contato | I | O | O | I |
| Clientes e contatos | B | I | I | I |
| Leads e oportunidades | B | I | O | I |
| Funil comercial | B | I | — | I |
| Propostas e orçamentos | — | I | O | I |
| Pedidos ou contratos simples | — | I | O | I |
| Agenda e tarefas | O | I | I | I |
| Solicitações de serviço | — | — | I | I |
| Ordens de serviço | — | — | I | I |
| Responsáveis e prazos | B | I | I | I |
| Evidências e anexos operacionais | O | O | I | I |
| Aceite ou conclusão | — | O | I | I |
| Atendimento e pós-venda | B | O | I | I |
| Documentos | O | I | I | I |
| Usuários e permissões | B | I | I | I |
| Relatórios | B | comercial | operacional | integrado |
| Notificações | O | O | O | O |
| Exportação | B | I | I | I |
| API | — | O | O | O |
| Integrações externas | O | O | O | O |
| Campos adicionais homologados | limitado | I | I | ampliado |
| Workflow customizável | básico | comercial | operacional | comercial e operacional |

## 5. Escopo detalhado por pacote

### 5.1 Business Start

#### Obrigatório

- identidade empresarial;
- site e páginas essenciais;
- portfólio;
- produtos e/ou serviços básicos;
- contato público;
- leads ou oportunidades básicas;
- clientes e contatos básicos;
- painel administrativo;
- usuários e permissões básicas;
- relatórios mínimos.

#### Adicionais adequados

- casos ou projetos;
- domínio próprio;
- migração inicial;
- notificações adicionais;
- agenda;
- analytics ampliado;
- campos extras homologados.

#### Não incluir silenciosamente

- proposta comercial;
- pedido;
- estoque;
- pagamento;
- emissão fiscal;
- ordem de serviço;
- integração não contratada.

### 5.2 VPC Sales

#### Obrigatório

- clientes e contatos;
- produtos e serviços;
- leads e oportunidades;
- funil comercial;
- propostas e orçamentos;
- pedidos ou contratos simples;
- agenda e tarefas;
- documentos;
- relatórios comerciais;
- usuários e permissões.

#### Adicionais adequados

- site e portfólio;
- assinatura eletrônica;
- integração de agenda;
- mensagens;
- pagamentos;
- automações comerciais;
- importação e enriquecimento autorizado de dados;
- API.

#### Não incluir silenciosamente

- contabilidade;
- faturamento fiscal;
- estoque avançado;
- comissionamento complexo;
- marketing automation completo;
- regras exclusivas não parametrizadas.

### 5.3 VPC Service

#### Obrigatório

- clientes, contatos e unidades atendidas;
- catálogo de serviços;
- solicitações;
- agenda;
- ordens de serviço;
- responsáveis e prazos;
- estados de execução;
- anexos e evidências;
- conclusão ou aceite;
- atendimento e pós-venda;
- relatórios operacionais.

#### Adicionais adequados

- site;
- contratos simples;
- propostas;
- mapa de ativos;
- formulários de campo;
- assinatura;
- notificações;
- API;
- integrações.

#### Não incluir silenciosamente

- gestão de frota completa;
- estoque técnico;
- roteirização avançada;
- manutenção preditiva;
- telemetria;
- faturamento fiscal.

### 5.4 VPC Business Complete

#### Obrigatório

- capacidades padrão de Start, Sales e Service;
- visão integrada do cliente;
- relatórios comerciais e operacionais;
- permissões ampliadas;
- documentos e históricos comuns;
- upgrade e governança de módulos.

#### Adicionais adequados

- edições setoriais;
- módulos geoespaciais;
- formulários avançados;
- APIs;
- integrações;
- relatórios exclusivos;
- automações homologadas;
- suporte prioritário.

#### Não incluir silenciosamente

Complete significa união dos módulos homologados, não desenvolvimento ilimitado. Funções financeiras, fiscais, contábeis, industriais ou reguladas continuam fora do padrão quando não estiverem explicitamente contratadas.

## 6. Baseline inicial de limites

Os números abaixo são hipóteses operacionais para pilotos e simulação de custos. Antes da publicação comercial, deverão ser confirmados por teste de carga, custo de infraestrutura, suporte e entrevistas.

| Limite por instância | Start | Sales | Service | Complete |
|---|---:|---:|---:|---:|
| Usuários internos ativos | 2 | 5 | 5 | 10 |
| Clientes e contatos | 500 | 5.000 | 5.000 | 10.000 |
| Produtos e serviços | 100 | 500 | 500 | 1.000 |
| Leads ou oportunidades abertas | 100 | 1.000 | 250 | 2.000 |
| Propostas por ano | — | 2.000 | 500 opcional | 5.000 |
| Ordens de serviço por ano | — | — | 2.000 | 5.000 |
| Armazenamento de arquivos | 1 GB | 5 GB | 5 GB | 10 GB |
| Domínios próprios | 1 opcional | 1 opcional | 1 opcional | 1 incluível na implantação |
| Ambientes produtivos | 1 | 1 | 1 | 1 |
| Campos adicionais por entidade elegível | 3 | 10 | 10 | 20 |
| Integrações simultâneas | 1 opcional | 3 opcionais | 3 opcionais | 5 opcionais |
| Backups | conforme política do plano | conforme política do plano | conforme política do plano | conforme política do plano |

### Regras de limite

- o cliente será avisado antes de atingir limites;
- nenhum excedente será cobrado sem regra contratual;
- aumento poderá ocorrer por adicional ou upgrade;
- redução não poderá deixar uso atual em estado inválido;
- limites técnicos de segurança poderão ser inferiores aos comerciais em situações de abuso;
- consumo de APIs externas terá medição separada.

## 7. Implantação

### Implantação padrão

- criação da conta cliente;
- configuração do manifesto;
- aplicação do preset visual;
- provisionamento da instância;
- domínio provisório ou configuração de domínio contratado;
- criação do administrador inicial;
- checklist de publicação;
- orientação de primeiro acesso;
- conversão de trial quando aplicável.

### Implantação assistida

- identidade fora dos presets;
- migração de dados;
- configuração de campos e workflows ampliados;
- integração;
- treinamento;
- revisão de conteúdo;
- domínio e DNS gerenciados;
- validação setorial.

### Projeto especial

Será exigido quando houver:

- desenvolvimento fora do catálogo;
- integração não homologada;
- requisitos regulatórios específicos;
- infraestrutura do cliente;
- alta disponibilidade especial;
- migração complexa;
- volume acima das faixas suportadas;
- responsabilidade técnica adicional.

## 8. Suporte

### Suporte padrão

- canal assíncrono oficial;
- documentação e base de conhecimento;
- tratamento de incidentes da plataforma;
- orientação sobre recursos contratados;
- atualizações compatíveis;
- comunicação de manutenção relevante.

### Suporte prioritário opcional

- prioridade de triagem;
- acompanhamento de implantação;
- reuniões periódicas quando contratadas;
- SLA específico;
- apoio a integrações e processos críticos dentro do escopo.

Tempos de resposta não serão prometidos até que capacidade operacional e classificação de severidade estejam aprovadas.

### Fora do suporte padrão

- operação diária do sistema pelo fornecedor;
- digitação ou gestão contínua de conteúdo;
- consultoria empresarial ilimitada;
- correção de dados inseridos incorretamente pelo cliente;
- suporte a terceiros sem integração contratada;
- customização não adquirida.

## 9. Estrutura de cobrança

### Componentes

1. **taxa de implantação:** preparação e ativação;
2. **assinatura da instância:** aplicação independente, hospedagem e manutenção;
3. **pacote funcional:** Start, Sales, Service ou Complete;
4. **faixa de capacidade:** limites contratados;
5. **adicionais:** módulos, domínio, armazenamento ou usuários;
6. **consumo externo:** mensagens, mapas, pagamentos e APIs;
7. **serviços profissionais:** migração, treinamento, integração e customização assistida;
8. **suporte:** padrão ou prioritário.

### Fórmula conceitual

```text
Receita inicial = implantação + serviços profissionais

Receita recorrente = instância + pacote + capacidade + adicionais + suporte

Consumo variável = serviços externos utilizados
```

### Itens pendentes para precificação

- custo mínimo de uma instância ativa;
- custo de backup e armazenamento;
- custo de domínio e certificados;
- custo de mensagens e e-mail;
- horas médias de implantação;
- volume de suporte por pacote;
- inadimplência e meios de pagamento;
- impostos;
- comissão comercial;
- margem mínima desejada;
- descontos anual, promocional ou por volume.

## 10. Upgrade, downgrade e adicionais

### Upgrade

- Start → Sales;
- Start → Service;
- Start → Complete;
- Sales → Complete;
- Service → Complete;
- qualquer pacote → faixa superior de capacidade;
- qualquer pacote elegível → módulo adicional.

O upgrade deverá preservar `applicationId`, ambiente, domínio, usuários, dados e histórico compatíveis.

### Downgrade

Somente será permitido quando:

- módulos removidos não possuírem processos ativos incompatíveis;
- dados puderem permanecer em modo leitura, ser exportados ou tratados pela política;
- consumo estiver dentro dos novos limites;
- integrações dependentes forem resolvidas;
- o cliente confirmar as consequências.

### Adicionais iniciais candidatos

- usuário adicional;
- armazenamento adicional;
- domínio gerenciado;
- migração de dados;
- notificações;
- assinatura eletrônica;
- integração de agenda;
- API;
- formulários avançados;
- mapa de ativos;
- relatório personalizado;
- suporte prioritário.

Nenhum adicional candidato será comercializado antes de possuir escopo, custo e critério de aceite.

## 11. Presets setoriais iniciais

| Preset | Pacote-base | Módulos e termos ajustados | Estado |
|---|---|---|---|
| Profissional autônomo | Start | portfólio, contato, agenda opcional | candidato a primeiro piloto |
| Prestador de serviços | Service | serviço, solicitação, ordem e conclusão | candidato a primeiro piloto |
| Consultoria | Sales ou Complete | oportunidade, proposta, projeto e entrega | planejamento |
| Escritório técnico | Complete | cliente, proposta, serviço e documento | planejamento |
| Engenharia e manutenção | Service ou Complete | unidade, ativo, ordem, evidência e aceite | planejamento |

O primeiro preset deverá ser escolhido a partir de acesso a clientes-piloto, clareza do problema e baixo risco regulatório.

## 12. Critérios para publicar preços

Preços somente poderão ser publicados quando:

1. o custo de provisionamento estiver medido;
2. o custo mensal por instância estiver medido;
3. backup, logs e armazenamento estiverem incluídos;
4. a implantação padrão possuir esforço previsível;
5. limites técnicos estiverem testados;
6. o suporte possuir capacidade e processo;
7. impostos e meios de cobrança estiverem definidos;
8. pelo menos um piloto de Start e um de Sales ou Service tiverem sido acompanhados;
9. upgrade e encerramento tiverem sido testados;
10. margem mínima tiver sido aprovada.

## 13. Indicadores de validação comercial

- visitas ao catálogo por pacote;
- início e conclusão do configurador;
- trials solicitados, provisionados e ativados;
- tempo até primeiro valor;
- uso de módulos durante o trial;
- conversão por pacote e preset;
- solicitações de customização fora do catálogo;
- tempo e custo de implantação;
- chamados de suporte por instância;
- upgrades;
- cancelamentos e motivos;
- margem por pacote depois dos custos diretos.

## 14. Questões abertas

- nomes definitivos dos pacotes;
- valores e periodicidade;
- cobrança ou isenção da implantação;
- faixas acima do baseline;
- política de excedentes;
- desconto anual;
- parceiros e comissionamento;
- meios de pagamento;
- canais de suporte;
- SLA prioritário;
- primeiro preset e clientes-piloto;
- quais integrações entram na primeira versão.

## 15. Decisão de encerramento

Esta matriz fecha o conteúdo comercial mínimo necessário para estimar custos, construir o configurador e conduzir pilotos. Os limites são baselines internos sujeitos a validação; não são oferta pública nem autorização para cobrança.

Os pacotes deverão permanecer composições versionadas do manifesto canônico. Qualquer proposta que exija uma base de código exclusiva será tratada como projeto especial, não como variação normal do VPC Business.
