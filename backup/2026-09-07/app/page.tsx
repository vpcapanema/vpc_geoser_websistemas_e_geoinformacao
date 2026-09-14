import {
  ArrowDown, ArrowRight, Boxes, CircleDot, CloudRain,
  Database, ExternalLink, FileSearch, Gauge, GitBranch,
  GraduationCap, Layers3, Map, Network, Radar, Route,
  ServerCog, ShieldCheck, Workflow,
} from "lucide-react";
import Image from "next/image";
import Link from "next/link";
import Motion from "./motion";
import HeroOrbits from "./hero-orbits";

const areas = [
  { title: "Geoinformação", description: "Processamento vetorial e raster, publicação de serviços OGC e interfaces de mapa que tratam território como dado de trabalho, não como ilustração.", icon: Map },
  { title: "Websistemas", description: "Sistemas corporativos, portais e aplicações de campo com autenticação, perfis de acesso e trilha de auditoria desde a concepção.", icon: Layers3 },
  { title: "Dados", description: "Catálogos, metadados, dicionários e modelagem relacional e espacial, para que a informação técnica tenha origem, responsável e histórico.", icon: Database },
  { title: "Automação", description: "Extração documental, integração entre sistemas e rotinas de processamento que eliminam etapas manuais repetidas.", icon: Workflow },
];

const graphNodes = [
  { title: "WebGIS e serviços OGC", icon: Map },
  { title: "Catálogo e metadados", icon: Database },
  { title: "Análise multicritério", icon: GitBranch },
  { title: "Integração e APIs", icon: Network },
  { title: "Automação documental", icon: FileSearch },
  { title: "Infraestrutura e observabilidade", icon: ServerCog },
];

const principles = [
  { title: "Rastreabilidade como requisito", text: "Fonte, parâmetro e decisão ficam registrados. Um resultado que não pode ser explicado depois não é entregável." },
  { title: "Indisponibilidade não vira zero", text: "Falta de dado é declarada como falta de dado. O sistema não preenche lacuna com estimativa silenciosa." },
  { title: "Soberania sobre os dados", text: "Preferência por soluções abertas, formatos interoperáveis e arquitetura que permite ao cliente levar seus dados embora." },
  { title: "Geoinformação nativa", text: "Quando há dimensão espacial relevante, ela entra no modelo de dados — não como camada decorativa no fim." },
];

const stack = ["Python · FastAPI", "TypeScript · React", "PostgreSQL · PostGIS", "GeoServer · QGIS Server", "Leaflet · MapLibre", "OGC WMS · WFS", "ETL/ELT geoespacial", "Docker · CI/CD", "AWS EC2 · RDS", "PyMuPDF · Tesseract"];

