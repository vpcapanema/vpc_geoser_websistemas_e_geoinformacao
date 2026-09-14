# Modelo Funcional Comum Oficial — Plataforma VPC

**Versão:** 1.0  
**Data:** 19 de julho de 2026  
**Estado:** modelo conceitual para validação; implementação não iniciada  
**Escopo inicial:** VPC Business Start  
**Evolução:** Sales, Service, Complete e capacidades Specialized

## Executive Summary

- **As aplicações VPC compartilharão conceitos canônicos.** Empresa, pessoa, cliente, contato, produto, serviço, lead, oportunidade, página, mídia, usuário e permissão deverão manter identidade semântica entre pacotes.
- **Modelo comum não significa banco compartilhado entre clientes.** Cada aplicação continuará isolada; o compartilhamento é de contratos, regras e componentes.
- **Campos customizados não substituirão o núcleo.** Extensões serão permitidas por schema, namespace, tipo e política, preservando atualização e relatórios.
- **O modelo nasce para evolução.** Business Start utilizará um subconjunto; Sales e Service ampliarão as mesmas entidades sem duplicá-las.

## 1. Objetivo

Definir o significado, os relacionamentos, estados, regras e responsabilidades das entidades comuns antes da arquitetura física de banco ou APIs.

## 2. Princípios

1. identificadores estáveis e não significativos;
2. isolamento por `applicationId`;
3. datas e autoria de criação e alteração;
4. arquivamento preferível à exclusão imediata;
5. histórico para mudanças relevantes;
6. dados pessoais minimizados;
7. nomes visíveis customizáveis sem alterar o significado canônico;
8. extensões declarativas;
9. regras no domínio, não apenas na interface;
10. compatibilidade com exportação e migração;
11. permissões por capacidade;
12. anexos referenciados, não embutidos indiscriminadamente.

## 3. Convenções comuns

Entidades persistentes deverão prever, quando aplicável:

- `id`;
- `applicationId`;
- `createdAt`;
- `createdBy`;
- `updatedAt`;
- `updatedBy`;
- `status`;
- `version` para concorrência;
- `archivedAt` e `archivedBy`;
- campos customizados validados;
- classificação de dados;
- referência de origem ou importação.

## 4. Mapa de domínios

```text
Identidade da aplicação
  ├─ Empresa
  ├─ Usuários, perfis e permissões
  └─ Configurações

Conteúdo público
  ├─ Página
  ├─ Seção
  ├─ Mídia
  └─ Menu

Catálogo
  ├─ Categoria
  ├─ Produto
  ├─ Serviço
  └─ Caso ou projeto

Relacionamento
  ├─ Organização ou pessoa
  ├─ Contato
  ├─ Lead
  ├─ Oportunidade
  └─ Interação

Operação futura
  ├─ Proposta
  ├─ Pedido ou contrato
  ├─ Solicitação
  ├─ Ordem de serviço
  └─ Atendimento
```

## 5. Empresa da aplicação

Representa a organização cuja marca e operação são atendidas pela instância.

### Campos conceituais

- nome legal opcional conforme contexto;
- nome de exibição;
- descrição curta e completa;
- documento empresarial protegido quando necessário;
- atividade;
- contatos institucionais;
- endereço;
- canais digitais;
- marca por referências de mídia;
- configurações públicas;
- estado de publicação.

### Regras

- uma empresa principal por aplicação Business V1;
- nome de exibição obrigatório;
- informações privadas separadas das públicas;
- alteração de documento crítico auditada;
- publicação exige contatos e políticas mínimas definidas.

## 6. Parte: organização ou pessoa

Cliente, fornecedor futuro, parceiro e lead convertido podem representar uma organização ou pessoa. O núcleo deverá evitar cadastros incompatíveis duplicados.

### Campos

- tipo: organização ou pessoa;
- nome principal;
- nome de exibição;
- documentos opcionais;
- endereços;
- canais de contato;
- tags homologadas;
- responsável interno;
- estado;
- origem;
- observações controladas.

### Papéis

Uma parte poderá exercer papéis como:

- prospect;
- cliente;
- parceiro;
- fornecedor futuro;
- contato de relacionamento.

Papéis não deverão exigir duplicação do cadastro principal.

## 7. Contato

Representa uma pessoa e seus canais no contexto de uma organização ou relacionamento direto.

### Campos

- nome;
- cargo ou função opcional;
- organização vinculada opcional;
- e-mails;
- telefones;
- canal preferido;
- consentimentos e preferências;
- responsável interno;
- estado.

