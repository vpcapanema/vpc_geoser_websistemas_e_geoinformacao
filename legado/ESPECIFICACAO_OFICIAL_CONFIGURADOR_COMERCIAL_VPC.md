# Especificação Oficial — Configurador Comercial VPC

**Versão:** 1.0  
**Data:** 19 de julho de 2026  
**Estado:** especificação funcional para validação; implementação não iniciada  
**Primeiro fluxo:** VPC Business Start Trial  
**Abrangência futura:** VPC Business e VPC Specialized

## Executive Summary

- **O configurador será a ponte entre catálogo, cliente e fábrica.** Ele coletará escolhas comerciais e funcionais, validará compatibilidade e produzirá um manifesto canônico pronto para aprovação e provisionamento.
- **A primeira versão será progressiva e curta.** O cliente escolherá Business Start, preset, identidade, conteúdo essencial e domínio provisório antes de criar a conta e aceitar o trial.
- **Configuração comercial não será edição de código.** Somente módulos, campos, componentes, temas e regras homologados poderão ser selecionados.
- **Nenhum recurso será criado antes do resumo e do aceite.** Pré-visualização poderá usar configuração temporária; provisionamento exigirá identidade verificada, termos aceitos e manifesto válido.

## 1. Objetivo

Permitir que uma pessoa sem conhecimento técnico configure e solicite uma aplicação independente, entendendo:

- o que está adquirindo;
- o que poderá customizar;
- quais limites se aplicam;
- o que não está incluído;
- quando a aplicação estará pronta;
- como o trial será convertido ou encerrado.

## 2. Princípios de experiência

1. linguagem orientada ao negócio, não à infraestrutura;
2. uma decisão principal por etapa;
3. defaults seguros a partir do preset;
4. possibilidade de voltar sem perder escolhas;
5. salvamento local ou associado à conta conforme estágio;
6. preço e limites visíveis antes do aceite, quando publicados;
7. nenhuma opção incompatível apresentada como válida;
8. resumo legível antes do provisionamento;
9. acessibilidade e uso móvel;
10. complexidade progressiva;
11. customizações assistidas encaminhadas para proposta, não simuladas como automáticas;
12. rastreabilidade entre cada escolha e o manifesto.
13. nenhuma opção comercial poderá tornar um serviço proprietário obrigatório para a operação básica sem indicação explícita e alternativa prevista.

## 3. Jornada V1

```text
Catálogo
  ↓
Business Start
  ↓
Segmento e preset
  ↓
Identidade visual
  ↓
Páginas e portfólio inicial
  ↓
Configuração funcional básica
  ↓
Pré-visualização
  ↓
Conta e verificação
  ↓
Resumo, limites e aceites
  ↓
Manifesto validado
  ↓
Provisionamento
  ↓
Primeiro acesso
```

## 4. Estados da sessão de configuração

```text
anonymous-draft → account-linked → verified → review-ready
                                      ↓
                         validation-required

review-ready → accepted → provisioning-requested → completed
                    ↘ expired-draft            ↘ failed
```

### Regras

- rascunho anônimo não conterá dados sensíveis;
- após identificação, o rascunho será vinculado ao cliente;
- alterações após aceite gerarão novo resumo e novo aceite quando materialmente necessário;
- rascunhos expirarão conforme política comunicada;
- sessões concorrentes deverão detectar conflito de revisão.

## 5. Estrutura comum de cada tela

Cada etapa deverá declarar:

- objetivo;
- informações de apoio;
- campos e componentes;
- obrigatoriedade;
- validações imediatas e finais;
- ações primárias e secundárias;
- mensagens de erro e advertência;
- dados salvos;
- bloco do manifesto afetado;
- evento analítico;
- critério de conclusão.

## 6. Tela 1 — Catálogo

### Objetivo

Apresentar as linhas VPC Business e VPC Specialized sem sugerir que possuem o mesmo processo de aquisição.

### Conteúdo

- proposta da fábrica de aplicações independentes;
- linha Business;
- linha Specialized;
- comparação de complexidade e entrada;
- indicação de trial, demonstração ou piloto;
- acesso a detalhes.

### Ações

- conhecer VPC Business;
- conhecer VPC Specialized;
- continuar configuração existente;
- entrar na conta.

### Saída

- linha selecionada;
- origem da navegação;
- evento `catalog_line_selected`.

### Critério de aceite

O visitante distingue claramente solução empresarial configurável de solução especializada assistida.

