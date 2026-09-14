from pathlib import Path
from copy import deepcopy
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "fontes/templates/TEMPLATE_CORPORATIVO_VPC_WEBSISTEMAS.docx"
OUT = ROOT / "output/candidatura_tdr_006_2026"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "071B45"; BLUE = "0878D1"; GREEN = "67B900"; CYAN = "11B8D8"; PALE = "EAF4F8"; GRAY = "59677A"; YELLOW = "FFF2CC"

def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); shd = tcPr.find(qn("w:shd"))
    if shd is None: shd = OxmlElement("w:shd"); tcPr.append(shd)
    shd.set(qn("w:fill"), fill)

def margins(cell, top=100, start=110, bottom=100, end=110):
    tc = cell._tc.get_or_add_tcPr(); mar = tc.first_child_found_in("w:tcMar")
    if mar is None: mar = OxmlElement("w:tcMar"); tc.append(mar)
    for tag, value in (("top",top),("start",start),("bottom",bottom),("end",end)):
        el=mar.find(qn(f"w:{tag}"))
        if el is None: el=OxmlElement(f"w:{tag}"); mar.append(el)
        el.set(qn("w:w"),str(value)); el.set(qn("w:type"),"dxa")

def clear_body(doc):
    body=doc._element.body
    for child in list(body):
        if child.tag != qn("w:sectPr"): body.remove(child)

def set_font(run, size=10, bold=False, color="162238"):
    run.font.name="Arial"; run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"),"Arial"); run._element.rPr.rFonts.set(qn("w:hAnsi"),"Arial")
    run.font.size=Pt(size); run.font.bold=bold; run.font.color.rgb=RGBColor.from_string(color)

def configure(doc):
    sec=doc.sections[0]; sec.page_width=Cm(21); sec.page_height=Cm(29.7); sec.top_margin=Cm(2.1); sec.bottom_margin=Cm(1.8); sec.left_margin=Cm(2); sec.right_margin=Cm(2)
    for style_name, size, color, bold in [("Normal",9.6,"162238",False),("Heading 1",16,NAVY,True),("Heading 2",12,BLUE,True),("Heading 3",10.5,NAVY,True)]:
        st=doc.styles[style_name]; st.font.name="Arial"; st._element.rPr.rFonts.set(qn("w:ascii"),"Arial"); st._element.rPr.rFonts.set(qn("w:hAnsi"),"Arial"); st.font.size=Pt(size); st.font.bold=bold; st.font.color.rgb=RGBColor.from_string(color)
        st.paragraph_format.space_after=Pt(5 if style_name=="Normal" else 7)
        st.paragraph_format.space_before=Pt(0 if style_name=="Normal" else 8)
    return doc

def new_doc():
    doc=Document(TEMPLATE); clear_body(doc); configure(doc); return doc

def add_title(doc, title, subtitle):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before=Pt(16); p.paragraph_format.space_after=Pt(6)
    set_font(p.add_run(title),22,True,NAVY)
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after=Pt(18); set_font(p.add_run(subtitle),11,False,BLUE)
    t=doc.add_table(rows=3, cols=2); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
    labels=[("Processo","TdR 006/2026 - TNC Brasil / Projeto Restaura Biomas"),("Proponente","Vinicius do Prado Capanema Ltda. | CNPJ 57.286.005/0001-40"),("Validade","30 dias a partir do prazo de submissão")]
    for row,(a,b) in zip(t.rows,labels):
        row.cells[0].width=Cm(3.2); row.cells[1].width=Cm(13.2); shade(row.cells[0],NAVY); shade(row.cells[1],PALE)
        for c in row.cells: margins(c); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
        set_font(row.cells[0].paragraphs[0].add_run(a),9,True,"FFFFFF"); set_font(row.cells[1].paragraphs[0].add_run(b),9,False,NAVY)
    doc.add_paragraph()

def p(doc, text, bold_lead=None):
    q=doc.add_paragraph(); q.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_lead and text.startswith(bold_lead): set_font(q.add_run(bold_lead),9.6,True,NAVY); set_font(q.add_run(text[len(bold_lead):]),9.6)
    else: set_font(q.add_run(text),9.6)
    return q

def bullet(doc,text):
    q=doc.add_paragraph(style="List Bullet"); q.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY; set_font(q.add_run(text),9.3); return q

def heading(doc,text,level=1): doc.add_heading(text,level=level)

