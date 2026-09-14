# Arquitetura Técnica Open Source Oficial — Plataforma VPC

**Versão:** 1.0  
**Data:** 21 de julho de 2026  
**Estado:** arquitetura de referência para planejamento; implementação não iniciada  
**Abrangência:** site comercial, plano de controle, fábrica e aplicações independentes dos clientes

## 1. Decisão arquitetural

A VPC-GEOSER operará uma fábrica de aplicações, e não uma única aplicação multiempresa. O site comercial permitirá selecionar, adquirir e configurar uma solução. A configuração aprovada será registrada em um manifesto versionado, transformada em artefatos reproduzíveis e provisionada como aplicação independente em ambiente próprio do cliente.

Toda a composição essencial deverá ser executável exclusivamente com software open source. Serviços proprietários somente poderão aparecer como integrações opcionais, isoladas por adaptadores e removíveis sem impedir o funcionamento básico do produto.

## 2. Limites do sistema

A plataforma será dividida em três domínios técnicos:

1. **Experiência comercial:** site da VPC, catálogo, configurador, trial, aquisição e área do cliente.
2. **Plano de controle:** clientes, ofertas, manifestos, validações, geração, provisionamento, versões, ciclo de vida, suporte, consumo e auditoria.
3. **Plano de dados do cliente:** aplicação gerada, banco, arquivos, usuários, domínio, integrações e telemetria da instância.

O plano de controle administra as instâncias, mas não será o banco operacional compartilhado delas. Uma falha ou encerramento do plano de controle não poderá apagar os dados do cliente nem tornar impossível sua exportação e restauração.

## 3. Princípios obrigatórios

- uma aplicação independente por cliente e por aquisição, salvo agrupamento expressamente contratado;
- banco lógico independente por aplicação; banco físico dedicado quando o risco, volume ou contrato exigir;
- identidade, domínio, segredos, arquivos, configuração e ciclo de vida isolados;
- infraestrutura gerada de forma declarativa, idempotente, auditável e reversível;
- customização descrita como dados validados, não como alterações manuais no código-base;
- módulos versionados, com dependências, migrações e compatibilidade declaradas;
- segredos fora do manifesto e do repositório;
- formatos abertos, APIs documentadas e exportação integral dos dados do cliente;
- observabilidade sem mistura indevida de conteúdo ou dados pessoais entre clientes;
- nenhuma tecnologia selecionada apenas por gratuidade ou popularidade;
- versões aprovadas e imagens fixadas por digest; não será permitido depender de `latest`;
- atualização de segurança e restauração testada farão parte do produto, não serão tarefas opcionais.

## 4. Fluxo técnico oficial

```text
Catálogo versionado
        ↓
Configuração do cliente
        ↓
Manifesto em rascunho
        ↓
Resolução de defaults e validações
        ↓
Manifesto aprovado e imutável
        ↓
Plano de composição da aplicação
        ↓
Build reproduzível + SBOM + testes
        ↓
Plano de infraestrutura
        ↓
Provisionamento idempotente
        ↓
Migração + carga inicial + verificação
        ↓
Publicação da instância independente
        ↓
Operação, atualização, exportação e encerramento
```

Falhas não poderão avançar silenciosamente o estado comercial. Cada etapa deverá registrar entrada, versão, resultado, responsável técnico e possibilidade de nova tentativa.

## 5. Arquitetura lógica

### 5.1 Experiência comercial

Responsabilidades:

- apresentar produtos por problema resolvido;
- comparar pacotes e adicionais;
- coletar configuração visual e funcional permitida;
- validar escolhas incompatíveis antes da compra;
- iniciar trial e acompanhar provisionamento;
- permitir conversão do trial preservando a instância;
- encaminhar o cliente à administração de sua aplicação.

O site não deverá gerar código diretamente. Ele produzirá uma solicitação validada ao plano de controle.

### 5.2 Plano de controle

Serviços lógicos mínimos:

- catálogo de produtos, pacotes, módulos e versões;
- cadastro comercial de clientes;
- configurador e resolvedor de defaults;
- registro e validador de manifestos;
- orquestrador de tarefas duráveis;
- gerador/compositor de aplicações;
- catálogo de templates e módulos;
- provisionador de infraestrutura;
- registro de instâncias e inventário de versões;
- domínio, certificados e referências de segredos;
- ciclo de vida de trial e contrato;
- medição de limites e eventos de cobrança;
- atualização, migração, backup, restauração e encerramento;
- auditoria e suporte operacional.

O primeiro desenho deverá ser um **monólito modular com trabalhadores assíncronos**, não um conjunto prematuro de microsserviços. Separações físicas ocorrerão quando isolamento de segurança, escalabilidade ou operação justificarem o custo.

