# Densidade da Malha Rodoviária — SP

**Análise exploratória da malha rodoviária estadual paulista**

> Onde a estrada não chega — e quanta gente mora lá.

---

## O problema

Investimento em infraestrutura rodoviária costuma ser decidido por demanda declarada: quem pede mais alto, com mais articulação, recebe primeiro.

Falta o contraponto técnico. Quanta rodovia existe por quilômetro quadrado em cada região? Por habitante? Onde a cobertura é desproporcionalmente baixa em relação à população atendida ou à produção escoada? Sem esse indicador, a carteira de investimento reproduz a distribuição política do pleito, não a distribuição territorial da necessidade.

## O que é

Estudo geoespacial da densidade da malha rodoviária estadual paulista, com indicadores calculados **por área e por população**, classificados por tipo de administração, categoria de rodovia e localização urbano-rural.

## A escala

| Indicador | Valor |
|---|---|
| Quilômetros de rodovias | 21.674 |
| Municípios analisados | 645 |
| Trechos rodoviários | 4.779 |
| População de referência (Censo 2022) | 44,6 milhões |

## O escopo é declarado

A análise cobre a rede sob jurisdição do departamento estadual de estradas de rodagem, incluindo rodovias estaduais, trechos de rodovias federais delegados ao estado, rodovias sob concessão e rodovias de administração direta.

E declara o que **não** cobre: rodovias municipais estão fora. É a delimitação que impede leitura equivocada dos resultados — densidade baixa aqui significa baixa cobertura estadual, não ausência de estrada.

## Recorte multinível

Os indicadores são calculados em três escalas territoriais: **municipal**, **regiões geográficas imediatas** e **regiões geográficas intermediárias**. A visão multinível é o que permite distinguir carência local de carência regional — problemas com soluções orçamentárias muito diferentes.

## Para que serve na prática

**Planejamento** — identificar áreas de baixa densidade para priorizar expansão e melhoria.

**Eficiência** — avaliar a relação entre extensão, área territorial e população para orientar alocação de recurso.

**Cobertura territorial** — mapear a distribuição espacial e evidenciar disparidades regionais na oferta.

**Acessibilidade** — analisar a relação entre infraestrutura e população para sustentar critério de equidade no acesso ao sistema rodoviário.

## Formato

Relatório técnico navegável, estruturado em introdução, objetivos, dados, metodologia, resultados, discussão, conclusão e anexo cartográfico, com **mapas interativos** em vez de figuras estáticas.

É um estudo publicável — não uma planilha com gráficos. A estrutura é a de um documento técnico defensável, com fontes e método explícitos.

## Para quem

Secretarias de transporte e infraestrutura, departamentos de estradas, agências de planejamento regional, consórcios intermunicipais, e equipes que precisam sustentar tecnicamente a distribuição territorial de investimento.

## Base técnica

Python com GeoPandas para o processamento geoespacial · Folium para a cartografia interativa · HTML, CSS e JavaScript para o relatório navegável · dados oficiais do órgão rodoviário estadual e do instituto federal de estatística.

## Fundamento científico

**Densidade como indicador normalizado.** Extensão bruta de malha não é indicador — é volume. Um município grande naturalmente tem mais quilômetros de estrada que um pequeno, o que não diz nada sobre cobertura. O estudo trabalha com **duas normalizações complementares**:

```text
densidade territorial   = extensão de malha / área da unidade      (km/km²)
densidade demográfica   = extensão de malha / população da unidade (km/habitante)
```

As duas respondem a perguntas diferentes e frequentemente divergem. Uma região de baixa densidade populacional e grande extensão territorial pode ter densidade demográfica alta e densidade territorial baixa. **A leitura conjunta é o que separa vazio de infraestrutura de vazio demográfico** — distinção decisiva para priorizar investimento, porque uma pede expansão de malha e a outra não.

**Análise multiescalar.** Os indicadores são calculados em três recortes territoriais encaixados: municipal, regiões geográficas imediatas e regiões geográficas intermediárias, seguindo a divisão regional oficial do instituto de estatística.

A escolha não é de conveniência. É o tratamento do **problema da unidade de área modificável** — o fato conhecido em análise espacial de que resultados agregados dependem da escala e do desenho das unidades de agregação. Um município pode aparecer como carente isoladamente e adequado quando lido no conjunto da sua região imediata, porque a rodovia que o atende passa ao lado. Analisar em três escalas expõe esse efeito em vez de escondê-lo.

**Estratificação por atributo.** A malha é classificada e analisada por tipo de administração (direta, delegada, concedida), categoria de rodovia e localização urbano-rural. Densidade agregada sem estratificação mistura infraestruturas com padrão de serviço, custo e responsabilidade distintos.

**Delimitação explícita do universo.** O estudo declara que analisa apenas a rede sob jurisdição estadual e federal delegada, excluindo malha municipal. É condição de validade da interpretação: densidade baixa no resultado significa baixa cobertura **estadual**, não ausência de estrada. Sem essa ressalva, o mesmo número sustentaria uma conclusão falsa.

**Processamento geoespacial.** Cálculo de extensão sobre geometria linear com projeção adequada à medição de comprimento, junção espacial entre trechos rodoviários e unidades territoriais, e agregação por unidade — com os 4.779 trechos distribuídos entre os 645 municípios e as regiões que os contêm.

**Cartografia interativa como evidência.** Os resultados são apresentados em mapas navegáveis, não em figuras estáticas, permitindo que o leitor verifique caso a caso em vez de aceitar a síntese. A estrutura do documento — introdução, objetivos, dados, metodologia, resultados, discussão, conclusão e anexo cartográfico — é a de um relatório técnico-científico, com método declarado e reprodutível.

---

**Nota de enquadramento.** Produto analítico desenvolvido sobre bases de dados públicas. Este documento descreve a capacidade demonstrada. Aplicação de acesso público.

*Base de apuração: portal público da aplicação.*
