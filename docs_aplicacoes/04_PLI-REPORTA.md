# PLI Reporta

**Reporte cidadão de ocorrências viárias**

> Quem passa pela via vê o problema antes de qualquer sensor.

---

## O problema

O cidadão que passa pela rodovia às 6h20 sabe do bloqueio horas antes de qualquer sistema oficial. Essa informação existe, é gratuita e chega rápido — mas quase nunca é aproveitada.

O motivo é legítimo: relato solto não é confiável o bastante para acionar operação. Não se desvia comboio, não se aciona equipe, não se altera rota com base em uma mensagem anônima que pode ser engano, duplicata ou má-fé.

O canal de reporte cidadão costuma virar caixa de reclamação: entra muito, sai pouco, ninguém confia no que está lá dentro.

## O que é

O PLI Reporta é um aplicativo de campo que transforma relato cidadão em **camada operacional de incidentes verificados**, com um mecanismo explícito de qualificação. A unidade de trabalho não é o formulário respondido: é o **incidente geoespacial verificável**.

## Dois scores, deliberadamente separados

Cada reporte recebe duas notas independentes e ortogonais:

**Veracidade** — *isto é real?*
**Relevância** — *isto importa para a operação?*

A separação é proposital, e é o núcleo do método. Um buraco pequeno em via sem volume é **verdadeiro** e **irrelevante**. Uma denúncia de bloqueio em corredor estratégico é **muito relevante** mesmo com confiança individual moderada, até que a reconfirmação chegue.

Sistemas que colapsam as duas coisas em um único "nível de confiança" erram nas duas pontas: descartam o que importa e promovem o que não importa.

Das duas notas deriva a **prioridade**: quão rápido aquilo precisa refletir na operação.

## Ciclo de vida auditável

Todo incidente percorre estados declarados:

`submetido → triado → validado → publicado → expirado ou resolvido`

**Toda decisão automática registra os sinais que a produziram.** Não há caixa-preta: é possível reconstituir por que um reporte subiu ou caiu.

## O compromisso com quem reporta

O sistema assume um princípio explícito: **o usuário tem direito de saber por que seu reporte foi aceito, modificado ou descartado.**

Não é cortesia. É o que sustenta a participação ao longo do tempo — canal que engole relato sem devolver resposta morre em poucas semanas.

## Feito para o campo

Aplicação web progressiva, desenhada para celular. O fluxo de captura é curto e guiado: escolher o tipo, descrever, fotografar, confirmar gravidade e enviar.

Duas naturezas de registro:

- **Evento de tráfego** — buraco, alagamento, acidente, bloqueio, obra, sinalização
- **Manifestação cidadã** — elogio, sugestão ou reclamação

Com **funcionamento offline**: sem conexão, o envio é salvo no aparelho e transmitido automaticamente em segundo plano quando a internet volta. Quem está na estrada raramente está com sinal bom.

Cada reporte recebe um número de referência para acompanhamento.

## Feito para integrar

O sistema expõe um **feed geoespacial estável e público** com os incidentes já publicados. É por ele que o roteirizador do ecossistema consome as ocorrências verificadas para recalcular rotas.

A arquitetura é deliberadamente desacoplada: **o cálculo de rota é cliente do feed e não conhece a origem do dado**. O Reporta pode ser trocado, ampliado ou substituído sem que nada mais precise ser reescrito.

Além do feed, há mapa público para consulta livre e área restrita para moderação e gestão.

## Para quem

Órgãos rodoviários e de trânsito, concessionárias, defesa civil, prefeituras e secretarias de mobilidade — qualquer operação que se beneficie de informação de campo em tempo quase real e que precise de um filtro confiável antes de agir sobre ela.

## Base técnica

FastAPI e Python · aplicação web progressiva com service worker, cache offline e sincronização em segundo plano · MapLibre GL · tratamento de imagem com leitura de metadados EXIF · ancoragem à malha viária e deduplicação de reportes próximos · banco relacional com migrações versionadas · endpoint GeoJSON estável para integração · Docker.

