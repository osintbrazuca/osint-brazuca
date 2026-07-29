# 🤝 Como Contribuir com o OSINT Brazuca

<p align="center">
  <a href="README.md"><img alt="README Principal" src="https://img.shields.io/badge/%F0%9F%8F%A0%20README%20Principal-1E88E5?style=flat-square"></a>
  <a href="EXEMPLOS_PRATICOS.md"><img alt="Exemplos Práticos" src="https://img.shields.io/badge/%F0%9F%93%96%20Exemplos%20Pr%C3%A1ticos-2E7D32?style=flat-square"></a>
  <a href="FLUXOGRAMA.md"><img alt="Fluxogramas" src="https://img.shields.io/badge/%F0%9F%94%80%20Fluxogramas-6A1B9A?style=flat-square"></a>
  <a href="GUIA_RAPIDO.md"><img alt="Guia Rápido" src="https://img.shields.io/badge/%F0%9F%93%8A%20Guia%20R%C3%A1pido-EF6C00?style=flat-square"></a>
  <a href="CONTRIBUICAO.md"><img alt="Contribuir" src="https://img.shields.io/badge/%F0%9F%A4%9D%20Contribuir-00838F?style=flat-square"></a>
  <a href="data/"><img alt="Dataset" src="https://img.shields.io/badge/%F0%9F%97%82%EF%B8%8F%20Dataset-F9A825?style=flat-square"></a>
  <a href="tools/"><img alt="Ferramentas" src="https://img.shields.io/badge/%F0%9F%9B%A0%EF%B8%8F%20Ferramentas-546E7A?style=flat-square"></a>
</p>

Obrigado por considerar contribuir com o projeto OSINT Brazuca! Este documento fornece diretrizes para diferentes tipos de contribuições.

---

## 📋 Tipos de Contribuição

### 1. 🔗 Reportar Links Quebrados

Se você encontrou um link que não está funcionando:

**Crie uma Issue com as seguintes informações:**
- **Título**: `[LINK QUEBRADO] Nome da fonte`
- **Descrição**: 
  - URL completo do link quebrado
  - Data em que testou
  - Tipo de erro (404, timeout, redirecionamento, etc.)
  - Se possível, sugira uma alternativa

**Exemplo:**
```markdown
**Título:** [LINK QUEBRADO] Consulta CNPJ Receita Federal

**Descrição:**
- URL: http://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/
- Data do teste: 02/02/2026
- Erro: 404 - Página não encontrada
- Alternativa sugerida: https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/
```

---

### 2. ➕ Adicionar Novas Fontes

Quer adicionar uma nova fonte de informação pública?

**Antes de submeter:**
1. ✅ Verifique se a fonte já não existe no README
2. ✅ Teste o link para garantir que está funcionando
3. ✅ Confirme que a fonte é **pública** e **legal**
4. ✅ Verifique se está no contexto brasileiro

**Informações a fornecer:**
- Nome da fonte
- Descrição clara e objetiva
- URL (testado e funcionando)
- Categoria apropriada
- Indicar se é gratuito ou pago
- Indicar se requer cadastro

**Exemplo de formatação:**
```markdown
### Nome da Nova Fonte
Descrição clara explicando o que a fonte oferece e qual tipo de informação pode ser consultada.

<details>
<summary>Links de pesquisa</summary>

- https://exemplo.gov.br/consulta
- https://exemplo.gov.br/api (se houver)

</details>
```

---

### 3. 📝 Melhorar Documentação

Contribuições para melhorar a documentação são sempre bem-vindas:

- Corrigir erros ortográficos ou gramaticais
- Melhorar explicações existentes
- Adicionar exemplos práticos
- Traduzir termos técnicos
- Melhorar a formatação

---

### 4. 🔧 Desenvolver Ferramentas

Contribuições técnicas também são valiosas:

- Scripts de automação para consultas
- Integrações com APIs públicas
- Parsers de dados
- Ferramentas de validação de links
- Conversores de formato

**Requisitos:**
- Código bem documentado
- Instruções claras de uso
- Respeitar as limitações das APIs
- Incluir avisos sobre LGPD

---

## 🔄 Processo de Pull Request

### Passo a Passo

1. **Fork o Repositório**
   - Clique em "Fork" no canto superior direito

2. **Clone seu Fork**
   ```bash
   git clone https://github.com/SEU-USUARIO/osint-brazuca.git
   cd osint-brazuca
   ```

