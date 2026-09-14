# Plano Oficial de Publicação e Infraestrutura — VPC-WEBSISTEMAS E GEOINFORMAÇÃO

**Versão:** 1.0  
**Data:** 03 de setembro de 2026  
**Estado:** vigente; verificações operacionais pendentes

## 1. Endereços

- endereço principal: `https://vpc-websistemas.com.br`;
- `www.vpc-websistemas.com.br` deve redirecionar para o endereço principal;
- DNS administrado na UOL Host.

## 2. Microsoft 365

Registros recuperados do histórico:

- TXT de verificação: host `@`, valor `MS=ms86323721`, TTL `3600`;
- MX: `vpcwebsistemas-com-br0i.mail.protection.outlook.com`, prioridade `0`;
- CNAME `autodiscover` para `autodiscover.outlook.com`;
- SPF: `v=spf1 include:spf.protection.outlook.com -all`.

### Regra crítica

Não apagar nem substituir MX, SPF, autodiscover ou TXT do Microsoft 365. A publicação do site pode acrescentar ou ajustar somente os registros destinados ao domínio raiz e ao `www`, conforme a hospedagem escolhida.

## 3. Verificações antes de alterar DNS

1. consultar o apontamento atual de `@`;
2. consultar o apontamento atual de `www`;
3. identificar hospedagem ou repositório já vinculado;
4. confirmar a configuração exigida pelo provedor de hospedagem;
5. registrar o estado anterior para permitir reversão;
6. verificar que os registros de e-mail permanecerão intactos.

## 4. Repositório e hospedagem

- conta pessoal conhecida: `vpcapanema`;
- ambiente empresarial conhecido: **VPC-WEBSISTEMAS**;
- o repositório específico do site ainda deve ser identificado ou criado;
- não presumir que `sra-pli-3` seja o repositório institucional;
- a hospedagem definitiva ainda deve ser identificada ou configurada.

## 5. Sequência de publicação

1. verificar repositório e hospedagem existentes;
2. criar repositório específico somente se necessário;
3. implementar e validar localmente a página institucional;
4. incorporar ativos visuais aprovados;
5. gerar a versão de produção;
6. publicar na hospedagem selecionada;
7. configurar domínio raiz e `www` sem afetar o Microsoft 365;
8. validar certificado HTTPS;
9. testar desktop, celular, links, metadados e canais de contato;
10. confirmar acesso público pelo endereço final.

## 6. Critério de conclusão

A publicação somente será considerada concluída quando o endereço público responder por HTTPS, o redirecionamento de `www` funcionar, o conteúdo correto estiver visível em computador e celular e os serviços de e-mail permanecerem funcionais.

