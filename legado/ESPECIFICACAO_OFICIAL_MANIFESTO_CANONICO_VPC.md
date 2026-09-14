# Especificação Oficial — Manifesto Canônico VPC

**Versão do documento:** 1.0  
**Data:** 19 de julho de 2026  
**Estado:** contrato conceitual para validação; implementação não iniciada  
**Aplicação inicial:** VPC Business Start  
**Abrangência futura:** VPC Business e VPC Specialized

**Documentos relacionados:** `ESPECIFICACAO_OFICIAL_VPC_BUSINESS_START.md`, `MATRIZ_COMERCIAL_OFICIAL_VPC_BUSINESS.md`, `ESPECIFICACAO_OFICIAL_TRIAL_VPC_BUSINESS.md`, `ESPECIFICACAO_OFICIAL_CONFIGURADOR_COMERCIAL_VPC.md` e `MODELO_FUNCIONAL_COMUM_OFICIAL_VPC.md`

## Executive Summary

- **O manifesto será a fonte de verdade de cada aplicação gerada.** Ele descreverá o que foi comprado, o que pode ser configurado, quais módulos estão ativos, onde a aplicação será provisionada e quais limites governam sua operação.
- **O manifesto não conterá segredos.** Credenciais, chaves e certificados serão referenciados por identificadores de um mecanismo seguro.
- **Customização e código serão separados.** Aparência, conteúdo estrutural, campos, fluxos e módulos deverão ser expressos como dados validados, permitindo atualização sem sobrescrever escolhas do cliente.
- **O contrato será versionado e extensível.** A primeira versão atenderá o Business Start, mas os mesmos blocos deverão comportar Sales, Service, Complete e produtos Specialized.

## 1. Finalidade

O manifesto canônico é o contrato entre:

- catálogo comercial;
- configurador;
- cliente;
- validação de compatibilidade;
- gerador da aplicação;
- provisionador de infraestrutura;
- registro de instâncias;
- cobrança;
- mecanismo de atualização;
- suporte e encerramento.

Ele deverá responder, de forma auditável:

1. quem é o cliente;
2. qual solução foi adquirida;
3. quais módulos e capacidades estão ativos;
4. como a aplicação deve parecer e funcionar;
5. quais limites e integrações se aplicam;
6. qual ambiente deverá ser criado;
7. qual versão da base e do schema está em uso;
8. qual é o estado do trial ou contrato;
9. quais mudanças foram aprovadas;
10. como atualizar, suspender, exportar ou encerrar a instância.

## 2. Princípios obrigatórios

1. **Versionamento:** toda alteração gera nova revisão identificável.
2. **Validação antes da execução:** manifestos inválidos não chegam ao gerador.
3. **Idempotência:** reaplicar a mesma revisão não deve gerar recursos duplicados.
4. **Ausência de segredos:** apenas referências seguras são permitidas.
5. **Separação de responsabilidades:** desejo comercial, configuração funcional e infraestrutura possuem blocos distintos.
6. **Compatibilidade declarada:** módulos informam dependências e versões aceitas.
7. **Imutabilidade histórica:** revisões anteriores permanecem auditáveis.
8. **Defaults explícitos:** valores herdados devem ser resolvidos e registrados antes do provisionamento.
9. **Portabilidade controlada:** o contrato não deve depender de detalhes acidentais de um único provedor.
10. **Extensões homologadas:** campos adicionais usam namespaces e schemas conhecidos.
11. **Isolamento:** cada manifesto representa uma aplicação cliente independente.
12. **Reversibilidade:** alterações relevantes devem possuir estratégia de rollback ou bloqueio explícito.
13. **Open source:** componentes centrais de execução deverão cumprir a diretriz oficial de stack open source.
14. **Integrações proprietárias opcionais:** dependências externas fechadas deverão ser substituíveis e explicitamente declaradas.

## 3. Identidade e versionamento

### Campos obrigatórios

- `manifestId`: identificador global do manifesto;
- `schemaVersion`: versão do contrato canônico;
- `revision`: número crescente da revisão;
- `applicationId`: identidade estável da aplicação;
- `customerId`: referência ao cliente no plano de controle;
- `createdAt` e `createdBy`;
- `approvedAt` e `approvedBy`, quando aplicável;
- `status`: estado da revisão;
- `previousRevision`: referência à revisão anterior;
- `changeReason`: motivo da alteração.