### 5.3 Aplicação do cliente

Cada instância deverá possuir:

- interface pública e administrativa;
- API da aplicação;
- módulos contratados;
- configuração resolvida assinada ou verificada;
- banco PostgreSQL próprio, com PostGIS quando necessário;
- armazenamento de arquivos isolado;
- realm ou domínio de identidade isolado, conforme o perfil aprovado;
- filas ou tarefas locais somente quando o produto exigir;
- política própria de backup, retenção e exportação;
- métricas, logs e verificações identificadas pela instância.

## 6. Stack de referência

As escolhas abaixo formam a referência inicial. A aprovação definitiva de cada versão dependerá de inventário de licença, segurança, manutenção e teste operacional.

| Camada | Referência inicial | Função | Condição |
|---|---|---|---|
| Sistema operacional | Linux | execução em servidor | distribuição suportada e atualizada |
| Conteinerização | Podman ou Docker Engine/Moby | empacotamento OCI | composição sem dependência de serviço proprietário |
| Orquestração inicial | Compose compatível com OCI | primeiras instâncias e baixa escala | automação e isolamento comprovados |
| Orquestração evolutiva | Kubernetes ou K3s | escala e múltiplos nós | somente quando a carga operacional justificar |
| Proxy e TLS | Traefik ou Caddy | roteamento, HTTPS e certificados | versão/licença homologada |
| Front-end | React com Next.js | site, configurador e aplicações | evitar dependência funcional de hospedagem exclusiva |
| Back-end | TypeScript com NestJS | APIs, domínio e trabalhadores | arquitetura modular e contratos OpenAPI |
| Banco | PostgreSQL | dados transacionais e metadados | padrão principal da plataforma |
| Geoespacial | PostGIS | geometrias, índices e análise espacial | ativado somente nos produtos que necessitem |
| Identidade | Keycloak | OIDC, OAuth 2.0, SAML e gestão de identidade | realms e políticas de isolamento definidos |
| Cache | Valkey | cache, locks e dados efêmeros | nunca como fonte única de verdade |
| Mensageria | RabbitMQ | tarefas e eventos assíncronos | adoção apenas para fluxos duráveis necessários |
| Objetos | implementação S3 open source homologada | documentos, imagens e exports | API substituível e teste de restauração obrigatório |
| Mapas web | MapLibre GL JS | visualização cartográfica | fontes e estilos independentes de provedor obrigatório |
| Servidor geoespacial | GeoServer | serviços OGC quando exigidos | não obrigatório em aplicações sem essa necessidade |
| ETL geoespacial | GDAL/OGR | transformação e interoperabilidade | execução controlada e limites de recursos |
| Infraestrutura como código | OpenTofu + Ansible | recursos e configuração | estado protegido e revisão de mudanças |
| Telemetria | OpenTelemetry | instrumentação interoperável | coleta com minimização de dados |
| Métricas | Prometheus | métricas operacionais | retenção definida por perfil |
| Painéis | Grafana OSS | visualização operacional | obrigações AGPL avaliadas por versão e distribuição |
| Logs | solução open source homologada | centralização e pesquisa | seleção após prova de custo e licença |
| CI/CD | GitLab CE, Forgejo Actions ou Jenkins | build, teste e publicação | sem obrigação de SaaS proprietário |
| Registro OCI | CNCF Distribution ou Harbor | imagens e artefatos | varredura, retenção e controle de acesso |
| Testes | Vitest/Jest, Playwright e ferramentas de API | qualidade automatizada | cenários funcionais e de isolamento obrigatórios |

PostgreSQL utiliza licença liberal própria; PostGIS é GPLv2 e seu uso normal como banco não impõe automaticamente GPL ao código da aplicação. Keycloak é open source e suporta padrões de identidade. Qualquer versão concreta ainda deverá passar pelo processo formal de homologação.

## 7. Decisões sobre complexidade

### 7.1 Primeira fase

A primeira composição deverá privilegiar simplicidade operacional:

- monólito modular para plano de controle;
- monólito modular para Business Start;
- processos assíncronos separados apenas para geração e provisionamento;
- PostgreSQL como fonte transacional;
- implantação em contêineres OCI;
- Compose para piloto controlado;
- automação integral desde o início;
- interfaces internas versionadas para permitir separação futura.

### 7.2 Quando adotar Kubernetes

Kubernetes não será requisito da primeira entrega. Sua adoção dependerá de evidências como:

