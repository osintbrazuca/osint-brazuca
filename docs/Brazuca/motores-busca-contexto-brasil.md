---
title: Motores de Busca Contexto Brasil
---
# Motores de Busca Contexto Brasil 🤖
## Google Hacking: DataLeak/SQL
```
site:com.br ext:sql "CREATE TABLE"

https://www.google.com/search?q=site%3Acom.br+ext%3Asql+%22CREATE+TABLE%22##
```
```
site:com.br intext:"phpMyAdmin" ext:txt

https://www.google.com/search?q=site%3Acom.br+intext%3A%22phpMyAdmin%22+ext%3Atxt
```

---
## Google Hacking: Documento em Arquivos
```
cpf "SEU_ALVO" ext:txt

https://www.google.com/search?q=cpf+%22SE_ALVO%22+%22123456789%22+ext
```
```
"cpf|cnpj|email|rg|contato" ext:xls "SEU_ALVO"

https://www.google.com/search?q=%22cpf%7Ccnpj%7Cemail%7Crg%7Ccontato%22+ext%3Axls+%22SE_ALVO%22
```

---
## Google Hacking: Sites do Governo
Adicione sua string alvo para direcionar a busca
```
site:mil.br

https://www.google.com/search?q=site%3Amil.br
```
```
site:gov.br

https://www.google.com/search?q=site%3Agov.br
```

---
## Google Hacking:  Documentos em Sites do Governo
Adicione sua string alvo para direcionar a busca
```
site:mil.br ext:pdf

https://www.google.com/search?q=site%3Amil.br
```
```
site:gov.br  ext:xls

https://www.google.com/search?q=site%3Agov.br
```
```
inurl:"mil.br" ext:php

https://www.google.com/search?q=inurl:%22mil.br%22+ext:php
```

---
## Google Hacking: Informações Expostas
Adicione sua string alvo para direcionar a busca
```
site:anonfiles.com "SE_ALVO"

https://www.google.com/search?q=site%3Aanonfiles.com+%22SE_ALVO%22
```
```
site:docs.google.com "SEU_ALVO"

https://www.google.com/search?q=site%3Adocs.google.com+%22SEU_ALVO%E2%80%9D
```
```
site:facebook.com "SEU_ALVO"

https://www.google.com/search?q=site%3Afacebook.com+%22SEU_ALVO%22
```
```
site:pastebin.com "SEU_ALVO" 

https://www.google.com/search?q=site%3Apastebin.com+%22nubank%22
```

---
## Google Hacking: Filtrar Empresa via Linkedin
Adicione sua string alvo para direcionar a busca
```
site:linkedin.com "at EMPRESA_ALVO"

https://www.google.com/search?q=site%3Alinkedin.com+%22at+EMPRESA_ALVO%22
```

---
## Google Hacking: Filtrar Grupos WhatsApp em Sites .br
```
"https://chat.whatsapp.com/" & site:br"

https://www.google.com/search?q=%22https%3A%2F%2Fchat.whatsapp.com%2F%22+%26+site%3Abr
```

---
## Google Hacking: Filtrar Grupos Telegram + Contexto da String
```
inurl:"https://t.me" site:me "SEU_ALVO"

https://www.google.com/search?q=inurl%3A%22https%3A%2F%2Ft.me%22+site%3Ame+%22SEU_ALVO%22
```
```
site:me "joinchat" "SEU_ALVO"

https://www.google.com/search?q=site%3Ame+%22joinchat%22+%22Bolsonaro%22
```

---
## Google Hacking: Identificar Powerbi Exposto
```
site:app.powerbi.com/view?r intext:"br"

https://www.google.com/search?q=site%3Aapp.powerbi.com%2Fview%3Fr+intext%3A%22br%22
```
```
site:app.powerbi.com/view?r intext:"brasil"

https://www.google.com/search?q=site%3Aapp.powerbi.com%2Fview%3Fr+intext%3A%22brasil%22
```

---
## Shodan: Busca de Servidores Brasileiro
Shodan é um mecanismo de pesquisa que permite ao usuário encontrar tipos específicos de computadores conectados à Internet usando uma variedade de filtros.
```
country:"BR"

https://www.shodan.io/search?query=country%3A%22BR%22
```