### Estados da revisão

```text
draft → validating → approved → applying → active
                    ↘ rejected       ↘ failed
active → superseded
```

Somente uma revisão poderá estar ativa por aplicação. Uma revisão falha não substituirá automaticamente a última revisão ativa.

## 4. Estrutura canônica

O manifesto será composto pelos seguintes blocos:

| Bloco | Responsabilidade |
|---|---|
| `metadata` | identidade, versão, revisão e auditoria |
| `customer` | referência e informações mínimas do contratante |
| `offer` | linha, produto, pacote e edição adquiridos |
| `lifecycle` | trial, contrato, suspensão e encerramento |
| `branding` | identidade visual e domínio de marca |
| `navigation` | páginas, menus e composição permitida |
| `modules` | capacidades ativadas e configurações |
| `roles` | perfis e permissões canônicas |
| `dataModel` | campos adicionais e listas homologadas |
| `workflows` | estados, transições e regras configuráveis |
| `limits` | cotas e limites comerciais ou técnicos |
| `integrations` | integrações e referências seguras |
| `deployment` | requisitos lógicos de provisionamento |
| `policies` | privacidade, retenção, backup e exportação |
| `observability` | saúde, logs, métricas e alertas previstos |
| `billing` | referências de plano, assinatura e consumo |
| `extensions` | configurações homologadas com namespace |

## 5. Exemplo conceitual

O exemplo abaixo serve para discutir o contrato. YAML não está definido como formato definitivo de persistência.

```yaml
metadata:
  manifestId: man_01
  schemaVersion: 1.0.0
  revision: 1
  applicationId: app_01
  customerId: cus_01
  status: approved
  createdAt: 2026-07-19T12:00:00-03:00
  createdBy: user_01
  changeReason: criação do trial

customer:
  displayName: Empresa Exemplo
  locale: pt-BR
  timezone: America/Sao_Paulo

offer:
  line: business
  product: business-start
  packageVersion: 1.0.0
  edition: service-provider

lifecycle:
  stage: trial
  startsAt: 2026-07-19T12:00:00-03:00
  expiresAt: 2026-08-02T23:59:59-03:00
  conversionMode: preserve-instance

branding:
  applicationName: Empresa Exemplo
  logoAssetRef: asset_logo_01
  themePreset: professional-light
  colors:
    primary: "#2457A7"
    secondary: "#EEF3FA"
    accent: "#E58A22"
  fontPreset: inter

navigation:
  publicPages:
    - type: home
      enabled: true
    - type: company
      enabled: true
    - type: catalog
      enabled: true
    - type: contact
      enabled: true

modules:
  - id: company-profile
    version: 1.0.0
    enabled: true
  - id: portfolio
    version: 1.0.0
    enabled: true
    config:
      products: true
      services: true
      cases: false
  - id: basic-crm
    version: 1.0.0
    enabled: true
    config:
      opportunityWorkflow: basic-v1

roles:
  presets:
    - application-admin
    - manager
    - commercial
    - content-editor

limits:
  users: 3
  contacts: 500
  storageMb: 1024
  publicFormSubmissionsPerMonth: 500

integrations:
  - id: transactional-email
    providerClass: email
    credentialRef: secret://app_01/email

deployment:
  isolationMode: dedicated-application
  regionPolicy: brazil-preferred
  databaseMode: isolated
  domain:
    mode: trial-subdomain
    hostname: empresa-exemplo.trial.example.invalid

policies:
  privacyPolicyRequired: true
  retentionPolicy: business-start-trial-v1
  backupPolicy: trial-basic-v1
  exportPolicy: basic-customer-data-v1

billing:
  planRef: business-start-trial
  subscriptionRef: null
```

## 6. Bloco `customer`

O manifesto não substituirá o cadastro completo do cliente no plano de controle. Ele conterá apenas referências e valores necessários à aplicação.

### Campos