## 7. Tela 2 — Comparação VPC Business

### Objetivo

Explicar Start, Sales, Service e Complete e conduzir a primeira versão ao Start.

### Conteúdo

- problema resolvido;
- capacidades principais;
- perfil de cliente;
- limites e adicionais quando aprovados;
- indicação de disponibilidade;
- comparação funcional resumida.

### Ações

- selecionar Business Start;
- solicitar contato sobre Sales, Service ou Complete enquanto não automatizados;
- abrir matriz detalhada.

### Manifesto

- `offer.line`;
- `offer.product`;
- `offer.packageVersion`.

### Eventos

- `package_compared`;
- `package_selected`;
- `assisted_package_contact_requested`.

## 8. Tela 3 — Segmento e preset

### Objetivo

Aplicar defaults de linguagem, módulos, páginas e conteúdo sem criar produto separado.

### Opções V1

- profissional autônomo;
- prestador de serviços;
- consultoria;
- escritório técnico;
- configuração genérica.

### Campos

- preset;
- atividade principal;
- objetivo principal: apresentar, captar contatos, vender ou organizar atendimento;
- possui site atual: sim ou não;
- possui domínio: sim ou não.

### Validações

- preset disponível para o pacote;
- atividade não pertence a categoria bloqueada;
- objetivo compatível com o Start;
- necessidade fora do escopo gera recomendação, não bloqueio silencioso.

### Manifesto

- `offer.edition`;
- defaults candidatos de `navigation`, `modules` e `workflows`.

## 9. Tela 4 — Identidade da empresa

### Campos

- nome de exibição;
- descrição curta;
- logotipo opcional;
- ícone opcional;
- tema preset;
- cores principal, secundária e de destaque;
- tipografia homologada;
- e-mail, telefone e canais públicos;
- cidade e localização pública opcional.

### Validações

- tamanho e formato de textos;
- arquivo, dimensão e tipo da imagem;
- cores válidas e contraste;
- ausência de HTML, script ou CSS arbitrário;
- e-mail e telefone válidos;
- confirmação de direito de uso dos ativos.

### Ações

- usar preset;
- enviar marca;
- restaurar padrão;
- ver prévia rápida.

### Manifesto

- `customer`;
- `branding`;
- ativos temporários posteriormente promovidos a referências definitivas.

## 10. Tela 5 — Domínio provisório

### Campo

- prefixo desejado para o subdomínio de trial.

### Regras

- caracteres permitidos;
- tamanho mínimo e máximo;
- palavras reservadas;
- unicidade;
- prevenção de representação enganosa;
- reserva temporária com expiração;
- domínio próprio apenas como intenção ou adicional futuro.

### Mensagens

- disponível;
- indisponível com sugestões;
- reservado;
- inválido;
- sujeito a confirmação final.

### Manifesto

- `deployment.domain.mode`;
- `deployment.domain.hostname`.

## 11. Tela 6 — Páginas públicas

### Páginas mínimas

- início;
- empresa;
- produtos e/ou serviços;
- contato;
- privacidade.

### Configurações

- habilitar páginas opcionais;
- ordenar itens permitidos do menu;
- escolher blocos homologados da página inicial;
- editar títulos e textos iniciais;
- escolher chamadas para ação;
- configurar rodapé.

### Validações

- páginas obrigatórias preservadas;
- slugs únicos;
- conteúdo mínimo;
- links válidos;
- política de privacidade exigida antes da publicação do formulário;
- componentes compatíveis com o pacote.

### Manifesto

- `navigation.publicPages`;
- `navigation.menu`;
- referências de conteúdo inicial.

## 12. Tela 7 — Portfólio inicial

### Objetivo

Permitir que o trial já demonstre valor sem exigir migração extensa.

### Ações

- escolher produtos, serviços ou ambos;
- criar categorias;
- cadastrar até o limite inicial guiado;
- usar itens demonstrativos claramente identificados;
- importar posteriormente, fora do configurador V1.

### Campos do item

- tipo;
- nome;
- resumo;
- descrição;
- categoria;
- imagem;
- preço público opcional;
- chamada para contato;
- destaque.

### Manifesto e dados

A estrutura e os módulos pertencem ao manifesto. Os itens empresariais são dados iniciais associados ao plano de bootstrap, não conteúdo extenso embutido no manifesto.

## 13. Tela 8 — Contato e oportunidade

### Configurações

- campos públicos permitidos;
- assunto ou interesse;
- mensagem;
- consentimento;
- responsável inicial;
- nomes visíveis dos estados do funil básico;
- canal de notificação disponível.

