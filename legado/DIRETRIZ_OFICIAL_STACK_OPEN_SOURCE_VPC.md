# Diretriz Oficial — Stack Open Source VPC

**Versão:** 1.0  
**Data:** 19 de julho de 2026  
**Estado:** obrigatória para arquitetura, seleção tecnológica e desenvolvimento  
**Abrangência:** site VPC-GEOSER, plano de controle, configurador, fábrica e aplicações geradas para clientes

## 1. Decisão obrigatória

Toda a stack principal de software utilizada pela VPC-GEOSER deverá adotar tecnologias open source.

Essa regra se aplica a:

- site institucional e comercial da empresa;
- catálogo e configurador;
- autenticação e autorização;
- plano de controle;
- manifesto e validação;
- gerador e provisionador;
- aplicações VPC Business;
- aplicações VPC Specialized;
- front-end e back-end;
- bancos de dados e mecanismos de busca;
- filas, cache e armazenamento compatível;
- componentes geoespaciais;
- analytics e relatórios;
- observabilidade;
- testes, build e automação;
- infraestrutura como código;
- ferramentas necessárias à operação do produto.

## 2. Significado de open source para a VPC

Uma tecnologia somente poderá ser tratada como open source quando:

1. seu código-fonte estiver disponível;
2. possuir licença open source identificável;
3. permitir uso comercial;
4. permitir execução e operação pela VPC ou pelo cliente;
5. não exigir um serviço proprietário para executar funções essenciais;
6. possuir condições de redistribuição e modificação compatíveis com o produto;
7. passar por análise de licença, segurança e manutenção.

“Gratuito”, “free tier”, “source available” ou “possui SDK aberto” não são equivalentes a open source.

## 3. Independência obrigatória

A arquitetura deverá evitar dependência obrigatória de:

- banco proprietário;
- plataforma low-code fechada;
- autenticação exclusivamente proprietária;
- mapas ou GIS exclusivamente proprietários;
- BI proprietário obrigatório;
- runtime proprietário sem alternativa operacional;
- API comercial externa necessária ao funcionamento básico;
- formato de dados fechado;
- mecanismo de hospedagem que impeça migração;
- componentes cuja licença não permita o modelo comercial da VPC.

Cada aplicação deverá poder ser implantada e operada com uma composição integralmente open source.

## 4. Serviços externos proprietários

Serviços proprietários poderão existir apenas quando forem:

- opcionais;
- explicitamente escolhidos ou aceitos pelo cliente;
- isolados por adaptadores;
- substituíveis por alternativa open source ou outro provedor;
- precificados separadamente quando houver consumo;
- incapazes de bloquear a operação básica da aplicação após sua remoção, salvo funcionalidade opcional claramente dependente.

Exemplos possíveis: pagamento, assinatura eletrônica, mensageria, e-mail, mapas premium ou dados comerciais. A integração não transforma o serviço externo em parte obrigatória da stack VPC.

## 5. Licenças

Toda dependência deverá possuir registro de:

- nome e versão;
- repositório oficial;
- licença;
- autor ou organização responsável;
- uso dentro da plataforma;
- forma de distribuição;
- obrigações de atribuição;
- riscos de copyleft;
- política de atualização;
- vulnerabilidades conhecidas relevantes.

Licenças permissivas, copyleft e copyleft de rede deverão ser avaliadas de acordo com a forma de uso e distribuição. Nenhuma biblioteca será aprovada apenas por ser popular.

## 6. Catálogo tecnológico

Antes da implementação, deverá existir um catálogo tecnológico aprovado contendo, para cada camada:

- alternativas avaliadas;
- licença;
- maturidade;
- comunidade;
- segurança;
- portabilidade;
- custo operacional;
- compatibilidade com aplicações independentes;
- justificativa da escolha;
- plano de substituição.

## 7. Dados e portabilidade

- formatos de exportação deverão ser abertos e documentados;
- dados do cliente não poderão ficar presos a formato proprietário;
- APIs deverão usar padrões documentados;
- componentes geoespaciais deverão priorizar padrões abertos;
- backups deverão ser restauráveis sem dependência exclusiva do fornecedor original;
- migração entre ambientes deverá ser prevista;
- o manifesto não deverá incluir detalhes que impeçam troca de provedor.

## 8. Critério de aceite arquitetural

Uma arquitetura somente poderá ser aprovada quando demonstrar:

1. licença open source de cada componente central;
2. funcionamento básico sem serviço proprietário obrigatório;
3. possibilidade de implantação independente;
4. exportação em formatos abertos;
5. substituição de integrações externas por adaptadores;
6. ausência de lock-in tecnológico injustificado;
7. inventário de dependências e licenças;
8. procedimento de atualização e correção de vulnerabilidades;
9. compatibilidade com o modelo comercial da VPC;
10. preservação das obrigações de autoria e licença.

## 9. Exceções

Qualquer exceção deverá:

- ser solicitada formalmente;
- identificar a funcionalidade;
- comprovar inexistência ou inadequação das alternativas open source;
- limitar escopo e duração;
- possuir plano de substituição;
- ser registrada no manifesto ou contrato quando afetar o cliente;
- nunca redefinir silenciosamente a stack principal.

## 10. Decisão de encerramento

A próxima etapa de arquitetura técnica deverá selecionar exclusivamente tecnologias compatíveis com esta diretriz. Nenhuma escolha técnica proprietária poderá ser tratada como padrão obrigatório do site, da fábrica ou das aplicações dos clientes.
