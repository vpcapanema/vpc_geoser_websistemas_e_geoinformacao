# Regras obrigatórias — VPC-WEBSISTEMAS E GEOINFORMAÇÃO

Estas regras se aplicam a todo o repositório. Nenhum agente deve implementar, publicar ou alterar materiais institucionais sem observá-las.

## Fontes de autoridade

Antes de implementar, ler:

1. `CONTEXTO_CODEX_VPC_WEBSISTEMAS.md`;
2. `IDENTIDADE_INSTITUCIONAL_OFICIAL_VPC.md`;
3. `DIRETRIZES_ENGENHARIA_OFICIAL_VPC.md`;
4. `ESPECIFICACAO_SITE_INSTITUCIONAL_OFICIAL_VPC.md`;
5. `PLANO_PUBLICACAO_E_INFRAESTRUTURA_OFICIAL_VPC.md` quando houver publicação ou infraestrutura.

Em caso de divergência, prevalecem as decisões mais recentes e explícitas do usuário. Conteúdo em `legado/` e `documentacao/adiado/` não é fonte ativa e só pode ser usado quando o usuário solicitar sua retomada.

## Posicionamento institucional

- A VPC desenvolve soluções digitais e geotecnológicas sob medida para cada cliente.
- Não apresentar a empresa como fábrica de software, catálogo de produtos ou fornecedora de pacotes fechados.
- WebGIS, dashboards, sistemas corporativos, processamento geoespacial, integrações e automações são capacidades aplicadas conforme cada problema.
- A comunicação deve partir do entendimento do contexto, desenho da solução, desenvolvimento, integração, implantação e evolução.
- Não inventar clientes, projetos, tecnologias, métricas, resultados, depoimentos, certificações, parcerias ou integrações.
- Separar fatos comprovados, decisões aprovadas e pendências de confirmação.

## Identidade imutável

- Nome oficial: `VPC-WEBSISTEMAS E GEOINFORMAÇÃO`.
- Razão social: `Vinicius do Prado Capanema Ltda.`.
- CNPJ: `57.286.005/0001-40`.
- Slogan exato: `Inteligência em geoprocessamento e sensoriamento remoto.`
- `VPC-GEOSER` é nome histórico e não pode aparecer como denominação atual.
- O satélite é o símbolo principal. O monitor é secundário e não substitui a assinatura institucional.
- É proibido redesenhar, reinterpretar ou gerar por IA uma nova versão da marca.
- Derivações devem partir exclusivamente da matriz aprovada em `assets/identidade-visual/simbolo-vpc-satelite-transparente.png` e do tratamento técnico já existente.
- Não alterar nome, slogan, cores, proporções ou composição da assinatura sem autorização explícita.
- Nas logos e assinaturas institucionais, usar Exo 2: peso 600 no nome e 400 no slogan, conforme escolha aprovada em 06/09/2026. Usar a fonte local em `assets/identidade-visual/tipografia/exo-2/`; nos SVGs, converter os textos em contornos para preservar a aparência. Arial, Helvetica ou `sans-serif` continuam válidos para textos corridos fora da marca.
- Todo novo ativo visual institucional deve ser conferido contra a matriz aprovada antes de ser incorporado.

## Implementação

- Preferir soluções abertas, simples, portáveis e fáceis de manter.
- Preservar modularidade, baixo acoplamento, segurança, acessibilidade, desempenho e testabilidade.
- Não adicionar back-end, banco de dados, autenticação, framework ou dependência sem necessidade demonstrada.
- Aplicar geoinformação como capacidade nativa quando houver dimensão espacial relevante.
- Não alegar uso comprovado de tecnologia sem evidência documental.
- Não publicar preços, SLA, promessas comerciais ou funcionalidades futuras como se estivessem disponíveis.
- Não expor documentos internos, informações sensíveis ou marcas de clientes sem autorização.

## Site institucional

- A primeira versão é uma página única, responsiva, leve e sem back-end.
- A narrativa deve destacar soluções sob medida, não produtos prontos.
- Manter conteúdo técnico, específico e verificável, sem frases promocionais vazias.
- Usar HTML semântico, navegação por teclado, foco visível, contraste suficiente e texto alternativo adequado.
- Configurar título, descrição, favicon e metadados de compartilhamento sem inventar imagens ou informações.
- Não publicar e-mail, telefone, LinkedIn, GitHub ou outro canal sem confirmação ou validação.
- Não considerar a entrega concluída sem testar build, links, desktop e celular.

### Estado visual aprovado e invariantes de implementação

