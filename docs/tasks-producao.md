# Task de publicação do repositório principal

Use **Terminal > Executar Tarefa > VPC principal: publicar producao**.

Este repositório contém documentação e a referência Git da aplicação `site/`.
Não possui um servidor de aplicação separado. Sua task publica o site existente
em `https://vpc-websistemas.com.br` e mantém os dois históricos sincronizados.

1. Commita primeiro o site e depois as alterações do repositório principal.
2. Sincroniza o upstream do site; se o SHA mudar por fast-forward, atualiza
   a referência `site` no pai, sincroniza o pai e confere a correspondência.
3. Publica o SHA do site via Codex CLI e conector Sites.
4. Confere a disponibilidade HTTPS e o redirecionamento de `www`.
5. Abre a página inicial no navegador padrão do Windows.

O fluxo mostra cada microoperação no terminal dedicado. Verde indica sucesso,
amarelo indica execução/atenção e vermelho indica erro. Ao falhar, para e mostra
o resumo; não continua para o navegador. `desktop.ini` e `tmp/` são ignorados.

Os requisitos e as verificações do adaptador Sites estão em
[site/docs/tasks-producao.md](../site/docs/tasks-producao.md). O plugin precisa
estar habilitado no Codex CLI autenticado. A task exige um comprovante nativo
de publicação bem-sucedida; uma resposta HTTP 200 isolada não prova novo deploy.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/publish-production.ps1 -DryRun
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/publish-production.ps1 -CheckOnly
```

O modo de simulação não commita, sincroniza, publica ou abre navegador.
`CheckOnly` testa somente a disponibilidade pública; não publica alterações.

## Mensagem autom?tica de commit

A task n?o solicita texto manual. Depois de preparar o stage, gera uma mensagem
exclusiva desse reposit?rio com os arquivos adicionados, alterados, removidos ou
renomeados e as estat?sticas reais do diff. O terminal mostra a mensagem antes
do commit. O corpo detalha os arquivos e mudan?as de estrutura/permiss?es, sem
inventar inten??o funcional. A gera??o ? local e n?o depende de IA.

Sem altera??es no stage, nenhum commit ? criado. Na task VPC principal, site
e reposit?rio pai recebem mensagens independentes, inclusive quando a refer?ncia
Git do site ? atualizada ap?s a sincroniza??o.
