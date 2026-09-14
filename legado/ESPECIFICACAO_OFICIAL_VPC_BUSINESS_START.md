# Especificação Oficial — VPC Business Start

**Versão:** 1.0  
**Data:** 19 de julho de 2026  
**Estado:** especificação de produto para validação; desenvolvimento não iniciado  
**Linha:** VPC Business  
**Documento superior:** `DOCUMENTACAO_OFICIAL_DIAGNOSTICO_PORTFOLIO_VPC_GEOSER.md`

**Documentos relacionados:** `ESPECIFICACAO_OFICIAL_MANIFESTO_CANONICO_VPC.md`, `MATRIZ_COMERCIAL_OFICIAL_VPC_BUSINESS.md`, `ESPECIFICACAO_OFICIAL_TRIAL_VPC_BUSINESS.md`, `ESPECIFICACAO_OFICIAL_CONFIGURADOR_COMERCIAL_VPC.md` e `MODELO_FUNCIONAL_COMUM_OFICIAL_VPC.md`

## Executive Summary

- **O VPC Business Start será a primeira composição comercial da fábrica.** Ele deverá gerar uma aplicação empresarial independente que reúna presença digital, portfólio, contatos, clientes e oportunidades em um único sistema.
- **O produto não será apenas um site institucional.** O conteúdo público e o painel interno compartilharão a mesma base, permitindo que o cliente publique produtos e serviços e organize os contatos gerados.
- **A customização será controlada por manifesto.** Marca, domínio, páginas, seções, categorias, campos permitidos, perfis e limites serão configuráveis sem criar uma bifurcação de código por cliente.
- **O trial deverá ser uma aplicação real e conversível.** Quando contratado, o cliente continuará na mesma instância, preservando identidade, configuração e dados.

## 1. Objetivo do produto

O VPC Business Start atende profissionais, microempresas e pequenas empresas que precisam substituir uma combinação desarticulada de redes sociais, páginas estáticas, mensagens e planilhas por uma aplicação empresarial simples e própria.

O produto deverá permitir:

1. apresentar a empresa publicamente;
2. publicar um portfólio de produtos e serviços;
3. receber contatos e solicitações;
4. registrar clientes, contatos e oportunidades;
5. administrar conteúdo e cadastros sem alterar código;
6. operar em domínio, ambiente e banco independentes;
7. evoluir posteriormente para VPC Sales, VPC Service ou VPC Business Complete.

## 2. Proposta de valor

**“Sua empresa online e organizada em um sistema próprio, com site, portfólio, clientes e oportunidades configurados para a sua marca.”**

O valor não está apenas na publicação de páginas. Está na continuidade entre presença pública e gestão interna:

```text
Visitante conhece a empresa
          ↓
Consulta produtos e serviços
          ↓
Envia contato ou solicitação
          ↓
Sistema registra a oportunidade
          ↓
Equipe acompanha e converte o contato
```

## 3. Público inicial

- profissionais autônomos;
- prestadores de serviços;
- consultorias pequenas;
- escritórios técnicos;
- empresas de manutenção e instalação;
- comércio consultivo sem operação completa de e-commerce;
- empresas recém-formadas;
- empresas que possuem site, mas não possuem gestão integrada de contatos.

Segmentos com dados sensíveis ou forte regulação não serão tratados automaticamente como presets básicos sem análise específica.

## 4. Limites da primeira versão

### Incluído

- site responsivo;
- página inicial configurável;
- páginas institucionais;
- portfólio público;
- catálogo simples de produtos;
- catálogo simples de serviços;
- formulário de contato e solicitação;
- registro de leads ou oportunidades;
- cadastro básico de clientes e contatos;
- painel administrativo;
- usuários e perfis básicos;
- identidade visual;
- domínio provisório no trial;
- domínio próprio após configuração contratada;
- relatórios operacionais básicos;
- exportação dos cadastros permitidos.

### Fora do escopo padrão

