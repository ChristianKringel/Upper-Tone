# 📋 Changelog - Upper Tone

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

---

## [2.0.0] - 2026-02-11

### ✨ Adicionado
- **Nova Interface com CustomTkinter**: Interface completamente redesenhada com visual moderno e profissional
- **Tema Dark**: Design escuro elegante com cores vibrantes
- **Slider Interativo**: Controle visual de semitons de 1 a 11 com preview do valor em tempo real
- **Opção de Direção**: Radio buttons para escolher entre subir ou descer tons
- **Badges Numerados**: Identificadores visuais (1, 2, 3) para cada passo do processo
- **Cards Organizados**: Seções divididas em cards com cantos arredondados
- **Barra de Status**: Feedback em tempo real sobre o estado da aplicação
- **Feedback Visual Aprimorado**: Mensagens coloridas (verde=sucesso, laranja=processando, vermelho=erro)
- **Mensagem de Sucesso Customizada**: Diálogo elegante ao finalizar o processamento
- **Logs de Debug**: Sistema de logs para facilitar troubleshooting
- **Suporte a .txt**: Além de .docx, agora processa arquivos de texto simples
- **requirements.txt**: Arquivo para instalação fácil de dependências
- **README.md Completo**: Documentação detalhada e profissional

### 🔧 Modificado
- **Título da Janela**: Renomeado de "Editor de Notas" para "Upper Tone - Editor de Notas Musicais"
- **Dimensões da Janela**: Aumentado de 400x200 para 700x720 pixels
- **Fluxo de Trabalho**: Simplificado de 4 botões para 3 passos claros
- **Input de Semitons**: Substituído campo de texto por slider visual
- **Botão de Processar**: Agora só fica habilitado após selecionar arquivo
- **Texto dos Botões**: Adicionados emojis e textos mais descritivos
- **Encoding**: Adicionado suporte UTF-8 para arquivos .txt

### 🗑️ Removido
- **Barra de Menu**: Removida a barra de menu confusa
- **Botão "Obter Quantidade"**: Fluxo simplificado, não é mais necessário
- **Números Negativos**: Não é mais necessário usar valores negativos, use o botão "Descer Tom"

### 🐛 Corrigido
- **SIGSEGV Error**: Resolvido problema com emojis causando crash no Linux
- **Fonte Incompatível**: Substituída fonte 'Segoe UI' (Windows) por 'Helvetica' (cross-platform)
- **Janela Pequena**: Botões cortados agora são totalmente visíveis
- **Feedback Ausente**: Usuário agora recebe confirmação visual de cada ação

### 📦 Dependências
- **Adicionado**: customtkinter >= 5.2.0
- **Adicionado**: pillow >= 10.0.0
- **Mantido**: python-docx >= 1.0.0

---

## [1.0.0] - Data Anterior

### ✨ Release Inicial
- Interface básica com tkinter
- Funcionalidade de transposição de notas
- Suporte para arquivos .docx
- Leitura e escrita de documentos Word
- Sistema de aumento/diminuição de semitons

---

## Tipos de Mudanças

- `✨ Adicionado` para novas funcionalidades
- `🔧 Modificado` para mudanças em funcionalidades existentes
- `🗑️ Removido` para funcionalidades removidas
- `🐛 Corrigido` para correções de bugs
- `🔒 Segurança` para correções de vulnerabilidades
- `📦 Dependências` para mudanças em bibliotecas externas