### Regras

- um canal principal quando disponível;
- e-mail não é identificador definitivo da pessoa;
- duplicidade deve gerar sugestão, não fusão destrutiva automática;
- preferências de comunicação respeitadas;
- dados de formulário não tornam automaticamente o contato um cliente.

## 8. Cliente

Cliente é um papel comercial de uma parte, não uma estrutura paralela desconectada.

### Dados específicos do papel

- data de início;
- estado do relacionamento;
- responsável;
- segmento;
- condições ou observações permitidas;
- origem da conversão;
- referências a oportunidades, vendas e serviços.

### Estados

```text
potential → active → inactive → archived
```

## 9. Lead

Representa uma manifestação ainda não qualificada, geralmente originada em formulário, importação autorizada ou registro interno.

### Campos

- nome informado;
- empresa informada;
- canais;
- assunto;
- mensagem;
- interesse;
- origem;
- consentimentos;
- estado de triagem;
- responsável;
- referência à submissão original;
- possível contato ou parte vinculada.

### Estados

```text
new → reviewing → qualified → converted
                ↘ disqualified
                ↘ duplicate
```

### Regras

- submissão original preservada;
- conversão não apaga o lead;
- duplicidade mantém rastreabilidade;
- desqualificação pode exigir motivo;
- dados maliciosos ou spam são separados da operação legítima.

## 10. Oportunidade

Representa possibilidade comercial qualificada.

### Campos

- título;
- parte ou contato;
- interesse em produto ou serviço;
- origem;
- responsável;
- etapa;
- prioridade;
- valor estimado opcional;
- data prevista opcional;
- próxima ação;
- motivo de perda ou encerramento;
- histórico.

### Workflow básico

```text
new → contacted → qualified → won
                   ↘ lost
```

### Regras

- nomes visíveis customizáveis;
- significado canônico preservado;
- ganho poderá ativar papel de cliente;
- perda exige motivo quando configurado;
- etapa e responsável auditáveis.

## 11. Interação e histórico

Registra acontecimentos relevantes sem misturar tudo em observação livre.

### Tipos

- nota;
- contato realizado;
- mudança de estado;
- tarefa criada ou concluída;
- documento associado;
- mensagem transacional;
- conversão;
- evento de sistema relevante.

### Campos

- tipo;
- data;
- ator;
- entidade-alvo;
- resumo;
- conteúdo permitido;
- referências;
- visibilidade;
- origem automática ou manual.

Logs técnicos e histórico de negócio são conceitos diferentes.

## 12. Categoria

Classifica itens de catálogo e conteúdo.

### Campos

- domínio: produto, serviço, projeto ou outro homologado;
- nome;
- descrição;
- categoria pai opcional dentro do limite;
- ordem;
- estado;
- visibilidade.

### Regras

- ciclos hierárquicos proibidos;
- slug único por domínio quando público;
- categoria arquivada não apaga itens;
- profundidade limitada por produto.

## 13. Produto

Item comercial tangível ou padronizado apresentado pela empresa.

### Campos

- nome;
- código interno opcional;
- categoria;
- resumo e descrição;
- mídia;
- preço público opcional;
- unidade comercial opcional;
- chamada para ação;
- destaque;
- SEO permitido;
- estado de publicação.

### Fora do núcleo V1

- estoque;
- lote;
- tributação;
- variação complexa;
- expedição;
- compra online.

## 14. Serviço

Oferta de atividade, atendimento ou entrega.

### Campos

- nome;
- código opcional;
- categoria;
- resumo e descrição;
- mídia;
- forma de atendimento;
- duração ou faixa opcional;
- preço ou condição pública opcional;
- chamada para ação;
- destaque;
- estado.

### Evolução

Service poderá relacionar serviço a solicitação, agenda e ordem sem recriar o catálogo.

## 15. Caso, projeto ou item de portfólio

### Campos

- título;
- tipo;
- cliente público opcional e autorizado;
- período;
- resumo;
- desafio, solução e resultado;
- mídia;
- produtos ou serviços relacionados;
- ordem e destaque;
- estado.

Nenhuma identificação de cliente será publicada sem autorização aplicável.

## 16. Página

### Campos

- tipo canônico;
- título;
- slug;
- estado;
- seções ordenadas;
- visibilidade;
- publicação;
- metadados permitidos;
- versão de conteúdo.

### Estados

```text
draft → published → archived
```

### Regras