const projects = [
  {
    title: "SIGMA-PLI", tag: "Plataforma de dados e governança", icon: Database,
    lead: "O conhecimento técnico de um plano estadual se dispersa entre documentos, planilhas e camadas sem dono — e se perde na troca de gestão.",
    body: "Catálogo de metadados com dicionário de dados, busca e versionamento; grafo de conhecimento para navegar relações entre bases; publicação de camadas em WMS/WFS; cadastro com autenticação JWT, perfis e trilha de auditoria. Onze módulos em operação, incluindo monitoramento da própria infraestrutura.",
  },
  {
    title: "SICARD", tag: "Decisão multicritério", icon: GitBranch,
    lead: "Definir quais projetos entram primeiro no orçamento exige critério que se sustente diante de questionamento.",
    body: "Cadastro e hierarquização de planos, programas e projetos em ciclo único. Análise AHP com comparação pareada, cálculo de pesos e verificação de consistência, incluindo julgamento colaborativo: especialistas recebem convite com prazo e token, e cada matriz individual fica registrada. A hierarquização percorre elegibilidade territorial, favorabilidade, ajuste por atributos e homologação.",
  },
  {
    title: "PLI-HazardTrack", tag: "Monitoramento geodinâmico", icon: CloudRain,
    lead: "Saber agora quais trechos rodoviários do litoral norte e da baixada santista estão sob risco de escorregamento e inundação.",
    body: "Implementa o modelo oficial de risco dinâmico RD = RA × ICC em quatro regiões climático-geológico-geomorfológicas. A cada ciclo consome as grades horárias de chuva do MERGE/CPTEC-INPE em streaming direto para memória, classifica o índice geológico e o hidrológico e retém o risco maior. Quando a rede falha, o estado é marcado como indisponível — não como risco zero.",
  },
  {
    title: "PLI Reporta", tag: "Ocorrências verificadas", icon: Radar,
    lead: "Quem passa pela via vê o bloqueio antes de qualquer sensor, mas relato solto não é confiável o bastante para desviar tráfego.",
    body: "Aplicação de campo que qualifica cada reporte por dois scores independentes: veracidade, que responde se o fato é real, e relevância, que responde se ele importa para a rota. O incidente percorre um ciclo de vida auditável até a publicação, e o feed resultante é exposto em formato estável para consumo por outros sistemas.",
  },
  {
    title: "PLI Smart Router", tag: "Roteirização com risco", icon: Route,
    lead: "Rota ótima calculada sobre base estática ignora que a estrada está interditada agora.",
    body: "Calcula rotas reais e, com as camadas de risco ativas, gera automaticamente alternativa que desvia dos obstáculos com faixa de segurança. Consome os alertas do PLI-HazardTrack e as ocorrências verificadas do PLI Reporta, e informa o percentual de exposição a risco de cada trajeto. Os três sistemas se conectam: não apenas coexistem.",
  },
  {
    title: "FAD-Stats", tag: "Análise territorial e temática", icon: Gauge,
    lead: "Cruzar produção, trabalho, comércio exterior e logística exige juntar bases oficiais que não conversam entre si.",
    body: "Ambiente de análise temporal, territorial e temática com filtros multidimensionais, indicadores, gráficos e mapas gerados sob demanda a partir de catálogo espacial e bases estatísticas integradas.",
  },
];

const tools = [
  { title: "Painel Analítico de Sinistros — DER/SP", url: "https://acidentes-der-analise-exploratoria.onrender.com", description: "Exploração interativa dos registros de sinistros nas rodovias estaduais, com recortes por rodovia e período para apoiar diagnóstico, comparação e priorização de análises de segurança viária.", icon: Radar },
  { title: "AHP Tool Calculator", url: "https://vpc-geoser-ahp-tool-calculator.onrender.com", description: "Análise hierárquica de processos para ponderação e priorização multicritério, com os pesos e a razão de consistência do julgamento visíveis a cada etapa.", icon: GitBranch },
];

const clients = [
  { id: "governo", name: "Governo do Estado de São Paulo", caption: "Governo do Estado de São Paulo", logo: "/clientes/governo-sp-display.png", width: 1023, height: 500 },
  { id: "semil", name: "Secretaria de Meio Ambiente, Infraestrutura e Logística — Subsecretaria de Logística e Transporte", caption: "SEMIL — Subsecretaria de Logística e Transporte", logo: "/clientes/semil-sp-display.png", width: 543, height: 500 },
  { id: "der", name: "Departamento de Estradas de Rodagem do Estado de São Paulo — DER/SP", caption: "DER/SP — Departamento de Estradas de Rodagem", logo: "/clientes/der-sp-display.png", width: 283, height: 168 },
];