- Preservar o zebrado azul e branco entre as seções.
- Em `Experiências relacionadas` e `Produtos em atividade`, toda a área de cada card é um link. Não aninhar um link menor dentro de um card apenas informativo.
- Esses cards-botão não podem exibir numeração, classificação, seta, botão ou outro elemento no canto superior direito.
- Nos cards-botão, ícone e título formam um único grupo centralizado.
- `Soluções sob medida` não é uma grade de cards. É um grafo informativo com `Soluções inteligentes` no núcleo e as capacidades conectadas ao redor.
- Exclusivamente no grafo de `Soluções sob medida`, o ícone deve ficar na mesma linha, imediatamente ao lado do título.
- A VPC-ITA é tratada no feminino. Usar `a VPC-ITA`, nunca `o VPC-ITA`.
- Nome aprovado: `VPC-ITA — Inteligência Territorial e Auditoria Ambiental`.
- Chamada aprovada: `Conheça antes, decida depois.`
- Usar `imóvel rural` como expressão fundiária abrangente; não usar `propriedade` como sinônimo geral.
- O bloco da VPC-ITA deve seguir o padrão da página, preservar o zebrado e ser integralmente clicável para `/ita`.
- O card tipográfico do PLI-SP 2050 usa as cores oficiais azul `#1C3D59` e verde `#00B86E`; não inventar logotipo.
- Os rodapés de `/` e `/ita` devem compartilhar conteúdo, estrutura, alinhamento e altura.
- No rodapé, as duas linhas da assinatura ficam alinhadas à direita ao lado do símbolo; o conjunto símbolo mais textos fica centralizado.
- O rodapé é compacto. Não aumentar sua altura ou seus espaçamentos sem autorização explícita.
- `Voltar ao início` fica na seção `Contato comercial`, no canto inferior direito, fora do rodapé.
- Não modificar conteúdo ou seção que o usuário não tenha colocado no escopo da solicitação.
- Validação visual é obrigatória. `lint` e `build` não substituem inspeção real das áreas alteradas em desktop e celular.

### Padrão estrutural dos cards de conteúdo

Referência de implementação: a seção `Uma leitura integrada do imóvel rural`, em `/ita`, com `.ita-investigation-grid` e `.ita-investigation-card`. Todo card informativo novo segue essa estrutura, salvo pedido explícito do usuário em contrário.

Estrutura da marcação:

```html
<article class="...-card">
  <div class="card-title-group">
    <svg />
    <h3>Título</h3>
  </div>
  <p>Texto de apoio</p>
</article>
```

Regras:

- Ícone e título formam um grupo único, empilhados e centralizados, com o ícone acima do título. Não separar os dois em elementos irmãos soltos.
- O ícone tem medida fixa, não proporcional à fonte, e traço fino. Referência: 26px e `stroke-width:1.7`.
- O título é centralizado.
- O texto de apoio é justificado, com hifenização e sem margem própria. É o único elemento que não é centralizado.
- Todos os cards da mesma grade têm altura mínima igual, para a linha fechar na mesma altura independentemente do comprimento do texto.
- A separação entre cards vem do vão da grade: espaçamento de 1px sobre fundo na cor da linha, com fundo próprio em cada card. Não usar borda por card, que produz linha dupla entre vizinhos.
- A grade reduz o número de colunas por faixa de largura até chegar a uma coluna no celular.
- Nada é posicionado no canto superior direito do card. Numeração, seta ou selo exigem autorização explícita.

## Publicação e infraestrutura

- Não alterar DNS sem registrar e conferir o estado anterior.
- Nunca apagar ou substituir MX, SPF, `autodiscover` ou TXT do Microsoft 365.
- Não presumir repositório, hospedagem ou estado de publicação.
- Não declarar publicação concluída sem HTTPS, domínio raiz, redirecionamento de `www`, conteúdo e e-mail validados.

## Controle documental

- Não usar arquivos de `legado/` como especificação vigente.
- Não reintroduzir a candidatura adiada no contexto, no site ou no planejamento sem solicitação explícita do usuário.
- Após mudanças estruturais, regenerar `ARVORE_COMPLETA_REPOSITORIO.md`.


<!-- BEGIN AWS Agent Toolkit rules -->
# AWS Guidance for the new AWS experience

This user has signed up for the new AWS experience. This experience lets you sign into AWS using a social provider and requires the following additional context.

Where this guidance conflicts with the project's own instructions, the project's instructions take precedence.

## Context

### Terminology:

- Say "project" instead of "account" — a project contains an AWS account and settings for sharing with other collaborators
- Say "team member" instead of "IAM user" — users are invited by email, not created or federated in IAM
- Say "AWS Settings" when referring to management tasks at [settings.aws.com](https://settings.aws.com/) (project management, billing, team members, spend limits). Users view their actual AWS resources in the AWS Management Console.
- Say "selected Region" when referring to the user's Region — not "home Region"
- The user has a managed IAM experience. This includes a managed service control policies (SCP) and resource control policies (RCP) that govern the use of AWS. They will still need to use IAM to create policies to let services work with each other. If there are questions about the SCPs or RCPs, go to the documentation at https://docs.aws.amazon.com/accounts/latest/reference/scps-and-rcps-for-projects.html

### Constraints:

- All projects share a single AWS Region determined by the user's contact address. Resources cannot be created in other Regions
- When developing:
  - MUST create all Regional resources in the project's assigned Region
  - You CAN create S3, Kinesis, Cloudwatch Logs, Cloudwatch metrics resources in us-east-1 when there are global resources (like a global WAF instance) that require a connection to dependencies in us-east-1. You should not use these for any other reason, because resources in the selected Region will provide lower cost (due to no cross-Region traffic), increased availability (due to no cross-Region traffic), and easier manageability (due to not needing to look in another Region). When you need to do an inventory of resources, you need to look in both the selected Region and us-east-1 for S3, Kinesis, Cloudwatch Logs, Cloudwatch metrics resources.
  - MUST NOT attempt to create Lambda, API Gateway, or other Regional resources in any other Region
  - MUST direct users to confirm their Region in AWS Settings > View all projects > Overview > Additional Info > Region. If the user cannot confirm their Region, check in ~/.aws/config
  - MUST NOT use Lambda@Edge — excluded from both Lambda and CloudFront
  - MUST NOT use CloudFormation StackSets — no multi-account or multi-Region deployments
  - MUST NOT attempt cross-Region actions — no cross-Region replication for DynamoDB/S3/RDS, no multi-Region KMS keys
  - MUST NOT use Route 53 cross-Region routing — geolocation, latency-based, and failover routing policies are not available
  - CloudFront is a global service and its actions ARE allowed in `us-east-1`. A user can create a CloudFront distribution pointing to their project-region Lambda function URL or API Gateway. However, Lambda and API Gateway themselves MUST NOT be created in `us-east-1` — they must be in the project Region.
  - Reduced availability in `eu-north-1` specifically: Amazon Rekognition, Amazon Textract, Amazon Personalize, AWS App Runner are not available in that Region.
- IAM permissions for human access are managed by AWS. Don't assign roles to team members unless absolutely necessary
- The user may have a spend limit if they are on the paid plan. The limit that pauses their project if it's exceeded. If resources suddenly become inaccessible, ask if they have a spend limit configured. Only project owners can modify a spend limit.
- When developing:
  - MUST ask about spend limit status if the user reports sudden "Access Denied" errors on operations that previously worked
  - MUST direct users to check spend status in AWS Settings > Billing
  - MUST check if a user has upgraded their account to the paid plan
  - MUST ask the user if they want to clean up the successfully created resources or keep them to reduce cost
- The user sets up billing, creates spend limits, and retrieves and pays invoices in AWS Settings. The user creates budgets and optimizes their costs in the AWS Billing and Cost Management console
- Not all AWS services are available. If a service isn't working, do the following:
  1. Run the command `aws freetier get-account-plan-state`
  2. If accountPlanType": "FREE", check the [Free Tier supported services list](https://docs.aws.amazon.com/accounts/latest/reference/supported-services-sign-up-new.html#supported-services-free-tier) next,
  3. If accountPlanType": "PAID", check the [Paid Tier supported services list](https://docs.aws.amazon.com/accounts/latest/reference/supported-services-sign-up-new.html#supported-services-paid-plan).
  4. If neither list shows the service, check the [Not supported for this experience list](https://docs.aws.amazon.com/accounts/latest/reference/supported-services-sign-up-new.html#unsupported-services). The user will need to activate advanced features to access this service.
- Users can activate advanced AWS services and capabilities for their account.
- Before starting a task, check whether a relevant AWS skill is available. Load the skill with retrieve_skill and prefer its guidance over general knowledge.

### Help level

- help_level (required): LOW, MEDIUM, or HIGH. While a user is building, you MUST ask the user: "How much guidance would you like from me? Low (I only flag security risks), medium (I ask a couple of clarifying questions if something seems off), or high (I explain what I'm doing, suggest alternatives, and flag best practices)."

You CAN update this rule file to save a user's help_level.

Constraints for each level:

**LOW:**

- MUST follow all constraints in this context file
- MUST execute the user’s request without modification
- MUST NOT ask clarifying questions unless the action would create a security vulnerability
- MUST NOT suggest alternatives or improvements

**MEDIUM:**

- MUST execute the user's request
- MAY ask up to two clarifying questions per task if the request has an ambiguity or a potential issue
- MUST NOT repeat a question or suggestion the user has already dismissed
- MUST NOT explain trade-offs or alternatives unless the user asks

**HIGH:**

- MUST explain what each step does and why before executing it
- MUST suggest alternatives when a better approach exists
- MUST flag best practices and explain trade-offs
- MUST still execute the user's choice if they disagree with a suggestion
<!-- END AWS Agent Toolkit rules -->