- rotas reservadas;
- página obrigatória protegida;
- slug único;
- publicação validada;
- histórico ou revisão conforme política;
- conteúdo estruturado por componentes homologados.

## 17. Seção de página

### Tipos iniciais

- hero;
- texto;
- destaques;
- produtos;
- serviços;
- casos;
- diferenciais;
- equipe;
- chamada para ação;
- contato;
- perguntas frequentes.

### Campos comuns

- identificador;
- tipo;
- ordem;
- variante homologada;
- conteúdo tipado;
- referências;
- visibilidade;
- configuração responsiva permitida.

HTML ou script arbitrário não integra o conteúdo comum.

## 18. Menu

### Campos

- localização;
- itens ordenados;
- rótulo;
- destino interno ou externo permitido;
- visibilidade;
- abertura;
- hierarquia limitada.

Destinos internos devem referenciar páginas existentes e acessíveis.

## 19. Mídia

### Campos

- referência de armazenamento;
- nome original e nome seguro;
- tipo MIME;
- tamanho;
- dimensões;
- checksum;
- texto alternativo;
- autoria e direito de uso declarados;
- entidade proprietária;
- estado de processamento;
- variantes derivadas;
- classificação de acesso.

### Regras

- validação real de tipo;
- limite por pacote;
- varredura de segurança quando aplicável;
- conteúdo público separado do privado;
- remoção respeita referências;
- URLs temporárias para conteúdo protegido.

## 20. Usuário da aplicação

### Campos

- referência de identidade;
- nome de exibição;
- e-mail verificado;
- estado;
- perfis;
- preferências;
- último acesso;
- convites;
- autenticação administrada pelo serviço apropriado.

### Estados

```text
invited → active → suspended → deactivated
```

Senha, token e segredo não pertencem ao modelo de domínio exposto.

## 21. Perfil e permissão

### Perfis iniciais

- administrador;
- gestor;
- comercial ou atendimento;
- editor de conteúdo.

### Permissões

Deverão seguir capacidades, por exemplo:

- ler, criar, editar, publicar e arquivar conteúdo;
- administrar catálogo;
- ler e gerir leads;
- ler e gerir clientes;
- consultar relatórios;
- exportar;
- administrar usuários;
- administrar configurações.

### Regras

- ao menos um administrador ativo;
- privilégio mínimo;
- separação entre visualizar e administrar;
- alterações críticas auditadas;
- perfis customizados limitados pelas permissões do pacote.

## 22. Documento e anexo

### Campos

- tipo;
- título;
- mídia protegida;
- entidade relacionada;
- versão;
- visibilidade;
- autor;
- datas;
- classificação;
- estado.

Documentos públicos e internos terão políticas distintas.

## 23. Notificação

### Campos

- evento de origem;
- destinatário;
- canal;
- template e versão;
- dados mínimos de renderização;
- estado;
- tentativas;
- resultado;
- referência externa.

### Estados

```text
queued → sent → delivered
   ↘ failed → retrying
```

Conteúdo sensível não deverá aparecer desnecessariamente em notificações.

## 24. Tarefa e agenda

### Campos

- título;
- tipo;
- responsável;
- entidade relacionada;
- início e prazo;
- prioridade;
- estado;
- conclusão;
- lembretes.

### Estados

```text
open → in-progress → completed
  ↘ cancelled
```

Integração com agenda externa será adaptador, não parte do núcleo.

## 25. Entidades futuras de Sales

### Proposta

- cliente e oportunidade;
- itens;
- versão;
- valores;
- validade;
- estado;
- documento gerado;
- aceite.

### Pedido ou contrato simples

- origem da proposta;
- cliente;
- itens;
- condições;
- estado;
- datas;
- documentos.

Essas entidades deverão reutilizar cliente, produto, serviço, usuário, documento e histórico.

## 26. Entidades futuras de Service

### Solicitação

- cliente;
- unidade ou local;
- serviço;
- descrição;
- prioridade;
- anexos;
- estado;
- responsável.

### Ordem de serviço

- origem;
- cliente;
- serviço;
- equipe;
- agenda;
- estados;
- evidências;
- conclusão;
- aceite;
- histórico.

Service deverá estender o núcleo, não criar um segundo cadastro de clientes e serviços.

## 27. Campos customizados

### Tipos permitidos

- texto curto e longo;
- número;
- moeda;
- data;
- booleano;
- seleção;
- referência homologada;
- endereço;
- localização quando autorizada.

### Metadados

