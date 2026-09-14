# Especificação Oficial — Trial VPC Business

**Versão:** 1.0  
**Data:** 19 de julho de 2026  
**Estado:** baseline para validação comercial, jurídica e operacional  
**Primeiro produto:** VPC Business Start  
**Abrangência futura:** Sales, Service e Complete

## Executive Summary

- **O trial inicial terá 14 dias e não exigirá cartão.** Essa é uma hipótese de entrada para reduzir fricção e deverá ser validada contra abuso, custo e conversão.
- **Cada trial será uma aplicação independente.** Ele terá domínio provisório, manifesto próprio, banco isolado, limites reduzidos e administrador definido pelo cliente.
- **A contratação converterá a mesma aplicação.** Identidade, conteúdo e dados compatíveis serão preservados; somente ciclo de vida, plano, limites e módulos serão atualizados.
- **Após a expiração haverá suspensão e recuperação por 30 dias.** Sem contratação ou solicitação válida, a instância seguirá para encerramento e exclusão conforme política comunicada.

## 1. Objetivo

O trial deve permitir que o cliente avalie uma aplicação real da VPC Business, configurada para sua marca e operação básica, sem que a VPC assuma compromisso comercial indefinido ou custo não controlado.

Ele deverá validar simultaneamente:

- proposta de valor;
- configurador;
- manifesto;
- provisionamento;
- primeiro acesso;
- ativação do produto;
- limites;
- suporte inicial;
- conversão;
- suspensão, recuperação e encerramento.

## 2. Baseline comercial do trial

| Item | Baseline V1 |
|---|---|
| Duração | 14 dias corridos |
| Cobrança | gratuita |
| Cartão | não exigido |
| Instância | independente por cliente aprovado |
| Pacote inicial | Business Start |
| Domínio | subdomínio provisório VPC |
| Usuários internos | até 2 |
| Clientes e contatos | até 200 |
| Produtos e serviços | até 25 |
| Leads ou oportunidades | até 50 abertos |
| Submissões públicas | até 100 no período |
| Armazenamento | até 250 MB |
| Integrações pagas | desabilitadas por padrão |
| Notificação | canal transacional básico disponível |
| Recuperação após expiração | 30 dias |
| Conversão | mesma instância |

Esses valores são hipóteses para piloto. Alterações deverão gerar nova versão da política e do preset de trial.

## 3. Elegibilidade

### Elegível

- pessoa capaz de aceitar os termos aplicáveis;
- empresa ou profissional com identificação e contato verificáveis;
- finalidade compatível com o VPC Business;
- configuração coberta pelo pacote de trial;
- aceite das políticas de uso e dados;
- aprovação nos controles básicos de abuso e disponibilidade.

### Não elegível automaticamente

- atividade proibida ou ilegal;
- tentativa de uso para spam, fraude ou coleta abusiva;
- armazenamento de dados altamente sensíveis ou regulados fora do escopo;
- volume incompatível com o trial;
- integração não homologada;
- repetição abusiva de trials;
- necessidade de infraestrutura ou responsabilidade especial;
- segmento que exija análise jurídica ou profissional específica.

### Regra de repetição

O baseline será um trial por cliente ou atividade empresarial em uma janela a definir. E-mail, domínio, documento, telefone e padrões de uso poderão auxiliar a análise, respeitando privacidade e proporcionalidade. Bloqueios automáticos deverão possuir tratamento de falso positivo.

## 4. Jornada de aquisição

```text
Visualização do pacote
        ↓
Escolha de preset
        ↓
Configuração inicial
        ↓
Criação ou acesso à conta VPC
        ↓
Verificação de contato
        ↓
Aceite de termos e políticas
        ↓
Resumo do trial e limites
        ↓
Solicitação
        ↓
Validação automática ou análise excepcional
        ↓
Manifesto aprovado
        ↓
Provisionamento
        ↓
Primeiro acesso guiado
```

Nenhum recurso deverá ser provisionado antes da validação mínima da identidade, aceite e manifesto.

## 5. Dados solicitados na aquisição

### Responsável

- nome;
- e-mail;
- telefone quando necessário;
- senha ou mecanismo de autenticação seguro;
- vínculo declarado com a empresa;
- aceite dos termos.

### Empresa

- nome de exibição;
- tipo de atividade;
- descrição curta;
- país, idioma e fuso;
- canais de contato;
- documento empresarial quando exigido pela política de elegibilidade;
- domínio existente opcional.

### Configuração