### Validações

- campos mínimos preservados;
- dados sensíveis não solicitados;
- consentimento quando aplicável;
- workflow canônico válido;
- usuário responsável existente ou default.

### Manifesto

- `modules.basic-crm.config`;
- `dataModel` para campos homologados;
- `workflows`;
- `integrations` quando houver notificação.

## 14. Tela 9 — Usuários e permissões

### V1

- administrador inicial obrigatório;
- segundo usuário opcional;
- perfil predefinido;
- convite enviado após provisionamento ou no primeiro acesso.

### Campos

- nome;
- e-mail;
- perfil;
- estado do convite.

### Validações

- e-mail único na aplicação;
- limite de dois usuários no trial;
- ao menos um administrador;
- permissões dentro do pacote;
- confirmação antes de reduzir privilégios críticos.

### Manifesto

- presets em `roles`;
- usuários iniciais como artefato seguro de bootstrap, não senha no manifesto.

## 15. Tela 10 — Pré-visualização

### Modos

- desktop;
- celular;
- página inicial;
- catálogo;
- detalhe de item;
- formulário de contato.

### Requisitos

- usar a configuração atual sem provisionar ambiente final;
- indicar conteúdo demonstrativo;
- impedir execução real de integração;
- exibir advertências de conteúdo ausente;
- permitir voltar à etapa de origem;
- apresentar contraste e problemas de marca.

### Critério de aceite

O cliente reconhece sua marca, entende as páginas e consegue testar o fluxo público sem confundir prévia com aplicação ativa.

## 16. Tela 11 — Conta e verificação

### Campos

- nome do responsável;
- e-mail;
- telefone quando necessário;
- senha segura ou método de autenticação aprovado;
- vínculo com a empresa;
- documento empresarial quando exigido pela política de risco.

### Ações

- criar conta;
- entrar;
- verificar contato;
- recuperar acesso;
- vincular rascunho anônimo.

### Segurança

- senha nunca integra o manifesto;
- tokens têm prazo e uso único;
- limitação de tentativas;
- prevenção de enumeração de contas;
- rascunho vinculado somente após comprovação adequada.

## 17. Tela 12 — Resumo, limites e aceites

### Resumo visível

- produto e preset;
- módulos;
- domínio provisório;
- identidade;
- páginas;
- usuários;
- duração de 14 dias;
- limites;
- conversão da mesma instância;
- recuperação de 30 dias;
- itens não incluídos;
- tratamento de dados;
- ausência de cartão no baseline.

### Aceites

- termos de uso;
- política de privacidade;
- política do trial;
- responsabilidade pelo conteúdo;
- comunicação transacional;
- confirmação de direitos sobre marca e mídia.

### Regras

- versão de cada documento registrada;
- aceite obrigatório separado quando necessário;
- alteração material invalida o resumo anterior;
- cliente recebe cópia ou acesso durável ao resumo.

## 18. Tela 13 — Validação final

### Validações

- schema;
- compatibilidade de pacote, preset e módulos;
- identidade;
- domínio;
- páginas;
- workflow;
- usuários;
- limites;
- elegibilidade;
- políticas;
- ausência de segredos;
- disponibilidade operacional.

### Saídas

- manifesto resolvido;
- resumo legível;
- plano de bootstrap;
- solicitação de provisionamento;
- lista de advertências;
- decisão automática ou encaminhamento para análise.

Erros deverão apontar a etapa exata e preservar dados válidos.

## 19. Tela 14 — Provisionamento

### Informações

- solicitação recebida;
- validação;
- preparação;
- criação;
- verificação;
- aplicação pronta;
- falha recuperável ou ação necessária.

### Regras de experiência

- não exibir detalhes internos sensíveis;
- permitir sair e acompanhar pela conta;
- notificar quando pronto;
- não iniciar prazo antes da prontidão;
- apresentar suporte quando ultrapassar tempo esperado;
- não criar solicitações duplicadas ao atualizar a página.

## 20. Tela 15 — Aplicação pronta

### Conteúdo

- URL;
- prazo do trial;
- administrador;
- checklist de primeiro valor;
- limites;
- acesso ao painel;
- prévia pública;
- suporte;
- opção de contratar quando disponível.

### Checklist

- completar empresa;
- revisar início;
- publicar produto ou serviço;
- testar contato;
- convidar segundo usuário;
- conhecer conversão e exportação.