- quantidade de instâncias que torne a operação manual inviável;
- necessidade de alta disponibilidade multi-nó;
- atualizações coordenadas em escala;
- isolamento e políticas de rede mais sofisticadas;
- equipe capaz de operar, proteger e recuperar o cluster.

### 7.3 Quando separar microsserviços

Um módulo somente se tornará serviço separado quando houver pelo menos uma razão comprovada: escala independente, isolamento de segurança, ritmo de entrega distinto, dependência tecnológica específica ou limite claro de responsabilidade operacional.

## 8. Modelo de isolamento

Perfis previstos:

| Perfil | Aplicação | Banco | Infraestrutura | Uso esperado |
|---|---|---|---|---|
| Essencial | independente | banco lógico independente | host ou cluster compartilhado com isolamento | VPC Business de menor porte |
| Profissional | independente | banco e credenciais exclusivos | namespace/rede e recursos reservados | Business com maior criticidade |
| Dedicado | independente | servidor ou cluster dedicado | ambiente dedicado | Specialized, contratos críticos ou requisito institucional |

Mesmo no perfil Essencial, tabelas compartilhadas por `tenant_id` entre aplicações não serão o padrão. O objetivo é preservar independência, exportação, restauração e migração por cliente.

## 9. Customização sem bifurcação de código

A identidade e o comportamento contratado deverão ser compostos por:

- tokens de tema;
- ativos validados;
- páginas e seções homologadas;
- módulos e versões;
- perfis e permissões canônicas;
- campos declarativos;
- workflows homologados;
- limites e políticas;
- adaptadores de integração.

Não serão permitidos, como customização comum:

- CSS, JavaScript ou SQL arbitrário do cliente;
- alteração manual de arquivos após provisionamento;
- fork permanente por cliente;
- plugin sem assinatura, versão, licença e revisão de segurança;
- mudança de banco sem migração registrada.

Necessidades exclusivas serão tratadas como novo componente reutilizável, extensão homologada ou projeto sob medida explicitamente separado do núcleo.

## 10. Segurança e privacidade

Controles mínimos:

- autenticação por OIDC e autorização no back-end;
- menor privilégio e segregação entre operação VPC e administração do cliente;
- MFA obrigatório para funções administrativas críticas;
- segredos em mecanismo dedicado, nunca em manifesto, imagem ou repositório;
- TLS em trânsito e criptografia de volumes/backups conforme risco;
- trilha de auditoria para mudanças administrativas e de ciclo de vida;
- validação de uploads e limites de tipo/tamanho;
- proteção contra abuso em formulários e APIs públicas;
- atualização contínua de dependências e imagens-base;
- SBOM por release e verificação de vulnerabilidades;
- política LGPD, retenção, exportação e exclusão por produto;
- teste de isolamento entre clientes antes de cada release relevante.

## 11. Dados, backup e portabilidade

Cada aplicação deverá oferecer:

- exportação dos dados de negócio em CSV e/ou JSON documentado;
- geodados em GeoJSON, GeoPackage ou formato aberto apropriado;
- documentos em seus formatos originais e índice de metadados;
- dump lógico PostgreSQL e procedimento documentado de restauração;
- backup criptografado, com retenção definida pelo pacote;
- teste periódico de restauração;
- migração entre ambientes sem alteração do manifesto funcional;
- encerramento com janela de recuperação e registro de eliminação.

Backup não será considerado válido apenas porque o arquivo foi produzido. A restauração deverá ser testável e mensurável.

## 12. Observabilidade e operação

O plano de controle deverá conhecer, no mínimo:

- estado comercial e estado técnico separados;
- versão da base, dos módulos, do schema e do manifesto;
- saúde da aplicação, API, banco e tarefas;
- data do último backup e último teste de restauração;
- uso de armazenamento e limites contratados;
- falhas de atualização, integração e provisionamento;
- eventos de segurança e auditoria;
- prazo de validade de domínio e certificado.

Logs não deverão conter senhas, tokens, documentos completos ou dados pessoais sem necessidade demonstrada. A VPC deverá distinguir telemetria central permitida de dados operacionais pertencentes ao cliente.

## 13. Cadeia de fornecimento e licenças

Cada release deverá produzir:

- SBOM em CycloneDX ou SPDX;
- inventário de componentes, versões e licenças;
- atribuições e avisos exigidos;
- relatório de vulnerabilidades e decisão sobre exceções;
- origem e digest das imagens;
- assinatura ou evidência de integridade dos artefatos;
- política de atualização e fim de suporte;
- registro de modificações em componentes copyleft distribuídos.