- preset;
- nome da aplicação;
- logotipo opcional;
- tema;
- produtos e/ou serviços iniciais, opcionalmente;
- páginas habilitadas;
- domínio provisório desejado;
- administrador inicial.

Somente dados necessários à aquisição serão exigidos. Informações adicionais poderão ser completadas dentro da aplicação.

## 6. Manifesto do trial

O manifesto deverá registrar:

- `offer.line = business`;
- `offer.product = business-start`;
- pacote e versão de trial;
- preset escolhido;
- estágio `trial`;
- início e expiração;
- conversão `preserve-instance`;
- módulos autorizados;
- limites;
- domínio provisório;
- política de retenção;
- política de backup;
- política de exportação;
- referência aos aceites;
- referências seguras das integrações permitidas.

O trial não será identificado apenas por um campo visual. Seu estado deverá governar limites, domínio, integrações e ciclo de vida.

## 7. Provisionamento

### Etapas

1. reservar `applicationId`;
2. validar disponibilidade do subdomínio;
3. gerar configuração resolvida;
4. criar ambiente lógico independente;
5. criar banco isolado;
6. aplicar schema e dados iniciais;
7. aplicar tema e páginas;
8. criar administrador;
9. configurar domínio e certificado;
10. ativar observabilidade e políticas;
11. executar verificações de saúde;
12. marcar o trial como ativo;
13. enviar instruções de primeiro acesso.

### Estados técnicos

```text
queued → preparing → provisioning → verifying → ready
             ↘ failed-recoverable   ↘ failed-final
```

### Falha

- falha não iniciará silenciosamente o período útil;
- o relógio começará quando a aplicação estiver pronta para primeiro acesso;
- tentativas deverão ser idempotentes;
- falhas recuperáveis poderão ser repetidas;
- falha final deverá liberar recursos não utilizados e comunicar o cliente;
- suporte deverá acessar diagnóstico sem expor segredos.

## 8. Ativação e primeiro valor

O trial será considerado ativado quando o administrador:

1. concluir o primeiro acesso;
2. confirmar ou completar os dados da empresa;
3. publicar ou revisar a página inicial;
4. cadastrar ou confirmar pelo menos um produto ou serviço;
5. visualizar a experiência pública;
6. receber ou criar um primeiro contato de teste.

Esses eventos serão usados para medir ativação, não para bloquear o uso legítimo.

## 9. Funcionalidades disponíveis

### Incluídas

- identidade visual dentro dos presets;
- páginas essenciais;
- produtos e serviços;
- contato público;
- leads e oportunidades básicas;
- clientes e contatos;
- dois usuários;
- relatórios mínimos;
- exportação básica;
- ajuda de configuração.

### Limitadas ou desabilitadas

- domínio próprio;
- integrações pagas;
- API pública;
- campos customizados avançados;
- migração assistida;
- notificações de alto volume;
- módulos Sales e Service completos;
- remoção das indicações de trial quando aplicável;
- SLA de produção.

## 10. Uso de dados reais

Dados comerciais comuns poderão ser inseridos após aceite, mas o trial não deverá receber:

- dados clínicos;
- dados financeiros sensíveis;
- credenciais;
- segredos empresariais desnecessários;
- documentos pessoais em massa;
- dados de crianças ou adolescentes sem base e tratamento aprovados;
- categorias especiais de dados pessoais fora do escopo;
- conteúdo ilegal ou sem direito de uso.

A interface deverá orientar o cliente a usar dados fictícios quando a avaliação puder ser realizada sem dados reais.

## 11. Privacidade e segurança

- termos e política identificados por versão;
- consentimentos registrados quando aplicáveis;
- isolamento por aplicação;
- autenticação segura;
- proteção de formulário público;
- limites de taxa e abuso;
- criptografia conforme arquitetura aprovada;
- segredos fora do manifesto;
- logs administrativos relevantes;
- exportação controlada;
- política de retenção comunicada;
- acesso de suporte auditável e limitado.

O trial gratuito não reduz os requisitos mínimos de segurança e privacidade.

## 12. Comunicação do ciclo de vida

### Mensagens mínimas

| Momento | Comunicação |
|---|---|
| Solicitação | recebimento e próximos passos |
| Pronto | acesso, prazo e limites |
| Dia 1 | orientação para ativação, se necessário |
| 7 dias restantes | lembrete, valor obtido e conversão |
| 3 dias restantes | expiração e opções |
| 1 dia restante | aviso final de uso ativo |
| Expiração | suspensão, exportação e recuperação |
| 7 dias após | lembrete de recuperação |
| 23 dias após | aviso de exclusão em 7 dias |
| 30 dias após | encerramento ou exceção formal |