## 21. Autosave, retomada e expiração de rascunho

- salvar após etapas e mudanças relevantes;
- indicar estado salvo;
- detectar falha de rede;
- permitir retomada autenticada;
- rascunho anônimo terá duração curta e conteúdo limitado;
- rascunho vinculado terá política comunicada;
- excluir ativos temporários abandonados;
- impedir mistura entre clientes;
- resolver conflito por revisão, nunca por sobrescrita silenciosa.

## 22. Mensagens e erros

### Categorias

- validação de campo;
- incompatibilidade de configuração;
- indisponibilidade temporária;
- elegibilidade;
- falha de upload;
- sessão expirada;
- conflito de revisão;
- provisionamento atrasado;
- falha final.

### Padrão

Toda mensagem deverá informar:

1. o que aconteceu;
2. o que foi preservado;
3. o que o usuário pode fazer;
4. quando procurar suporte;
5. referência de atendimento quando necessária.

## 23. Eventos de mensuração

- `catalog_viewed`;
- `catalog_line_selected`;
- `package_selected`;
- `preset_selected`;
- `branding_completed`;
- `domain_checked`;
- `pages_completed`;
- `portfolio_item_added`;
- `crm_configured`;
- `preview_opened`;
- `account_created`;
- `contact_verified`;
- `summary_viewed`;
- `terms_accepted`;
- `manifest_validation_failed`;
- `trial_requested`;
- `provisioning_started`;
- `provisioning_ready`;
- `first_access_completed`;
- `configuration_abandoned`.

Eventos não deverão registrar conteúdo, senha ou dados pessoais desnecessários.

## 24. Correspondência resumida com o manifesto

| Etapa | Blocos principais |
|---|---|
| Pacote | `offer` |
| Preset | `offer`, defaults de módulos e navegação |
| Empresa | `customer` |
| Marca | `branding` |
| Domínio | `deployment.domain` |
| Páginas | `navigation` |
| Funções | `modules`, `dataModel`, `workflows` |
| Usuários | `roles` e bootstrap seguro |
| Trial | `lifecycle`, `limits`, `policies`, `billing` |
| Provisionamento | `deployment`, `observability` |

## 25. Acessibilidade e responsividade

- navegação por teclado;
- rótulos e instruções associados aos campos;
- mensagens que não dependem apenas de cor;
- contraste validado;
- foco preservado em erros;
- progresso compreensível;
- prévia móvel sem bloquear a configuração;
- uploads utilizáveis em dispositivos móveis;
- linguagem clara;
- confirmação antes de ações irreversíveis.

## 26. Critérios de aceite V1

1. selecionar Business Start;
2. aplicar preset;
3. configurar marca válida;
4. reservar domínio provisório;
5. configurar páginas mínimas;
6. inserir portfólio inicial;
7. configurar contato e funil básico;
8. criar administrador;
9. visualizar desktop e celular;
10. criar ou vincular conta;
11. verificar contato;
12. visualizar resumo e limites;
13. registrar aceites versionados;
14. gerar manifesto válido;
15. tratar erros por etapa;
16. solicitar provisionamento sem duplicidade;
17. acompanhar progresso;
18. receber URL e primeiro acesso;
19. medir abandono e ativação;
20. retomar rascunho sem perda indevida.

## 27. Fora do escopo V1

- configurador completo de Sales, Service e Complete;
- preço dinâmico complexo;
- provisionamento automático de Specialized;
- construtor livre de páginas;
- edição arbitrária de workflow;
- marketplace de extensões;
- múltiplos idiomas por aplicação;
- compra de domínio dentro do fluxo;
- migração completa de site anterior;
- integração paga durante o trial.

## 28. Questões pendentes

- identidade visual final do configurador;
- nível de conteúdo solicitado antes do trial;
- política exata de rascunho;
- documento empresarial baseado em risco;
- ferramenta de pré-visualização;
- prazo operacional esperado de provisionamento;
- revisão manual em quais segmentos;
- primeira edição setorial;
- testes de usabilidade com clientes;
- textos jurídicos finais.

## 29. Decisão de encerramento

O configurador V1 deverá produzir um manifesto Business Start válido e uma solicitação idempotente de trial. Ele não executará customização fora do catálogo nem esconderá itens assistidos como se fossem automáticos.

Esta especificação encerra o fluxo funcional necessário para projetar a interface, mas não autoriza implementação antes da arquitetura técnica, dos schemas executáveis e dos textos jurídicos.