- e-commerce completo;
- estoque e logística;
- emissão fiscal;
- contabilidade;
- folha de pagamento;
- pagamentos nativos;
- automação de marketing avançada;
- CRM avançado;
- ordens de serviço;
- prontuário ou dados clínicos;
- marketplace entre empresas;
- aplicativo móvel nativo;
- edição livre de código pelo cliente.

Essas capacidades poderão surgir como integração, upgrade ou produto posterior, mas não pertencem ao contrato inicial do Business Start.

## 5. Módulos funcionais

| Módulo | Obrigatoriedade | Resultado entregue |
|---|---|---|
| Identidade empresarial | obrigatório | marca, contatos, domínio e informações institucionais |
| Site institucional | obrigatório | páginas públicas responsivas |
| Portfólio | obrigatório | produtos, serviços, projetos ou casos publicados |
| Contato e oportunidades | obrigatório | captura, registro e acompanhamento inicial |
| Clientes e contatos | obrigatório em modo básico | base de relacionamento da empresa |
| Administração de conteúdo | obrigatório | gestão das informações publicadas |
| Usuários e permissões | obrigatório | acesso controlado ao painel |
| Relatórios básicos | obrigatório | visão de contatos, oportunidades e catálogo |
| Documentos e mídia | básico | imagens e arquivos utilizados nas páginas |
| Notificações | opcional | avisos de novos contatos por canais contratados |
| Integrações | opcional | serviços externos autorizados pelo pacote |

## 6. Estrutura de navegação pública

### Páginas obrigatórias

1. **Início**
   - proposta principal;
   - destaques de produtos ou serviços;
   - diferenciais;
   - chamada para contato;
   - contatos essenciais.
2. **Empresa**
   - apresentação;
   - história, missão ou valores, quando utilizados;
   - equipe, quando habilitada.
3. **Produtos e/ou Serviços**
   - categorias;
   - listagem;
   - página de detalhes;
   - chamada para solicitação.
4. **Contato**
   - formulário;
   - canais de contato;
   - localização, quando publicada;
   - consentimentos aplicáveis.

### Páginas opcionais

- portfólio de projetos;
- casos de sucesso;
- equipe;
- perguntas frequentes;
- política de privacidade;
- termos de uso;
- página livre baseada em blocos homologados.

## 7. Estrutura do painel administrativo

1. **Visão geral**
   - contatos recentes;
   - oportunidades abertas;
   - itens publicados;
   - alertas de configuração.
2. **Conteúdo**
   - páginas;
   - seções;
   - menu e rodapé;
   - mídia.
3. **Portfólio**
   - produtos;
   - serviços;
   - categorias;
   - projetos ou casos, quando habilitados.
4. **Relacionamento**
   - leads;
   - oportunidades;
   - clientes;
   - contatos;
   - histórico básico.
5. **Configurações**
   - empresa;
   - identidade visual;
   - domínio;
   - usuários;
   - permissões;
   - privacidade;
   - integrações disponíveis.
6. **Relatórios**
   - contatos por período;
   - oportunidades por estado;
   - itens ativos no portfólio;
   - origem declarada do contato, quando coletada.

## 8. Entidades principais

### Empresa

- identificador;
- nome empresarial;
- nome de exibição;
- descrição curta e completa;
- documento empresarial opcional conforme necessidade;
- contatos;
- endereço;
- redes e canais digitais;
- logotipo e ícone;
- estado de publicação.

### Página

- identificador;
- tipo;
- título;
- slug;
- seções ordenadas;
- metadados de busca permitidos;
- estado: rascunho, publicada ou arquivada;
- datas de publicação e atualização.

### Categoria

- identificador;
- tipo: produto, serviço, projeto ou caso;
- nome;
- descrição;
- ordem;
- estado.

### Produto

- identificador;
- categoria;
- nome;
- resumo;
- descrição;
- imagens;
- código interno opcional;
- preço público opcional;
- chamada para ação;
- destaque;
- estado de publicação.

O Business Start não controla estoque, tributação ou expedição.

