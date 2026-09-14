# Formulário de Entrevista com Embarcadores

**Levantamento de campo para caracterização do transporte de mercadorias**

> Pesquisa logística morre na transcrição. Esta já nasce estruturada.

---

## O problema

Todo plano de logística começa com pesquisa de campo: entrevistar embarcadores, transportadores e operadores para entender o que se move, de onde para onde, por qual modal e em que volume.

Historicamente essa pesquisa é feita em papel ou em planilha solta. O entrevistador anota, alguém digita depois, o nome da empresa vem grafado de três formas diferentes, o município tem erro de digitação, o produto é descrito em linguagem livre e a consolidação vira um projeto em si — muitas vezes mais caro que a coleta.

Pior: erro detectado na consolidação não tem conserto. O entrevistado não volta.

## O que é

Instrumento digital de coleta estruturada para entrevista com embarcadores, voltado à caracterização do transporte de mercadorias em escala estadual. Substitui o formulário em papel por captura validada na origem.

## Coleta com validação na fonte

**Identificação do preenchimento** — o formulário distingue se quem responde é o **entrevistado**, representante da empresa, ou o **entrevistador**, consultor ou pesquisador, com seleção em lista controlada de entrevistadores. A autoria de cada registro fica identificada.

**Consulta automática à base federal de CNPJ** — informado o CNPJ, o sistema recupera razão social, nome fantasia, situação cadastral e atividade principal por classificação de atividade econômica, em campos não editáveis marcados como oriundos da fonte oficial.

Este é o ponto que muda a qualidade do dado: a identificação da empresa deixa de ser digitada e passa a ser recuperada. Acaba a divergência de grafia, e a base já nasce com chave de cruzamento com qualquer outra base econômica.

**Listas controladas** em toda parte — função do entrevistado, tipo de agente (embarcador dono da carga, transportador, operador logístico), estados e municípios encadeados, modalidade e acondicionamento.

## Estrutura da entrevista

**Dados do entrevistado** — contato e perfil de quem detém a informação logística.

**Dados da empresa** — natureza do agente na cadeia, identificação recuperada da base federal e municípios das unidades de produção.

**Produtos transportados** — o núcleo. Para cada produto: movimentação anual em toneladas, origem, destino, distância, modalidade e acondicionamento, com adição dinâmica de linhas e confirmação item a item.

É exatamente a matriz origem-destino por produto que alimenta modelagem de transporte.

## Além da coleta

O instrumento não para no formulário. Inclui módulos de **respostas**, **analytics**, **instruções** e **visualizador** — ou seja, a equipe acompanha o andamento do levantamento e explora os resultados enquanto a coleta ainda está em curso.

Detectar em campo que uma região está sub-amostrada, com tempo de corrigir, é a diferença entre uma pesquisa utilizável e uma pesquisa refeita.

## Para quem

Equipes de planejamento logístico e de transporte, consultorias contratadas para estudos de matriz origem-destino, agências de desenvolvimento, secretarias de transporte e infraestrutura, e qualquer levantamento de campo estruturado que precise de dado consolidável desde o primeiro registro.

## Base técnica

Aplicação web com backend em Python · consulta a serviço público de dados cadastrais de pessoa jurídica · listas controladas e validação em formulário · módulo de acompanhamento e análise das respostas · interface responsiva para uso em campo.

## Fundamento científico

**Instrumento de pesquisa, não formulário genérico.** A estrutura segue a lógica de um questionário estruturado de pesquisa aplicada: seções encadeadas do geral ao específico, com identificação do respondente, caracterização da unidade observada e, por fim, o bloco de dados quantitativos.

**Controle de viés de resposta pela identificação do papel.** A primeira pergunta distingue se responde o **entrevistado** ou o **entrevistador**. A distinção parece burocrática e não é: respostas coletadas por intermediário têm propriedades diferentes das autodeclaradas, e registrar o modo de coleta permite controlar esse efeito na análise. A lista fechada de entrevistadores ainda possibilita avaliar **efeito de entrevistador** — variação sistemática atribuível a quem aplicou.

**Validação na origem em vez de limpeza posterior.** O princípio metodológico é que erro de dado deve ser impedido no momento da captura, não corrigido na consolidação. Isso porque o erro detectado depois é, em geral, irrecuperável: o entrevistado não retorna.

A **recuperação automática da identificação da empresa em base cadastral oficial** — razão social, nome fantasia, situação cadastral e atividade econômica — elimina a fonte mais comum de inconsistência em pesquisa empresarial: a mesma firma grafada de várias formas, impedindo agregação e cruzamento. Os campos vêm marcados como não editáveis e com origem declarada.

O ganho não é só de limpeza. A base **já nasce com chave de integração**: identificada por registro fiscal e classificada por atividade econômica na taxonomia nacional, ela cruza diretamente com registros de emprego formal, comércio exterior e qualquer estatística econômica oficial.

**Vocabulário controlado.** Função do respondente, natureza do agente na cadeia logística — embarcador dono da carga, transportador, operador logístico —, unidades territoriais encadeadas, modalidade de transporte e tipo de acondicionamento vêm de listas fechadas. Campo aberto em pesquisa quantitativa gera categoria irreconciliável na tabulação; a alternativa "outro, especifique" é preservada apenas onde a taxonomia pode ser genuinamente insuficiente.

**Matriz origem-destino por produto.** O bloco central captura, por carga: movimentação anual em tonelada, origem, destino, distância, modalidade e acondicionamento. É a estrutura de dados que alimenta **modelagem de transporte** — a matriz O-D é o insumo básico de modelo de alocação de fluxo, dimensionamento de infraestrutura e avaliação de alternativa modal.

Coletar diretamente nessa estrutura, com adição dinâmica de linhas e confirmação item a item, evita a etapa de reinterpretação de descrição livre em fluxo quantificado — onde a maior parte da informação de pesquisa logística se perde.

**Monitoramento da coleta em andamento.** Módulos de acompanhamento de respostas e de análise permitem avaliar cobertura amostral enquanto o campo ainda está aberto. Identificar sub-representação de uma região, de um porte de empresa ou de um setor **com tempo de corrigir** é o que separa amostra utilizável de amostra enviesada — e uma pesquisa entregue de uma pesquisa refeita.

---

**Nota de enquadramento.** Instrumento desenvolvido no contexto de um levantamento específico. Este documento descreve a capacidade demonstrada; a aplicação a outro levantamento é projeto sob medida.

*Base de apuração: interface pública da aplicação.*