def table(doc, headers, rows, widths=None, small=8.3):
    t=doc.add_table(rows=1,cols=len(headers)); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
    for i,h in enumerate(headers):
        c=t.rows[0].cells[i]; shade(c,NAVY); margins(c); set_font(c.paragraphs[0].add_run(h),small,True,"FFFFFF")
    for row in rows:
        cells=t.add_row().cells
        for i,val in enumerate(row):
            margins(cells[i]); cells[i].vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if len(t.rows)%2==1: shade(cells[i],"F2F7FA")
            set_font(cells[i].paragraphs[0].add_run(str(val)),small,False,"162238")
    if widths:
        for row in t.rows:
            for i,w in enumerate(widths): row.cells[i].width=Cm(w)
    return t

def page_break(doc): doc.add_page_break()

def technical():
    d=new_doc(); add_title(d,"PROPOSTA TÉCNICA E APRESENTAÇÃO PROFISSIONAL","Sistema de Monitoramento Geoespacial e Reporte da Recuperação da Vegetação Nativa do Brasil - perfil front-end")
    heading(d,"1. Apresentação da pessoa jurídica")
    p(d,"A VPC-WEBSISTEMAS E GEOINFORMAÇÃO é uma empresa brasileira de engenharia digital e geoinformação que desenvolve soluções sob medida para transformar dados técnicos e territoriais em sistemas operacionais. Reúne geoprocessamento, sensoriamento remoto, análise de dados e engenharia de software na concepção de WebGIS, dashboards, plataformas de dados, integrações e automações.")
    p(d,"A proposta responde ao desafio do Restaura Biomas de estruturar uma experiência front-end confiável para um sistema nacional, hospedado no INPE e alinhado ao TerraBrasilis. O trabalho será conduzido com arquitetura modular, interoperabilidade geoespacial, acessibilidade, desempenho, segurança, documentação e transferência de conhecimento.")
    heading(d,"2. Responsável técnico e equipe executora")
    p(d,"Vinicius do Prado Capanema - responsável técnico, arquiteto de solução e desenvolvedor front-end/geoespacial. Atuará diretamente em levantamento de requisitos, arquitetura, prototipação, biblioteca de componentes, integração, desenvolvimento, testes, conteinerização, documentação e reuniões técnicas.")
    table(d,["Formação","Instituição / área"],[("Doutorado","Sensoriamento Remoto - INPE"),("Mestrado","Sensoriamento Remoto - INPE"),("MBA","Gestão de Projetos - UNOPAR"),("Especialização","Georreferenciamento - AJES/INCRA"),("Graduação","Engenharia Florestal - UNEMAT")],[4,12.4],8.6)
    heading(d,"3. Experiência e aderência",1)
    p(d,"A trajetória profissional combina ciência ambiental, análise territorial e construção de sistemas digitais. Inclui atuação em monitoramento ambiental da Amazônia, classificação e validação de dados de sensoriamento remoto, planejamento territorial, infraestrutura logística e desenvolvimento de aplicações geoespaciais para instituições públicas.")
    table(d,["Experiência correlata","Aderência ao TdR"],[("SIGMA-PLI","Plataforma integrada de memória técnica, documentos, dados e informação geoespacial."),("SICARD","Cadastro, triagem socioambiental, análise territorial e hierarquização multicritério."),("FAD-Stats","Dashboards, filtros multidimensionais, estatística e visualização espacial de grandes conjuntos de dados."),("PLI Smart Router / HazardTrack / Reporta","Interfaces geoespaciais, serviços externos, monitoramento, mapas públicos e fluxos operacionais."),("Pesquisa no INPE e FUNCATE","Sensoriamento remoto, monitoramento ambiental, processamento espacial e produção técnico-científica.")],[5.2,11.2],8.2)
    page_break(d)
    heading(d,"4. Entendimento do objeto")
    p(d,"O sistema deverá converter uma metodologia nacional e um banco geoespacial em uma interface compreensível, auditável e sustentável. A solução deverá atender públicos técnicos e institucionais distintos, tornar visíveis indicadores e evidências territoriais, integrar serviços de back-end em evolução e operar com desempenho nos ambientes homologados pelo INPE.")
    p(d,"A abordagem considera desde o início usabilidade, acessibilidade, responsividade, interoperabilidade, segurança, escalabilidade e rastreabilidade. Protótipos serão validados com stakeholders antes da consolidação dos componentes, reduzindo retrabalho e mantendo decisões de interface vinculadas a requisitos verificáveis.")
    heading(d,"5. Metodologia e serviços ofertados")
    services=[("Descoberta e requisitos","Entrevistas e oficinas; inventário de usuários, jornadas, dados, APIs, regras, riscos e requisitos funcionais e não funcionais."),("Arquitetura de experiência","Arquitetura da informação, navegação, estados da interface, contratos de integração e critérios de aceite."),("Prototipação e validação","Wireframes e protótipos navegáveis; ciclos documentados de revisão com stakeholders."),("Sistema de design","Tokens, padrões de interação e biblioteca de componentes acessíveis e reutilizáveis."),("Desenvolvimento front-end","Interfaces responsivas para visualização e análise de dados espaciais, dashboards e WebGIS."),("Integração","Consumo de APIs REST e serviços geoespaciais WMS, WFS, TMS e CSW conforme disponibilidade da arquitetura."),("Qualidade","Testes funcionais, responsivos, de usabilidade, acessibilidade, compatibilidade e desempenho."),("Implantação e documentação","Docker, configuração para ambientes do INPE, documentação de arquitetura, componentes, integrações, operação e evolução.")]
    table(d,["Frente","Execução"],services,[4.2,12.2],8.0)
    heading(d,"6. Arquitetura e princípios técnicos")
    for x in ["Componentes modulares e baixo acoplamento entre visualização, regras de apresentação e clientes de API.","HTML semântico, navegação por teclado, contraste, foco visível e testes alinhados às WCAG.","Integração baseada em contratos versionados, tratamento explícito de carregamento, vazio, erro e indisponibilidade.","Desempenho orientado por métricas, carregamento progressivo e estratégias adequadas a dados geoespaciais volumosos.","Código versionado em Git, revisão técnica, automação de build/testes e imagens Docker reproduzíveis.","Documentação viva e transferência de conhecimento para reduzir dependência do fornecedor."]:
        bullet(d,x)
    page_break(d)
    heading(d,"7. Plano de trabalho e cronograma")
    p(d,"Adota-se duração contratual de 105 dias corridos. Como a soma literal dos intervalos sucessivos da tabela de produtos do TdR resulta em 190 dias, propõe-se execução parcialmente paralela e marcos comprimidos, sujeitos a alinhamento na reunião inicial. Essa interpretação preserva os seis produtos e o prazo global informado nas condições de contratação.")
    rows=[("P1","Dias 1-15","Requisitos e arquitetura do front-end","S1 + testes/reuniões transversais"),("P2","Dias 8-30","Protótipos e especificações de interfaces","S2-S3 + validação"),("P3","Dias 20-45","Biblioteca de componentes e estrutura-base integrada","S4 + testes"),("P4","Dias 35-80","Versão beta responsiva e acessível","S5-S6 + testes"),("P5","Dias 65-90","Plataforma integrada e homologada - primeira versão","S7 + homologação"),("P6","Dias 75-105","Implantação e documentação técnica","S8 + encerramento")]
    table(d,["Produto","Período","Objetivo / entrega","Serviços"],rows,[1.4,2.4,7.2,5.4],7.8)
    heading(d,"8. Produtos e critérios de aceite")
    products=[("Produto 1","Documento de requisitos, arquitetura, mapa de integrações, riscos e critérios de aceite."),("Produto 2","Protótipos navegáveis e especificações de interface validadas com stakeholders."),("Produto 3","Biblioteca documentada de componentes e estrutura-base conectada aos contratos do back-end."),("Produto 4","Versão beta funcional, responsiva, acessível e acompanhada de evidências de testes."),("Produto 5","Primeira versão integrada, conteinerizada e homologada nos ambientes definidos pelo INPE."),("Produto 6","Pacote de implantação e documentação de arquitetura, componentes, integrações, operação e manutenção.")]
    table(d,["Entrega","Conteúdo verificável"],products,[3.1,13.3],8.2)
    heading(d,"9. Governança, validação e comunicação")
    p(d,"Serão mantidos backlog rastreável, registro de decisões, demonstrações incrementais e critérios de aceite por produto. Reuniões técnicas apoiarão integração, desempenho, segurança, interoperabilidade e gestão de dependências. A execução observará as salvaguardas ambientais e sociais do projeto e divulgará os canais da Ouvidoria do Restaura Biomas quando houver atividades com público engajado.")
    heading(d,"10. Tecnologias e ferramentas")
    p(d,"JavaScript/TypeScript, HTML5, CSS3, React, D3.js ou bibliotecas equivalentes de visualização, APIs REST, padrões OGC, bancos espaciais, Git/GitHub, Docker, YAML, Linux e práticas CI/CD. A seleção final será compatibilizada com a arquitetura e os padrões definidos pelo MMA, INPE e parceiros.")
    heading(d,"11. Declaração de disponibilidade")
    p(d,"A equipe proposta possui disponibilidade para execução remota, reuniões técnicas e pelo menos uma viagem a São José dos Campos - INPE, conforme previsto no TdR. O detalhamento operacional será consolidado na reunião de início.")
    d.save(OUT/"01_PROPOSTA_TECNICA_E_CV_VPC_TDR_006_2026.docx")

