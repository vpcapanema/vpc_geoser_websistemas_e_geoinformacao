import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";

export const metadata: Metadata = {
  title: "Política de Privacidade | VPC-WEBSISTEMAS E GEOINFORMAÇÃO",
  description: "Como a VPC-WEBSISTEMAS E GEOINFORMAÇÃO trata dados pessoais neste site, conforme a Lei Geral de Proteção de Dados (Lei 13.709/2018).",
  robots: { index: true, follow: true },
};

export default function PrivacidadePage() {
  return <main className="legal-page">
    <a className="skip-link" href="#conteudo-legal">Ir para o conteúdo</a>
    <header className="site-header"><div className="shell header-inner"><Link className="brand" href="/" aria-label="Voltar ao site da VPC"><Image src="/simbolo-vpc-satelite.png" width="64" height="64" alt="" priority /><span><strong>VPC-WEBSISTEMAS E GEOINFORMAÇÃO</strong><small>Inteligência em geoprocessamento e sensoriamento remoto.</small></span></Link><Link className="header-cta" href="/"><ArrowLeft aria-hidden="true" size={13} /> Voltar à VPC</Link></div></header>

    <div id="conteudo-legal">
      <section className="legal-hero"><div className="shell">
        <p className="section-kicker">Documento legal</p>
        <h1>Política de Privacidade</h1>
        <p className="legal-lead">Como tratamos dados pessoais neste site, conforme a Lei Geral de Proteção de Dados — Lei nº 13.709/2018.</p>
        <p className="legal-date">Última atualização: 6 de setembro de 2026</p>
      </div></section>

      <section className="section legal-body"><div className="shell legal-shell">
        <h2>1. Quem é o controlador dos dados</h2>
        <p>O controlador dos dados pessoais tratados neste site é <strong>Vinicius do Prado Capanema Ltda.</strong>, inscrita no CNPJ sob o nº 57.286.005/0001-40, que atua sob o nome VPC-WEBSISTEMAS E GEOINFORMAÇÃO.</p>
        <p>Contato para assuntos de privacidade e proteção de dados: <a href="mailto:comercial@vpc-websistemas.com.br?subject=Privacidade%20e%20prote%C3%A7%C3%A3o%20de%20dados">comercial@vpc-websistemas.com.br</a>.</p>

        <h2>2. O que este site coleta</h2>
        <p>Este site é institucional e de apresentação. Ele <strong>não possui formulários de cadastro, não utiliza cookies e não emprega ferramentas de análise de audiência ou rastreamento de comportamento</strong>. Nenhum dado pessoal é coletado automaticamente pelas páginas para finalidades de marketing, perfilamento ou publicidade.</p>
        <p>Como ocorre em qualquer serviço acessível pela internet, o provedor responsável pela hospedagem pode registrar dados técnicos de acesso — como endereço IP, data e hora da requisição e tipo de navegador — para fins de operação, segurança e prevenção a abusos, conforme as políticas do próprio provedor.</p>

        <h2>3. Dados enviados voluntariamente por você</h2>
        <p>Os canais de contato deste site abrem uma mensagem no seu próprio aplicativo de e-mail. Ao nos escrever, você decide quais informações compartilhar. Normalmente recebemos nome, endereço de e-mail, organização e as informações que você escolher incluir sobre o seu desafio técnico.</p>
        <p><strong>Finalidade:</strong> responder à sua mensagem, elaborar diagnóstico inicial, apresentar proposta e conduzir o relacionamento comercial.</p>
        <p><strong>Base legal:</strong> procedimentos preliminares e execução de contrato, nos termos do art. 7º, V, da LGPD, e legítimo interesse para comunicação comercial de natureza técnica, nos termos do art. 7º, IX.</p>
        <p><strong>Recomendação:</strong> não envie por e-mail dados pessoais sensíveis, credenciais de acesso ou informações sigilosas de terceiros. Se um projeto exigir o tratamento desse tipo de informação, definimos previamente em contrato o instrumento e as medidas de segurança adequadas.</p>

        <h2>4. Compartilhamento</h2>
        <p>Não vendemos, alugamos nem cedemos dados pessoais. O compartilhamento ocorre apenas com prestadores de serviço necessários à operação — como provedores de hospedagem e de correio eletrônico — e quando houver obrigação legal, regulatória ou determinação de autoridade competente.</p>

        <h2>5. Retenção</h2>
        <p>As mensagens de contato e os dados nelas contidos são mantidos pelo período necessário ao atendimento da solicitação e ao cumprimento de obrigações legais, contratuais e de defesa de direitos. Encerrada essa necessidade, os dados são eliminados ou anonimizados.</p>

        <h2>6. Segurança</h2>
        <p>Adotamos medidas técnicas e administrativas para proteger os dados sob nossa responsabilidade, incluindo tráfego cifrado por HTTPS, controle de acesso às contas corporativas e princípio da menor exposição. Nenhum sistema é integralmente imune a incidentes; em caso de evento de segurança relevante, adotaremos as providências previstas no art. 48 da LGPD.</p>

        <h2>7. Seus direitos</h2>
        <p>A LGPD assegura a você, titular dos dados, o direito de obter a qualquer momento:</p>
        <ul className="legal-list">
          <li>confirmação da existência de tratamento e acesso aos dados;</li>
          <li>correção de dados incompletos, inexatos ou desatualizados;</li>
          <li>anonimização, bloqueio ou eliminação de dados desnecessários ou tratados em desconformidade com a lei;</li>
          <li>portabilidade a outro fornecedor, mediante requisição expressa;</li>
          <li>eliminação dos dados tratados com base no consentimento;</li>
          <li>informação sobre entidades com as quais os dados foram compartilhados;</li>
          <li>revogação do consentimento, quando esta for a base legal aplicável.</li>
        </ul>
        <p>Para exercer qualquer desses direitos, escreva para <a href="mailto:comercial@vpc-websistemas.com.br?subject=Exerc%C3%ADcio%20de%20direitos%20LGPD">comercial@vpc-websistemas.com.br</a>. Responderemos no menor prazo possível, podendo solicitar informações adicionais para confirmar sua identidade antes de atender ao pedido.</p>

        <h2>8. Sistemas desenvolvidos para clientes</h2>
        <p>Esta política trata exclusivamente do site institucional da VPC. Os sistemas que desenvolvemos e operamos para clientes possuem governança própria: nesses casos, a VPC atua tipicamente como <strong>operadora</strong>, tratando dados por conta e ordem do controlador contratante, segundo o que estiver definido no respectivo instrumento contratual.</p>

        <h2>9. Alterações desta política</h2>
        <p>Esta política pode ser revisada para refletir mudanças legais, técnicas ou de processo. A data de atualização no topo da página indica a versão vigente.</p>
      </div></section>
    </div>

    <footer id="rodape"><div className="shell footer-inner"><div className="footer-brand"><Image src="/simbolo-vpc-satelite.png" width="64" height="64" alt="" /><span><strong>VPC-WEBSISTEMAS E GEOINFORMAÇÃO</strong><small>Inteligência em geoprocessamento e sensoriamento remoto.</small></span></div><p>Vinicius do Prado Capanema Ltda.</p><p>CNPJ 57.286.005/0001-40 · © 2026 · Todos os direitos reservados.</p><p><Link className="footer-link" href="/privacidade">Política de Privacidade</Link></p></div></footer>
  </main>;
}