export default function Home() {
  return (
    <main>
      <a className="skip-link" href="#conteudo">Ir para o conteúdo</a>

      <header className="site-header">
        <div className="shell header-inner">
          <a className="brand" href="#inicio" aria-label="VPC — início">
            <Image src="/simbolo-vpc-satelite.png" width="64" height="64" alt="" priority />
            <span><strong>VPC-WEBSISTEMAS E GEOINFORMAÇÃO</strong><small>Inteligência em geoprocessamento e sensoriamento remoto.</small></span>
          </a>
          <nav aria-label="Navegação principal">
            <a href="#atuacao">Atuação</a><a href="#engenharia">Engenharia</a><a href="#projetos">Experiências</a><a href="#vpc-ita">VPC-ITA</a><a href="#produtos">Produtos</a><a href="#clientes">Clientes</a><a href="#sobre">Sobre</a>
          </nav>
          <a className="header-cta" href="#contato"><span className="cta-long">Fale sobre seu desafio</span><span className="cta-short">Contato</span><ArrowRight aria-hidden="true" size={13} /></a>
        </div>
      </header>

      <div id="conteudo">
        <section className="hero" id="inicio">
          <div className="hero-grid" aria-hidden="true" />
          <div className="shell hero-layout">
            <div className="hero-copy">
              <h1>Sistemas que sustentam <em>decisão técnica.</em></h1>
              <p className="hero-lead">A VPC reúne geoprocessamento, sensoriamento remoto, análise de dados e engenharia de software para transformar dados técnicos e territoriais em sistemas digitais operacionais — construídos para o contexto de cada instituição.</p>
              <div className="hero-actions">
                <a className="button button-primary" href="#atuacao">Conheça a abordagem <ArrowDown aria-hidden="true" size={13} /></a>
                <a className="text-link" href="#projetos">Ver experiências relacionadas <ArrowRight aria-hidden="true" size={13} /></a>
              </div>
              <div className="hero-pillars" aria-label="Pilares da atuação">
                <span><CircleDot aria-hidden="true" /> Rastreabilidade</span>
                <span><CircleDot aria-hidden="true" /> Geoinformação nativa</span>
                <span><CircleDot aria-hidden="true" /> Arquitetura aberta</span>
              </div>
            </div>
            <div className="hero-visual" aria-label="Identidade visual da VPC">
              <HeroOrbits />
              <div className="hero-mark hero-mark-top">
                <strong>VPC-<em>WEBSISTEMAS</em><br /><em>E GEOINFORMAÇÃO</em></strong>
              </div>
              <div className="logo-frame" role="img" aria-label="Globo com satélite, símbolo da VPC" style={{ backgroundImage: "url(/logo-vpc-oficial.png)" }} />
              <div className="hero-mark hero-mark-bottom">
                <span>Inteligência em geoprocessamento<br />e sensoriamento remoto</span>
              </div>
            </div>
          </div>
        </section>

        <section className="section section-light" id="atuacao"><div className="shell">
          <div className="section-heading split-heading"><div><p className="section-kicker">Áreas de atuação</p><h2>Quatro frentes que raramente aparecem separadas.</h2></div><p>Instituições que lidam com território, infraestrutura e dados públicos costumam precisar das quatro ao mesmo tempo. É por isso que elas são desenvolvidas juntas, e não contratadas em pedaços que depois não se encaixam.</p></div>
          <div className="area-grid area-grid-four">{areas.map(({ title, description, icon: Icon }) => <article className="area-card" key={title}><div className="card-title-group"><Icon aria-hidden="true" /><h3>{title}</h3></div><p>{description}</p></article>)}</div>
        </div></section>

        <section className="section section-graph" id="solucoes"><div className="shell">
          <div className="section-heading split-heading inverse"><div><p className="section-kicker">Soluções sob medida</p><h2>Não vendemos um pacote fechado.</h2></div><p>Cada problema define quais capacidades entram e como se conectam. O que se repete é o método, não a solução.</p></div>
          <div className="graph">
            <svg className="graph-links" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
              <line x1="50" y1="50" x2="2" y2="17" /><line x1="50" y1="50" x2="2" y2="50" /><line x1="50" y1="50" x2="2" y2="83" />
              <line x1="50" y1="50" x2="98" y2="17" /><line x1="50" y1="50" x2="98" y2="50" /><line x1="50" y1="50" x2="98" y2="83" />
            </svg>
            <div className="graph-column">{graphNodes.slice(0, 3).map(({ title, icon: Icon }) => <div className="graph-node" key={title}><Icon aria-hidden="true" /><span>{title}</span></div>)}</div>
            <div className="graph-core"><strong>Soluções<br />inteligentes</strong></div>
            <div className="graph-column">{graphNodes.slice(3).map(({ title, icon: Icon }) => <div className="graph-node" key={title}><Icon aria-hidden="true" /><span>{title}</span></div>)}</div>
          </div>
        </div></section>

        <section className="section section-light" id="engenharia"><div className="shell">
          <div className="section-heading split-heading"><div><p className="section-kicker">Engenharia VPC</p><h2>O que sustenta um resultado é poder explicá-lo depois.</h2></div><p>Princípios aplicados na construção de cada sistema, e o conjunto de tecnologias efetivamente empregado nos projetos entregues.</p></div>
          <div className="principle-grid">{principles.map(({ title, text }) => <article className="principle-card" key={title}><h3>{title}</h3><p>{text}</p></article>)}</div>
          <div className="stack-strip"><span className="stack-label"><Boxes aria-hidden="true" /> Tecnologias em uso</span><ul>{stack.map(item => <li key={item}>{item}</li>)}</ul></div>
        </div></section>

        <section className="section section-experiences" id="projetos"><div className="shell">
          <div className="section-heading split-heading inverse"><div><p className="section-kicker">Experiências relacionadas</p><h2>Seis sistemas em operação no ecossistema do PLI-SP 2050.</h2></div><p>Foram construídos para problemas distintos, mas compartilham base de dados, autenticação e linguagem territorial — e três deles trocam informação entre si em tempo real.</p></div>
          <div className="experience-list">{projects.map(({ title, tag, lead, body, icon: Icon }) => <article className="experience-card" key={title}>
            <div className="card-title-group"><Icon aria-hidden="true" /><h3>{title}</h3></div>
            <p className="experience-tag">{tag}</p>
            <p className="experience-lead">{lead}</p>
            <p>{body}</p>
          </article>)}</div>
          <p className="access-note"><ShieldCheck aria-hidden="true" /> <span>Sistemas em operação no ambiente restrito do cliente. Uma versão demonstrativa está em preparação — <a href="#contato">solicite uma apresentação</a>.</span></p>
        </div></section>

        <section className="section section-product" id="vpc-ita"><div className="shell">
          <div className="section-heading split-heading"><div><p className="section-kicker">Solução própria</p><h2>Conheça o território, assuma o risco depois.</h2></div><p>Uma leitura técnica do imóvel rural baseada em fontes oficiais, sensoriamento remoto e processamento geoespacial rastreável.</p></div>
          <Link className="product-feature" href="/ita" aria-label="Conheça a VPC-ITA — Inteligência Territorial e Auditoria Ambiental">
            <div className="product-feature-copy">
              <h3>VPC-ITA, Inteligência Territorial e Auditoria Ambiental</h3>
              <p>Um imóvel rural pode parecer regular até que os dados contem outra história. Descubra como fontes oficiais, sensoriamento remoto e processamento geoespacial se transformam em um diagnóstico territorial rastreável.</p>
              <span className="product-discover">O que existe dentro deste perímetro? <ArrowRight aria-hidden="true" size={14} /></span>
            </div>
            <div className="product-feature-visual" aria-hidden="true"><div className="ita-symbol"><svg viewBox="0 0 240 240"><path className="ita-parcel" d="M48 52 139 31l57 45-15 102-89 31-54-61Z" /><path className="ita-leaf" d="M76 150c5-50 38-80 91-82-4 49-34 82-91 82Z" /><path className="ita-vein" d="m82 145 68-61M112 119l-2-26M128 104l27 3" /><path className="ita-check" d="m91 161 20 19 43-48" /></svg></div><div className="product-coordinate">IMÓVEL · AMBIENTE · EVIDÊNCIA</div></div>
          </Link>
        </div></section>

        <section className="section section-solutions" id="produtos"><div className="shell">
          <div className="section-heading split-heading inverse"><div><p className="section-kicker">Produtos em atividade</p><h2>Aplicações abertas ao público.</h2></div><p>Ferramentas de escopo delimitado, disponíveis para uso direto, que aplicam os mesmos métodos analíticos presentes nos sistemas maiores.</p></div>
          <div className="solutions-grid solutions-grid-pair">{tools.map(({ title, url, description, icon: Icon }) => <a className="solution-card" href={url} target="_blank" rel="noreferrer" key={title} aria-label={`${title} — abrir aplicação`}>
            <div className="solution-icon"><Icon aria-hidden="true" /></div>
            <h3>{title}</h3><p>{description}</p>
            <span className="solution-open">Abrir aplicação <ExternalLink aria-hidden="true" size={13} /></span>
          </a>)}</div>
        </div></section>

        <section className="section section-clients" id="clientes"><div className="shell">
          <div className="section-heading split-heading"><div><p className="section-kicker">Clientes atendidos</p><h2>Tecnologia aplicada ao planejamento logístico de São Paulo.</h2></div><p>O trabalho atende o Governo do Estado de São Paulo em três instâncias — a SEMIL, sua Subsecretaria de Logística e Transporte e o DER/SP — no âmbito do PLI-SP 2050.</p></div>
          <div className="clients-grid">{clients.map((client) => <article className={`client-card client-${client.id}`} key={client.name}>
            <div className="client-logo"><Image src={client.logo} alt={`Marca oficial — ${client.name}`} width={client.width} height={client.height} sizes="(max-width: 720px) 86vw, 340px" /></div>
            <p className="client-name">{client.caption}</p>
          </article>)}<article className="client-card client-pli"><div className="pli-wordmark"><span>Plano de Logística e Investimentos</span><strong>PLI/SP-2050</strong></div><p className="client-name">Programa no qual os sistemas operam</p></article></div>
        </div></section>

        <section className="section section-about" id="sobre"><div className="shell about-layout">
          <div className="about-mark" aria-hidden="true"><Image src="/simbolo-vpc-satelite.png" alt="" width="520" height="520" sizes="(max-width: 720px) 90vw, 520px" /></div>
          <div className="about-copy"><p className="section-kicker">Sobre a VPC</p><h2>Conhecimento técnico-científico com visão de território.</h2><p className="about-lead">A VPC-WEBSISTEMAS E GEOINFORMAÇÃO é conduzida por Vinicius do Prado Capanema e reúne geoprocessamento, sensoriamento remoto, análise de dados e engenharia de software para criar soluções digitais sob medida. Quem conversa com o cliente é quem projeta e constrói o sistema.</p>
            <div className="founder-card"><div className="founder-icon"><GraduationCap aria-hidden="true" /></div><div><strong>Vinicius do Prado Capanema</strong><span>Engenheiro e desenvolvedor de soluções geoespaciais</span><p>Engenheiro florestal pela UNEMAT, especialista em Georreferenciamento pela AJES/INCRA, MBA em Gestão de Projetos pela UNOPAR, mestre e doutor em Sensoriamento Remoto pelo INPE.</p><a className="founder-link" href="https://vpcapanema.github.io/curriculo_viniciuscapanema/" target="_blank" rel="noreferrer">Conheça o currículo completo <ExternalLink aria-hidden="true" size={13} /></a></div></div>
          </div>
        </div></section>

        <section className="contact" id="contato"><div className="shell contact-layout">
          <div><p className="section-kicker">Contato comercial</p><h2>Descreva o problema. Respondemos com leitura técnica.</h2><p>Conte o contexto, quem vai usar o sistema e que decisão precisa ser sustentada no fim. Descreva também os dados de que sua organização já dispõe — é deles que sai o diagnóstico inicial.</p></div>
          <div className="contact-action"><span className="contact-label">Fale com a VPC</span><a className="contact-email" href="mailto:comercial@vpc-websistemas.com.br?subject=Contato%20comercial%20—%20VPC-WEBSISTEMAS">comercial@vpc-websistemas.com.br</a><a className="button button-light" href="mailto:comercial@vpc-websistemas.com.br?subject=Contato%20comercial%20—%20VPC-WEBSISTEMAS">Iniciar conversa <ArrowRight aria-hidden="true" size={13} /></a></div>
          <a className="back-to-top" href="#inicio">Voltar ao início <ArrowDown aria-hidden="true" size={12} /></a>
        </div></section>
      </div>

      <footer id="rodape"><div className="shell footer-inner"><div className="footer-brand"><Image src="/simbolo-vpc-satelite.png" width="64" height="64" alt="" /><span><strong>VPC-WEBSISTEMAS E GEOINFORMAÇÃO</strong><small>Inteligência em geoprocessamento e sensoriamento remoto.</small></span></div><p>Vinicius do Prado Capanema Ltda.</p><p>CNPJ 57.286.005/0001-40 · © 2026 · Todos os direitos reservados. · <Link className="footer-link" href="/privacidade">Política de Privacidade</Link></p></div></footer>
      <Motion />
    </main>
  );
}