Mensagens deverão respeitar preferências, finalidade transacional e canais disponíveis.

## 13. Expiração e suspensão

Ao fim dos 14 dias:

1. novas alterações serão bloqueadas conforme política;
2. páginas públicas poderão ser substituídas por aviso neutro ou despublicadas;
3. integrações serão suspensas;
4. dados permanecerão preservados durante 30 dias;
5. administrador poderá acessar conversão, exportação e suporte limitado;
6. a aplicação entrará em `trial-expired` e depois `suspended`;
7. a infraestrutura poderá ser reduzida sem impedir recuperação contratada.

A suspensão não equivale a exclusão imediata.

## 14. Recuperação

Durante 30 dias após a expiração, o cliente poderá:

- contratar e reativar;
- solicitar exportação disponível;
- resolver falha de pagamento ou cadastro, quando aplicável;
- solicitar análise excepcional documentada.

A recuperação deverá preservar a aplicação quando tecnicamente possível. Se restauração for necessária, o cliente deverá ser informado.

## 15. Encerramento e exclusão

Após a janela de recuperação, sem contratação ou exceção:

```text
suspended → termination-pending → backup/retention-check
          → resources-removal → data-deletion/anonymization → terminated
```

### Requisitos

- verificar bloqueios jurídicos ou contratuais;
- oferecer avisos previstos;
- registrar a revisão e o motivo;
- revogar credenciais e integrações;
- remover domínio e certificados aplicáveis;
- executar política de dados;
- registrar comprovação técnica de encerramento;
- preservar apenas informações administrativas legalmente necessárias;
- impedir recriação acidental com o mesmo identificador.

Prazos de backup residual deverão ser descritos na política final antes da abertura pública do trial.

## 16. Conversão para contratação

### Princípio

O trial será convertido, não recriado.

### Fluxo

1. cliente escolhe pacote produtivo;
2. sistema apresenta módulos, limites, implantação e cobrança;
3. cliente confirma dados e contrato;
4. pagamento ou autorização aplicável é validado;
5. nova revisão do manifesto é criada;
6. compatibilidade e upgrade são validados;
7. limites produtivos são aplicados;
8. domínio próprio pode ser iniciado;
9. marcação de trial é removida quando prevista;
10. assinatura e ciclo produtivo são ativados;
11. dados e histórico permanecem.

### Garantias

- preservar `applicationId`;
- preservar usuários e permissões compatíveis;
- preservar conteúdo e cadastros;
- não duplicar submissões;
- registrar alteração de plano;
- manter histórico do trial;
- permitir rollback operacional antes da conclusão irreversível;
- não prometer integrações ainda não configuradas.

## 17. Conversão para Sales, Service ou Complete

O upgrade deverá executar análise de compatibilidade:

- módulos a ativar;
- migrações necessárias;
- novos campos e workflows;
- limites;
- usuários;
- integrações;
- conteúdo já existente;
- treinamento e implantação assistida.

O cliente poderá contratar Business Start produtivo primeiro e realizar o upgrade depois. A conversão não deverá forçar o pacote mais amplo.

## 18. Exportação

### Durante o trial ativo

- clientes e contatos permitidos;
- produtos e serviços;
- leads e oportunidades;
- conteúdo textual quando suportado;
- mídia conforme política e direitos;
- resumo da configuração.

### Após expiração

Exportação permanecerá disponível durante a janela de recuperação, sujeita a autenticação, limites e capacidade técnica.

O formato deverá ser documentado. Exportar dados não significa exportar propriedade intelectual da plataforma, código ou componentes VPC.

## 19. Suporte do trial

### Incluído

- orientação de primeiro acesso;
- documentação;
- recuperação de acesso;
- reporte de falha;
- esclarecimento de limites e conversão;
- tratamento de incidentes da plataforma.

### Não incluído

- migração completa;
- treinamento extenso;
- criação integral do conteúdo;
- consultoria empresarial;
- integração;
- desenvolvimento específico;
- suporte operacional contínuo.

Solicitações repetidas de implantação assistida deverão ser encaminhadas a uma oferta comercial.

## 20. Prevenção de abuso

- verificação de e-mail;
- proteção contra automação abusiva;
- limites de taxa;
- controle de volume de formulários;
- análise de repetições;
- bloqueio de conteúdo malicioso;
- suspensão emergencial;
- listas e sinais de risco proporcionais;
- revisão manual para casos legítimos bloqueados;
- proibição de envio massivo não solicitado.