def commercial():
    d=new_doc(); add_title(d,"PROPOSTA COMERCIAL","TdR 006/2026 - Sistema de Monitoramento e Reporte Nacional")
    heading(d,"1. Orçamento detalhado")
    p(d,"A proposta considera contrato por preço fixo, execução por pessoa jurídica e dedicação estimada de 600 horas técnicas do responsável, incluindo todos os serviços, reuniões, documentação, testes, encargos, tributos, despesas administrativas e uma viagem a São José dos Campos - SP.")
    table(d,["Equipe executora","Perfil","Valor/hora","Horas","Total"],[("Vinicius do Prado Capanema","Especialista front-end e geoespacial","R$ 250,00","600","R$ 150.000,00")],[4.2,5.1,2.7,1.5,3.2],8)
    heading(d,"2. Cronograma de desembolso")
    rows=[("Produto 1","Dia 15","10%","R$ 15.000,00"),("Produto 2","Dia 30","17,5%","R$ 26.250,00"),("Produto 3","Dia 45","17,5%","R$ 26.250,00"),("Produto 4","Dia 80","17,5%","R$ 26.250,00"),("Produto 5","Dia 90","17,5%","R$ 26.250,00"),("Produto 6","Dia 105","20%","R$ 30.000,00"),("TOTAL","-","100%","R$ 150.000,00")]
    t=table(d,["Produto","Entrega proposta","Percentual","Valor"],rows,[3,4.5,3.5,5.2],8.3)
    for row in t.rows[1:]:
        for c in row.cells:
            if "PREENCHER" in c.text: shade(c,YELLOW)
    heading(d,"3. Narrativa orçamentária")
    for lead,text in [("Honorários técnicos. ","Cobrem levantamento de requisitos, arquitetura, prototipação, sistema de design, desenvolvimento, integração, testes, conteinerização, documentação, reuniões e apoio à homologação."),("Despesas e viagem. ","O valor global contempla deslocamento, hospedagem, alimentação e locomoção necessários para pelo menos uma agenda presencial no INPE em São José dos Campos."),("Tributos, taxas e encargos. ","Todos os tributos incidentes, taxas, custos administrativos e demais ônus diretos ou indiretos estão incorporados ao valor global, sem cobrança adicional."),("Pagamento. ","Valores vinculados à entrega, aprovação de cada produto e apresentação da respectiva Nota Fiscal, conforme condições a serem formalizadas contratualmente.")]:
        p(d,lead+text,lead)
    heading(d,"4. Dados da empresa")
    data=[("Nome fantasia","VPC-WEBSISTEMAS E GEOINFORMAÇÃO"),("Razão social","Vinicius do Prado Capanema Ltda."),("CNPJ","57.286.005/0001-40"),("Inscrição Municipal (CCM)","1.501.676-5"),("Endereço","Rua Sérgio Tomás, 422, ap. 206, Torre Fly, Bom Retiro, São Paulo - SP, CEP 01131-010"),("Objeto na Nota Fiscal","Consultoria especializada em desenvolvimento front-end de sistema geoespacial"),("Código do serviço","01521 - Engenharia e congêneres"),("Responsável legal / CPF","Vinicius do Prado Capanema / 014.992.961-77"),("E-mail / telefone","comercial@vpc-websistemas.com.br / (11) 92252-9858"),("Banco / agência / conta PJ","Banco Bradesco | Agência 0549 | Conta corrente 42917-1")]
    t=table(d,["Campo","Informação"],data,[5,11.4],8.2)
    for row in t.rows[1:]:
        if "PREENCHER" in row.cells[1].text: shade(row.cells[1],YELLOW)
    heading(d,"5. Condições gerais")
    bullet(d,"Moeda: Real brasileiro (R$).")
    bullet(d,"Validade: 30 dias a partir do prazo de submissão.")
    bullet(d,"Valor global fechado, incluindo lucro, taxas, impostos, despesas e demais custos necessários à execução integral.")
    bullet(d,"Cronograma financeiro condicionado à entrega e aprovação dos produtos.")
    p(d,"Valor global da proposta: R$ 150.000,00", "Valor global da proposta: ")
    p(d,"São Paulo, 03 de setembro de 2026.")
    table(d,["Assinatura do responsável legal","Nome e qualificação"],[("ASSINAR DIGITALMENTE","Vinicius do Prado Capanema\nResponsável legal - Vinicius do Prado Capanema Ltda.")],[6.2,10.2],8.2)
    d.save(OUT/"02_PROPOSTA_COMERCIAL_VPC_TDR_006_2026.docx")