- identificador do cliente;
- nome de exibição;
- idioma e localidade;
- fuso horário;
- país e região operacional;
- contatos administrativos por referência;
- classificação comercial quando necessária;
- referência ao aceite dos termos.

Dados de cobrança detalhados, credenciais e documentos sensíveis permanecerão nos sistemas próprios.

## 7. Bloco `offer`

### Campos

- linha: `business` ou `specialized`;
- produto;
- pacote;
- edição ou preset;
- versão do pacote;
- canal de aquisição;
- módulos incluídos;
- módulos adicionais;
- serviços profissionais associados por referência.

### Regra

Pacote e edição resolvem defaults. O manifesto aprovado deverá registrar a configuração efetiva, evitando que uma alteração futura no catálogo modifique silenciosamente aplicações existentes.

## 8. Bloco `lifecycle`

### Etapas da aplicação

```text
requested → trial-provisioning → trial-active → conversion-pending
                                      ↓                 ↓
                               trial-expired      contracted-active
                                      ↓                 ↓
                                  suspended ← suspension-pending
                                      ↓
                              termination-pending → terminated
```

### Campos

- etapa atual;
- início e expiração do trial;
- modo de conversão;
- referência ao contrato;
- datas de suspensão e encerramento;
- janela de recuperação;
- política de retenção;
- motivo de mudança de estado.

Estados comerciais não substituem estados técnicos de provisionamento. Ambos deverão ser registrados separadamente.

## 9. Bloco `branding`

### Configurações permitidas

- nome da aplicação;
- logotipo e ícone por referência de ativo;
- preset de tema;
- cores dentro das regras de contraste e formato;
- tipografia homologada;
- imagens institucionais;
- identidade de e-mails e documentos quando suportada.

### Validações

- formato e tamanho de ativos;
- contraste mínimo;
- tokens de cor permitidos;
- inexistência de código ou CSS arbitrário;
- direitos de uso declarados para ativos enviados;
- fallback obrigatório.

## 10. Bloco `navigation`

O bloco descreve páginas, seções e menus por componentes homologados.

### Página

- identificador estável;
- tipo canônico;
- slug;
- título;
- estado;
- seções ordenadas;
- visibilidade;
- requisitos de autenticação;
- metadados permitidos.

### Restrições

- páginas obrigatórias não podem ser removidas quando necessárias ao produto;
- slugs devem ser únicos;
- rotas reservadas não podem ser usadas;
- componentes precisam ser compatíveis com o pacote;
- referências devem apontar para conteúdo válido.

## 11. Bloco `modules`

Cada módulo deverá declarar em seu catálogo técnico:

- identificador canônico;
- versão;
- schema de configuração;
- dependências;
- incompatibilidades;
- permissões fornecidas;
- entidades utilizadas;
- migrações exigidas;
- limites aplicáveis;
- eventos emitidos e consumidos;
- suporte a ativação e desativação;
- política de rollback.

### Validações

- módulo existente e homologado;
- versão suportada pela base da aplicação;
- dependências presentes;
- ausência de conflitos;
- configuração conforme schema;
- cobertura pelo pacote ou adicional contratado.

## 12. Bloco `roles`

Perfis visíveis serão composições de permissões canônicas.

Exemplos de permissões:

- `content.read`;
- `content.write`;
- `content.publish`;
- `portfolio.manage`;
- `leads.read`;
- `leads.manage`;
- `customers.read`;
- `customers.manage`;
- `users.manage`;
- `settings.manage`;
- `reports.read`;
- `exports.execute`.

O manifesto poderá renomear perfis e selecionar permissões dentro dos limites do pacote, mas não criar permissões desconhecidas.

## 13. Bloco `dataModel`

Campos adicionais deverão ser declarativos e limitados a tipos homologados:

- texto curto;
- texto longo;
- número;
- moeda;
- data ou data e hora;
- booleano;
- seleção simples;
- seleção múltipla;
- referência controlada;
- endereço;
- localização, quando o módulo permitir.

Cada campo deverá informar:

- namespace;
- entidade;
- chave estável;
- rótulo;
- tipo;
- obrigatoriedade;
- validação;
- visibilidade;
- permissões;
- comportamento de exportação;
- tratamento de dados pessoais.

Alterações destrutivas de tipo ou remoção com dados existentes exigirão migração aprovada.

