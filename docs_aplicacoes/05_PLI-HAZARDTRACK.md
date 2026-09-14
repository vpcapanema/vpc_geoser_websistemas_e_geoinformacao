# PLI-HazardTrack

**Monitoramento de riscos climáticos extremos na malha rodoviária**

> Onde a estrada vai ceder — antes de ceder.

---

## O problema

Chuva extrema em serra derruba encosta sobre pista. O evento é rápido, e a decisão que importa — interditar, desviar, acionar equipe — precisa ser tomada com horas de antecedência, não depois do escorregamento.

O que existe na maioria das operações é reação: o alerta chega quando a via já está bloqueada. E quando existe monitoramento, ele costuma ser genérico — um aviso de chuva forte para uma região inteira, que não diz nada sobre qual trecho de qual rodovia está sob qual nível de risco.

## O que é

O PLI-HazardTrack é a interface operacional de monitoramento de riscos associados a eventos climáticos extremos sobre a malha rodoviária estadual. Reúne, sobre a mesma malha, **três produtos de risco operando em paralelo**:

| Produto | O que monitora | Base |
|---|---|---|
| **Movimentos de massa** | risco geológico por Unidade de Análise | chuva observada + previsão meteorológica |
| **Inundação** | risco hidrológico por Unidade de Análise | janela de chuva acumulada |
| **Incêndios** | risco de fogo por trecho rodoviário | produto observado e previsão até D+3 |

## O modelo não é improvisado

O risco geológico e o hidrológico seguem um **modelo oficial de risco dinâmico** — o produto de um fator de risco analisado por um índice de condição de chuva —, calibrado para **regiões climático-geológico-geomorfológicas** distintas. Cada região tem sua própria sensibilidade e seus próprios limiares de classificação.

O sistema calcula, por unidade de análise: intensidade de chuva, acumulado em 24 h, acumulado em 96 h, o coeficiente de precipitação crítica, o índice de condição classificado nos canais geológico e hidrológico, e o risco dinâmico resultante — retendo sempre o maior entre os dois canais.

A classificação final é entregue nos **níveis operacionais do Plano de Prevenção de Defesa Civil**: monitoramento, observação, atenção, alerta e alerta máximo. O gestor não recebe um número abstrato — recebe o nível que já está no protocolo dele.

## Dado real, em streaming

A cada ciclo o sistema consome as **grades horárias de chuva observada** produzidas pelo serviço meteorológico oficial, processando-as **diretamente em memória**, sem gravar nada em disco, com amostragem em lote de todos os pontos de monitoramento em uma única operação nativa.

O ciclo completo termina em segundos. A atualização é automática a cada dez minutos no servidor, com refresh de trinta segundos na tela.

## Previsão, não só observação

Além da chuva observada, o sistema incorpora **previsão meteorológica** para antecipar o risco: acumulado previsto de +24 h para movimentos de massa e de +6 h para inundação, calculados na unidade de análise correspondente.

É a diferença entre saber que o risco subiu e saber que ele vai subir.

## Reconstrução temporal

**Evolução de 96 horas** — o sistema reconstrói hora a hora as últimas 96 horas com base na chuva observada, recalculando o risco em cada quadro. O operador avança quadro a quadro e identifica exatamente quando a unidade de análise mudou de nível.

**Busca histórica** — reconstitui mapa e indicadores para qualquer data e hora passadas, usando somente chuva observada da época. O sistema oferece uma lista de **eventos com alerta elevado já validados**, para verificar o comportamento em condição real.

Essa capacidade responde à pergunta que todo gestor faz antes de confiar em um sistema de alerta: *o que ele teria dito no dia do desastre?* O modelo foi validado por reconstituição de evento real de grande porte.

## Honestidade operacional

Quando a rede falha e o dado não chega, o sistema marca o estado como **indisponível**. Não preenche a lacuna com estimativa, não assume o último valor conhecido, não devolve risco zero.

É uma decisão de projeto com consequência direta: em sistema de alerta, ausência silenciosamente convertida em "sem risco" é o modo mais eficiente de matar gente.

O sistema também declara o próprio limite de cobertura — as rodovias com unidades de análise oficiais são identificadas, e as demais vias aparecem explicitamente como apoio cartográfico.

## Consulta e integração