Componentes AGPL, SSPL, BSL, Elastic License, licenças `source available` ou termos semelhantes não serão tratados automaticamente como equivalentes. AGPL é open source, mas exige avaliação jurídica e operacional específica; SSPL, BSL e licenças `source available` não serão aceitas como open source apenas porque o código é visível.

## 14. Integrações externas

Pagamento, e-mail, WhatsApp, assinatura eletrônica, mapas premium, dados comerciais e IA poderão ser integrados mediante adaptadores. Cada adaptador deverá declarar:

- provedor e alternativa;
- dados transmitidos;
- credenciais exclusivas;
- custo e limites;
- comportamento na indisponibilidade;
- modo de desativação;
- exportação ou migração;
- responsabilidade contratual.

E-mail básico deverá possuir alternativa SMTP. Mapas deverão funcionar com padrões e fontes abertas ou auto-hospedáveis. A aplicação não poderá deixar de iniciar porque uma integração opcional foi removida.

## 15. Ambientes

Ambientes mínimos:

- desenvolvimento local reproduzível;
- integração e testes automatizados;
- homologação da base e dos módulos;
- produção do plano de controle;
- produção isolada das aplicações;
- ambiente temporário para restauração e ensaio de migração.

Dados reais de clientes não serão copiados para desenvolvimento. Quando forem indispensáveis para diagnóstico autorizado, deverão ser minimizados, protegidos e eliminados ao término.

## 16. Roadmap técnico

### Fase 0 — homologação arquitetural

- fechar catálogo de tecnologias e versões;
- produzir matriz de licenças;
- definir ameaças, perfis de isolamento e política de segredos;
- tornar o schema do manifesto executável;
- definir contratos do catálogo de módulos e das políticas;
- preparar prova de restauração e portabilidade.

### Fase 1 — composição mínima verificável

- site/catalogador e configurador mínimo;
- plano de controle modular;
- Business Start como primeira base gerável;
- criação de manifesto, validação e composição determinística;
- provisionamento automatizado de uma instância de teste;
- identidade, domínio, banco, backup, telemetria e exportação;
- nenhum pagamento real ainda necessário para comprovar a fábrica.

### Fase 2 — trial operacional

- trial de 14 dias;
- conversão preservando a instância;
- limites, suspensão e recuperação;
- painel operacional e suporte;
- atualização segura da base e módulos;
- piloto com clientes controlados.

### Fase 3 — linha Business

- pacotes Sales, Service e Complete;
- adicionais e integrações homologadas;
- automação de cobrança por adaptador;
- escala operacional e metas de serviço;
- avaliação objetiva da necessidade de Kubernetes.

### Fase 4 — produtos Specialized

- núcleo geoespacial comum;
- VPC Forest Dynamics em posição de destaque, inicialmente como piloto científico assistido;
- Territorial Intelligence, Climate & Infrastructure Resilience e Territorial Operations;
- perfis dedicados de infraestrutura, dados e suporte.

### Fase 5 — ecossistema

- catálogo interno de módulos e extensões;
- SDK e regras para parceiros homologados;
- assinatura e distribuição segura de componentes;
- marketplace somente após governança, suporte e compatibilidade estarem maduros.

## 17. Critérios para iniciar implementação

Nenhum desenvolvimento da fábrica deverá começar antes de existirem:

1. stack e versões homologadas;
2. matriz de licenças aprovada;
3. manifesto V1 executável e casos de teste;
4. modelo de isolamento definido para o Business Start;
5. estratégia de segredos;
6. modelo de backup, restauração, exportação e encerramento;
7. ameaça mínima e controles de segurança;
8. contrato do catálogo de módulos;
9. definição do primeiro ambiente de referência;
10. critérios mensuráveis de aceite da composição mínima.

## 18. Questões ainda pendentes

- versões exatas de cada componente;
- escolha entre Podman e Moby/Docker Engine na operação inicial;
- proxy padrão entre Traefik e Caddy;
- implementação S3 open source padrão;
- solução central de logs;
- mecanismo de segredos;
- ferramenta de tarefas duráveis do provisionador;
- CI/CD e registro OCI oficiais;
- localização inicial de hospedagem e requisitos de soberania;
- RPO, RTO e SLA por pacote;
- política jurídica definitiva para componentes AGPL;
- custo de infraestrutura por perfil e margem mínima.

Essas pendências devem ser resolvidas por provas técnicas e matriz comparativa, não por preferência pessoal.

## 19. Decisão de encerramento

Esta arquitetura estabelece o desenho técnico-alvo e a sequência de validação. O próximo artefato será o **Catálogo Tecnológico Homologado**, com versões, licenças, alternativas, critérios, custos operacionais e decisão por camada. Somente depois deverá ser preparada a composição mínima executável da fábrica.