## 14. Bloco `workflows`

O manifesto poderá selecionar um workflow homologado e customizar:

- nomes visíveis dos estados;
- estados opcionais permitidos;
- transições habilitadas;
- perfil autorizado por transição;
- campos obrigatórios na transição;
- notificações vinculadas.

Não será permitido criar ciclos inválidos, remover o estado inicial, remover todos os estados finais ou alterar significados canônicos necessários aos relatórios.

## 15. Bloco `limits`

Limites devem ser expressos em unidades claras:

- usuários ativos;
- armazenamento;
- registros por entidade;
- submissões públicas por período;
- volume de notificações;
- chamadas de integração;
- domínios;
- frequência de backup;
- retenção;
- capacidade computacional quando aplicável.

O manifesto deverá distinguir:

- limite comercial;
- limite técnico;
- consumo atual, que pertence à telemetria e não ao manifesto;
- comportamento ao atingir o limite: avisar, bloquear, cobrar excedente ou solicitar upgrade.

## 16. Bloco `integrations`

### Campos

- identificador da integração;
- classe de provedor;
- versão do adaptador;
- estado;
- referência de credencial;
- escopos autorizados;
- endpoints permitidos por referência;
- limites e política de falha;
- dados enviados e recebidos;
- base legal ou consentimento quando aplicável.

### Proibições

- senha, token ou chave em texto aberto;
- endpoint arbitrário não homologado;
- escopo superior ao necessário;
- integração sem política de revogação;
- compartilhamento de credencial entre clientes.

## 17. Bloco `deployment`

O manifesto descreverá intenção lógica, não comandos específicos de infraestrutura.

### Campos

- modo de isolamento;
- política de região;
- perfil de capacidade;
- modo de banco;
- domínio e aliases;
- política de certificados;
- referências de rede;
- perfil de armazenamento;
- classe de disponibilidade;
- política de atualização;
- estratégia de migração;
- restrições do cliente.

O plano resolvido de infraestrutura será um artefato derivado e auditável, separado do manifesto comercial-funcional.

## 18. Bloco `policies`

- privacidade;
- termos aplicáveis;
- classificação de dados;
- retenção;
- backup;
- restauração;
- exportação;
- auditoria;
- encerramento;
- localização de dados;
- anonimização ou exclusão quando aplicável.

Políticas deverão ser referenciadas por identificador e versão. Texto alterado posteriormente não poderá modificar retroativamente o aceite registrado.

## 19. Bloco `observability`

Deverá declarar:

- perfil de logs;
- métricas de saúde;
- verificações de disponibilidade;
- alertas técnicos;
- retenção de telemetria;
- mascaramento de dados;
- destinos autorizados;
- SLA aplicável por referência.

O manifesto não armazenará a telemetria; apenas definirá sua política.

## 20. Bloco `billing`

- referência do plano;
- referência da assinatura;
- moeda e periodicidade por referência comercial;
- módulos cobertos;
- limites contratados;
- regras de excedente;
- estado de cobrança necessário ao ciclo de vida;
- serviços profissionais por referência.

Valores financeiros e histórico de transações pertencem ao sistema de cobrança. O manifesto registra o contrato operacional efetivo.

## 21. Extensões

Extensões deverão usar namespace, por exemplo:

```text
extensions.vpc.business.sales
extensions.vpc.specialized.forestDynamics
extensions.partner.<identificador>
```

Cada namespace deverá possuir:

- responsável;
- schema;
- versão;
- compatibilidade;
- política de migração;
- classificação de segurança;
- autorização comercial.

Campos desconhecidos fora de `extensions` deverão causar falha de validação ou advertência explícita conforme a política do schema, nunca ser ignorados silenciosamente.

## 22. Processo de resolução e validação

```text
Configuração do cliente
          ↓
Manifesto em rascunho
          ↓
Aplicação de defaults do pacote e edição
          ↓
Validação estrutural
          ↓
Validação semântica e de compatibilidade
          ↓
Validação comercial e de limites
          ↓
Validação de segurança e políticas
          ↓
Manifesto resolvido para aprovação
          ↓
Plano de geração e provisionamento
```

