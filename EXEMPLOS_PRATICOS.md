# 🔍 Exemplos Práticos de Investigação OSINT

> **Voltar para**: [README Principal](README.md) | [Guia Rápido](GUIA_RAPIDO.md)

## Índice
- [Caso 1: Due Diligence Empresarial](#caso-1)
- [Caso 2: Verificação de Pessoa Física](#caso-2)
- [Caso 3: Investigação de Fraude Imobiliária](#caso-3)
- [Caso 4: Verificação de Veículo](#caso-4)
- [Caso 5: Investigação de Servidor Público](#caso-5)
- [Caso 6: Rastreamento de Domínio Suspeito](#caso-6)
- [Dicas e Metodologias](#dicas)

---

## Caso 1: Due Diligence Empresarial {#caso-1}

### 🎯 Objetivo
Verificar idoneidade de empresa antes de estabelecer parceria comercial.

### 📋 Informações Necessárias
- CNPJ da empresa
- Razão Social
- Nome dos sócios (opcional)

### 🔎 Passo a Passo

#### **Etapa 1: Verificação Cadastral Básica**
```
1. CNPJ → Receita Federal
   URL: http://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp
   ✅ Verificar: Situação cadastral, data de abertura, capital social, sócios
```

#### **Etapa 2: Contrato Social e Alterações**
```
2. Razão Social → JUCESP (se SP)
   URL: https://www.jucesponline.sp.gov.br/pesquisa.aspx
   ✅ Verificar: Contrato social, alterações contratuais, atas
   ⚠️ Serviço pago para visualização completa
```

#### **Etapa 3: Relacionamento com Governo**
```
3. CNPJ → Portal da Transparência
   URL: https://portaldatransparencia.gov.br/
   ✅ Verificar: Contratos públicos, convênios, valores recebidos
   ✅ Verificar: Sanções, impedimentos, CEIS/CNEP
```

#### **Etapa 4: Reclamações e Reputação**
```
4. CNPJ → Consumidor.gov.br
   URL: https://www.consumidor.gov.br/
   ✅ Verificar: Quantidade de reclamações, taxa de resposta, nota

5. Razão Social → PROCON-SP
   URL: https://www.procon.sp.gov.br/
   ✅ Verificar: Processos administrativos, notificações
```

#### **Etapa 5: Histórico Judicial**
```
6. CNPJ → CNJ PJe
   URL: https://www.cnj.jus.br/pjeconsulta/
   ✅ Verificar: Processos judiciais ativos

7. Razão Social → JusBrasil/Escavador
   URL: https://www.jusbrasil.com.br/
   ✅ Verificar: Histórico completo de processos
```

#### **Etapa 6: Validação dos Sócios**
```
8. Nome dos Sócios → CNJ (processos)
   ✅ Verificar: Processos criminais, cíveis, trabalhistas

9. CPF Sócios → Receita Federal
   ✅ Verificar: Situação cadastral dos sócios
```

#### **Etapa 7: Presença Digital**
```
10. Domínio da Empresa → Registro.br
    URL: https://registro.br/tecnologia/ferramentas/whois/
    ✅ Verificar: Data de criação, responsável técnico

11. Razão Social → Google/LinkedIn
    ✅ Verificar: Presença online, redes sociais corporativas
```

### ✅ Checklist Final
- [ ] Empresa ativa na Receita Federal
- [ ] Sem pendências no CNPJ
- [ ] Sem sanções no Portal da Transparência
- [ ] Taxa de reclamações aceitável
- [ ] Sócios sem processos criminais graves
- [ ] Histórico judicial compatível com atividade
- [ ] Presença digital consistente

### 🚩 Red Flags (Sinais de Alerta)
- ⛔ CNPJ suspenso ou irregular
- ⛔ Empresa recém-criada com grandes contratos públicos
- ⛔ Sócios com múltiplas empresas inativas
- ⛔ Alta taxa de reclamações não respondidas
- ⛔ Processos trabalhistas em massa
- ⛔ Endereço fictício ou compartilhado
- ⛔ Capital social incompatível com atividade

---

## Caso 2: Verificação de Pessoa Física {#caso-2}

### 🎯 Objetivo
Background check para contratação, compliance ou parceria.

### 📋 Informações Necessárias
- Nome completo
- CPF (se disponível)
- Data de nascimento (opcional)

### 🔎 Passo a Passo

#### **Etapa 1: Validação Cadastral**
```
1. CPF → Receita Federal
   URL: https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp
   ✅ Verificar: Situação cadastral (regular/irregular/suspenso)
```

#### **Etapa 2: Histórico Judicial**
```
2. Nome Completo → CNJ PJe
   URL: https://www.cnj.jus.br/pjeconsulta/
   ✅ Verificar: Processos em tribunais estaduais e federais

3. Nome → Escavador
   URL: https://www.escavador.com/
   ✅ Verificar: Histórico completo de processos, publicações
```

#### **Etapa 3: Vínculos Governamentais**
```
4. CPF/Nome → Portal da Transparência
   URL: https://portaldatransparencia.gov.br/
   ✅ Verificar: Vínculos como servidor, bolsas, benefícios
   ✅ Verificar: Viagens oficiais, cartões corporativos
```

#### **Etapa 4: Participação Política**
```
5. Nome → TSE Divulga Candidaturas
   URL: https://divulgacandcontas.tse.jus.br/
   ✅ Verificar: Candidaturas anteriores, doações, prestação de contas
```

#### **Etapa 5: Pegada Digital**
```
6. Nome → LinkedIn
   ✅ Verificar: Histórico profissional, conexões, recomendações

7. Nome → Facebook/Instagram/Twitter
   ✅ Verificar: Postagens públicas, comportamento, conexões

8. Nome → Google
   ✅ Usar dorks: "nome completo" site:br
```

#### **Etapa 6: Segurança Digital**
```
9. E-mail → Have I Been Pwned
   URL: https://haveibeenpwned.com/
   ✅ Verificar: Exposição em vazamentos de dados

10. E-mail → Monitor Firefox
    URL: https://monitor.firefox.com/
    ✅ Verificar: Vazamentos recentes
```

#### **Etapa 7: Currículo e Formação**
```
11. Nome → Plataforma Lattes (se acadêmico)
    URL: https://buscatextual.cnpq.br/buscatextual/busca.do
    ✅ Verificar: Formação, publicações, projetos

12. Nome → E-MEC (validar diploma)
    URL: https://emec.mec.gov.br/
    ✅ Verificar: Instituição reconhecida pelo MEC
```

### ✅ Checklist Final
- [ ] CPF regular na Receita Federal
- [ ] Sem processos criminais graves
- [ ] Histórico profissional consistente
- [ ] Formação validada
- [ ] Redes sociais compatíveis com perfil
- [ ] Sem exposição crítica em vazamentos

### 🚩 Red Flags
- ⛔ CPF irregular ou suspenso
- ⛔ Processos criminais ocultos
- ⛔ Divergências no currículo
- ⛔ Diploma de instituição não reconhecida
- ⛔ Comportamento inadequado em redes sociais
- ⛔ Múltiplos vazamentos de dados

---

## Caso 3: Investigação de Fraude Imobiliária {#caso-3}

### 🎯 Objetivo
Validar autenticidade de propriedade e negociação imobiliária.

### 📋 Informações Necessárias
- Endereço completo do imóvel
- Matrícula do imóvel (se disponível)
- Nome/CPF do proprietário alegado

### 🔎 Passo a Passo

#### **Etapa 1: Validação Física**
```
1. Endereço → Google Maps / Street View
   ✅ Verificar: Existência física, condição, entorno
   ✅ Verificar: Histórico de imagens (evolução temporal)

2. CEP → Correios
   URL: https://www.correios.com.br/enviar-e-receber/ferramentas/consulta-cep
   ✅ Verificar: CEP válido, bairro correto
```

#### **Etapa 2: Documentação do Imóvel**
```
3. Matrícula → Cartório de Imóveis (presencial ou online)
   URL: https://www.registrodeimoveis.org.br/cartorios
   ✅ Verificar: Proprietário real, ônus, gravames, hipotecas
   ⚠️ Serviço geralmente pago

4. Endereço → IPTU (Prefeitura)
   ✅ São Paulo: https://iptu.prefeitura.sp.gov.br/
   ✅ Rio: https://carioca.rio/servicos/consulta-iptu/
   ✅ Verificar: Proprietário, débitos, área construída
```

#### **Etapa 3: Cadastro Ambiental (se rural)**
```
5. Coordenadas/Proprietário → CAR/SICAR
   URL: https://www.car.gov.br/#/consultar
   ✅ Verificar: Cadastro Ambiental Rural, área, proprietário
```

#### **Etapa 4: Validação do Proprietário**
```
6. CPF/CNPJ → Receita Federal
   ✅ Verificar: Situação cadastral do alegado proprietário

7. Nome Proprietário → CNJ
   ✅ Verificar: Ações judiciais sobre o imóvel
   ✅ Buscar: "endereço" ou "matrícula" no processo
```

#### **Etapa 5: Validação do Corretor**
```
8. Nome Corretor → CRECI
   URL: https://www.creci.org.br/ (por estado)
   ✅ Verificar: Registro ativo, situação regular
   ✅ Verificar: Empresa tem CRECI-J (pessoa jurídica)
```

#### **Etapa 6: Histórico de Anúncios**
```
9. Endereço → OLX, ZAP, Viva Real
   ✅ Verificar: Histórico de anúncios, valores, fotos
   ✅ Comparar: Informações consistentes

10. Endereço → Google (dorks)
    ✅ Buscar: "endereço completo" site:olx.com.br
```

### ✅ Checklist Final
- [ ] Imóvel existe fisicamente
- [ ] Matrícula válida e atualizada
- [ ] Proprietário confere com documentação
- [ ] Sem ônus ou gravames não declarados
- [ ] IPTU sem débitos (ou declarados)
- [ ] Corretor com CRECI ativo
- [ ] Valor compatível com mercado

### 🚩 Red Flags (Fraude Detectada)
- ⛔ Imóvel não existe no endereço informado
- ⛔ Proprietário diferente da matrícula
- ⛔ Matrícula falsa ou adulterada
- ⛔ Corretor sem CRECI ou inativo
- ⛔ Valor muito abaixo do mercado
- ⛔ Vendedor pressiona por sinal/entrada urgente
- ⛔ Processos judiciais sobre o imóvel
- ⛔ Múltiplas hipotecas não declaradas

---

## Caso 4: Verificação de Veículo {#caso-4}

### 🎯 Objetivo
Checagem completa antes de compra de veículo usado.

### 📋 Informações Necessárias
- Placa do veículo
- Chassi (se disponível)
- RENAVAM
- Nome/CPF do vendedor

### 🔎 Passo a Passo

#### **Etapa 1: Dados Básicos**
```
1. Placa → DETRAN (por estado)
   ✅ Verificar: Proprietário, débitos, restrições, multas
   ⚠️ Maioria requer cadastro

Exemplos por estado:
   - SP: https://www.detran.sp.gov.br/
   - RJ: https://www.detran.rj.gov.br/
   - MG: https://www.detran.mg.gov.br/
```

#### **Etapa 2: Histórico de Roubo/Furto**
```
2. Placa/Chassi → SINESP Cidadão
   ✅ Verificar: Registro de roubo/furto
   ⚠️ Requer app ou acesso restrito

3. Placa → Histórico de Leilão
   URL: https://www.portaldeleiloes.com/
   ✅ Verificar: Se foi leiloado (pode indicar sinistro)
```

#### **Etapa 3: Débitos e Restrições**
```
4. Placa → IPVA (estado específico)
   ✅ Verificar: Débitos de IPVA

5. RENAVAM → Multas
   ✅ Verificar: Multas pendentes, pontos CNH transferíveis
```

#### **Etapa 4: Validação do Vendedor**
```
6. CPF Vendedor → Receita Federal
   ✅ Verificar: Situação cadastral

7. Nome Vendedor → CNJ
   ✅ Verificar: Processos judiciais relacionados a fraudes
```

#### **Etapa 5: Recalls e Manutenção**
```
8. Chassi → PROCON Recall
   URL: https://sistemas.procon.sp.gov.br/recall/
   ✅ Verificar: Recalls pendentes do fabricante

9. Marca/Modelo → Site Fabricante
   ✅ Verificar: Campanhas de recall abertas
```

#### **Etapa 6: Valor de Mercado**
```
10. Modelo/Ano → FIPE
    URL: https://veiculos.fipe.org.br/
    ✅ Verificar: Valor de mercado (comparar com pedido)

11. Placa → Histórico de Anúncios
    ✅ Buscar: site:olx.com.br "placa"
    ✅ Verificar: Histórico de vendas anteriores
```

### ✅ Checklist Final
- [ ] Veículo sem restrição judicial ou roubo
- [ ] Débitos de IPVA e multas verificados
- [ ] Proprietário confere com documentação
- [ ] Chassi sem adulteração
- [ ] Recalls regularizados
- [ ] Valor compatível com FIPE

### 🚩 Red Flags
- ⛔ Restrição judicial ou alienação
- ⛔ Registro de roubo/furto
- ⛔ Chassi adulterado ou regravado
- ⛔ Débitos elevados não declarados
- ⛔ Vendedor com múltiplos processos de estelionato
- ⛔ Valor muito abaixo da FIPE
- ⛔ Documentação irregular ou falsa

---

## Caso 5: Investigação de Servidor Público {#caso-5}

### 🎯 Objetivo
Verificar vínculos, remuneração e transparência de servidor público.

### 🔎 Passo a Passo

```
1. Nome/CPF → Portal da Transparência
   URL: https://portaldatransparencia.gov.br/
   ✅ Verificar: Remuneração, cargo, órgão
   ✅ Verificar: Viagens oficiais, diárias, passagens

2. Nome → Dados JusBR
   URL: https://dadosjusbr.org/
   ✅ Verificar: Remuneração de membros do Judiciário

3. Nome → CNJ Improbidade
   URL: https://www.cnj.jus.br/improbidade_adm/
   ✅ Verificar: Processos de improbidade administrativa

4. CPF → TSE
   ✅ Verificar: Doações políticas, candidaturas

5. Nome → ABRAJI Publique-se
   URL: https://www.publique-se.org.br/
   ✅ Verificar: Processos com interesse público
```

---

## Caso 6: Rastreamento de Domínio Suspeito {#caso-6}

### 🎯 Objetivo
Investigar domínio suspeito de phishing ou fraude.

### 🔎 Passo a Passo

```
1. Domínio → Registro.br WHOIS
   URL: https://registro.br/tecnologia/ferramentas/whois/
   ✅ Verificar: Proprietário, data de criação, responsável

2. Domínio → RDAP
   URL: https://rdap.registro.br/domain/
   ✅ Verificar: Dados técnicos, nameservers

3. Domínio → VirusTotal
   URL: https://www.virustotal.com/
   ✅ Verificar: Reputação, detecções de malware

4. Domínio → URLScan.io
   URL: https://urlscan.io/
   ✅ Verificar: Screenshot, recursos carregados, redirects

5. CNPJ do Titular → Receita Federal
   ✅ Verificar: Se empresa existe e é legítima

6. Domínio → Google Safe Browsing
   ✅ Verificar: Status de segurança

7. Site → PROCON-SP Evite Site
   URL: https://sistemas.procon.sp.gov.br/evitesite/
   ✅ Verificar: Se está na lista de sites problemáticos
```

---

## 💡 Dicas e Metodologias {#dicas}

### 🎯 Metodologia OSINT Profissional

#### **1. Planejamento**
- Defina objetivo claro
- Liste informações necessárias
- Estabeleça limites éticos e legais
- Documente metodologia

#### **2. Coleta**
- Use múltiplas fontes
- Salve evidências (screenshots, PDFs)
- Registre data/hora de cada consulta
- Mantenha cadeia de custódia

#### **3. Análise**
- Cruze informações de diferentes fontes
- Identifique inconsistências
- Valide dados com fontes oficiais
- Documente discrepâncias

#### **4. Relatório**
- Seja objetivo e factual
- Cite todas as fontes
- Inclua evidências
- Apresente conclusões baseadas em fatos

### 🛡️ Segurança Operacional

- **Use VPN** para consultas sensíveis
- **Não faça login** em contas pessoais durante investigação
- **Crie personas** separadas se necessário
- **Documente tudo** em local seguro
- **Respeite privacidade** e legislação

### ⚖️ Aspectos Legais

- ✅ Consulte apenas **fontes públicas**
- ✅ Respeite a **LGPD**
- ✅ Tenha **propósito legítimo**
- ❌ Não invada sistemas
- ❌ Não pratique engenharia social
- ❌ Não compartilhe dados sensíveis publicamente

### 📚 Recursos Adicionais

- [README Principal](README.md) - Lista completa de fontes
- [Guia Rápido](GUIA_RAPIDO.md) - Tabelas e consultas rápidas
- [Fluxogramas](FLUXOGRAMA.md) - Diagramas visuais de processos
- [LGPD](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) - Lei de proteção de dados
- [LAI](http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm) - Lei de acesso à informação

---

<p align="center">
  <sub>Última atualização: Dezembro 2025</sub><br>
  <sub>Projeto OSINT Brazuca - Exemplos Práticos de Investigação</sub><br>
  <sub>⚠️ Uso responsável e ético das informações</sub>
</p>