### Serviço

- identificador;
- categoria;
- nome;
- resumo;
- descrição;
- imagens;
- forma de atendimento opcional;
- faixa ou condição comercial opcional;
- chamada para ação;
- destaque;
- estado de publicação.

### Lead ou oportunidade

- identificador;
- nome;
- empresa opcional;
- e-mail;
- telefone opcional;
- assunto;
- mensagem;
- produto ou serviço de interesse opcional;
- origem;
- consentimentos registrados;
- responsável;
- estado;
- histórico;
- datas de criação e atualização.

### Cliente e contato

- identificador;
- tipo de pessoa;
- nome ou razão social;
- nome de exibição;
- documento opcional e protegido;
- contatos;
- endereço opcional;
- observações controladas;
- estado;
- histórico de relacionamento.

### Usuário

- identificador;
- nome;
- e-mail;
- perfil;
- estado;
- último acesso;
- vínculo com a aplicação.

## 9. Estados e fluxos

### Publicação de conteúdo

```text
Rascunho → Revisão opcional → Publicado → Arquivado
```

### Oportunidade básica

```text
Nova → Em contato → Qualificada → Convertida
                         ↘ Perdida
```

Os nomes visíveis dos estados poderão ser customizados, mas seus significados canônicos deverão permanecer estáveis para relatórios e upgrades.

### Conversão de lead

1. visitante envia formulário;
2. sistema valida e registra a submissão;
3. sistema cria lead ou oportunidade;
4. responsável recebe notificação, quando habilitada;
5. usuário registra acompanhamento;
6. oportunidade pode gerar ou ser vinculada a cliente e contato;
7. histórico é preservado.

## 10. Perfis e permissões

### Administrador da aplicação

- administra usuários permitidos;
- configura empresa e identidade;
- administra todos os módulos contratados;
- publica conteúdo;
- exporta dados autorizados;
- consulta relatórios.

### Gestor

- administra conteúdo, portfólio e relacionamento;
- publica conforme permissão;
- consulta relatórios;
- não altera configurações críticas da instância.

### Comercial ou atendimento

- consulta e atualiza leads, oportunidades, clientes e contatos;
- consulta catálogo;
- não altera identidade, domínio ou usuários.

### Editor de conteúdo

- cria e edita páginas e portfólio;
- publica somente quando autorizado;
- não acessa dados comerciais além do necessário.

As permissões serão representadas por capacidades canônicas, ainda que os nomes dos perfis sejam customizados.

## 11. Customização

### Em autosserviço

- nome e descrição da empresa;
- logotipo, ícone e imagens;
- paleta a partir de regras válidas;
- tipografia homologada;
- textos e conteúdo;
- escolha e ordem de blocos permitidos;
- menus dentro da estrutura suportada;
- categorias;
- produtos, serviços e casos;
- campos adicionais previamente homologados;
- nomes visíveis dos estados comerciais;
- usuários dentro do limite;
- domínio provisório disponível.

### Assistida

- domínio próprio;
- migração de clientes, produtos ou serviços;
- identidade visual fora dos presets;
- campos ou regras não disponíveis no catálogo;
- integrações;
- relatórios exclusivos;
- automações específicas.

### Não permitida diretamente

- alteração arbitrária do banco;
- scripts inseridos pelo cliente;
- remoção de controles de segurança e privacidade;
- mudança de contratos canônicos;
- instalação de extensões não homologadas;
- edição direta do código da aplicação gerada.

## 12. Trial e conversão

### Requisitos do trial

- instância independente identificada como trial;
- manifesto válido e versionado;
- domínio provisório;
- limites de usuários, registros, mídia e integrações;
- indicação da data de expiração;
- dados de demonstração opcionais;
- possibilidade controlada de dados reais;
- exportação conforme política;
- avisos antes da expiração;
- suspensão recuperável.

### Conversão

A conversão deverá:

1. preservar o identificador da instância;
2. preservar configuração e dados permitidos;
3. atualizar plano, limites e estado comercial;
4. permitir domínio próprio;
5. ativar módulos adquiridos;
6. registrar aceite contratual e versão aplicável;
7. não reconstruir a aplicação do zero, salvo falha técnica formalmente tratada.

## 13. Relatórios mínimos

- quantidade de novos contatos por período;
- oportunidades por estado;
- tempo desde o último acompanhamento;
- produtos, serviços e páginas publicados;
- itens mais associados a solicitações, quando rastreáveis;
- usuários ativos dentro da aplicação;
- consumo dos limites relevantes.

Métricas de audiência web dependerão do mecanismo de analytics e do consentimento aplicável.

## 14. Requisitos não funcionais de produto

- interface responsiva;
- acessibilidade compatível com o escopo definido;
- isolamento entre clientes;
- autenticação segura;
- proteção contra abuso em formulários públicos;
- registro de eventos administrativos relevantes;
- backups conforme plano;
- exportação de dados essenciais;
- observabilidade da instância;
- tratamento de erros sem exposição de segredos;
- política de privacidade configurada antes da coleta pública;
- atualizações sem sobrescrever customizações válidas;
- desempenho aceitável nas páginas públicas e no painel.

Metas numéricas de disponibilidade, recuperação e desempenho serão definidas por plano e infraestrutura antes do desenvolvimento.

## 15. Integrações previstas

### Primeira versão

- e-mail transacional ou notificação equivalente;
- DNS e certificados para domínio;
- armazenamento de mídia;
- analytics opcional;
- proteção antispam ou antiabuso.

### Futuras ou adicionais

- mensageria;
- agenda externa;
- pagamentos;
- assinatura eletrônica;
- emissão fiscal;
- automação de marketing;
- APIs de terceiros;
- importadores e exportadores especializados.

Toda integração deverá ser declarada no manifesto por referência segura, nunca por segredo em texto aberto.

## 16. Critérios de aceite do produto

O Business Start estará apto a piloto quando for possível demonstrar, de ponta a ponta:

1. configuração válida de uma empresa;
2. geração de uma instância independente;
3. aplicação de tema sem alteração de código;
4. publicação de páginas, produtos e serviços;
5. envio público de contato;
6. criação automática da oportunidade;
7. acompanhamento pelo painel;
8. cadastro e associação de cliente;
9. aplicação de permissões;
10. exportação de dados permitidos;
11. backup e restauração testados;
12. expiração controlada do trial;
13. conversão do trial sem perda de dados;
14. atualização da aplicação preservando customizações;
15. encerramento conforme política.

## 17. Dependências para desenvolvimento

- manifesto canônico aprovado;
- catálogo de módulos e capacidades;
- design system parametrizável;
- modelo de identidade e autenticação;
- estratégia de isolamento por aplicação;
- provisionador;
- registro de instâncias;
- política de domínio e certificados;
- política de backup, exportação e encerramento;
- validação dos limites iniciais definidos na especificação oficial do trial;
- critérios de segurança e LGPD.

## 18. Questões pendentes

- validação do baseline de 14 dias, gratuito e sem cartão;
- quantidade de usuários por plano;
- limites de registros e armazenamento;
- domínio incluído ou cobrado separadamente;
- canais de notificação padrão;
- modelos de página inicialmente disponíveis;
- nível de analytics incluído;
- validação jurídica e operacional da recuperação por 30 dias e do backup residual;
- suporte padrão;
- preço de implantação e assinatura;
- primeiro segmento usado para piloto.

## 19. Decisão de encerramento da especificação

O VPC Business Start será considerado uma composição da fábrica, não um repositório ou produto técnico isolado. Sales, Service e Complete deverão expandir os mesmos contratos de identidade, clientes, catálogo, usuários e configuração, evitando reconstruções posteriores.

Este documento define o escopo funcional oficial para planejamento. Ele não autoriza implementação até que o manifesto, os limites comerciais e os critérios técnicos da fábrica sejam validados.