Busca simples por camada, campo e valor; busca avançada com múltiplos critérios combinados por E/OU, independente por camada. Os filtros alteram apenas a visualização: **não recalculam risco nem nível** — separação explícita entre explorar e decidir.

Camadas de apoio incluem regiões monitoradas, malha rodoviária, câmeras, limites administrativos, municípios e unidades operacionais de conservação e atendimento.

Há **API pública das três camadas de risco**, com parâmetros documentados e exemplos de consumo — é por ela que o roteirizador do ecossistema desvia rotas automaticamente.

## Para quem

Órgãos rodoviários e concessionárias, defesa civil estadual e municipal, operações de transporte em região serrana ou litorânea, gestores de contingência e planos de emergência.

## Base técnica

Flask e Python · processamento de grades meteorológicas em memória com decodificação nativa e paralelismo · Leaflet · scheduler de atualização · API pública em JSON · testes unitários do módulo de risco e teste de integração com a fonte meteorológica real · Docker.

## Fundamento científico

**Envoltória crítica de deflagração.** O núcleo do modelo geológico é a relação empírica entre intensidade e chuva antecedente que define o limiar de deflagração de escorregamentos:

```
I_envoltória = K · Ac96h^(−0,9)
CPC = I / I_envoltória
```

O expoente negativo expressa o princípio físico do processo: quanto maior a chuva acumulada prévia, menor a intensidade instantânea necessária para deflagrar o movimento. Solo saturado rompe com pouco. O coeficiente de precipitação crítica (CPC) é a razão entre a chuva observada e o limiar — acima de 1, o ponto entrou na zona crítica da envoltória.

**Regionalização geotécnica.** O parâmetro de sensibilidade **K** é calibrado por região climático-geológico-geomorfológica, e varia por fator de cinco entre as regiões monitoradas. Valores menores indicam maior resposta à precipitação acumulada. Cada região tem também seus próprios limiares de classificação do índice de condição, tanto no canal geológico quanto no hidrológico. Não existe limiar único para o estado — a mesma chuva significa coisas diferentes em litologias e relevos diferentes.

**Composição de janelas observadas e previstas.** O risco não é calculado apenas sobre o passado. As janelas de chuva compõem observação e previsão numericamente:

- canal geológico: 72 h observadas + 24 h previstas = Ac96h
- canal hidrológico: 18 h observadas + 6 h previstas = Ac24h

Sem previsão disponível, o sistema **degrada de forma transparente** para observado apenas, e declara a fonte do dado (`WRF` ou `OBS_ONLY`) junto com o resultado.

**Matriz de composição do risco.** O risco dinâmico resulta do cruzamento matricial entre o risco analisado da unidade — atributo estrutural do terreno — e o índice de condição de chuva — atributo conjuntural:

```
RD = M[RA][ICC],  RA, ICC ∈ {0..4}
```

A matriz é assimétrica e satura: terreno sem suscetibilidade (RA0) permanece em risco zero sob qualquer chuva, enquanto terreno de suscetibilidade máxima (RA4) atinge alerta máximo já no primeiro nível de condição crítica. É o comportamento correto — chuva não cria instabilidade onde não há material para mobilizar.

**Independência dos canais.** Risco geológico e hidrológico são calculados de forma independente, sem fallback entre eles. Ausência de dado em um canal não é suprida pelo outro. O risco final do trecho é o máximo entre os dois, não a média — a via fica interditada pelo pior processo, não pela média deles.

**Propagação de distribuição.** Quando um trecho contém múltiplas unidades de análise com classes distintas de risco analisado, o sistema propaga a distribuição inteira pela matriz, devolvendo quantas unidades resultam em cada nível de risco dinâmico — em vez de reduzir o trecho a um único número e perder a dispersão interna.

**Validação por retrodição.** O modelo foi verificado por reconstituição de evento real de grande porte, comparando os níveis calculados retroativamente com os danos efetivamente observados em localidades distintas. O sistema mantém uma lista de eventos validados acessível ao usuário, para que qualquer pessoa possa repetir a verificação.

---

**Nota de enquadramento.** Sistema concebido e desenvolvido no contexto de um cliente específico, implementando metodologia de terceiros contratada por esse cliente. Este documento descreve a capacidade demonstrada; não constitui oferta de produto de prateleira nem autoriza revenda.

*Base de apuração: interface pública da aplicação, README e documentação do repositório.*
