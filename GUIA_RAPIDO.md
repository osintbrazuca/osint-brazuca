# 📊 Guia Rápido de Consultas - OSINT Brazuca

> **Voltar para**: [README Principal](README.md)

## Índice
- [Tabela Comparativa por Tipo de Busca](#tabela-comparativa)
- [Top 10 Consultas Mais Utilizadas](#top-10)
- [Legenda de Status](#legenda)

---

## 📊 Tabela Comparativa por Tipo de Busca {#tabela-comparativa}

| Tipo de Busca | Categorias Principais | Quantidade de Fontes | Requer Cadastro? |
|---------------|----------------------|----------------------|------------------|
| **CPF** | Situação Cadastral, Processos, Benefícios | 15+ fontes | Algumas |
| **CNPJ** | Receita Federal, Juntas Comerciais, Transparência | 25+ fontes | Não |
| **Nome Completo** | Processos Judiciais, Redes Sociais, Eleições | 20+ fontes | Algumas |
| **Placa Veicular** | DETRAN, Multas, Leilões | 10+ fontes | Sim (maioria) |
| **Processos** | CNJ, TRFs, TJs, STF, STJ | 30+ tribunais | Não |
| **Imóveis** | IPTU, CAR, Cartórios | 8+ fontes | Algumas |
| **Empresas** | CNPJ, Contratos Públicos, Licitações | 15+ fontes | Não |
| **Telefone** | Operadora, Portabilidade, Cadastro Pré | 5+ fontes | Não |
| **E-mail** | Redes Sociais, Vazamentos, WHOIS | 10+ fontes | Algumas |
| **Domínios** | Registro.br, WHOIS, DNS | 5+ fontes | Não |

---

## 🎯 Top 10 Consultas Mais Utilizadas {#top-10}

### 1. **CNPJ - Receita Federal**
- **URL**: http://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp
- **Status**: 🟢 Gratuito | Oficial
- **O que retorna**: Situação cadastral, sócios, endereço, atividades

### 2. **CPF - Situação Cadastral**
- **URL**: https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp
- **Status**: 🟢 Gratuito | Oficial
- **O que retorna**: Situação cadastral (regular, irregular, suspenso)

### 3. **Processos - CNJ PJe**
- **URL**: https://www.cnj.jus.br/pjeconsulta/
- **Status**: 🟢 Gratuito | Oficial
- **O que retorna**: Processos judiciais em tribunais que usam PJe

### 4. **Nome Social - TRT3 Certidão**
- **URL**: https://sistemas.trt3.jus.br/certidao/feitosTrabalhistas/aba1.emissao.htm
- **Status**: 🟢 Gratuito | Oficial
- **O que retorna**: Nome completo a partir de CPF/CNPJ

### 5. **CNPJ - Portal da Transparência**
- **URL**: https://portaldatransparencia.gov.br/
- **Status**: 🟢 Gratuito | Oficial
- **O que retorna**: Contratos, convênios, favorecidos, sanções

### 6. **Telefone - Qual Operadora**
- **URL**: https://www.qualoperadora.net/
- **Status**: 🟢 Gratuito
- **O que retorna**: Operadora atual do número

### 7. **Imóvel - CAR/SICAR**
- **URL**: https://www.car.gov.br/#/consultar
- **Status**: 🟢 Gratuito | Oficial
- **O que retorna**: Cadastro Ambiental Rural, propriedades rurais

### 8. **Empresa - JUCESP**
- **URL**: https://www.jucesponline.sp.gov.br/pesquisa.aspx
- **Status**: 🟡 Parcialmente Pago
- **O que retorna**: Contratos sociais, alterações, atas (SP)

### 9. **Veículo - Leilão**
- **URL**: https://www.portaldeleiloes.com/
- **Status**: 🟢 Gratuito
- **O que retorna**: Veículos em leilão público

### 10. **Endereço - CEP Correios**
- **URL**: https://www.correios.com.br/enviar-e-receber/ferramentas/consulta-cep
- **Status**: 🟢 Gratuito | Oficial
- **O que retorna**: CEP, logradouro, bairro, cidade, UF

---

## 🏷️ Legenda de Status {#legenda}

| Ícone | Significado | Descrição |
|-------|------------|-----------|
| 🟢 | **Gratuito** | Acesso livre sem necessidade de pagamento |
| 🟡 | **Limitado/Parcialmente Pago** | Algumas funcionalidades gratuitas, outras pagas |
| 🔴 | **Pago** | Requer pagamento para acesso |
| 🔒 | **Requer Cadastro** | Necessário criar conta para usar |
| ⚠️ | **CAPTCHA** | Possui verificação CAPTCHA |
| 🔧 | **Ferramenta** | Script, bot ou aplicação |
| ⚖️ | **Oficial** | Fonte governamental/oficial |
| 📊 | **API Disponível** | Possui API para automação |

---

## 📌 Dicas Importantes

### ✅ Boas Práticas
- Sempre documente a fonte da informação
- Verifique a data de atualização dos dados
- Cruze informações de múltiplas fontes
- Respeite a LGPD e legislação vigente

### ⚠️ Atenção
- Alguns sites podem estar temporariamente offline
- Dados públicos podem estar desatualizados
- Nem todas as consultas retornam 100% de informações
- Respeite limites de requisições em APIs

### 🐛 Encontrou Problemas?
Se você encontrou alguma URL com problemas, ajude a comunidade:

**Reporte através de uma Issue no GitHub:**
1. Acesse: https://github.com/osintbrazuca/osint-brazuca/issues/new
2. Informe no título: `[URL] Nome da fonte com problema`
3. Descreva o problema:
   - ❌ **Offline**: Site fora do ar ou erro 404
   - 🔒 **Requer Login**: Antes era público, agora pede cadastro
   - ⚠️ **CAPTCHA Excessivo**: Impede uso automatizado
   - 🔄 **URL Mudou**: Site migrou para novo endereço
   - 🐌 **Lentidão**: Demora excessiva para carregar
4. Se possível, sugira uma alternativa

**Sua contribuição é valiosa!** Ajuda a manter o repositório atualizado e útil para todos.

### 🔒 Segurança
- Use VPN quando necessário
- Não compartilhe credenciais de acesso
- Cuidado com phishing em sites não oficiais
- Mantenha logs de suas consultas

---

## 🔗 Links Úteis

- [README Principal](README.md)
- [Exemplos Práticos de Investigação](EXEMPLOS_PRATICOS.md)
- [Fluxogramas de Investigação](FLUXOGRAMA.md)
- [Avisos Legais e LGPD](README.md#avisos-legais)
- [Repositório GitHub](https://github.com/osintbrazuca/osint-brazuca)

---

<p align="center">
  <sub>Última atualização: Dezembro 2025</sub><br>
  <sub>Projeto OSINT Brazuca - Inteligência de Fontes Abertas no Contexto Brasileiro</sub>
</p>