def annex():
    d=new_doc(); add_title(d,"DECLARAÇÃO DO PROPONENTE","Anexo A - Transparência, Integridade, Responsabilidade Ambiental e Social")
    sec=d.sections[0]; sec.top_margin=Cm(1.7); sec.bottom_margin=Cm(1.5)
    p(d,"A Vinicius do Prado Capanema Ltda., inscrita no CNPJ 57.286.005/0001-40, por seu responsável legal, declara compreender e aceitar os padrões de transparência, justiça e integridade aplicáveis às aquisições da TNC Brasil e do Projeto Restaura Biomas, bem como os Códigos de Conduta e a Política de Práticas Proibidas referidos no TdR 006/2026.")
    heading(d,"I. Transparência e integridade")
    bullet(d,"Compromete-se com os mais altos padrões de transparência, justiça, integridade e conformidade durante a candidatura e eventual execução contratual.")
    bullet(d,"Declara não ter participado da redação ou recomendação do escopo deste processo, não praticar conluio ou fixação de preços e não oferecer vantagem indevida.")
    bullet(d,"Declara não adotar medidas que restrinjam a participação de outras empresas, organizações ou indivíduos no processo competitivo.")
    heading(d,"II. Responsabilidade social e ambiental")
    bullet(d,"Compromete-se com a proteção dos direitos humanos e com a proibição de tráfico de pessoas, trabalho infantil, trabalho forçado, abuso, exploração ou assédio sexual.")
    bullet(d,"Respeita os padrões ambientais e sociais reconhecidos internacionalmente, as convenções fundamentais da OIT e a legislação aplicável.")
    bullet(d,"Compromete-se a proteger pessoas vulneráveis, habitats naturais, biodiversidade e os ecossistemas relacionados às atividades contratadas.")
    heading(d,"III. Elegibilidade e conduta profissional")
    bullet(d,"Declara que a empresa, seus afiliados e contratados não se encontram em falência, liquidação ou encerramento de atividade e não foram declarados culpados de má conduta profissional grave.")
    bullet(d,"Declara não ter praticado atos criminosos ou fraudulentos e não ter condenação transitada em julgado, nos últimos cinco anos, por fraude, corrupção, lavagem de dinheiro ou má conduta profissional.")
    bullet(d,"Declara estar em dia com obrigações previdenciárias e tributárias aplicáveis.")
    bullet(d,"Declara não fornecer suporte material ou recursos a pessoas ou entidades ligadas a atos terroristas e observar as Leis nº 13.260/2016 e nº 9.613/1998.")
    bullet(d,"Declara que a empresa, seus diretores, executivos, funcionários-chave e proprietários beneficiários não constam das listas de sanções, impedimentos ou suspensões referidas no art. 39 da Lei nº 13.019/2014.")
    p(d,"CERTIFICO QUE AS INFORMAÇÕES FORNECIDAS ACIMA ESTÃO COMPLETAS E CORRETAS, DE ACORDO COM O MEU CONHECIMENTO.")
    table(d,["Assinatura do proponente","Nome e cargo","Data"],[("ASSINAR DIGITALMENTE","Vinicius do Prado Capanema - Responsável legal","03/09/2026")],[5.2,7.4,3.8],8.0)
    for para in d.paragraphs[2:]:
        para.paragraph_format.space_before=Pt(1.5)
        para.paragraph_format.space_after=Pt(2.5)
        for run in para.runs:
            if run.font.size and run.font.size.pt > 9:
                run.font.size=Pt(8.7)
    d.save(OUT/"03_ANEXO_A_DECLARACAO_VPC_TDR_006_2026.docx")

technical(); commercial(); annex()
print(OUT)