3. **Crie uma Branch**
   ```bash
   git checkout -b minha-contribuicao
   ```
   
   **Convenção de nomes:**
   - `adicionar-fonte-X` - para novas fontes
   - `corrigir-link-Y` - para correções de links
   - `melhorar-docs-Z` - para melhorias na documentação

4. **Faça suas Alterações**
   - Edite os arquivos necessários
   - Siga os padrões de formatação (veja abaixo)
   - Teste todas as URLs adicionadas

5. **Regenere o Dataset** (se mexeu em fontes ou URLs do README)
   ```bash
   python3 tools/build_dataset.py
   ```
   Isso atualiza `data/sources.json` e `data/index.json`. Inclua esses arquivos no commit.
   Veja a seção [Dataset JSON](#dataset-json) abaixo.

6. **Commit suas Mudanças**
   ```bash
   git add .
   git commit -m "Adiciona fonte de consulta X"
   ```
   
   **Boas práticas para mensagens de commit:**
   - Use verbos no imperativo ("Adiciona", "Corrige", "Atualiza")
   - Seja específico e conciso
   - Explique o "por quê" se necessário

7. **Push para seu Fork**
   ```bash
   git push origin minha-contribuicao
   ```

8. **Abra um Pull Request**
   - Acesse o repositório original no GitHub
   - Clique em "New Pull Request"
   - Selecione sua branch
   - Preencha a descrição detalhadamente

**Template para Pull Request:**
```markdown
## Tipo de Mudança
- [ ] Nova fonte
- [ ] Correção de link
- [ ] Melhoria de documentação
- [ ] Outra (especifique)

## Descrição
Descreva claramente as mudanças realizadas.

## Checklist
- [ ] Testei todos os links adicionados
- [ ] Segui o padrão de formatação do projeto
- [ ] Verifiquei que não há duplicatas
- [ ] Rodei `python3 tools/build_dataset.py` e incluí os JSON atualizados
- [ ] Li as diretrizes de contribuição
- [ ] Minhas mudanças respeitam a LGPD

## Informações Adicionais
Qualquer contexto adicional sobre as mudanças.
```

---

## 🗂️ Dataset JSON <a name="dataset-json"></a>

O README é a fonte de verdade do catálogo. A pasta `data/` contém uma versão estruturada dele, usada para busca por tipo de entrada e de retorno.

```bash
python3 tools/build_dataset.py            # regenera o dataset
python3 tools/build_dataset.py --report   # mostra estatísticas e fontes sem classificação
python3 tools/build_dataset.py --check    # só verifica se está atualizado
```

Requer apenas Python 3, sem dependências.

| Arquivo | O que é |
|---|---|
| `data/sources.json` | **Gerado.** Uma entrada por fonte, com os links aninhados. |
| `data/index.json` | **Gerado.** Um registro por link, achatado para busca. |
| `data/taxonomy.json` | Manual. Vocabulário permitido de `input`, `output` e `tipo_fonte`. |
| `data/overrides.json` | Manual. Correções de classificação, por fonte. |

> [!CAUTION]
> Nunca edite `sources.json` ou `index.json` à mão. Eles são sobrescritos no próximo build e seu trabalho é perdido.

### Corrigindo a classificação de uma fonte

Os campos `input` (o que a fonte aceita) e `output` (o que ela devolve) não existem no texto do README: são inferidos automaticamente por categoria e palavra-chave. Quando a inferência erra, corrija em `data/overrides.json`:

```json
{
  "overrides": {
    "apis-publicas-brasileiras/receitaws-api-cnpj": {
      "input": ["cnpj"],
      "output": ["api_json", "dados_cadastrais", "socios"],
      "observacao": "Rate limit de 3 requisições por minuto."
    }
  }
}
```

A chave é o `id` da fonte, visível em `sources.json`. Campos aceitos: `input`, `output`, `tipo_fonte`, `descricao`, `observacao`.

Todo termo é validado contra `taxonomy.json`. Para usar um termo novo, adicione-o lá antes, senão o build falha. Rode `--report` para ver a lista de fontes ainda sem classificação: são as que mais precisam de curadoria.

---

## 📐 Padrões de Formatação

### Pontuação

Não use travessão (`—`) em nenhum texto do projeto. Prefira vírgula, dois-pontos, ponto final ou parênteses. Em títulos de fonte, separe com hífen simples:

```markdown
### IBAMA - Consulta de Autuações Ambientais
```

### Alertas

Para destaques, use os alertas nativos do GitHub em vez de negrito com emoji. Os cinco tipos válidos são `NOTE`, `TIP`, `IMPORTANT`, `WARNING` e `CAUTION`:

```markdown
> [!WARNING]
> Respeite os limites de requisição das APIs públicas.
```

O marcador fica sozinho na primeira linha e todo o conteúdo seguinte é prefixado com `>`. Use com parcimônia: alerta em excesso perde o efeito. O menu de navegação no topo de cada documento é um bloco de badges centralizado (`<p align="center">` com badges do shields.io), idêntico em todos os arquivos: ao alterar um item do menu, replique a mudança em todos os documentos.

### Estrutura de Seções

```markdown
### Nome da Fonte
Descrição objetiva da fonte, explicando que tipo de informação pode ser consultada.

<details>
<summary>Links de pesquisa</summary>

- https://exemplo1.gov.br/
- https://exemplo2.gov.br/

</details>
```

### Para Fontes Únicas (sem details)

```markdown
### Nome da Fonte
Descrição da fonte.
- https://exemplo.gov.br/
```

### Para APIs

```markdown
### Nome da API
Descrição da API e seus recursos.

**Documentação:** https://api.exemplo.gov.br/docs

**Requisitos:**
- Autenticação: Chave API (solicitar em: link)
- Rate Limit: X requisições/minuto
- Formato: JSON

<details>
<summary>Exemplo de uso</summary>

```python
import requests

url = "https://api.exemplo.gov.br/v1/consulta"
headers = {"Authorization": "Bearer SUA_CHAVE"}
response = requests.get(url, headers=headers)
print(response.json())
```

</details>
```

### Para Listas por Estado

```markdown
### Consulta por Estado

<details>
<summary>Links por estado</summary>

**São Paulo:**
- Portal: https://sp.gov.br/consulta

**Rio de Janeiro:**
- Portal: https://rj.gov.br/consulta

</details>
```

---

## ✅ Checklist Antes de Submeter

Antes de enviar seu Pull Request, verifique:

- [ ] **Contexto brasileiro** - É relevante para o Brasil?
- [ ] **Testei todos os links** - Todos funcionam?
- [ ] **Não há duplicatas** - Já existe no README?
- [ ] **Formatação correta** - Segue os padrões?
- [ ] **Descrição clara** - É fácil entender?
- [ ] **Categoria apropriada** - Está na seção certa?
- [ ] **Fonte pública** - É de acesso público?


---

## 🚫 O Que NÃO Será Aceito

> [!CAUTION]
> Pull requests com qualquer um dos itens abaixo são recusados sem análise adicional.

- ❌ Links fora do contexto brasileiro
- ❌ Links fora do contexto proposto
- ❌ Links para foruns de fraud / exploits
- ❌ Conteúdo discriminatório
- ❌ Links afiliados ou spam
- ❌ Ferramentas pagas sem versão gratuita (exceto se oficial)

---

## 🏆 Reconhecimento

Todos os contribuidores serão:
- Listados na seção de **Contribuições** do README
- Creditados no histórico do Git
- Mencionados nas releases quando aplicável

---

## 📞 Dúvidas?

Se tiver dúvidas sobre como contribuir:

1. **Leia a documentação:** README.md, GUIA_RAPIDO.md
2. **Consulte Issues existentes:** Alguém já teve a mesma dúvida?
3. **Abra uma Discussion:** Para perguntas gerais
4. **Abra uma Issue:** Para problemas específicos

---

## 📜 Código de Conduta

Ao contribuir, você concorda em:

- ✅ Ser respeitoso com outros contribuidores
- ✅ Aceitar críticas construtivas
- ✅ Focar no melhor para a comunidade
- ✅ Demonstrar empatia com outros membros
- ✅ Respeitar diferentes pontos de vista

---

## 🎓 Primeiras Contribuições

Novo em contribuições open source? Sem problema!

**Boas primeiras contribuições:**
- Corrigir erros de digitação
- Atualizar links quebrados
- Melhorar descrições existentes
- Adicionar exemplos práticos

**Issues marcadas com:**
- `good first issue` - Boas para iniciantes
- `help wanted` - Precisam de ajuda
- `documentation` - Relacionadas a documentação

---

<p align="center">
  <strong>Obrigado por contribuir com o OSINT Brazuca! 🇧🇷</strong><br>
  <sub>Juntos estamos construindo a maior base de conhecimento OSINT do Brasil</sub>
</p>
