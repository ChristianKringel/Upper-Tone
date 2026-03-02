# 🎵 Upper Tone - Editor de Notas Musicais

<div align="center">

**Transponha suas músicas de forma rápida e profissional**

![Version](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

</div>

---

## 📖 Sobre o Projeto

Upper Tone é um aplicativo moderno e intuitivo para edição de notas musicais em arquivos `.docx` e `.txt`. Com uma interface gráfica profissional construída com **CustomTkinter**, o aplicativo permite transpor músicas de forma rápida, precisa e sem complicações.

### ✨ Características Principais

- 🎨 **Interface Moderna**: Design profissional com tema dark, cards arredondados e animações suaves
- 🎹 **Controle Intuitivo**: Slider interativo para selecionar de 1 a 11 semitons
- ⬆️⬇️ **Direção Flexível**: Escolha entre subir ou descer tons
- 📁 **Múltiplos Formatos**: Suporta arquivos `.docx` e `.txt`
- ✅ **Feedback Visual**: Status em tempo real de cada operação
- 🚀 **Rápido e Preciso**: Processamento instantâneo mantendo a formatação original

---

## 🖥️ Interface do Usuário

A interface foi completamente redesenhada usando **CustomTkinter**, uma biblioteca moderna que oferece widgets personalizados e um visual profissional:

### 📝 Fluxo de Trabalho em 3 Passos

**Passo 1: Selecione o Arquivo**
- Clique no botão "Escolher Arquivo Musical"
- Selecione um arquivo `.docx` ou `.txt` com suas notas musicais
- O nome do arquivo aparecerá com um ✓ verde quando carregado

**Passo 2: Configure a Transposição**
- **Direção**: Escolha entre "Subir Tom" ou "Descer Tom"
- **Quantidade**: Use o slider para selecionar de 1 a 11 semitons
- O número selecionado aparece em destaque ao lado do slider

**Passo 3: Processar e Salvar**
- Clique no botão verde 🚀 "Processar Arquivo"
- Escolha o local e nome para salvar o arquivo transposto
- Receba confirmação visual do sucesso da operação

### 🎨 Elementos Visuais

- **Badges Numerados**: Cada passo tem um badge azul (1, 2, 3) para fácil identificação
- **Cards Escuros**: Seções organizadas em cards com cantos arredondados
- **Cores Inteligentes**: Verde para sucesso, azul para ações, laranja para processamento
- **Barra de Status**: Informações em tempo real na parte inferior da janela

---

## 📦 Instalação e Requisitos

### Requisitos do Sistema

- **Python 3.10 ou superior** - [Download aqui](https://www.python.org/downloads/)
- Sistema operacional: Windows, Linux ou macOS

### Bibliotecas Necessárias

O projeto utiliza as seguintes bibliotecas Python:

```bash
pip install python-docx customtkinter pillow
```

**Descrição das bibliotecas:**

- **python-docx**: Manipulação de arquivos Word (.docx)
- **customtkinter**: Interface gráfica moderna e profissional
- **pillow**: Processamento de imagens (dependência do CustomTkinter)

### Instalação Rápida

1. Clone ou baixe este repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o programa:
   ```bash
   python upperTone.py
   ```

---

## 🚀 Como Usar

### Executando o Aplicativo

**Via Executável:**
- Clique duas vezes no arquivo executável (se disponível)

**Via Python:**
```bash
python upperTone.py
```

### Passo a Passo Detalhado

1. **Abra o aplicativo** - A janela principal será exibida com 3 seções claras

2. **Selecione seu arquivo musical**
   - Clique em "Escolher Arquivo Musical" na seção 1
   - Navegue até seu arquivo `.docx` ou `.txt`
   - Aguarde a confirmação verde ✓

3. **Configure a transposição**
   - **Direção**: Selecione "Subir Tom" para aumentar ou "Descer Tom" para diminuir
   - **Semitons**: Arraste o slider ou clique para escolher de 1 a 11 semitons

4. **Processe o arquivo**
   - Clique no botão verde 🚀 "Processar Arquivo"
   - Escolha onde salvar o arquivo transposto
   - O arquivo original será preservado, criando uma nova cópia

5. **Confirmação**
   - Uma mensagem de sucesso aparecerá
   - O arquivo transposto estará salvo no local escolhido

### 💡 Dicas de Uso

- O arquivo original **nunca é modificado**, sempre é criada uma cópia
- Números negativos não são necessários - use o botão "Descer Tom"
- O preview do arquivo selecionado aparece na tela
- A barra de status mostra o progresso em tempo real

---

## 🎯 Motivações do Projeto

Este projeto foi desenvolvido com o objetivo de facilitar a transposição de notas musicais em arquivos de texto de forma **moderna, rápida e intuitiva**.

Músicos frequentemente precisam ajustar a tonalidade de uma música para adequá-la à voz de um cantor ou ao tom de um instrumento. Este aplicativo automatiza completamente esse processo, oferecendo uma experiência visual agradável e profissional.

### 🌟 Principais Benefícios

- **🎨 Interface Moderna**: Design profissional com CustomTkinter, muito superior ao tkinter tradicional
- **👥 Facilidade de Uso**: Interface intuitiva dividida em 3 passos claros, permitindo que usuários de todos os níveis utilizem sem dificuldades
- **🎯 Precisão Total**: Garantia de que todas as notas serão transpostas corretamente, mantendo a integridade musical
- **⚡ Eficiência Máxima**: Redução significativa do tempo necessário para ajustar manualmente cada nota
- **📊 Feedback Visual**: Status em tempo real com cores e mensagens claras
- **🔄 Flexibilidade**: Capacidade de subir ou descer tons com apenas um clique

### 🎼 Para Quem é Este Projeto?

- 🎤 **Cantores** que precisam ajustar músicas ao seu tom vocal
- 🎸 **Músicos** que tocam instrumentos em diferentes afinações
- 👨‍🏫 **Professores de música** que preparam material didático
- 🎹 **Arranjadores** que trabalham com transposições frequentes
- ⛪ **Ministérios de louvor** que adaptam músicas para diferentes vozes

---

## 🛠️ Tecnologias Utilizadas

### Interface Gráfica

**CustomTkinter** - Uma biblioteca moderna de interface gráfica que oferece:
- Widgets personalizados e modernos
- Tema dark/light automático
- Animações e transições suaves
- Botões arredondados com efeitos hover
- Sliders interativos e responsivos
- Cards e frames estilizados

### Processamento de Arquivos

**python-docx** - Biblioteca robusta para:
- Leitura de arquivos Word (.docx)
- Preservação da formatação original
- Criação de novos documentos
- Manipulação de parágrafos e texto

### Processamento de Imagens

**Pillow** - Suporte para recursos visuais do CustomTkinter

---

## 📋 Formato dos Arquivos de Entrada

O aplicativo processa arquivos com notas musicais no formato:

```
DO RE MI FA SOL LA SI
DO# RE# FA# SOL# LA#
```

### Regras de Formatação

- Use letras maiúsculas para as notas: `DO, RE, MI, FA, SOL, LA, SI`
- Use `#` para notas sustenidas: `DO#, RE#, FA#, SOL#, LA#`
- Separe as notas por espaços, hífens ou quebras de linha
- O aplicativo mantém a formatação original do documento

### Exemplo de Arquivo

```
Verso 1:
DO - RE - MI - FA
SOL - LA - SI - DO

Refrão:
MI - FA# - SOL - LA
SI - DO# - RE - MI
```

---

## 🔧 Resolução de Problemas

### Problemas Comuns

**O botão "Processar Arquivo" está desabilitado**
- Certifique-se de que você selecionou um arquivo primeiro
- O botão só fica verde após carregar um arquivo válido

**Erro ao abrir arquivo**
- Verifique se o arquivo é `.docx` ou `.txt`
- Certifique-se de que o arquivo não está aberto em outro programa

**Notas não foram transpostas**
- Verifique se as notas estão em letras maiúsculas
- Use o formato: `DO, RE, MI, FA, SOL, LA, SI`
- Para sustenidos use `#`: `DO#, RE#, etc.`

**Interface não carrega**
- Certifique-se de ter instalado todas as dependências
- Execute: `pip install python-docx customtkinter pillow`

---

## 📝 Notas de Versão

### Versão 2.0 (Atual)
- ✨ Interface completamente redesenhada com CustomTkinter
- 🎨 Tema dark moderno e profissional
- 🎚️ Slider interativo para selecionar semitons
- ⬆️⬇️ Opção de subir ou descer tons
- 📊 Barra de status com feedback em tempo real
- 🏷️ Badges numerados para cada passo
- 🖼️ Cards organizados com cantos arredondados
- 🎯 Botões com estados visuais claros
- ✅ Mensagem de sucesso customizada

### Versão 1.0 (Anterior)
- Interface básica com tkinter
- Funcionalidade de transposição essencial

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

- 🐛 Reportar bugs
- 💡 Sugerir novas funcionalidades
- 🔧 Enviar pull requests
- 📖 Melhorar a documentação

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

---

## 👨‍💻 Desenvolvedor

**Christian Kringel**

Desenvolvido com ❤️ para facilitar a vida de músicos e profissionais da música.

---

<div align="center">

**Esperamos que este projeto seja útil para você!**

Se você gostou do projeto, considere dar uma ⭐

</div>
