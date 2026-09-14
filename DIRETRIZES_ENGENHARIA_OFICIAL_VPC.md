# Diretrizes de Engenharia Oficiais — VPC-WEBSISTEMAS E GEOINFORMAÇÃO

**Versão:** 1.0  
**Data:** 03 de setembro de 2026  
**Estado:** vigente

## 1. Princípios de engenharia

1. Soberania tecnológica e preferência por soluções abertas.
2. Modularidade e baixo acoplamento.
3. Padronização estrutural.
4. Segurança desde a concepção.
5. Observabilidade, rastreabilidade e auditabilidade.
6. Soberania, interoperabilidade e portabilidade dos dados.
7. Reprodutibilidade e automação.
8. Customização sem fragmentação.
9. Qualidade e testabilidade.
10. Experiência consistente, preservando a identidade do cliente.
11. Geoinformação como capacidade nativa sempre que houver dimensão espacial relevante.

## 2. Arquitetura de referência

As soluções são organizadas em sete blocos:

1. **Experiência:** interfaces, acessibilidade, navegação e interação.
2. **Aplicação:** casos de uso, coordenação de fluxos e serviços de aplicação.
3. **Domínio:** regras, entidades e invariantes do negócio.
4. **Dados:** persistência, qualidade, metadados, intercâmbio e ciclo de vida.
5. **Integrações:** APIs, serviços externos e padrões de interoperabilidade.
6. **Plataforma:** infraestrutura, segurança, entrega, operação e observabilidade.
7. **IA e Agentes:** capacidade transversal, controlada e substituível.

Os componentes devem ser classificados conforme seu pertencimento:

- **Core**;
- **Shared Capabilities**;
- **Solution Domain**;
- **Client Layer**.

## 3. Diretriz de inteligência artificial

- abstrair provedores por contratos substituíveis;
- não depender exclusivamente de modelos generativos em decisões críticas;
- preservar regras determinísticas onde necessárias;
- avaliar qualidade e riscos;
- monitorar comportamento e custos;
- manter fallback e operação degradada quando aplicável;
- registrar rastreabilidade compatível com o risco do processo.

## 4. Capacidades demonstráveis

- Python e FastAPI;
- JavaScript/TypeScript;
- React;
- HTML e CSS;
- PostgreSQL/PostGIS;
- GeoServer e QGIS Server;
- Leaflet;
- APIs REST;
- WMS e WFS;
- ETL/ELT geoespacial;
- AWS EC2 e RDS;
- Docker;
- Git e GitHub;
- CI/CD;
- PyMuPDF e Tesseract;
- autenticação e controle de acesso;
- monitoramento, logs e auditoria.

Uma tecnologia somente deve ser citada como experiência comprovada quando estiver documentada em projeto ou currículo.

## 5. Aplicação ao site institucional

A primeira versão do site deve ser estática e simples de operar, sem back-end salvo necessidade comprovada. Deve priorizar HTML semântico, responsividade, acessibilidade, desempenho, segurança, metadados, portabilidade e manutenção direta.

## 6. Planejamento futuro

Os estudos históricos sobre fábrica de aplicações, manifesto, trial e produtos Business permanecem como material de referência em `legado/`. Eles não constituem autorização automática para implementação nem substituem validação comercial, jurídica, técnica e operacional futura.