## Fundamento científico

**Veracidade como soma ponderada de sinais independentes.**

```text
V = Σ (wᵢ · sᵢ) / Σ wᵢ,   sᵢ ∈ [0,1],   Σ wᵢ = 1
```

Sete sinais, cada um com peso justificado e função de resposta em degraus explícitos:

| Sinal | Critério | Peso |
|---|---|---|
| GPS do navegador | acurácia < 50 m → 1,0; < 200 m → 0,5 | 0,20 |
| Captura no aplicativo | câmera nativa com nonce validado no servidor → 1,0; galeria → 0,4 | 0,20 |
| Coerência EXIF | GPS coerente (Δ < 100 m) e timestamp (Δ < 5 min) → 1,0 | 0,15 |
| Integridade da imagem | análise de nível de erro (ELA) + software declarado no EXIF | 0,15 |
| Ancoragem à malha | distância à via navegável < 30 m → 1,0; > 200 m → 0,0 | 0,10 |
| Reputação do contribuinte | histórico normalizado | 0,10 |
| Plausibilidade temporal | envio em até 30 min da captura → 1,0; > 24 h → 0,2 | 0,10 |

Duas decisões metodológicas merecem destaque. A **ausência de EXIF não é punida — a incoerência é**: arquivo sem metadado recebe valor neutro, arquivo com metadado contraditório é penalizado. E o **GPS do navegador pesa mais que o EXIF**, porque é coletado pelo próprio código no momento do envio, enquanto EXIF é trivialmente forjável.

A **análise de nível de erro** aplica técnica de forense de imagem digital para detectar recompressão localizada, indício de edição.

**Relevância como produto de fatores multiplicativos.**

```text
R = R_severidade · R_confirmação · R_persistência · R_afetação
```

- **Confirmação independente** segue curva de saturação exponencial sobre o número de contribuintes distintos em um mesmo agrupamento espaço-temporal (raio de 80 m, janela por categoria):
  `R_conf = 0,5 + 0,5·(1 − e^(−k·n))`, com k = 0,6. Dois relatos elevam de 0,50 para 0,65; dez chegam a 0,99. A forma da curva reflete o valor marginal decrescente de cada confirmação adicional.
- **Persistência** decai exponencialmente com o tempo, normalizada pelo tempo de vida da categoria: `R_pers = e^(−idade/TTL)`. Abaixo de 0,1 o incidente expira. Nova confirmação zera o relógio. Buraco vive 90 dias; lentidão vive 1 hora.
- **Afetação viária** pondera pela hierarquia funcional da via na classificação da base cartográfica aberta, de via expressa (1,00) a via de serviço (0,15).

**Prioridade e efeito no grafo.** `P = V · R`, aplicada como penalização multiplicativa sobre o custo da aresta:

```text
w' = w · (1 + α · max(Pᵢ)),   α = 3,0
```

Duas escolhas justificadas no próprio documento metodológico:

- **máximo, não soma** — porque a aresta tem o pior problema reportado, não a média deles; e porque somar é vulnerável a inflação por relatos repetidos no mesmo ponto.
- **multiplicativo, não aditivo** — porque preserva a escala original do custo e permite explicar o desvio ao usuário em linguagem direta: *"o trecho está três vezes mais custoso"*.

Bloqueio total é tratado fora do modelo contínuo: acima de prioridade 0,80, a aresta é removida do grafo durante o cálculo.

**Portões de decisão automatizada.** Limiares configuráveis separam descarte automático, moderação humana e validação automática — com a faixa intermediária reservada explicitamente ao julgamento humano, em vez de forçar decisão binária.

---

**Nota de enquadramento.** Sistema concebido e desenvolvido no contexto de um cliente específico. Este documento descreve a capacidade demonstrada; não constitui oferta de produto de prateleira nem autoriza revenda.

*Base de apuração: interface pública da aplicação, documento de metodologia conceitual do repositório, documentação de API e modelo de dados.*