### Erros bloqueantes

- schema inválido;
- dependência ausente;
- conflito de módulos;
- segredo exposto;
- limite incompatível;
- domínio inválido;
- política obrigatória ausente;
- versão não suportada;
- alteração destrutiva sem migração;
- oferta não coberta pelo contrato.

### Advertências

- configuração incompleta com fallback válido;
- conteúdo não publicado;
- integração opcional ausente;
- domínio provisório;
- métrica ou relatório desabilitado por falta de fonte.

## 23. Mudanças e mutabilidade

### Alterações normalmente seguras

- textos;
- imagens;
- cores válidas;
- ordem de seções;
- publicação de conteúdo;
- inclusão de usuário dentro do limite;
- configuração não estrutural de módulo.

### Alterações que exigem plano

- ativar ou desativar módulo;
- mudar pacote;
- alterar domínio;
- adicionar integração;
- alterar campos;
- mudar workflow;
- aumentar perfil de infraestrutura;
- modificar retenção ou região.

### Alterações potencialmente destrutivas

- remover entidade ou campo com dados;
- reduzir limite abaixo do consumo;
- trocar tipo de dado;
- encerrar aplicação;
- migrar região ou provedor;
- revogar integração necessária a processos ativos.

Essas alterações exigirão pré-condições, simulação, backup e confirmação adequada.

## 24. Artefatos derivados

O manifesto aprovado poderá gerar:

- configuração resolvida da aplicação;
- plano de infraestrutura;
- plano de banco e migrações;
- mapa de rotas e páginas;
- tema compilado a partir de tokens;
- matriz de permissões;
- configuração de domínios;
- plano de integrações;
- política de backup e observabilidade;
- registro de cobrança operacional;
- resumo legível para o cliente;
- checklist de aceite.

Esses artefatos deverão registrar a revisão de origem.

## 25. Critérios de aceite do manifesto V1

O contrato estará pronto para implementação quando:

1. representar integralmente uma configuração Business Start;
2. validar campos obrigatórios e tipos;
3. resolver defaults sem ambiguidade;
4. bloquear segredos em texto aberto;
5. validar dependências de módulos;
6. representar tema, páginas, perfis, limites, trial e domínio;
7. produzir uma configuração resolvida determinística;
8. permitir nova revisão sem apagar histórico;
9. distinguir alterações seguras, planejadas e destrutivas;
10. sustentar conversão de trial para contrato na mesma aplicação;
11. identificar políticas por versão;
12. permitir exportação de um resumo compreensível pelo cliente;
13. suportar extensão futura sem quebrar a V1;
14. possuir casos de teste válidos e inválidos definidos;
15. permitir associar todos os artefatos derivados à revisão de origem.

## 26. Casos de teste conceituais obrigatórios

- Business Start mínimo válido;
- Business Start com produtos e serviços;
- trial expirado e recuperável;
- conversão para contrato;
- upgrade para Sales;
- domínio próprio válido e inválido;
- cor inválida ou sem contraste;
- módulo sem dependência;
- versão incompatível;
- segredo exposto;
- limite inferior ao uso;
- campo customizado válido;
- remoção destrutiva de campo;
- integração revogada;
- reaplicação idempotente da mesma revisão;
- falha de provisionamento sem perda da revisão ativa.

## 27. Questões pendentes

- formato técnico definitivo do schema;
- política de compatibilidade semântica de versões;
- mecanismo de assinatura e integridade;
- responsável por aprovar cada classe de mudança;
- estratégia de rollback por módulo;
- catálogo inicial de políticas;
- catálogo de perfis de infraestrutura;
- limites exatos do trial;
- tratamento de conteúdo extenso e localização;
- limites de campos customizados;
- portabilidade entre provedores;
- política de extensões de parceiros.

## 28. Decisão de encerramento

O manifesto canônico será o primeiro contrato técnico-funcional da fábrica. Nenhum gerador ou provisionador deverá ser implementado antes que uma versão executável desse schema represente integralmente o VPC Business Start e passe pelos casos de validação definidos.

Esta especificação não define linguagem, framework, provedor ou formato final. Ela define as responsabilidades e garantias que qualquer implementação deverá cumprir.