Controles não deverão coletar dados excessivos nem discriminar clientes legítimos sem possibilidade de revisão.

## 21. Indicadores do trial

### Aquisição

- visualizações do pacote;
- início e conclusão da configuração;
- verificação concluída;
- solicitações aprovadas e rejeitadas;
- abandono por etapa.

### Provisionamento

- tempo de fila;
- tempo até aplicação pronta;
- taxa de sucesso;
- falhas por etapa;
- custo inicial por instância.

### Ativação

- primeiro acesso;
- perfil empresarial concluído;
- primeiro item publicado;
- primeira visualização pública;
- primeiro contato de teste ou real;
- tempo até primeiro valor.

### Uso e conversão

- usuários ativos;
- módulos utilizados;
- limites atingidos;
- conversão total e por preset;
- pacote escolhido;
- tempo até conversão;
- pedidos de ajuda;
- motivo de não conversão.

### Operação

- custo do trial;
- suporte por instância;
- abuso;
- exportações;
- recuperações;
- exclusões concluídas.

## 22. Critérios de aceite

O trial estará pronto para piloto quando for possível validar:

1. aquisição sem cartão;
2. verificação e aceite versionado;
3. geração do manifesto;
4. provisionamento independente;
5. início do prazo somente após prontidão;
6. primeiro acesso;
7. aplicação dos limites;
8. uso dos módulos Business Start;
9. avisos de ciclo de vida;
10. expiração automática;
11. suspensão sem perda imediata;
12. exportação;
13. recuperação durante 30 dias;
14. conversão da mesma instância;
15. upgrade de limites e módulos;
16. encerramento controlado;
17. prevenção de duplicidade e abuso;
18. observabilidade e auditoria;
19. ausência de segredos no manifesto;
20. mensuração de custo e conversão.

## 23. Cenários de teste obrigatórios

- trial mínimo válido;
- subdomínio indisponível;
- contato não verificado;
- manifesto inválido;
- falha recuperável de provisionamento;
- falha final sem início do relógio;
- limite de usuário;
- limite de armazenamento;
- formulário sob abuso;
- expiração com usuário ativo;
- exportação antes e depois da expiração;
- conversão no dia 1 e no dia 14;
- conversão durante recuperação;
- upgrade para Sales;
- abandono sem conversão;
- encerramento após 30 dias;
- tentativa de trial repetido;
- falso positivo de bloqueio;
- solicitação com dados não permitidos;
- indisponibilidade de integração opcional.

## 24. Riscos e controles

| Risco | Controle inicial |
|---|---|
| custo excessivo de trials | limites, suspensão, medição e elegibilidade |
| abuso e spam | verificação, rate limit e revisão |
| baixa ativação | onboarding e medição de primeiro valor |
| perda indevida de dados | avisos, recuperação, exportação e política |
| expectativa de serviço completo | escopo e limitações visíveis antes da aquisição |
| conversão tecnicamente frágil | mesma instância, revisão de manifesto e testes |
| dados sensíveis | orientação, termos, bloqueios e escopo |
| suporte inviável | autosserviço, documentação e limites claros |
| criação de recursos órfãos | idempotência e limpeza de falhas |
| trial repetido | sinais proporcionais e análise de elegibilidade |

## 25. Decisões estabelecidas

- duração baseline de 14 dias;
- sem cartão no baseline;
- aplicação independente;
- Business Start como primeiro pacote;
- domínio provisório;
- limites reduzidos;
- integrações pagas desabilitadas;
- dados reais comuns permitidos com orientação;
- conversão da mesma aplicação;
- 30 dias de recuperação;
- exportação durante a recuperação;
- encerramento controlado após a janela.

## 26. Questões pendentes

- meio exato de verificação;
- documento empresarial obrigatório ou baseado em risco;
- início automático ou aprovação manual em quais casos;
- política jurídica final de retenção e backup residual;
- conteúdo visual de marcação do trial;
- canal transacional padrão;
- nível de suporte humano;
- formas de pagamento da conversão;
- política de extensão excepcional;
- países inicialmente aceitos;
- tratamento de domínio próprio comprado durante o trial;
- limites revisados após pilotos.

## 27. Decisão de encerramento

Esta especificação fecha o baseline necessário para projetar o configurador e o ciclo de vida da primeira aplicação. Os parâmetros deverão ser configuráveis por política versionada, evitando valores fixos espalhados pelo código.

O trial somente poderá ser aberto ao público após validação jurídica, segurança, custos, suporte, exportação, conversão e encerramento. Até lá, será conduzido como piloto controlado.