- namespace;
- entidade;
- chave;
- rótulo;
- tipo;
- validação;
- obrigatoriedade;
- visibilidade;
- permissões;
- classificação de dado;
- exportação.

### Regras

- limite por pacote;
- chave imutável após uso;
- alteração de tipo exige migração;
- remoção com dados exige tratamento;
- campos não substituem relações essenciais;
- relatórios precisam declarar suporte.

## 28. Deduplicação e identidade

- nenhum campo isolado será universalmente considerado identidade humana;
- documentos poderão ter unicidade contextual quando coletados;
- e-mail e telefone podem mudar;
- sugestões de duplicidade usam múltiplos sinais;
- fusão requer permissão, prévia e histórico;
- referências serão redirecionadas com segurança;
- desfazer fusão deverá ser considerado antes da implementação.

## 29. Arquivamento, exclusão e retenção

- arquivar retira da operação sem apagar histórico;
- exclusão lógica não substitui política de dados;
- exclusão definitiva depende de retenção, vínculos e base aplicável;
- itens referenciados não serão removidos silenciosamente;
- exportação antecede encerramento quando previsto;
- trial segue política própria de 30 dias de recuperação;
- backups residuais seguem política versionada.

## 30. Auditoria

Eventos mínimos:

- login e mudanças críticas de acesso;
- convite e alteração de perfil;
- publicação e arquivamento;
- exportação;
- alteração de empresa e domínio;
- mudança de workflow;
- conversão de lead;
- mudanças comerciais relevantes;
- acesso de suporte;
- encerramento.

Auditoria não deverá registrar senha, token ou conteúdo sensível desnecessário.

## 31. Importação e exportação

### Importação

- arquivo homologado;
- mapeamento de colunas;
- validação antes de aplicar;
- prévia de erros;
- idempotência ou chave de importação;
- relatório de resultado;
- rollback quando possível.

### Exportação

- formato documentado;
- filtros;
- autorização;
- registro de auditoria;
- mascaramento quando necessário;
- arquivos temporários protegidos;
- abrangência compatível com o pacote e a política.

## 32. Eventos de domínio candidatos

- `lead.created`;
- `lead.qualified`;
- `lead.converted`;
- `opportunity.stage.changed`;
- `opportunity.won`;
- `customer.activated`;
- `catalog.item.published`;
- `page.published`;
- `contact.request.received`;
- `user.invited`;
- `user.role.changed`;
- `trial.expiring`;
- `trial.converted`;
- `application.limit.approaching`.

Eventos descrevem fatos; não devem carregar objetos completos ou dados excessivos.

## 33. Critérios de aceite do modelo comum

1. representar integralmente o Business Start;
2. permitir evolução para Sales e Service sem duplicar clientes ou catálogo;
3. separar público e privado;
4. sustentar permissões;
5. sustentar histórico e auditoria;
6. suportar campos customizados controlados;
7. tratar arquivamento e retenção;
8. permitir importação e exportação;
9. representar workflows canônicos;
10. manter isolamento por aplicação;
11. não armazenar segredos;
12. possuir regras de duplicidade e conversão;
13. mapear entidades para módulos do manifesto;
14. permitir testes de invariantes;
15. não depender de banco, ORM ou framework específico.

## 34. Invariantes essenciais

- toda entidade pertence a uma aplicação;
- uma aplicação Business V1 possui uma empresa principal;
- ao menos um administrador permanece ativo;
- oportunidade ganha não perde histórico;
- conversão de lead não apaga a submissão;
- página publicada possui rota válida;
- mídia protegida não recebe URL pública permanente;
- categoria não pode ser ancestral de si mesma;
- campo obrigatório possui valor válido antes da transição aplicável;
- downgrade não deixa dados ativos em estrutura inexistente;
- exclusão respeita retenção e referências;
- segredo não integra entidade de negócio.

## 35. Questões pendentes

- identificadores e estratégia de ordenação;
- granularidade de histórico de conteúdo;
- política de fusão e desfusão;
- entidades de endereço e localização;
- multiempresa futura dentro de uma instância;
- localização e múltiplos idiomas;
- versionamento de documentos comerciais;
- mecanismo de busca;
- taxonomia e tags;
- política de dados pessoais por campo;
- eventos definitivos;
- mapeamento físico e transações.

## 36. Decisão de encerramento

Este modelo encerra a definição funcional comum necessária antes da arquitetura técnica. A próxima etapa poderá escolher fronteiras de serviços, persistência, APIs e tecnologias, mas deverá preservar os significados, invariantes e caminhos de evolução aqui definidos.
